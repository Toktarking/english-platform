import os
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from vocabulary.models import VocabularyWord


class Command(BaseCommand):
    help = (
        "Normalize and attach vocabulary audio files "
        "using stable CEFR level + source_id filenames."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--level",
            required=True,
            type=str,
            help="CEFR level, e.g. A2",
        )

        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Show changes without modifying files/database.",
        )

    def handle(self, *args, **options):

        level_code = options["level"].upper().strip()
        dry_run = options["dry_run"]

        words = (
            VocabularyWord.objects
            .filter(
                lesson__group__level__code__iexact=level_code,
                is_active=True,
            )
            .select_related(
                "lesson__group__level"
            )
            .order_by("id")
        )

        if not words.exists():
            raise CommandError(
                f"No words found for level {level_code}."
            )

        renamed = 0
        attached = 0
        already_ok = 0
        missing = 0

        self.stdout.write(
            f"Level: {level_code}"
        )
        self.stdout.write(
            f"Words: {words.count()}"
        )
        self.stdout.write(
            f"Dry run: {dry_run}"
        )
        self.stdout.write("")

        for word in words:

            stable_filename = (
                f"{level_code.lower()}_"
                f"{word.source_id}.mp3"
            )

            stable_relative = (
                f"vocabulary_audio/"
                f"{stable_filename}"
            )

            stable_path = (
                Path(settings.MEDIA_ROOT)
                / stable_relative
            )

            current_relative = (
                word.audio_file.name
                if word.audio_file
                else ""
            )

            current_path = (
                Path(settings.MEDIA_ROOT)
                / current_relative
                if current_relative
                else None
            )

            # ---------------------------------------------
            # Already correct
            # ---------------------------------------------

            if (
                current_relative
                ==
                stable_relative
                and
                stable_path.exists()
            ):
                already_ok += 1
                continue

            # ---------------------------------------------
            # Stable file already exists.
            # Useful on Railway after import.
            # ---------------------------------------------

            if stable_path.exists():

                if not dry_run:
                    word.audio_file.name = (
                        stable_relative
                    )

                    word.save(
                        update_fields=[
                            "audio_file"
                        ]
                    )

                attached += 1

                continue

            # ---------------------------------------------
            # Old file exists locally.
            # Rename:
            #
            # word_900.mp3
            # ->
            # a2_200022.mp3
            # ---------------------------------------------

            if (
                current_path
                and
                current_path.exists()
            ):

                if not dry_run:

                    stable_path.parent.mkdir(
                        parents=True,
                        exist_ok=True,
                    )

                    os.replace(
                        current_path,
                        stable_path,
                    )

                    word.audio_file.name = (
                        stable_relative
                    )

                    word.save(
                        update_fields=[
                            "audio_file"
                        ]
                    )

                renamed += 1

                continue

            missing += 1

            self.stdout.write(
                self.style.WARNING(
                    f"MISSING: "
                    f"{word.word} "
                    f"(source_id={word.source_id})"
                )
            )

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "Finished."
            )
        )

        self.stdout.write(
            f"Renamed: {renamed}"
        )
        self.stdout.write(
            f"Attached existing: {attached}"
        )
        self.stdout.write(
            f"Already OK: {already_ok}"
        )
        self.stdout.write(
            f"Missing: {missing}"
        )
