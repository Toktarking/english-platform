from django.core.management.base import BaseCommand

from grammar.models import (
    GrammarExercise,
    GrammarLesson,
    GrammarLessonSection,
)


class Command(BaseCommand):

    help = (
        "Create/update interactive A1 Grammar "
        "Lesson 38: Present Continuous for future."
    )


    def handle(self, *args, **options):

        lesson, _ = GrammarLesson.objects.update_or_create(
            level="A1",
            order=38,
            defaults={
                "title": "Present Continuous для будущего",
                "slug": "present-continuous-future",
                "theory_text": (
                    "Present Continuous for future arrangements."
                ),
                "estimated_minutes": 20,
                "pass_score": 70,
                "xp_reward": 100,
                "is_published": True,
            },
        )


        # =================================================
        # 10 MICRO RULES
        # =================================================

        sections = [

            {
                "order": 1,
                "title": "Present Continuous может говорить о будущем",
                "body": """Present Continuous используется
не только для того, что происходит сейчас.

Он может говорить о будущем,
если действие уже организовано.

I am meeting my teacher tomorrow.

We are flying to Astana on Friday.

She is seeing the doctor at ten.

Главная идея:

есть конкретный план
или договорённость.""",
            },

            {
                "order": 2,
                "title": "Формула",
                "body": """Формула:

AM / IS / ARE + verb-ing

I am meeting him tomorrow.

She is coming tonight.

They are leaving on Monday.

Форма та же,
что и у обычного Present Continuous.

Будущее значение показывает контекст:

tomorrow
tonight
next week
on Monday
at six.""",
            },

            {
                "order": 3,
                "title": "Конкретная договорённость",
                "body": """Present Continuous особенно подходит,
когда встреча уже согласована.

I am meeting Marat at six.

Это обычно значит:

время известно;

другой человек знает;

встреча уже договорена.

Ещё пример:

We are having lunch
with the manager tomorrow.""",
            },

            {
                "order": 4,
                "title": "Назначенные встречи",
                "body": """Часто используем Present Continuous
для appointments.

I am seeing the doctor tomorrow.

She is meeting the dean at eleven.

He is seeing the dentist on Friday.

Здесь SEE может означать:

встречаться с кем-то
по назначению.""",
            },

            {
                "order": 5,
                "title": "Поездки и организованные планы",
                "body": """Present Continuous часто используется
с поездками.

We are flying to Almaty tomorrow.

She is leaving on Friday.

They are arriving at ten.

I am staying at a hotel next week.

Обычно уже есть:

билет;

бронь;

время;

место.""",
            },

            {
                "order": 6,
                "title": "Отрицание",
                "body": """Отрицание:

AM / IS / ARE + NOT + verb-ing

I am not working tomorrow.

She isn't coming tonight.

They aren't travelling next week.

То есть отрицание строится
через TO BE.""",
            },

            {
                "order": 7,
                "title": "Вопросы",
                "body": """В вопросе TO BE идёт первым.

Are you working tomorrow?

Is she coming tonight?

Are they travelling next week?

Краткие ответы:

Yes, I am.

No, I'm not.

Yes, she is.

No, she isn't.""",
            },

            {
                "order": 8,
                "title": "Present Continuous или GOING TO?",
                "body": """BE GOING TO чаще показывает:

намерение;

общий план.

I'm going to visit the doctor
next week.

Present Continuous:

конкретную договорённость.

I'm seeing the doctor
on Tuesday at ten.

То есть:

GOING TO → план

Present Continuous → arrangement.""",
            },

            {
                "order": 9,
                "title": "Present Continuous или WILL?",
                "body": """WILL часто используется,
если решение принято сейчас.

The phone is ringing.

I'll answer it.

Present Continuous показывает,
что действие организовано заранее.

I'm meeting him tomorrow at ten.

Сравни:

I'll call her now.

I'm calling her at six tomorrow.""",
            },

            {
                "order": 10,
                "title": "Present Continuous или расписание?",
                "body": """Present Simple используется
для официального расписания.

The train leaves at six.

The lesson starts at nine.

Present Continuous:

личный организованный план.

We are taking the six o'clock train.

I am attending the lesson tomorrow.

Коротко:

расписание → Present Simple

личный arrangement
→ Present Continuous.""",
            },

        ]


        section_objects = {}


        for data in sections:

            section, _ = GrammarLessonSection.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "title": data["title"],
                    "body": data["body"],
                },
            )

            section_objects[data["order"]] = section


        # =================================================
        # 20 TRAINING EXERCISES
        # =================================================

        training = [

            # SECTION 1
            {
                "order": 1,
                "section": 1,
                "type": "choice",
                "prompt":
                    "We ___ having dinner with friends tonight.",
                "options": [
                    "are",
                    "is",
                    "am",
                    "do",
                ],
                "answer":
                    "are",
                "explanation":
                    "WE → ARE + verb-ing.",
            },

            {
                "order": 2,
                "section": 1,
                "type": "choice",
                "prompt":
                    "My sister ___ flying to Astana tomorrow.",
                "options": [
                    "is",
                    "am",
                    "are",
                    "does",
                ],
                "answer":
                    "is",
                "explanation":
                    "MY SISTER = SHE → IS.",
            },


            # SECTION 2
            {
                "order": 3,
                "section": 2,
                "type": "build",
                "prompt":
                    "Собери предложение о будущем.",
                "options": [
                    "I",
                    "am",
                    "meeting",
                    "him",
                    "tomorrow",
                ],
                "answer":
                    "I am meeting him tomorrow",
                "explanation":
                    "AM + MEETING + future time.",
            },

            {
                "order": 4,
                "section": 2,
                "type": "choice",
                "prompt":
                    "They are ___ on Monday.",
                "options": [
                    "leaving",
                    "leave",
                    "left",
                    "leaves",
                ],
                "answer":
                    "leaving",
                "explanation":
                    "Present Continuous = ARE + verb-ing.",
            },


            # SECTION 3
            {
                "order": 5,
                "section": 3,
                "type": "choice",
                "prompt":
                    "The meeting is confirmed. I ___ Marat at six.",
                "options": [
                    "am meeting",
                    "meet every day",
                    "will meeting",
                    "am meet",
                ],
                "answer":
                    "am meeting",
                "explanation":
                    "Конкретная договорённость → Present Continuous.",
            },

            {
                "order": 6,
                "section": 3,
                "type": "choice",
                "prompt":
                    "We have a reservation. We ___ dinner at eight.",
                "options": [
                    "are having",
                    "have every day",
                    "will having",
                    "are have",
                ],
                "answer":
                    "are having",
                "explanation":
                    "Есть организованный план.",
            },


            # SECTION 4
            {
                "order": 7,
                "section": 4,
                "type": "choice",
                "prompt":
                    "I have an appointment. I ___ the doctor tomorrow.",
                "options": [
                    "am seeing",
                    "see every day",
                    "will see suddenly",
                    "am see",
                ],
                "answer":
                    "am seeing",
                "explanation":
                    "Назначенная встреча → Present Continuous.",
            },

            {
                "order": 8,
                "section": 4,
                "type": "choice",
                "prompt":
                    "She ___ the dentist at ten on Friday.",
                "options": [
                    "is seeing",
                    "sees every day",
                    "will seeing",
                    "is see",
                ],
                "answer":
                    "is seeing",
                "explanation":
                    "Есть конкретное назначенное время.",
            },


            # SECTION 5
            {
                "order": 9,
                "section": 5,
                "type": "choice",
                "prompt":
                    "We bought the tickets. We ___ to Almaty tomorrow.",
                "options": [
                    "are flying",
                    "fly every day",
                    "will flying",
                    "are fly",
                ],
                "answer":
                    "are flying",
                "explanation":
                    "Поездка уже организована.",
            },

            {
                "order": 10,
                "section": 5,
                "type": "choice",
                "prompt":
                    "Their flight is booked. They ___ at nine.",
                "options": [
                    "are leaving",
                    "leave every morning",
                    "will leaving",
                    "are leave",
                ],
                "answer":
                    "are leaving",
                "explanation":
                    "Есть конкретный организованный план.",
            },


            # SECTION 6
            {
                "order": 11,
                "section": 6,
                "type": "choice",
                "prompt":
                    "She ___ coming tonight.",
                "options": [
                    "isn't",
                    "doesn't",
                    "won't be to",
                    "not is",
                ],
                "answer":
                    "isn't",
                "explanation":
                    "Отрицание Present Continuous → ISN'T + verb-ing.",
            },

            {
                "order": 12,
                "section": 6,
                "type": "choice",
                "prompt":
                    "Choose the correct negative sentence.",
                "options": [
                    "We aren't working tomorrow.",
                    "We don't working tomorrow.",
                    "We aren't work tomorrow.",
                    "We won't working tomorrow.",
                ],
                "answer":
                    "We aren't working tomorrow.",
                "explanation":
                    "ARE NOT + WORKING.",
            },


            # SECTION 7
            {
                "order": 13,
                "section": 7,
                "type": "choice",
                "prompt":
                    "___ you meeting the manager tomorrow?",
                "options": [
                    "Are",
                    "Do",
                    "Will",
                    "Did",
                ],
                "answer":
                    "Are",
                "explanation":
                    "Вопрос начинается с ARE.",
            },

            {
                "order": 14,
                "section": 7,
                "type": "choice",
                "prompt":
                    "Is Anna coming tonight?",
                "options": [
                    "Yes, she is.",
                    "Yes, she does.",
                    "Yes, she will be.",
                    "Yes, she has.",
                ],
                "answer":
                    "Yes, she is.",
                "explanation":
                    "Краткий ответ повторяет IS.",
            },


            # SECTION 8
            {
                "order": 15,
                "section": 8,
                "type": "choice",
                "prompt":
                    "I intend to visit the doctor next week, but no appointment is fixed yet.",
                "options": [
                    "I'm going to visit the doctor.",
                    "I'm seeing the doctor at ten.",
                    "I saw the doctor.",
                    "I'll seeing the doctor.",
                ],
                "answer":
                    "I'm going to visit the doctor.",
                "explanation":
                    "Есть намерение, но нет конкретной договорённости.",
            },

            {
                "order": 16,
                "section": 8,
                "type": "choice",
                "prompt":
                    "The appointment is at 10:00 on Tuesday.",
                "options": [
                    "I'm seeing the doctor on Tuesday at ten.",
                    "I'm going to see the doctor sometime.",
                    "I will seeing the doctor.",
                    "I see the doctor yesterday.",
                ],
                "answer":
                    "I'm seeing the doctor on Tuesday at ten.",
                "explanation":
                    "Конкретная договорённость → Present Continuous.",
            },


            # SECTION 9
            {
                "order": 17,
                "section": 9,
                "type": "choice",
                "prompt":
                    "The phone is ringing. I ___ it.",
                "options": [
                    "will answer",
                    "am answering tomorrow",
                    "will answered",
                    "am answer",
                ],
                "answer":
                    "will answer",
                "explanation":
                    "Спонтанное решение → WILL.",
            },

            {
                "order": 18,
                "section": 9,
                "type": "choice",
                "prompt":
                    "The call is scheduled for six. I ___ her at six.",
                "options": [
                    "am calling",
                    "will call suddenly",
                    "call every day",
                    "am call",
                ],
                "answer":
                    "am calling",
                "explanation":
                    "Заранее организованное действие → Present Continuous.",
            },


            # SECTION 10
            {
                "order": 19,
                "section": 10,
                "type": "choice",
                "prompt":
                    "The train ___ at 7:30.",
                "options": [
                    "leaves",
                    "is leave",
                    "will leaving",
                    "leaving",
                ],
                "answer":
                    "leaves",
                "explanation":
                    "Официальное расписание → Present Simple.",
            },

            {
                "order": 20,
                "section": 10,
                "type": "choice",
                "prompt":
                    "We have tickets for the 7:30 train. We ___ it tomorrow.",
                "options": [
                    "are taking",
                    "take every day",
                    "will taking",
                    "are take",
                ],
                "answer":
                    "are taking",
                "explanation":
                    "Это наш организованный план.",
            },

        ]


        # =================================================
        # FINAL TEST — 10 NEW QUESTIONS
        # =================================================

        final_test = [

            {
                "order": 21,
                "prompt":
                    "I ___ my supervisor tomorrow at eleven.",
                "options": [
                    "am meeting",
                    "meet every day",
                    "will meeting",
                    "am meet",
                ],
                "answer":
                    "am meeting",
                "explanation":
                    "Есть конкретная будущая договорённость.",
            },

            {
                "order": 22,
                "prompt":
                    "They ___ to Dubai on Saturday. The tickets are booked.",
                "options": [
                    "are flying",
                    "fly every Saturday",
                    "will flying",
                    "are fly",
                ],
                "answer":
                    "are flying",
                "explanation":
                    "Организованная поездка → Present Continuous.",
            },

            {
                "order": 23,
                "prompt":
                    "Choose the correct negative sentence.",
                "options": [
                    "He isn't working tomorrow.",
                    "He doesn't working tomorrow.",
                    "He isn't work tomorrow.",
                    "He won't working tomorrow.",
                ],
                "answer":
                    "He isn't working tomorrow.",
                "explanation":
                    "IS NOT + verb-ing.",
            },

            {
                "order": 24,
                "prompt":
                    "Choose the correct question.",
                "options": [
                    "Are you seeing the dentist tomorrow?",
                    "Do you seeing the dentist tomorrow?",
                    "Will you seeing the dentist tomorrow?",
                    "Are you see the dentist tomorrow?",
                ],
                "answer":
                    "Are you seeing the dentist tomorrow?",
                "explanation":
                    "ARE + subject + verb-ing?",
            },

            {
                "order": 25,
                "prompt":
                    "Which sentence shows a concrete arrangement?",
                "options": [
                    "I'm meeting Aida at five tomorrow.",
                    "I'm going to meet Aida sometime.",
                    "I think I will meet Aida one day.",
                    "I meet Aida every Friday.",
                ],
                "answer":
                    "I'm meeting Aida at five tomorrow.",
                "explanation":
                    "Конкретное время и договорённость → Present Continuous.",
            },

            {
                "order": 26,
                "prompt":
                    "Which sentence shows a general intention?",
                "options": [
                    "I'm going to look for a new apartment.",
                    "I'm meeting the landlord at three.",
                    "The office opens at nine.",
                    "I'll answer the phone.",
                ],
                "answer":
                    "I'm going to look for a new apartment.",
                "explanation":
                    "Общее намерение → BE GOING TO.",
            },

            {
                "order": 27,
                "prompt":
                    "Which sentence describes an official timetable?",
                "options": [
                    "The plane arrives at 18:20.",
                    "We are arriving at the hotel at 19:00.",
                    "I'm going to travel next month.",
                    "I'll travel if I have time.",
                ],
                "answer":
                    "The plane arrives at 18:20.",
                "explanation":
                    "Официальное расписание → Present Simple.",
            },

            {
                "order": 28,
                "prompt":
                    "The decision is made right now. Which is best?",
                "options": [
                    "I'll carry your bag.",
                    "I'm carrying your bag tomorrow at five.",
                    "I carry your bag every day.",
                    "I am going carrying your bag.",
                ],
                "answer":
                    "I'll carry your bag.",
                "explanation":
                    "Решение в момент речи → WILL.",
            },

            {
                "order": 29,
                "prompt":
                    "Choose the correct comparison.",
                "options": [
                    "I'm going to visit him next week. / I'm meeting him on Tuesday at four.",
                    "I'm going visit him. / I'm meet him at four.",
                    "I will going to visit him. / I'm meeting to him.",
                    "I'm going to visiting him. / I meeting him.",
                ],
                "answer":
                    "I'm going to visit him next week. / I'm meeting him on Tuesday at four.",
                "explanation":
                    "GOING TO → намерение; Present Continuous → конкретная договорённость.",
            },

            {
                "order": 30,
                "prompt":
                    "Choose the fully correct pair.",
                "options": [
                    "The train leaves at six. / We are taking the six o'clock train.",
                    "The train is leave at six. / We taking the train.",
                    "The train will leaving at six. / We are take the train.",
                    "The train leaving at six. / We will taking it.",
                ],
                "answer":
                    "The train leaves at six. / We are taking the six o'clock train.",
                "explanation":
                    "Расписание → Present Simple; личный организованный план → Present Continuous.",
            },

        ]


        all_exercises = training + final_test

        valid_orders = [
            item["order"]
            for item in all_exercises
        ]


        for data in all_exercises:

            if data["order"] <= 20:
                section = section_objects[data["section"]]
            else:
                section = None


            GrammarExercise.objects.update_or_create(
                lesson=lesson,
                order=data["order"],
                defaults={
                    "section": section,
                    "exercise_type": data.get(
                        "type",
                        "choice",
                    ),
                    "prompt": data["prompt"],
                    "options": data["options"],
                    "correct_answer": data["answer"],
                    "explanation": data["explanation"],
                    "is_published": True,
                },
            )


        GrammarExercise.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=valid_orders,
        ).delete()


        GrammarLessonSection.objects.filter(
            lesson=lesson,
        ).exclude(
            order__in=[
                item["order"]
                for item in sections
            ],
        ).delete()


        self.stdout.write(
            self.style.SUCCESS(
                "✅ Interactive A1 Lesson 38 seeded"
            )
        )

        self.stdout.write(
            f"Micro rules: {lesson.sections.count()}"
        )

        self.stdout.write(
            "Training exercises: "
            f"{lesson.exercises.filter(section__isnull=False).count()}"
        )

        self.stdout.write(
            "Final test: "
            f"{lesson.exercises.filter(section__isnull=True).count()}"
        )
