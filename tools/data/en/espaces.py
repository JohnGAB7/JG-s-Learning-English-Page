# Content of the Path and Speak spaces, and the six workshops (bilingual site).

# The six workshops. Each colour is defined once, as a CSS variable in tools/palette.css
# (--ws-listening, --ws-pronunciation…); the key below is the variable suffix.
ATELIERS = [
 # key, name, description, link for the hub card, link label, icon, practice formats, available now?
 ("listening", "Listening Studio", "Train your ear to recognise sounds, linked words, accents and the overall meaning.", "speak/", "Speak lab", "◖",
  ["Graded dialogues", "Focused listening and comprehension", "Transcripts and vocabulary"], False),
 ("pronunciation", "Pronunciation Lab", "Work on clarity, word stress, rhythm, sounds and intonation.", "speak/#method", "Speak method", "〰",
  ["Sound contrasts", "Word stress and sentence stress", "Repetition and shadowing"], False),
 ("reading", "Reading Room", "Read to understand, grow your vocabulary and notice ideas and nuance.", "news/", "News", "▤",
  ["Texts by level", "Comprehension and inference", "Reading authentic content"], False),
 ("writing", "Writing Workshop", "Build clear, coherent texts that fit the situation.", "lessons/", "Lessons", "✎",
  ["Sentences and paragraphs", "Messages and emails", "Essays and argued texts"], False),
 ("vocabulary", "Vocabulary & Expressions", "Learn words in context and build natural word combinations.", "lessons/", "Lessons", "Aa",
  ["Topics and word families", "Collocations and phrasal verbs", "Useful expressions in context"], False),
 ("memory", "Memory & Review", "Review regularly and strengthen what you have already learnt.", "review/", "Review", "⟳",
  ["Vocabulary cards", "Lesson reminders", "Review by level"], True),
]

# The eight skills of the path, with the workshop whose colour identifies them (None = neutral).
DIMENSIONS = [
 ("Grammar", "Structures and sentence building", None),
 ("Vocabulary", "Words, expressions and collocations", "vocabulary"),
 ("Pronunciation", "Sounds, rhythm, stress, intonation", "pronunciation"),
 ("Listening", "Understanding conversations and talks", "listening"),
 ("Speaking", "Answering, interacting, telling, arguing", None),
 ("Reading", "Reading and interpreting different texts", "reading"),
 ("Writing", "Writing clearly and coherently", "writing"),
 ("Functional English", "Getting things done in real life", None),
]

# For each level: title, objective, and the seven blocks (block name, workshop key or None, content).
NIVEAUX_DETAIL = {
 "A1": {"titre": "Build your foundations.", "objectif": "Understand and use familiar everyday expressions. Introduce yourself, ask simple questions and interact in predictable situations.",
  "blocs": [("Grammar", None, "Pronouns, be / have, articles, plurals, present simple, basic questions, demonstratives, possessives, can, there is / are, simple prepositions."),
            ("Vocabulary", "vocabulary", "Identity, the alphabet, numbers, dates, countries, family, home, objects, food, time, routines and places."),
            ("Pronunciation", "pronunciation", "The alphabet and spelling, key sounds, word stress, sentence rhythm and question intonation."),
            ("Listening", "listening", "Short dialogues at a slow pace, instructions, personal information and very simple conversations."),
            ("Speaking", None, "Introduce yourself, talk about what you like, describe a person or a place, answer simple questions."),
            ("Reading and writing", "reading", "Forms, signs, short messages, simple descriptions, personal sentences and short notes."),
            ("Practical English", None, "Greet, thank, ask someone to repeat, spell, ask a price, order simply, ask for directions.")]},
 "A2": {"titre": "Become more independent.", "objectif": "Handle routine exchanges and describe your surroundings, needs, activities and past events.",
  "blocs": [("Grammar", None, "Past simple, past continuous, future plans, quantifiers, comparatives and superlatives, frequency, modals, a first look at the present perfect, infinitive and gerund."),
            ("Vocabulary", "vocabulary", "Work, studies, shopping, transport, health, travel, meals, free time, weather, services and relationships."),
            ("Pronunciation", "pronunciation", "-ed endings and plurals, contractions, weak forms, common linking and intonation."),
            ("Listening", "listening", "Everyday conversations, announcements, instructions, exchanges at work and in shops."),
            ("Speaking", None, "Describe your habits, tell a recent story, explain your preferences, organise an activity and ask for help."),
            ("Reading and writing", "writing", "Simple emails, instructions, short articles, linked paragraphs, invitations, requests and descriptions."),
            ("Practical English", None, "Make an appointment, order, buy, explain a problem, suggest, accept, refuse and make a polite request.")]},
 "B1": {"titre": "Speak with confidence.", "objectif": "Be independent on familiar topics, tell about experiences, explain choices and give a reasoned opinion.",
  "blocs": [("Grammar", None, "Tense contrasts, narrative tenses, future forms, conditionals, relative clauses, passive, reported speech, modals of deduction, gerund and infinitive."),
            ("Vocabulary", "vocabulary", "Education, careers, society, technology, the environment, culture, travel, relationships, emotions and personal growth."),
            ("Pronunciation", "pronunciation", "Thought groups, sentence stress, linking, weak forms, rhythm and intelligibility."),
            ("Listening", "listening", "Interviews, longer conversations, explanations, accessible podcasts and standard speech."),
            ("Speaking", None, "Tell a story, explain a process, compare, justify, give an opinion and keep a longer conversation going."),
            ("Reading and writing", "reading", "Articles, opinion pieces, stories, structured emails, argued paragraphs and short reports."),
            ("Practical English", None, "Clarify, rephrase, sort out a misunderstanding, make a suggestion, negotiate a solution and share an experience.")]},
 "B2": {"titre": "Express, debate & nuance.", "objectif": "Understand complex content, defend a point of view and communicate spontaneously and fluently.",
  "blocs": [("Grammar", None, "Advanced tense contrasts, all conditionals, passive, reported speech, nuanced modals, participle clauses, inversion and emphasis."),
            ("Vocabulary", "vocabulary", "Collocations, phrasal verbs, idioms in context, abstract, professional and academic vocabulary."),
            ("Pronunciation", "pronunciation", "Expressive intonation, emphasis, pace, nuance and adapting to the listener."),
            ("Listening", "listening", "Long authentic recordings, a range of accents, implied meaning, interviews and discussions."),
            ("Speaking", None, "Argue, negotiate, hypothesise, summarise, compare points of view and debate spontaneously."),
            ("Reading and writing", "writing", "Complex articles, essays, reports, proposals, formal letters and summaries."),
            ("Practical English", None, "Disagree with nuance, persuade, defend a recommendation, manage a discussion and adapt your register.")]},
 "C1": {"titre": "Master precision & flexibility.", "objectif": "Understand demanding texts and express yourself spontaneously with precision, flexibility and control of register.",
  "blocs": [("Grammar and discourse", None, "Complex structures, inversion, ellipsis, cleft sentences, hedging, modality, register, discourse markers and fine nuances of tense and aspect."),
            ("Vocabulary and style", "vocabulary", "Lexical precision, idiomatic language, connotation, metaphor, register, and academic and professional phrasing."),
            ("Pronunciation", "pronunciation", "Expressive control, rhythm, discourse intonation and clarity in varied contexts."),
            ("Listening", "listening", "Implied attitudes, fast speech, varied accents, lectures and complex discussions."),
            ("Speaking", None, "Nuanced argument, presentations, facilitation, diplomacy, complex storytelling and spontaneous adaptation."),
            ("Reading and writing", "writing", "Long demanding texts, rhetoric, synthesis, critical analysis, proposals and nuanced professional writing."),
            ("Practical English", None, "Handle ambiguity, persuade with tact, rephrase precisely, adjust your tone and catch what is implied.")]},
}

METHODE_PARLER = [
 ("Watch & understand", "Watch a short scene with subtitles. Understand the situation, the intention and the useful expressions.", "listening"),
 ("Listen & imitate", "Listen sentence by sentence. Notice the stress, linking, rhythm and intonation, then imitate out loud.", "pronunciation"),
 ("Repeat & rebuild", "Repeat with pauses, then replace the details with your own: your time, your tastes, your job, your experience.", "memory"),
 ("Answer naturally", "Answer a question without reading. Compare your answer with the model and try again, more fluently.", None),
]

THEMES = [
 ("Everyday routines & personal life", "Talk about yourself and your daily life.", [
   ("Daily routine", "My morning routine", "Waking up, getting ready, having breakfast, starting your day.", "Wake up · Get ready · Have breakfast · Head out"),
   ("Evening", "My evenings & bedtime", "Your evenings, your habits and how you end the day.", "Wind down · Relax · Go to bed · Fall asleep"),
   ("Home", "My home & neighbourhood", "Describe your home, your area, the places nearby and where you live.", "There is · Located · Nearby · Comfortable"),
   ("Personal story", "Who I am", "Introduce yourself, your background, where you come from and how you have changed.", "Background · Grow up · Experience · Currently")]),
 ("Interests, passions & free time", "Talk about your tastes, hobbies and curiosity.", [
   ("Hobbies", "My hobbies & passions", "Say what you like doing, why, and for how long.", "Be into · Be keen on · Enjoy · Take up"),
   ("Culture", "Music, films & books", "Talk about your favourite artists, films, series and books, and recommend them.", "Soundtrack · Plot · Character · Recommend"),
   ("Sport & wellbeing", "Sports & healthy habits", "Describe your physical activities, your energy and your wellbeing habits.", "Work out · Stay fit · Practise · Improve"),
   ("Travel", "Travel & memorable experiences", "Tell the story of a trip, describe a place and talk about where you want to go.", "Explore · Journey · Sightseeing · Memorable")]),
 ("Work, studies & ambitions", "Communicate at work and in your studies.", [
   ("Work", "My job & working day", "Present your job, your tasks, your colleagues and your working day.", "In charge of · Deal with · Deadline · Colleague"),
   ("Studies", "My studies & learning", "Talk about your studies, your subjects, your difficulties and your methods.", "Major in · Assignment · Skill · Make progress"),
   ("Career", "Goals, plans & career", "Present your goals, your plans, your motivation and your next steps.", "Aim to · Plan to · Would like to · Eventually"),
   ("Problems", "Challenges & problem-solving", "Explain a problem, ask for help and suggest solutions.", "Run into · Figure out · Work out · Sort out")]),
 ("People, relationships & social life", "Build connections and keep a conversation going.", [
   ("Family", "Family & friends", "Introduce the people close to you, describe your relationships and share moments together.", "Get along · Close to · Support · Spend time"),
   ("Socialising", "Meeting people & small talk", "Start a conversation, ask questions and answer naturally.", "By the way · How about you? · Nice to meet you"),
   ("Feelings", "Feelings & personality", "Describe your character, your emotions, your reactions and your needs.", "Feel like · Proud of · Worried about · Rather"),
   ("Relationships", "Communication & relationships", "Express agreement, limits and expectations, and resolve a disagreement.", "Understand · Mean · Agree · Set boundaries")]),
 ("Practical everyday situations", "Handle common situations with ease.", [
   ("Food", "Food, cooking & restaurants", "Order, describe a dish, talk about your preferences and cook.", "Order · Ingredients · Taste · Well-done"),
   ("Shopping", "Shopping & money", "Ask a price, compare, buy, return an item and talk about your budget.", "Affordable · Receipt · Refund · Worth it"),
   ("Transport", "Getting around", "Ask for directions, use public transport and explain a delay.", "Get on · Get off · Transfer · Delayed"),
   ("Services", "Appointments & everyday services", "Make an appointment, phone, explain a request and make a complaint.", "Book · Reschedule · Available · Complaint")]),
 ("Ideas, opinions & storytelling", "Move from short answers to personal, structured speech.", [
   ("Opinions", "Giving opinions & explaining why", "Give your opinion, justify it, add nuance and react to another point of view.", "I believe · From my point of view · Whereas"),
   ("Storytelling", "Tell a story about your life", "Tell about a memory, a success, a mistake or an experience that mattered.", "At first · Eventually · Looking back · As a result"),
   ("Hypotheticals", "Dreams & what-if situations", "Imagine, compare possibilities and talk about hypothetical situations.", "If I could · I would rather · Suppose"),
   ("Conversation", "Keep a conversation going", "Follow up, clarify, rephrase, bounce back and go beyond short answers.", "What do you mean? · That reminds me · Tell me more")]),
]

PROGRESSION_PARLER = [
 ("A1–A2", "Name, describe, answer in simple sentences and talk about your habits."),
 ("B1", "Tell, explain, compare and hold a conversation for several minutes."),
 ("B2", "Develop a point of view, add nuance, argue and interact spontaneously."),
 ("C1", "Express yourself with precision, naturalness, subtlety and awareness of context."),
]
