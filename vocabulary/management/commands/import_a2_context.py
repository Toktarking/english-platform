import pandas as pd

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from vocabulary.models import VocabularyWord


class Command(BaseCommand):
    help = "Import A2 context sentences and three distractors by Source ID."

    def add_arguments(self, parser):
        parser.add_argument("xlsx_path", type=str)
        parser.add_argument("--dry-run", action="store_true",
                            help="Validate without saving changes.")

    @transaction.atomic
    def handle(self, *args, **options):
        try:
            df = pd.read_excel(options["xlsx_path"],
                               sheet_name="A2_Master", header=0)
        except Exception as error:
            raise CommandError(f"Could not read workbook: {error}")

        required = ["Source ID", "context_sentence",
                    "context_wrong_1", "context_wrong_2", "context_wrong_3"]
        missing = [c for c in required if c not in df.columns]
        if missing:
            raise CommandError("Missing columns: " + ", ".join(missing))

        updated = skipped = errors = 0

        for _, row in df.iterrows():
            try:
                source_id = int(row["Source ID"])
            except (TypeError, ValueError):
                skipped += 1
                continue

            context = self.clean(row.get("context_sentence"))
            wrong = [self.clean(row.get("context_wrong_1")),
                     self.clean(row.get("context_wrong_2")),
                     self.clean(row.get("context_wrong_3"))]

            if (not context or context.count("___") != 1
                    or any(not x for x in wrong)
                    or len({x.casefold() for x in wrong}) != 3):
                self.stdout.write(self.style.ERROR(
                    f"Invalid row: Source ID {source_id}"))
                errors += 1
                continue

            try:
                word = VocabularyWord.objects.get(
                    source_id=source_id,
                    lesson__group__level__code__iexact="A2")
            except VocabularyWord.DoesNotExist:
                self.stdout.write(self.style.WARNING(
                    f"Not found in A2: {source_id}"))
                skipped += 1
                continue
            except VocabularyWord.MultipleObjectsReturned:
                self.stdout.write(self.style.ERROR(
                    f"Duplicate Source ID in A2: {source_id}"))
                errors += 1
                continue

            if word.word.casefold() in {x.casefold() for x in wrong}:
                self.stdout.write(self.style.ERROR(
                    f"Correct word among distractors: {source_id} {word.word}"))
                errors += 1
                continue

            word.context_sentence = context
            word.context_wrong_options = wrong
            if not options["dry_run"]:
                word.save(update_fields=[
                    "context_sentence", "context_wrong_options"])
            updated += 1

        if options["dry_run"]:
            transaction.set_rollback(True)

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(
            "Validation finished." if options["dry_run"] else "Import finished."))
        self.stdout.write(f"Updated/valid: {updated}")
        self.stdout.write(f"Skipped: {skipped}")
        self.stdout.write(f"Errors: {errors}")

        if errors:
            raise CommandError(f"{errors} validation/import error(s).")

    @staticmethod
    def clean(value):
        if pd.isna(value):
            return ""
        return str(value).strip()
