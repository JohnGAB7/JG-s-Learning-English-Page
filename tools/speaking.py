"""Shared Speak catalogue and bilingual pilot learning units.

The existing six universes and 24 topics are kept in their original order.
Topic IDs are language-independent and never derived from translated titles.
"""
LEVELS = ("A1", "A2", "B1", "B2", "C1")

RELATED_LESSONS = {"daily-routine": [6, 7, 21, 29], "food-dining-out": [26, 30]}

BASE_IDS = [
    ["daily-routine", "evening-routine", "home-neighbourhood", "personal-introduction"],
    ["hobbies", "culture-music-film-books", "sports-wellbeing", "travel-experiences"],
    ["workday", "studies-learning", "goals-career", "challenges-problem-solving"],
    ["family-friends", "meeting-people-small-talk", "feelings-personality", "relationships-communication"],
    ["food-dining-out", "shopping-money", "transport-getting-around", "appointments-services"],
    ["opinions", "life-stories", "hypotheticals", "conversation-flow"],
]

ADDITIONS = {
"en": {
0: [
("childhood-memories","Real-life conversation","Childhood memories","Describe childhood routines, places, people and memorable moments.","Grow up · Used to · Remind me of"),
("immigration-experiences","Real-life conversation","Moving abroad and immigration","Explain why people move, describe settling in and share cross-cultural experiences.","Move abroad · Settle in · Belong · Adapt"),
],
1: [
("movies-tv","Culture","Movies and TV","Discuss genres, plots, characters, reviews and recommendations.","Plot · Cast · Episode · Worth watching"),
("books-reading","Culture","Books and reading","Describe books, reading habits, favourite authors and recommendations.","Page-turner · Chapter · Fiction · Engaging"),
("outdoor-adventures","Outdoor life","Outdoor adventures","Plan a walk or trip, describe landscapes and talk about an unexpected challenge.","Trail · Hike · Viewpoint · Get lost"),
("sports-photography","Sport and creativity","Sports and photography","Talk about sport, taking photographs and capturing a decisive moment.","Capture · Frame · Action shot · Competition"),
],
2: [
("meetings-teamwork","Work","Meetings and teamwork","Contribute to a meeting, clarify responsibilities and agree on next steps.","Agenda · Follow up · Deadline · Take ownership"),
("collaborating-event","Organisation","Organising an event together","Suggest ideas, divide tasks, compare options and coordinate an event.","Venue · Budget · Arrange · Run through"),
("productivity-hacks","Work habits","Productivity and time management","Explain routines, prioritise tasks and evaluate ways of working.","Prioritise · Focus time · Get things done · Procrastinate"),
("goals-achievements","Personal growth","Goals and achievements","Set goals, describe progress, explain setbacks and celebrate results.","Milestone · Achieve · Setback · Make progress"),
],
3: [
("managing-stress","Wellbeing","Managing stress","Describe pressure, explain what helps and discuss ways to respond.","Under pressure · Cope with · Take a break · Overwhelmed"),
("social-media","Digital life","Social media and digital life","Discuss online habits, digital communication, privacy and influence.","Feed · Scroll · Privacy settings · Misinformation"),
("relationships-boundaries","Relationships","Relationships and boundaries","Express expectations, negotiate boundaries and handle sensitive conversations.","Respect · Boundary · Misunderstanding · Bring up"),
],
4: [
("online-shopping","Shopping","Online shopping","Compare products, check delivery details, return an item and request a refund.","Delivery slot · In stock · Return policy · Refund"),
("commuting-transport","Transport","Commuting and transport","Describe a commute, compare transport options and explain disruptions.","Commute · Rush hour · Transfer · Service disruption"),
("making-plans","Social life","Making plans and organising activities","Suggest an activity, check availability and agree on a practical plan.","Are you free…? · How about…? · Works for me · Reschedule"),
],
5: [
("news-discussion","Ideas and society","Discussing the news","Summarise a story, distinguish fact from opinion and discuss its implications.","According to · Reportedly · Evidence · Point of view"),
("future-scenarios","Ideas and society","The future and possible scenarios","Talk about predictions, intentions, uncertainty and possible changes.","Likely to · In the long run · Scenario · Tend to"),
],
},
"fr": {
0: [
("childhood-memories","Souvenirs","Les souvenirs d’enfance","Décrire les habitudes, les lieux, les personnes et les moments marquants de l’enfance.","Grandir · Avoir l’habitude de · Me rappeler"),
("immigration-experiences","Mobilité","Partir vivre à l’étranger et immigrer","Expliquer les raisons d’un départ, raconter son installation et partager une expérience interculturelle.","Partir à l’étranger · S’installer · Trouver sa place · S’adapter"),
],
1: [
("movies-tv","Culture","Films et séries","Parler des genres, des intrigues, des personnages, donner un avis et recommander un film ou une série.","Intrigue · Distribution · Épisode · À voir absolument"),
("books-reading","Culture","Livres et lecture","Présenter des livres, ses habitudes de lecture, ses auteurs préférés et ses recommandations.","Livre captivant · Chapitre · Fiction · Prenant"),
("outdoor-adventures","Plein air","Aventures en plein air","Préparer une sortie, décrire un paysage et raconter un imprévu.","Sentier · Randonnée · Point de vue · Se perdre"),
("sports-photography","Sport et créativité","Sport et photographie","Parler de sport, de photographie et de la manière de saisir un instant décisif.","Capturer · Cadrer · Photo d’action · Compétition"),
],
2: [
("meetings-teamwork","Travail","Réunions et travail en équipe","Participer à une réunion, clarifier les responsabilités et convenir des prochaines étapes.","Ordre du jour · Faire le suivi · Échéance · Prendre en charge"),
("collaborating-event","Organisation","Organiser un événement à plusieurs","Proposer des idées, répartir les tâches, comparer les options et coordonner un événement.","Lieu · Budget · Organiser · Passer en revue"),
("productivity-hacks","Méthodes de travail","Productivité et gestion du temps","Présenter ses routines, hiérarchiser les tâches et évaluer ses méthodes de travail.","Hiérarchiser · Temps de concentration · Avancer · Procrastiner"),
("goals-achievements","Développement personnel","Objectifs et réussites","Définir des objectifs, présenter ses progrès, expliquer les obstacles et célébrer les résultats.","Étape clé · Atteindre · Revers · Progresser"),
],
3: [
("managing-stress","Bien-être","Gérer le stress","Décrire la pression, expliquer ce qui aide et discuter des façons d’y faire face.","Sous pression · Faire face à · Faire une pause · Dépassé"),
("social-media","Vie numérique","Réseaux sociaux et vie numérique","Parler de ses habitudes en ligne, de communication numérique, de vie privée et d’influence.","Fil d’actualité · Faire défiler · Paramètres de confidentialité · Désinformation"),
("relationships-boundaries","Relations","Relations et limites personnelles","Exprimer ses attentes, négocier des limites et gérer des conversations délicates.","Respecter · Limite · Malentendu · Aborder"),
],
4: [
("online-shopping","Achats","Achats en ligne","Comparer des produits, vérifier la livraison, retourner un article et demander un remboursement.","Créneau de livraison · En stock · Politique de retour · Remboursement"),
("commuting-transport","Transports","Trajets domicile-travail et transports","Décrire son trajet, comparer les moyens de transport et expliquer une perturbation.","Trajet quotidien · Heure de pointe · Correspondance · Perturbation du service"),
("making-plans","Vie sociale","Faire des projets et organiser des activités","Proposer une activité, vérifier les disponibilités et convenir d’un programme concret.","Tu es libre… ? · Et si… ? · Ça me va · Reprogrammer"),
],
5: [
("news-discussion","Idées et société","Discuter de l’actualité","Résumer une information, distinguer les faits des opinions et discuter de ses implications.","Selon · D’après les informations · Preuve · Point de vue"),
("future-scenarios","Idées et société","Le futur et les scénarios possibles","Parler de prévisions, d’intentions, d’incertitude et de changements possibles.","Susceptible de · À long terme · Scénario · Avoir tendance à"),
],
}
}

PILOTS = {
"en": {
"daily-routine": {
"scenario":"You meet a new classmate and explain a normal weekday.",
"outcomes":["Say when you get up","Describe three daily actions","Ask a simple question about another person's routine"],
"dialogue":[["Mia","What time do you get up?"],["Alex","I get up at seven. I have breakfast at half past seven."],["Mia","Do you go to work by bus?"],["Alex","Yes, I do. I leave home at eight."]],
"expressions":["I usually get up at…","I have breakfast at…","I leave home at…","How about you?"],
"vocabulary":[["get up","I get up at seven.","leave your bed"],["get dressed","I get dressed after breakfast.","put your clothes on"],["have breakfast","I have breakfast at home.","eat the first meal of the day"],["leave home","I leave home at eight.","go out of your home"],["usually","I usually walk to work.","in most situations"]],
"grammar":"Present simple: I/you/we/they + base verb. Use do/does to ask questions: What time do you get up?",
"pronunciation":"Stress the important time words: I get UP at SEVen. Keep get up connected when you speak naturally.",
"questions":["What time do you get up?","What do you do before work or school?","How do you travel there?"],
"roleplay":"Student A asks about a weekday. Student B answers with three true details, then asks the same questions.",
"free_speaking":"Speak for 30 seconds about your morning. Use three time expressions.",
"writing":"Write four short sentences about your morning.",
"self_check":["I can say what time I get up.","I can describe three actions.","I can ask about another person's routine."]
},
"food-dining-out": {
"scenario":"You are at a restaurant. You order a meal, ask about a dish and request the bill.",
"outcomes":["Ask for a table and a menu","Order food politely","Ask for information and the bill"],
"dialogue":[["Server","Good evening. Do you have a reservation?"],["Guest","No, we don't. Do you have a table for two?"],["Server","Certainly. Here are your menus. Would you like something to drink?"],["Guest","Still water, please. What do you recommend?"],["Server","The grilled salmon is very popular."],["Guest","That sounds lovely. I'll have that, please. Could we have the bill when you're ready?"]],
"expressions":["Do you have a table for two?","Could I see the menu, please?","What do you recommend?","I'll have…","Could we have the bill, please?"],
"vocabulary":[["menu","Could I see the menu, please?","the list of food and drinks"],["starter","I'll have soup for a starter.","the first small course"],["main course","The fish is my main course.","the principal dish"],["recommend","What would you recommend?","suggest something as a good choice"],["bill","Could we have the bill, please?","the amount you need to pay"]],
"grammar":"Use would like / could for polite requests. Use I'll have… when choosing from a menu.",
"pronunciation":"In polite requests, keep the tone friendly and let please fall gently at the end. Link could you and could we smoothly.",
"questions":["What do you usually order at a restaurant?","Do you prefer eating in or taking food away?","What would you recommend to a visitor?"],
"roleplay":"Take turns being the server and the guest. Order a main course, ask one question and request the bill.",
"free_speaking":"Speak for 45–60 seconds about a restaurant you recommend. Explain what makes it good.",
"writing":"Write a short online review of a restaurant you know.",
"self_check":["I can order politely.","I can ask about a dish.","I can request the bill."]
}
},
"fr": {
"daily-routine": {
"scenario":"Tu rencontres un nouveau camarade et tu lui décris une journée habituelle.",
"outcomes":["Dire à quelle heure tu te lèves","Décrire trois actions quotidiennes","Poser une question simple sur la routine de l’autre"],
"dialogue":[["Mia","What time do you get up?"],["Alex","I get up at seven. I have breakfast at half past seven."],["Mia","Do you go to work by bus?"],["Alex","Yes, I do. I leave home at eight."]],
"expressions":["I usually get up at… — Je me lève généralement à…","I have breakfast at… — Je prends mon petit-déjeuner à…","I leave home at… — Je quitte la maison à…","How about you? — Et toi ?"],
"vocabulary":[["get up","I get up at seven.","se lever"],["get dressed","I get dressed after breakfast.","s’habiller"],["have breakfast","I have breakfast at home.","prendre le petit-déjeuner"],["leave home","I leave home at eight.","quitter la maison"],["usually","I usually walk to work.","généralement"]],
"grammar":"Present simple : I/you/we/they + base verbale. Pour poser une question, utilise do/does : What time do you get up?",
"pronunciation":"Accentue les mots importants : I get UP at SEVen. Relie naturellement get et up.",
"questions":["What time do you get up? — À quelle heure te lèves-tu ?","What do you do before work or school? — Que fais-tu avant le travail ou les cours ?","How do you travel there? — Comment t’y rends-tu ?"],
"roleplay":"À deux : une personne interroge l’autre sur sa journée. Réponds avec trois détails vrais, puis inversez les rôles.",
"free_speaking":"Parle pendant 30 secondes de ta matinée. Utilise trois expressions de temps.",
"writing":"Écris quatre phrases courtes sur ta matinée.",
"self_check":["Je peux dire à quelle heure je me lève.","Je peux décrire trois actions.","Je peux poser une question sur la routine de quelqu’un."]
},
"food-dining-out": {
"scenario":"Tu es au restaurant. Tu commandes un repas, poses une question sur un plat et demandes l’addition.",
"outcomes":["Demander une table et une carte","Commander poliment","Demander une information et l’addition"],
"dialogue":[["Server","Good evening. Do you have a reservation?"],["Guest","No, we don't. Do you have a table for two?"],["Server","Certainly. Here are your menus. Would you like something to drink?"],["Guest","Still water, please. What do you recommend?"],["Server","The grilled salmon is very popular."],["Guest","That sounds lovely. I'll have that, please. Could we have the bill when you're ready?"]],
"expressions":["Do you have a table for two? — Avez-vous une table pour deux ?","Could I see the menu, please? — Puis-je voir la carte, s’il vous plaît ?","What do you recommend? — Que recommandez-vous ?","I'll have… — Je vais prendre…","Could we have the bill, please? — Pourrions-nous avoir l’addition, s’il vous plaît ?"],
"vocabulary":[["menu","Could I see the menu, please?","la carte"],["starter","I'll have soup for a starter.","l’entrée"],["main course","The fish is my main course.","le plat principal"],["recommend","What would you recommend?","recommander"],["bill","Could we have the bill, please?","l’addition"]],
"grammar":"Utilise would like / could pour formuler une demande polie. Utilise I'll have… pour choisir sur la carte.",
"pronunciation":"Dans une demande polie, garde une intonation chaleureuse et fais descendre doucement la voix sur please. Relie could you et could we.",
"questions":["What do you usually order at a restaurant? — Que commandes-tu habituellement au restaurant ?","Do you prefer eating in or taking food away? — Préfères-tu manger sur place ou emporter ?","What would you recommend to a visitor? — Que recommanderais-tu à un visiteur ?"],
"roleplay":"Jouez à tour de rôle le serveur et le client. Commande un plat, pose une question et demande l’addition.",
"free_speaking":"Parle pendant 45 à 60 secondes d’un restaurant que tu recommandes. Explique ce qui le rend intéressant.",
"writing":"Rédige un court avis en ligne sur un restaurant que tu connais.",
"self_check":["Je peux commander poliment.","Je peux poser une question sur un plat.","Je peux demander l’addition."]
}
}
}

def build_catalogue(themes, lang):
    additions = ADDITIONS[lang]
    pilots = PILOTS[lang]
    categories, topics = [], []
    for ci, (category_title, category_desc, base_topics) in enumerate(themes):
        category_id = f"universe-{ci+1:02d}"
        categories.append({"id":category_id,"title":category_title,"description":category_desc,"order":ci+1})
        for ti, (tag,title,desc,keywords) in enumerate(base_topics):
            topic_id = BASE_IDS[ci][ti]
            unit_levels = {level:{"status":"planned"} for level in LEVELS}
            if topic_id in pilots:
                unit_levels["A1" if topic_id=="daily-routine" else "A2"] = {"status":"published", **pilots[topic_id]}
            if topic_id == "culture-music-film-books":
                if lang == "en":
                    title, desc, keywords = "Music and cultural interests", "Talk about music, favourite artists, concerts and cultural activities.", "Artist · Concert · Performance · Recommend"
                else:
                    title, desc, keywords = "Musique et découvertes culturelles", "Parler de musique, de ses artistes préférés, de concerts et d’activités culturelles.", "Artiste · Concert · Spectacle · Recommander"
            if topic_id == "food-dining-out":
                if lang == "en":
                    title, desc, keywords = "Dining out, food and restaurants", "Choose a restaurant, order politely, discuss dishes and ask for the bill.", "Menu · Order · Dish · Bill"
                else:
                    title, desc, keywords = "Restaurants, repas et sorties", "Choisir un restaurant, commander poliment, parler des plats et demander l’addition.", "Carte · Commander · Plat · Addition"
            topics.append({"id":topic_id,"category_id":category_id,"tag":tag,"title":title,"description":desc,
                           "keywords":[x.strip() for x in keywords.split("·")],"levels":unit_levels,"related_lesson_ids":RELATED_LESSONS.get(topic_id,[])})
        for topic_id,tag,title,desc,keywords in additions.get(ci,[]):
            topics.append({"id":topic_id,"category_id":category_id,"tag":tag,"title":title,"description":desc,
                           "keywords":[x.strip() for x in keywords.split("·")],
                           "levels":{level:{"status":"planned"} for level in LEVELS},"related_lesson_ids":[]})
    return {
        "version":1,"levels":list(LEVELS),
        "entry_point":{"id":"start-from-zero","title":"Start from zero" if lang=="en" else "Commencer de zéro",
                       "description":"A calm first step for learners who cannot yet say anything in English." if lang=="en" else "Un premier pas rassurant pour les personnes qui ne savent encore rien dire en anglais.",
                       "status":"published","level":"pre-A1"},
        "categories":categories,"topics":topics
    }

def validate_catalogue(catalogue):
    category_ids={c["id"] for c in catalogue["categories"]}
    seen=set()
    for topic in catalogue["topics"]:
        assert topic["id"] not in seen, f"Duplicate topic ID: {topic['id']}"
        seen.add(topic["id"])
        assert topic["category_id"] in category_ids
        assert all(isinstance(i, int) and 1 <= i <= 290 for i in topic.get("related_lesson_ids", []))
        assert set(topic["levels"])==set(LEVELS)
        for level,unit in topic["levels"].items():
            assert unit["status"] in {"planned","draft","needs_review","reviewed","published"}
            if unit["status"]=="published":
                required={"scenario","outcomes","dialogue","expressions","vocabulary","grammar","pronunciation","questions","roleplay","free_speaking","writing","self_check"}
                assert required.issubset(unit), f"Incomplete unit {topic['id']} {level}"
                assert unit["dialogue"] and unit["vocabulary"] and unit["questions"]
    return True
