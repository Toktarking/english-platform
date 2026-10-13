import pandas as pd

from django.core.management.base import BaseCommand, CommandError

from vocabulary.models import VocabularyWord


class Command(BaseCommand):
    help = "Import Stage 3 context sentences and distractors into existing A1 words."

    def add_arguments(self, parser):
        parser.add_argument(
            "xlsx_path",
            type=str,
            help="Path to A1_vocabulary_bank_contextual_stage3.xlsx",
        )

    def handle(self, *args, **options):
        xlsx_path = options["xlsx_path"]

        try:
            df = pd.read_excel(
                xlsx_path,
                sheet_name="A1_Master",
                header=2,
            )
        except Exception as error:
            raise CommandError(
                f"Could not read workbook: {error}"
            )

        required_columns = [
            "Normalized word",
            "POS (source)",
            "context_sentence",
            "context_wrong_1",
            "context_wrong_2",
            "context_wrong_3",
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:
            raise CommandError(
                "Missing columns: " + ", ".join(missing_columns)
            )

        updated = 0
        skipped = 0
        ambiguous = 0

        for _, row in df.iterrows():
            word_text = self.clean_value(
                row.get("Normalized word")
            )

            part_of_speech = self.clean_value(
                row.get("POS (source)")
            )

            context_sentence = self.clean_value(
                row.get("context_sentence")
            )

            wrong_options = [
                self.clean_value(row.get("context_wrong_1")),
                self.clean_value(row.get("context_wrong_2")),
                self.clean_value(row.get("context_wrong_3")),
            ]

            wrong_options = [
                option
                for option in wrong_options
                if option
            ]

            if not word_text or not context_sentence:
                skipped += 1
                continue

            if len(wrong_options) != 3:
                self.stdout.write(
                    self.style.WARNING(
                        f"Skipped '{word_text}': expected 3 wrong options."
                    )
                )
                skipped += 1
                continue

            queryset = VocabularyWord.objects.filter(
                word__iexact=word_text,
                part_of_speech=part_of_speech,
                lesson__group__level__code__iexact="A1",
            )

            count = queryset.count()

            # Fallback: sometimes POS formatting can differ slightly.
            if count == 0:
                fallback = VocabularyWord.objects.filter(
                    word__iexact=word_text,
                    lesson__group__level__code__iexact="A1",
                )

                if fallback.count() == 1:
                    queryset = fallback
                    count = 1

            if count == 0:
                self.stdout.write(
                    self.style.WARNING(
                        f"Not found: {word_text} [{part_of_speech}]"
                    )
                )
                skipped += 1
                continue

            if count > 1:
                self.stdout.write(
                    self.style.ERROR(
                        f"Ambiguous: {word_text} [{part_of_speech}] -> {count} rows"
                    )
                )
                ambiguous += 1
                continue

            word = queryset.get()

            word.context_sentence = context_sentence
            word.context_wrong_options = wrong_options

            word.save(
                update_fields=[
                    "context_sentence",
                    "context_wrong_options",
                ]
            )

            updated += 1

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                f"Updated: {updated}"
            )
        )
        self.stdout.write(
            f"Skipped/not found: {skipped}"
        )
        self.stdout.write(
            f"Ambiguous: {ambiguous}"
        )

    @staticmethod
    def clean_value(value):
        if pd.isna(value):
            return ""

        return str(value).strip()
