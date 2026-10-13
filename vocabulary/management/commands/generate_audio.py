import asyncio
import os

import edge_tts

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from vocabulary.models import VocabularyWord


VOICE = "en-GB-SoniaNeural"


async def create_audio(
    text,
    output_path,
):

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate="-10%",
    )

    await communicate.save(
        output_path
    )


class Command(BaseCommand):

    help = (
        "Generate pronunciation audio "
        "for vocabulary words."
    )


    def handle(
        self,
        *args,
        **options,
    ):

        words = (
            VocabularyWord.objects
            .filter(
                is_active=True
            )
            .order_by(
                "id"
            )
        )


        temp_directory = (
            settings.BASE_DIR
            /
            "temp_audio"
        )


        os.makedirs(
            temp_directory,
            exist_ok=True,
        )


        total = words.count()

        created = 0

        skipped = 0

        errors = 0


        for index, word in enumerate(
            words,
            start=1,
        ):

            # Уже есть аудио —
            # заново не генерируем.
            if word.audio_file:

                skipped += 1

                self.stdout.write(
                    f"[{index}/{total}] "
                    f"SKIP: {word.word}"
                )

                continue


            temp_path = (
                temp_directory
                /
                f"word_{word.id}.mp3"
            )


            try:

                asyncio.run(
                    create_audio(
                        word.word,
                        str(
                            temp_path
                        ),
                    )
                )


                with open(
                    temp_path,
                    "rb",
                ) as audio:

                    word.audio_file.save(
                        f"word_{word.id}.mp3",
                        File(audio),
                        save=True,
                    )


                created += 1


                self.stdout.write(
                    self.style.SUCCESS(
                        f"[{index}/{total}] "
                        f"OK: {word.word}"
                    )
                )


            except Exception as error:

                errors += 1


                self.stdout.write(
                    self.style.ERROR(
                        f"[{index}/{total}] "
                        f"ERROR: "
                        f"{word.word} "
                        f"— {error}"
                    )
                )


            finally:

                if os.path.exists(
                    temp_path
                ):

                    os.remove(
                        temp_path
                    )


        self.stdout.write(
            ""
        )


        self.stdout.write(
            self.style.SUCCESS(
                "Finished."
            )
        )


        self.stdout.write(
            f"Generated: {created}"
        )

        self.stdout.write(
            f"Skipped: {skipped}"
        )

        self.stdout.write(
            f"Errors: {errors}"
        )