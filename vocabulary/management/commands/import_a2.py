import math

import pandas as pd

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from vocabulary.models import (
    VocabularyGroup,
    VocabularyLesson,
    VocabularyLevel,
    VocabularyWord,
)


class Command(BaseCommand):
    help = "Import A2 vocabulary from A2_vocabulary_complete_1134.xlsx"

    def add_arguments(self, parser):
        parser.add_argument(
            "xlsx_path",
            type=str,
            help="Path to the A2 vocabulary XLSX file",
        )

    @staticmethod
    def clean_value(value):
        if value is None:
            return ""
        try:
            if pd.isna(value):
                return ""
        except (TypeError, ValueError):
            pass
        return str(value).strip()

    @staticmethod
    def clean_int(value, field_name):
        if value is None:
            raise CommandError(f"Missing integer value for {field_name}")
        try:
            if pd.isna(value):
                raise CommandError(f"Missing integer value for {field_name}")
        except (TypeError, ValueError):
            pass
        try:
            return int(value)
        except (TypeError, ValueError):
            raise CommandError(
                f"Invalid integer value for {field_name}: {value!r}"
            )

    def handle(self, *args, **options):
        xlsx_path = options["xlsx_path"]

        try:
            df = pd.read_excel(
                xlsx_path,
                sheet_name="A2_Master",
            )
        except Exception as error:
            raise CommandError(f"Could not read workbook: {error}")

        required_columns = [
            "Source ID",
            "Original headword",
            "Normalized word",
            "Sense",
            "POS (source)",
            "Group #",
            "Group",
            "Lesson in group",
            "Global lesson",
            "Item in lesson",
            "Translation RU",
            "Translation KZ",
            "Example EN",
            "Example RU",
            "Example KZ",
            "CEFR",
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

        if len(df) != 1134:
            self.stdout.write(
                self.style.WARNING(
                    f"Workbook contains {len(df)} rows; expected 1134."
                )
            )

        cefr_values = {
            self.clean_value(value).upper()
            for value in df["CEFR"].dropna().tolist()
        }
        if cefr_values != {"A2"}:
            raise CommandError(
                f"Unexpected CEFR values in A2 workbook: {sorted(cefr_values)}"
            )

        created_words = 0
        updated_words = 0
        created_groups = 0
        created_lessons = 0

        with transaction.atomic():
            level, _ = VocabularyLevel.objects.update_or_create(
                code="A2",
                defaults={
                    "name": "A2",
                    "order": 2,
                    "is_active": True,
                },
            )

            for row_number, (_, row) in enumerate(df.iterrows(), start=2):
                source_id = self.clean_int(row.get("Source ID"), "Source ID")
                group_number = self.clean_int(row.get("Group #"), "Group #")
                lesson_number = self.clean_int(
                    row.get("Lesson in group"),
                    "Lesson in group",
                )
                global_lesson = self.clean_int(
                    row.get("Global lesson"),
                    "Global lesson",
                )
                item_in_lesson = self.clean_int(
                    row.get("Item in lesson"),
                    "Item in lesson",
                )

                group_name = self.clean_value(row.get("Group"))
                word = self.clean_value(row.get("Normalized word"))
                translation_ru = self.clean_value(row.get("Translation RU"))
                translation_kz = self.clean_value(row.get("Translation KZ"))
                example_en = self.clean_value(row.get("Example EN"))
                example_ru = self.clean_value(row.get("Example RU"))
                example_kz = self.clean_value(row.get("Example KZ"))

                if not group_name:
                    raise CommandError(f"Row {row_number}: empty Group")
                if not word:
                    raise CommandError(f"Row {row_number}: empty Normalized word")
                if not translation_ru or not translation_kz:
                    raise CommandError(
                        f"Row {row_number}: missing RU/KZ translation for {word!r}"
                    )

                group, group_created = VocabularyGroup.objects.update_or_create(
                    level=level,
                    code=f"G{group_number:02d}",
                    defaults={
                        "name": group_name,
                        "order": group_number,
                        "description": "",
                    },
                )
                if group_created:
                    created_groups += 1

                lesson, lesson_created = VocabularyLesson.objects.update_or_create(
                    group=group,
                    number=lesson_number,
                    defaults={
                        "global_number": global_lesson,
                        "title": f"Lesson {global_lesson}",
                        "order": lesson_number,
                        "is_active": True,
                    },
                )
                if lesson_created:
                    created_lessons += 1

                _, word_created = VocabularyWord.objects.update_or_create(
                    source_id=source_id,
                    defaults={
                        "lesson": lesson,
                        "original_headword": self.clean_value(
                            row.get("Original headword")
                        ),
                        "word": word,
                        "sense": self.clean_value(row.get("Sense")),
                        "part_of_speech": self.clean_value(row.get("POS (source)")),
                        "translation_ru": translation_ru,
                        "translation_kz": translation_kz,
                        "example_en": example_en,
                        "example_ru": example_ru,
                        "example_kz": example_kz,
                        "order": item_in_lesson,
                        "is_active": True,
                    },
                )

                if word_created:
                    created_words += 1
                else:
                    updated_words += 1

        total_groups = VocabularyGroup.objects.filter(level__code="A2").count()
        total_lessons = VocabularyLesson.objects.filter(
            group__level__code="A2"
        ).count()
        total_words = VocabularyWord.objects.filter(
            lesson__group__level__code="A2"
        ).count()

        self.stdout.write(
            self.style.SUCCESS(
                "A2 import completed successfully.\n"
                f"Created groups: {created_groups}\n"
                f"Created lessons: {created_lessons}\n"
                f"Created words: {created_words}\n"
                f"Updated words: {updated_words}\n"
                f"A2 totals -> groups: {total_groups}, "
                f"lessons: {total_lessons}, words: {total_words}"
            )
        )
