"""Canonical contracts for the six Practice Studio pilot activities.

The lesson corpus remains the source of truth for language content. This module
stores only the practice design, source references, interaction type and editorial
availability of each Studio activity.
"""

STUDIO_IDS = (
    "listening",
    "pronunciation",
    "reading",
    "writing",
    "vocabulary",
    "memory",
)

COMPLETION_RULES = {
    "listening": "correct_quiz",
    "pronunciation": "self_check_all",
    "reading": "correct_quiz",
    "writing": "saved_draft_word_range_and_self_check",
    "vocabulary": "learner_example_min_4_words_and_self_check",
    "memory": "manual_review_confirmation",
}

SUPPORTED_INTERACTIONS = {
    "listen_quiz_transcript",
    "listen_repeat_self_check",
    "dialogue_reading_comprehension",
    "guided_writing_local_draft",
    "active_recall",
    "lesson_corpus_review",
}

ACTIVITIES = [
    {
        "activity_id": "listening-a2-041-weekend-dialogue",
        "studio_id": "listening",
        "completion_rule": "correct_quiz",
        "level": "A2",
        "source_lesson_id": 41,
        "duration_minutes": 5,
        "duration_en": "3–5 min",
        "duration_fr": "3–5 min",
        "outcome_en": "Identify a key event in a short conversation before revealing its transcript.",
        "outcome_fr": "Repérer un événement important dans un court échange avant d’en afficher la transcription.",
        "interaction_type": "listen_quiz_transcript",
        "content_status": "published",
        "media_status": "browser_speech_synthesis",
        "quiz": {
            "prompt_en": "Where did Daniel and his cousin go on Saturday?",
            "prompt_fr": "Où Daniel et son cousin sont-ils allés samedi ?",
            "options": [
                {"id": "a", "en": "To the Grand-Place", "fr": "À la Grand-Place"},
                {"id": "b", "en": "To the office", "fr": "Au bureau"},
                {"id": "c", "en": "To the cinema", "fr": "Au cinéma"},
            ],
            "correct_option_id": "a",
            "evidence": "Grand-Place",
            "feedback_en": "Correct: Daniel and his cousin walked around the Grand-Place on Saturday.",
            "feedback_fr": "Bonne réponse : Daniel et son cousin se sont promenés autour de la Grand-Place samedi.",
            "retry_en": "Try again. Listen for the place mentioned after “On Saturday”.",
            "retry_fr": "Réessaie. Repère le lieu mentionné après « On Saturday ».",
        },
    },
    {
        "activity_id": "pronunciation-b1-091-present-perfect",
        "studio_id": "pronunciation",
        "completion_rule": "self_check_all",
        "level": "B1",
        "source_lesson_id": 91,
        "duration_minutes": 5,
        "duration_en": "4–6 min",
        "duration_fr": "4–6 min",
        "outcome_en": "Notice sentence stress and connected speech, then repeat and shadow a model sentence.",
        "outcome_fr": "Repérer l’accentuation et les liaisons, puis répéter et imiter une phrase modèle.",
        "interaction_type": "listen_repeat_self_check",
        "content_status": "published",
        "media_status": "browser_speech_synthesis",
    },
    {
        "activity_id": "reading-b1-091-present-perfect-dialogue",
        "studio_id": "reading",
        "completion_rule": "correct_quiz",
        "level": "B1",
        "source_lesson_id": 91,
        "duration_minutes": 6,
        "duration_en": "5–7 min",
        "duration_fr": "5–7 min",
        "outcome_en": "Find explicit information in a dialogue and connect a time expression to its meaning.",
        "outcome_fr": "Retrouver une information explicite dans un dialogue et interpréter une expression de durée.",
        "interaction_type": "dialogue_reading_comprehension",
        "content_status": "published",
        "media_status": "none",
        "quiz": {
            "prompt_en": "How long has Amina been in Brussels?",
            "prompt_fr": "Depuis combien de temps Amina est-elle à Bruxelles ?",
            "options": [
                {"id": "a", "en": "For eight months", "fr": "Depuis huit mois"},
                {"id": "b", "en": "For eight weeks", "fr": "Depuis huit semaines"},
                {"id": "c", "en": "For eight years", "fr": "Depuis huit ans"},
            ],
            "correct_option_id": "a",
            "evidence": "eight months",
            "feedback_en": "Correct: Amina says she has been in Brussels for eight months.",
            "feedback_fr": "Bonne réponse : Amina dit qu’elle est à Bruxelles depuis huit mois.",
            "retry_en": "Try again. Look for the duration Amina gives after “I’ve been here”.",
            "retry_fr": "Réessaie. Repère la durée donnée par Amina après « I’ve been here ».",
        },
    },
    {
        "activity_id": "writing-a2-041-recent-experience",
        "studio_id": "writing",
        "completion_rule": "saved_draft_word_range_and_self_check",
        "level": "A2",
        "source_lesson_id": 41,
        "duration_minutes": 12,
        "duration_en": "10–15 min",
        "duration_fr": "10–15 min",
        "outcome_en": "Write a short account of a recent experience using the past simple and a clear sequence.",
        "outcome_fr": "Raconter brièvement une expérience récente au prétérit en respectant une chronologie claire.",
        "interaction_type": "guided_writing_local_draft",
        "content_status": "published",
        "media_status": "none",
    },
    {
        "activity_id": "vocabulary-b1-091-present-perfect",
        "studio_id": "vocabulary",
        "completion_rule": "learner_example_min_4_words_and_self_check",
        "level": "B1",
        "source_lesson_id": 91,
        "duration_minutes": 6,
        "duration_en": "5–8 min",
        "duration_fr": "5–8 min",
        "outcome_en": "Retrieve the meaning of lesson vocabulary, inspect its example and produce a new sentence.",
        "outcome_fr": "Retrouver le sens du vocabulaire de la leçon, observer son exemple et produire une nouvelle phrase.",
        "interaction_type": "active_recall",
        "content_status": "published",
        "media_status": "none",
    },
    {
        "activity_id": "memory-review-validated-lesson-corpus",
        "studio_id": "memory",
        "completion_rule": "manual_review_confirmation",
        "level": "ALL",
        "source_lesson_id": None,
        "source_collection": "validated_lesson_vocabulary",
        "duration_minutes": 5,
        "duration_en": "5 min or more",
        "duration_fr": "5 min ou plus",
        "outcome_en": "Retrieve vocabulary across the validated lesson corpus and mark difficult items for more frequent review.",
        "outcome_fr": "Retrouver le vocabulaire des leçons validées et signaler les éléments difficiles pour les revoir plus souvent.",
        "interaction_type": "lesson_corpus_review",
        "content_status": "published",
        "media_status": "none",
    },
]


def validate_activities(activities, lessons):
    """Return contract violations for a list of activities and lesson records."""
    errors = []
    seen_ids = set()
    seen_studios = set()
    lessons_by_id = {item.get("n"): item for item in lessons}

    for activity in activities:
        activity_id = activity.get("activity_id", "<missing-id>")
        studio_id = activity.get("studio_id")

        if not activity.get("activity_id") or activity_id in seen_ids:
            errors.append(f"{activity_id}: missing or duplicate activity_id")
        seen_ids.add(activity_id)

        if studio_id not in STUDIO_IDS:
            errors.append(f"{activity_id}: unsupported studio_id {studio_id!r}")
        elif not str(activity_id).startswith(f"{studio_id}-"):
            errors.append(f"{activity_id}: activity_id must use the stable {studio_id}- prefix")
        elif studio_id in seen_studios:
            errors.append(f"{activity_id}: more than one pilot activity for {studio_id}")
        seen_studios.add(studio_id)

        if activity.get("interaction_type") not in SUPPORTED_INTERACTIONS:
            errors.append(f"{activity_id}: unsupported interaction_type")
        if activity.get("completion_rule") != COMPLETION_RULES.get(studio_id):
            errors.append(f"{activity_id}: completion_rule does not match its Studio")
        if activity.get("content_status") not in {"planned", "draft", "needs_review", "published", "blocked"}:
            errors.append(f"{activity_id}: invalid content_status")
        if not activity.get("duration_en") or not activity.get("duration_fr"):
            errors.append(f"{activity_id}: bilingual duration labels are required")
        if activity.get("level") not in {"A1", "A2", "B1", "B2", "C1", "ALL"}:
            errors.append(f"{activity_id}: unsupported CEFR level")
        if activity.get("media_status") not in {"none", "browser_speech_synthesis", "recorded_audio", "licensed_external"}:
            errors.append(f"{activity_id}: invalid media_status")
        requires_quiz = activity.get("interaction_type") in {"listen_quiz_transcript", "dialogue_reading_comprehension"}
        quiz = activity.get("quiz")
        if requires_quiz and not quiz:
            errors.append(f"{activity_id}: this interaction type requires a quiz")
        if quiz:
            for key in ("prompt_en", "prompt_fr", "feedback_en", "feedback_fr", "retry_en", "retry_fr", "evidence"):
                if not quiz.get(key):
                    errors.append(f"{activity_id}: quiz field {key} is required")
            for option in quiz.get("options") or []:
                if not option.get("id") or not option.get("en") or not option.get("fr"):
                    errors.append(f"{activity_id}: every quiz option needs an id and EN/FR labels")
        if not isinstance(activity.get("duration_minutes"), int) or activity["duration_minutes"] < 1:
            errors.append(f"{activity_id}: duration_minutes must be a positive integer")
        if not activity.get("outcome_en") or not activity.get("outcome_fr"):
            errors.append(f"{activity_id}: bilingual learning outcomes are required")

        source_id = activity.get("source_lesson_id")
        if source_id is None:
            if studio_id != "memory" or activity.get("source_collection") != "validated_lesson_vocabulary":
                errors.append(f"{activity_id}: a supported source lesson or source collection is required")
            elif not any(item.get("mots") for item in lessons):
                errors.append(f"{activity_id}: the validated lesson vocabulary collection is empty")
            continue

        lesson = lessons_by_id.get(source_id)
        if lesson is None:
            errors.append(f"{activity_id}: source lesson {source_id} does not exist")
            continue
        if activity.get("level") != lesson.get("niveau"):
            errors.append(
                f"{activity_id}: declared level {activity.get('level')} does not match "
                f"source lesson level {lesson.get('niveau')}"
            )

        dialogue = (lesson.get("dialogue") or {}).get("lignes") or []
        if studio_id in {"listening", "pronunciation", "reading"} and len(dialogue) < 2:
            errors.append(f"{activity_id}: source lesson needs a usable dialogue")
        if studio_id == "pronunciation" and not (lesson.get("prononciation") or []):
            errors.append(f"{activity_id}: source lesson needs pronunciation guidance")
        if studio_id == "vocabulary" and len(lesson.get("mots") or []) < 5:
            errors.append(f"{activity_id}: source lesson needs at least five vocabulary items")
        if studio_id == "writing" and not (lesson.get("exercices") or []):
            errors.append(f"{activity_id}: source lesson needs writing/grammar support")

        quiz = activity.get("quiz")
        if quiz:
            options = quiz.get("options") or []
            option_ids = [option.get("id") for option in options]
            if not 2 <= len(options) <= 5:
                errors.append(f"{activity_id}: quizzes must have between two and five options")
            if len(option_ids) != len(set(option_ids)) or quiz.get("correct_option_id") not in option_ids:
                errors.append(f"{activity_id}: quiz options or correct_option_id are invalid")
            evidence = str(quiz.get("evidence") or "").casefold()
            transcript = " ".join(str(line[1]) for line in dialogue if len(line) >= 2).casefold()
            if not evidence or evidence not in transcript:
                errors.append(f"{activity_id}: quiz evidence is not present in the source dialogue")
            correct_option = next((option for option in options if option.get("id") == quiz.get("correct_option_id")), None)
            if correct_option and evidence and evidence not in str(correct_option.get("en", "")).casefold():
                errors.append(f"{activity_id}: the correct option does not contain the declared evidence")

    missing = set(STUDIO_IDS) - seen_studios
    errors.extend(f"missing pilot activity for studio {studio_id}" for studio_id in sorted(missing))
    return errors
