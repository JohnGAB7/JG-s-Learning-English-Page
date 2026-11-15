# A1 and A2 lessons, written in simple English (the whole site is English-only).
# Fields: n, niveau, titre, intro, regle[list], formule, exemples[list of [sentence, note]],
# mots[5 x [word, example sentence, simple English meaning]], exercice[list], corrige[list], piege.

NOTIONS = [
# ---------------------------------------------------------------- A1
{
 "n": 1, "niveau": "A1", "titre": "The verb “to be”",
 "intro": "The most useful verb in English. Use it to say who you are, how you feel and where you are.",
 "regle": [
  "“To be” changes with the person: I am, you are, he/she/it is, we are, they are.",
  "In speech and in messages, we almost always use the short form: I'm, you're, he's, she's, it's, we're, they're.",
  "An English sentence always needs a subject: “It is late”, never “Is late”."
 ],
 "formule": "I am · you are · he / she / it is · we are · they are",
 "exemples": [
  ["I am a student.", "I + am"],
  ["She's an engineer.", "she + is → she's"],
  ["We are at home.", "we + are"],
  ["It's cold today.", "the subject “it” is necessary"]
 ],
 "mots": [
  ["student", "I am a student.", "a person who studies at a school or university"],
  ["ready", "Are you ready?", "prepared to do something"],
  ["tired", "I'm tired tonight.", "needing rest or sleep"],
  ["busy", "She is very busy.", "with a lot of things to do"],
  ["home", "They are at home.", "the place where you live"]
 ],
 "exercice": [
  "Complete: I ___ happy.",
  "Complete: They ___ in Brussels.",
  "Complete: My brother ___ a developer.",
  "Write the short form: we are → ___"
 ],
 "corrige": ["am", "are", "is", "we're"],
 "piege": "For age, use “to be”, not “have”: “I am 25”, not “I have 25”. The same for hunger and cold: I'm hungry, I'm cold."
},
{
 "n": 2, "niveau": "A1", "titre": "Introducing yourself",
 "intro": "Say your name, your country, your city and your job in a few simple sentences.",
 "regle": [
  "Your name: “My name is …” or “I'm …”.",
  "Where you come from: “I'm from Cameroon / Belgium / Canada.”",
  "The city where you live: “I live in Yaoundé.”",
  "Your job: “I'm a nurse / an engineer”. Always put a or an before a job."
 ],
 "formule": "My name is … · I'm from … · I live in … · I'm a / an …",
 "exemples": [
  ["Hi, my name is Paul.", "your name"],
  ["I'm from Cameroon, but I live in Brussels.", "origin + city"],
  ["I'm a teacher.", "a + job"],
  ["Nice to meet you!", "what you say when you meet someone new"]
 ],
 "mots": [
  ["name", "What's your name?", "the word people call you"],
  ["live", "I live in Douala.", "to have your home in a place"],
  ["job", "What's your job?", "the work you do for money"],
  ["meet", "Nice to meet you.", "to see and talk to someone for the first time"],
  ["country", "My country is Belgium.", "a nation, like France or Canada"]
 ],
 "exercice": [
  "Say it in English: you come from France.",
  "Say it in English: your job is engineer.",
  "Complete: Nice to ___ you.",
  "Ask a person about their job."
 ],
 "corrige": ["I'm from France.", "I'm an engineer.", "meet", "What's your job? (or: What do you do?)"],
 "piege": "Don't forget the article: “I'm a doctor”, never “I'm doctor”. Before a vowel sound, use an: an engineer, an accountant."
},
{
 "n": 3, "niveau": "A1", "titre": "Numbers from 0 to 20",
 "intro": "Count, give your age, a phone number or a quantity.",
 "regle": [
  "0 zero, 1 one, 2 two, 3 three, 4 four, 5 five, 6 six, 7 seven, 8 eight, 9 nine, 10 ten.",
  "11 eleven, 12 twelve, 13 thirteen, 14 fourteen, 15 fifteen, 16 sixteen, 17 seventeen, 18 eighteen, 19 nineteen, 20 twenty.",
  "From 13 to 19, the stress is on the end: thirTEEN. For 30, 40… (thirty, forty), the stress is at the start: THIRty.",
  "For a phone number, say each digit separately. People often say 0 as “oh”."
 ],
 "formule": "13–19: -teen (stress at the end) · 20, 30…: -ty (stress at the start)",
 "exemples": [
  ["I am nineteen years old.", "age with “to be”"],
  ["There are twelve students in the class.", "a quantity"],
  ["My number is oh-four-seven-five…", "one digit at a time"]
 ],
 "mots": [
  ["number", "What's your phone number?", "a figure like 1, 2 or 3"],
  ["old", "How old are you?", "used to talk about age"],
  ["count", "Can you count to twenty?", "to say numbers in order"],
  ["year", "I'm twenty years old.", "a period of twelve months"],
  ["phone", "My phone is new.", "a device you use to call people"]
 ],
 "exercice": [
  "Write in words: 14",
  "Write in words: 18",
  "Ask a person their age.",
  "Which one has the stress at the end: fifteen or fifty?"
 ],
 "corrige": ["fourteen", "eighteen", "How old are you?", "fifteen (fifTEEN). We say FIFty."],
 "piege": "Watch the spelling: forty (40) has no “u”, but four (4) has one. And twelve (12) follows no rule."
},
{
 "n": 4, "niveau": "A1", "titre": "“To be”: negatives and questions",
 "intro": "Say what you are not, and ask simple questions with “to be”.",
 "regle": [
  "Negative: add “not” after the verb: I'm not, you aren't, he isn't, we aren't, they aren't.",
  "Question: put the verb before the subject: Are you ready? Is she at work?",
  "Short answers: Yes, I am. / No, I'm not. Yes, it is. / No, it isn't."
 ],
 "formule": "Negative: subject + be + not · Question: Be + subject … ?",
 "exemples": [
  ["I'm not tired.", "negative"],
  ["The code isn't ready.", "is not → isn't"],
  ["Are you a student? — Yes, I am.", "question + short answer"],
  ["Is it correct? — No, it isn't.", "question + short answer"]
 ],
 "mots": [
  ["correct", "Is it correct?", "right, with no mistakes"],
  ["late", "Sorry, I'm late.", "after the expected time"],
  ["open", "Is the shop open?", "not closed; you can go in"],
  ["sure", "Are you sure?", "certain"],
  ["right", "You're right.", "correct; true"]
 ],
 "exercice": [
  "Make it negative: She is at home.",
  "Make it a question: They are ready.",
  "Give a short answer (no): Is he your brother?",
  "Correct the mistake: I amn't hungry."
 ],
 "corrige": ["She isn't at home. (She's not at home.)", "Are they ready?", "No, he isn't.", "I'm not hungry."],
 "piege": "A positive short answer is never contracted: “Yes, I am”, not “Yes, I'm”."
},
{
 "n": 5, "niveau": "A1", "titre": "“Have got” (possession)",
 "intro": "Say what you have: a family, an object, a problem.",
 "regle": [
  "Form: I / you / we / they have got (I've got); he / she / it has got (she's got).",
  "Negative: I haven't got, she hasn't got.",
  "Question: Have you got a car? — Yes, I have. / No, I haven't.",
  "“Have got” is mostly British. In the US and Canada, people usually say “I have / Do you have…?”."
 ],
 "formule": "have got / has got · haven't got / hasn't got · Have … got … ?",
 "exemples": [
  ["I've got two brothers.", "I have got → I've got"],
  ["She hasn't got a laptop.", "negative"],
  ["Have you got a minute?", "British question"],
  ["Do you have a minute?", "the same question in American English"]
 ],
 "mots": [
  ["brother", "I've got a brother.", "a boy or man with the same parents as you"],
  ["sister", "She's got two sisters.", "a girl or woman with the same parents as you"],
  ["laptop", "Have you got a laptop?", "a small computer you can carry"],
  ["minute", "Have you got a minute?", "sixty seconds; a short time"],
  ["problem", "We've got a problem.", "something difficult that needs a solution"]
 ],
 "exercice": [
  "Complete: He ___ got a new phone.",
  "Make it negative: They have got a car.",
  "Make it a question: You have got a pen.",
  "Say it the American way: Have you got a minute?"
 ],
 "corrige": ["has", "They haven't got a car.", "Have you got a pen?", "Do you have a minute?"],
 "piege": "“She's got” = she has got (possession), but “she's tired” = she is tired. The context shows the difference."
},
{
 "n": 6, "niveau": "A1", "titre": "The present simple",
 "intro": "Talk about habits, general facts and your daily routine.",
 "regle": [
  "Form: the base verb (I work, they work), with -s for he, she and it: he works, she lives.",
  "Negative: don't / doesn't + base verb: I don't work, she doesn't work.",
  "Question: Do / Does + subject + base verb: Do you work? Does she live here?",
  "After does and doesn't, the verb loses its -s: “Does she work?”, not “Does she works?”."
 ],
 "formule": "he / she / it + verb-s · don't / doesn't + base · Do / Does … + base ?",
 "exemples": [
  ["I work in a bank.", "a fact about my life"],
  ["He studies computer science.", "study → studies"],
  ["She doesn't drink coffee.", "doesn't + base verb"],
  ["Do you speak English?", "Do + subject + base verb"]
 ],
 "mots": [
  ["work", "I work from 8 to 5.", "to do a job"],
  ["study", "She studies at university.", "to learn about a subject"],
  ["speak", "Do you speak English?", "to use a language"],
  ["every day", "I read every day.", "on all days, daily"],
  ["usually", "We usually eat at 7.", "in most cases, normally"]
 ],
 "exercice": [
  "Complete: My father ___ (work) in Douala.",
  "Make it negative: She likes tea.",
  "Make it a question: They live in Liège.",
  "Correct the mistake: Does he speaks French?"
 ],
 "corrige": ["works", "She doesn't like tea.", "Do they live in Liège?", "Does he speak French?"],
 "piege": "Spelling of the -s: study → studies, go → goes, watch → watches, have → has."
},
{
 "n": 7, "niveau": "A1", "titre": "Adverbs of frequency",
 "intro": "Say how often you do something: always, often, never…",
 "regle": [
  "From most to least frequent: always, usually, often, sometimes, rarely, never.",
  "They go BEFORE the main verb: I often read. She never drinks coffee.",
  "But they go AFTER the verb “to be”: I'm always late. He's never tired.",
  "To ask: How often do you…?"
 ],
 "formule": "subject + adverb + verb · subject + be + adverb",
 "exemples": [
  ["I always get up at 6.", "adverb before the verb"],
  ["She often works late.", "adverb before the verb"],
  ["We are never bored.", "adverb after “be”"],
  ["How often do you play football?", "question about frequency"]
 ],
 "mots": [
  ["always", "I always check my emails.", "every time"],
  ["often", "He often travels.", "many times"],
  ["sometimes", "Sometimes I walk to work.", "on some occasions, not always"],
  ["never", "She never smokes.", "not at any time"],
  ["get up", "I get up early.", "to leave your bed in the morning"]
 ],
 "exercice": [
  "Put the adverb in the right place: I drink coffee. (often)",
  "Put the adverb in the right place: He is late. (never)",
  "Complete: She ___ goes to the cinema. (on some occasions)",
  "Ask a friend how often they study."
 ],
 "corrige": ["I often drink coffee.", "He is never late.", "sometimes", "How often do you study?"],
 "piege": "“Never” is already negative: “I never eat meat”, never “I don't never eat meat”."
},
{
 "n": 8, "niveau": "A1", "titre": "The present continuous",
 "intro": "Describe what is happening now, at this moment.",
 "regle": [
  "Form: be (am / is / are) + verb-ing: I am working, she is reading.",
  "Use it for an action in progress (now, right now, at the moment) or a temporary situation (this week).",
  "Negative: I'm not working. Question: Are you working?",
  "Some state verbs are not used with -ing: know, like, want, need, understand."
 ],
 "formule": "am / is / are + verb-ing",
 "exemples": [
  ["I'm studying English right now.", "an action in progress"],
  ["She's talking on the phone.", "happening now"],
  ["They aren't working this week.", "a temporary situation"],
  ["What are you doing?", "a question about now"]
 ],
 "mots": [
  ["right now", "I'm busy right now.", "at this exact moment"],
  ["at the moment", "She's working at the moment.", "now, for this period"],
  ["wait", "I'm waiting for the bus.", "to stay until something happens"],
  ["cook", "He's cooking dinner.", "to prepare food with heat"],
  ["rain", "It's raining.", "water falling from the sky"]
 ],
 "exercice": [
  "Complete: Listen! The baby ___ (cry).",
  "Make it negative: We are watching TV.",
  "Make it a question: He is working now.",
  "Choose: I ___ (know / am knowing) the answer."
 ],
 "corrige": ["is crying", "We aren't watching TV.", "Is he working now?", "know (a state verb)"],
 "piege": "Spelling: make → making (drop the e), run → running (double the consonant), lie → lying."
},
{
 "n": 9, "niveau": "A1", "titre": "Present simple or present continuous?",
 "intro": "Choose the right present: a habit or a fact, or something happening now.",
 "regle": [
  "Present simple: habits, routines and facts that are always true: I work in a bank. Water boils at 100 °C.",
  "Present continuous: an action happening now or around now: I'm working from home this week.",
  "Time words help: every day, usually, often, never → present simple; now, right now, at the moment, today, this week → present continuous.",
  "State verbs (know, like, love, want, need, understand, believe) stay in the present simple, even now: I know the answer."
 ],
 "formule": "habit / fact → I work · now / temporary → I'm working",
 "exemples": [
  ["I usually drink tea, but today I'm drinking coffee.", "habit vs. today"],
  ["She lives in Brussels.", "a permanent situation"],
  ["She's living with a friend this month.", "a temporary situation"],
  ["Do you understand? — Yes, I understand.", "state verb: present simple"]
 ],
 "mots": [
  ["usually", "I usually walk to work.", "in most cases, normally"],
  ["today", "Today I'm working late.", "on this day"],
  ["this week", "He's on holiday this week.", "during the present week"],
  ["understand", "I understand the question.", "to know the meaning of something"],
  ["wear", "She's wearing a red coat.", "to have clothes on your body"]
 ],
 "exercice": [
  "Choose: I (read / am reading) a book now.",
  "Choose: He (plays / is playing) football every Saturday.",
  "Choose: I (want / am wanting) a glass of water.",
  "Complete: Look! It ___ (snow)."
 ],
 "corrige": ["am reading", "plays", "want (a state verb)", "is snowing"],
 "piege": "Don't use the continuous for a habit: “I go to the gym every day”, not “I am going to the gym every day”."
},
{
 "n": 10, "niveau": "A1", "titre": "Subject and object pronouns",
 "intro": "Use the right pronoun: the person who does the action, or the person who receives it.",
 "regle": [
  "Subject pronouns come before the verb: I, you, he, she, it, we, they: “She calls me every day.”",
  "Object pronouns come after the verb or after a preposition: me, you, him, her, it, us, them: “I know him.” “This is for them.”",
  "“You” and “it” are the same in both positions: “You see it. It sees you.”",
  "Use “it” for things and animals, “they / them” for plural people and things."
 ],
 "formule": "I → me · he → him · she → her · we → us · they → them · you / it (no change)",
 "exemples": [
  ["I love my parents. I call them every Sunday.", "they → them"],
  ["Where is Paul? I can't see him.", "he → him"],
  ["She helps us with our homework.", "we → us"],
  ["This message is for you.", "after a preposition"]
 ],
 "mots": [
  ["call", "I call her every day.", "to phone someone"],
  ["help", "Can you help me?", "to make something easier for someone"],
  ["know", "Do you know him?", "to have met someone before"],
  ["with", "Come with us!", "together with"],
  ["for", "This gift is for you.", "intended to be given to"]
 ],
 "exercice": [
  "Complete: My sister lives in Paris. I visit ___ every year.",
  "Complete: ___ (we) are students.",
  "Complete: Tom and Lisa are my friends. I like ___ a lot.",
  "Correct the mistake: Me and my brother play football."
 ],
 "corrige": ["her", "We", "them", "My brother and I play football."],
 "piege": "After a preposition, use the object form: “between you and me”, not “between you and I”."
},
# ---------------------------------------------------------------- A2
{
 "n": 41, "niveau": "A2", "titre": "The past simple: regular verbs",
 "intro": "Talk about a finished action at a specific time in the past.",
 "regle": [
  "Use it for a finished action, often with a time: yesterday, last week, two days ago, in 2024.",
  "Positive: verb + -ed, the same form for every person: I worked, she worked.",
  "Negative: didn't + base verb: They didn't call. Question: Did + subject + base verb: Did you check?",
  "Pronouncing -ed: /t/ after p, k, s, sh, ch, f (stopped, worked); /d/ after voiced sounds (played); /ɪd/ only after t or d (tested, added)."
 ],
 "formule": "verb-ed · didn't + base · Did … + base ?",
 "exemples": [
  ["I worked late yesterday.", "finished, with a time"],
  ["She studied in Montreal in 2022.", "study → studied"],
  ["We didn't expect such a fall.", "didn't + base verb"],
  ["Did you finish the report?", "Did + subject + base verb"]
 ],
 "mots": [
  ["finish", "I finished the report.", "to complete something"],
  ["expect", "We didn't expect that.", "to think something will happen"],
  ["ago", "two days ago", "before now (used after a period of time)"],
  ["last", "last week", "the one before this one"],
  ["decide", "She decided to stay.", "to make a choice"]
 ],
 "exercice": [
  "Put it in the past: I play football.",
  "Make it negative: They visited Paris.",
  "Make it a question: She called you.",
  "How do you pronounce the end of “wanted”: /t/, /d/ or /ɪd/?"
 ],
 "corrige": ["I played football.", "They didn't visit Paris.", "Did she call you?", "/ɪd/, because the verb ends in t"],
 "piege": "After did / didn't, use the base verb: “Did you call?”, not “Did you called?”. Spelling: study → studied, stop → stopped."
},
{
 "n": 42, "niveau": "A2", "titre": "The past simple: irregular verbs",
 "intro": "Many common verbs have an irregular past form that you need to learn by heart.",
 "regle": [
  "These verbs don't take -ed: go → went, have → had, make → made, take → took, see → saw, get → got, buy → bought, think → thought.",
  "The form is the same for every person: I went, she went.",
  "Negatives and questions work like regular verbs, with did + BASE verb: I didn't go, Did you see…?"
 ],
 "formule": "irregular form · didn't + base · Did … + base ?",
 "exemples": [
  ["I went to the bank yesterday.", "go → went"],
  ["She took the train to Brussels.", "take → took"],
  ["We didn't buy anything.", "didn't + base verb"],
  ["Did you see the news?", "Did + base verb"]
 ],
 "mots": [
  ["went", "I went home early.", "past of go"],
  ["bought", "She bought a ticket.", "past of buy"],
  ["thought", "I thought it was easy.", "past of think"],
  ["took", "It took two hours.", "past of take"],
  ["met", "We met last year.", "past of meet"]
 ],
 "exercice": [
  "Put it in the past: I make a mistake.",
  "Put it in the past: They have a meeting.",
  "Make it negative: He went to work.",
  "Correct the mistake: Did you saw the email?"
 ],
 "corrige": ["I made a mistake.", "They had a meeting.", "He didn't go to work.", "Did you see the email?"],
 "piege": "Never use the irregular form after did: “He didn't go”, not “He didn't went”."
},
{
 "n": 43, "niveau": "A2", "titre": "The past continuous",
 "intro": "Describe an action in progress at a moment in the past, often interrupted by another action.",
 "regle": [
  "Form: was / were + verb-ing: I was working, they were sleeping.",
  "It sets the scene, the action in progress: “At 8 pm, I was cooking.”",
  "With the past simple: the long action in the past continuous, the short action that interrupts it in the past simple: “I was cooking when the phone rang.”",
  "“While” often introduces the long action: “While I was driving, it started to rain.”"
 ],
 "formule": "was / were + verb-ing · long action (continuous) + when + short action (past simple)",
 "exemples": [
  ["I was reading when you called.", "long action + short action"],
  ["They were working at midnight.", "in progress at a time"],
  ["While she was studying, her phone rang.", "while + long action"]
 ],
 "mots": [
  ["while", "while I was driving", "during the time that"],
  ["ring", "The phone rang.", "to make a sound (phone, bell); past: rang"],
  ["happen", "What happened?", "to take place"],
  ["sleep", "I was sleeping.", "to rest with your eyes closed"],
  ["suddenly", "Suddenly, the lights went out.", "quickly and unexpectedly"]
 ],
 "exercice": [
  "Complete: I ___ (watch) TV when he arrived.",
  "Complete: While we ___ (walk), it started to rain.",
  "Complete: What ___ you ___ (do) at 9 pm yesterday?",
  "Choose: She (cooked / was cooking) when I (arrived / was arriving)."
 ],
 "corrige": ["was watching", "were walking", "were … doing", "was cooking … arrived"],
 "piege": "With I, he, she, it: was. With you, we, they: were. “You was” is a mistake."
},
{
 "n": 44, "niveau": "A2", "titre": "“Used to” (past habits)",
 "intro": "Talk about a past habit or situation that is no longer true.",
 "regle": [
  "Form: used to + base verb: I used to play football (but I don't now).",
  "Negative: didn't use to + base verb. Question: Did you use to…?",
  "It only exists in the past. For a present habit, use the present simple or “usually”."
 ],
 "formule": "used to + base · didn't use to · Did … use to … ?",
 "exemples": [
  ["I used to live in Yaoundé.", "not any more"],
  ["She used to smoke, but she stopped.", "a past habit"],
  ["We didn't use to have internet at home.", "negative"],
  ["Did you use to play an instrument?", "question"]
 ],
 "mots": [
  ["anymore", "I don't live there anymore.", "not now, as before"],
  ["childhood", "in my childhood", "the time when you were a child"],
  ["stop", "She stopped smoking.", "to not continue"],
  ["village", "We used to live in a village.", "a very small town in the country"],
  ["change", "Things have changed.", "to become different"]
 ],
 "exercice": [
  "Rewrite with “used to”: When I was a child, I played outside every day.",
  "Make it negative: He used to like coffee.",
  "Make it a question: You used to live in Paris.",
  "Correct the mistake: I use to go to school by bike when I was ten."
 ],
 "corrige": ["When I was a child, I used to play outside every day.", "He didn't use to like coffee.", "Did you use to live in Paris?", "I used to go to school by bike when I was ten."],
 "piege": "Don't confuse it with “be used to + -ing” (to be familiar with): “I'm used to working early” means working early is normal for me."
},
{
 "n": 45, "niveau": "A2", "titre": "“Be going to” (plans and predictions)",
 "intro": "Talk about your plans and about things that are clearly going to happen.",
 "regle": [
  "Form: am / is / are + going to + base verb: I'm going to apply.",
  "A plan you have already decided: “Next year, I'm going to study in Canada.”",
  "A prediction based on what you can see: “Look at the clouds, it's going to rain.”",
  "Negative: I'm not going to… Question: Are you going to…?"
 ],
 "formule": "be + going to + base verb",
 "exemples": [
  ["I'm going to start a business.", "a plan"],
  ["They're going to move to Montreal.", "a decision already made"],
  ["Is she going to apply for the job?", "question"],
  ["Be careful, you're going to fall!", "a prediction from what we see"]
 ],
 "mots": [
  ["plan", "What are your plans?", "something you have decided to do"],
  ["apply", "I'm going to apply.", "to ask officially for a job or a place"],
  ["move", "We're going to move.", "to go and live in a new home"],
  ["save", "I'm going to save money.", "to keep money for later"],
  ["next", "next month", "the one after this one"]
 ],
 "exercice": [
  "Complete: I ___ (visit) my parents next week.",
  "Make it negative: She is going to buy a car.",
  "Make it a question: They are going to travel.",
  "Look at the dark clouds. Make a prediction with “rain”."
 ],
 "corrige": ["am going to visit", "She isn't going to buy a car.", "Are they going to travel?", "It's going to rain."],
 "piege": "Don't forget “be”: “I'm going to work”, not “I going to work”. In speech you often hear “gonna”, but don't write it in a professional email."
},
{
 "n": 46, "niveau": "A2", "titre": "Comparatives",
 "intro": "Compare two things: bigger, cheaper, as good as.",
 "regle": [
  "Short adjectives (one syllable, or two syllables ending in -y): add -er: cheap → cheaper, big → bigger, easy → easier.",
  "Long adjectives: more + adjective: more expensive, more interesting.",
  "Compare with “than”: “Toronto is bigger than Ottawa.”",
  "The same level: as … as. A lower level: less … than or not as … as.",
  "To add nuance: much / far bigger (a big difference), a bit cheaper (a small difference)."
 ],
 "formule": "short + -er + than · more + long + than · as … as · less … than",
 "exemples": [
  ["Rent is cheaper in Ottawa than in Toronto.", "short adjective + -er"],
  ["This course is more interesting than the last one.", "more + long adjective"],
  ["My English is not as good as yours.", "not as … as"],
  ["The new model is much faster.", "much + comparative"]
 ],
 "mots": [
  ["cheap", "It's cheaper online.", "not costing a lot of money"],
  ["expensive", "more expensive than", "costing a lot of money"],
  ["fast", "faster than before", "quick"],
  ["than", "taller than me", "used to compare two things"],
  ["salary", "a higher salary", "the money you earn from your job"]
 ],
 "exercice": [
  "Complete: My car is ___ (old) than yours.",
  "Complete: This book is ___ (interesting) than the film.",
  "Complete: She is as tall ___ her sister.",
  "Irregular forms: good → ___ ; bad → ___"
 ],
 "corrige": ["older", "more interesting", "as", "better ; worse"],
 "piege": "Don't use both forms: “more cheaper” is wrong. And good / bad are irregular: better, worse."
},
{
 "n": 47, "niveau": "A2", "titre": "Superlatives",
 "intro": "Say that something is the most (or the least) … in a group.",
 "regle": [
  "Short adjectives: the + adjective-est: the cheapest, the biggest, the easiest.",
  "Long adjectives: the most + adjective: the most important.",
  "Irregular forms: good → the best, bad → the worst, far → the furthest.",
  "“One of the + superlative + PLURAL noun”: one of the biggest problems.",
  "For a place or group, use in (in the world, in the team). It often comes with the present perfect: the best film I've ever seen."
 ],
 "formule": "the + short-est · the most + long · one of the + superlative + plural noun",
 "exemples": [
  ["Canada is the second largest country in the world.", "the + -est + in"],
  ["It's the most important decision of my life.", "the most + long adjective"],
  ["She's one of the best students in the class.", "one of the + plural"],
  ["That was the worst meeting ever.", "bad → the worst"]
 ],
 "mots": [
  ["important", "the most important thing", "that matters a lot"],
  ["largest", "the largest city", "the biggest in size"],
  ["ever", "the best I've ever seen", "at any time in my life"],
  ["worst", "the worst day", "the most bad"],
  ["world", "in the world", "the Earth and all its countries"]
 ],
 "exercice": [
  "Complete: This is the ___ (cheap) hotel in town.",
  "Complete: She is the ___ (intelligent) person I know.",
  "Complete: It's one of the ___ (big) ___ (problem) in the country.",
  "Correct the mistake: He is the most tall in the team."
 ],
 "corrige": ["cheapest", "most intelligent", "biggest problems", "He is the tallest in the team."],
 "piege": "After “one of the”, the noun is ALWAYS plural: one of the best teams (not “team”)."
},
{
 "n": 48, "niveau": "A2", "titre": "“Too” and “enough”",
 "intro": "Say that there is too much, or enough, of something.",
 "regle": [
  "Too + adjective: It's too expensive. With a noun: too much (uncountable), too many (countable).",
  "Adjective + enough: He isn't old enough. “Enough” goes AFTER the adjective.",
  "Enough + noun: We have enough time. “Enough” goes BEFORE the noun.",
  "You can add “to + verb”: It's too late to call. She's old enough to drive."
 ],
 "formule": "too + adj · too much / many + noun · adj + enough · enough + noun",
 "exemples": [
  ["This flat is too small for us.", "too + adjective"],
  ["I have too many emails.", "too many + countable noun"],
  ["Is your English good enough for the interview?", "adjective + enough"],
  ["We don't have enough money to travel.", "enough + noun"]
 ],
 "mots": [
  ["enough", "Is it big enough?", "as much as you need"],
  ["too", "It's too late.", "more than is good or possible"],
  ["flat", "a small flat", "a home on one floor of a building (British)"],
  ["afford", "I can't afford it.", "to have enough money for something"],
  ["crowded", "The bus is too crowded.", "full of people"]
 ],
 "exercice": [
  "Complete: There are ___ people here. (more than is comfortable)",
  "Add “enough”: She isn't experienced.",
  "Add “enough”: We have time.",
  "Correct the mistake: He is enough tall to play basketball."
 ],
 "corrige": ["too many", "She isn't experienced enough.", "We have enough time.", "He is tall enough to play basketball."],
 "piege": "“Too” shows a problem: “It's too hot” is not the same as “It's very hot”. To say “very”, use very."
},
{
 "n": 49, "niveau": "A2", "titre": "The future with “will”",
 "intro": "Make predictions, promises, offers and quick decisions about the future.",
 "regle": [
  "Form: will + base verb, the same for every person: I will help, she will come. Short form: I'll, she'll, they'll.",
  "Negative: won't (= will not) + base verb: It won't rain. Question: Will you come?",
  "Use it for a prediction or an opinion about the future (often with I think, probably, maybe): I think she'll win.",
  "Use it for a decision made now, a promise or an offer: I'll call you tonight. I'll carry that for you."
 ],
 "formule": "will / 'll + base verb · won't + base verb · Will … + base verb ?",
 "exemples": [
  ["I think it will be sunny tomorrow.", "an opinion about the future"],
  ["I'll send you the details tonight.", "a promise"],
  ["The bag looks heavy. — I'll help you.", "an offer, decided now"],
  ["Don't worry, I won't forget.", "negative: won't"]
 ],
 "mots": [
  ["probably", "She'll probably be late.", "very likely"],
  ["maybe", "Maybe I'll come.", "perhaps; it is possible"],
  ["promise", "I promise I'll write.", "to say that you will certainly do something"],
  ["forget", "I won't forget your birthday.", "to not remember"],
  ["help", "I'll help you with your bags.", "to make something easier for someone"]
 ],
 "exercice": [
  "Complete: I think Canada ___ (win) the match.",
  "Make it negative: It will rain tomorrow.",
  "Make it a question: They will arrive on time.",
  "Make an offer: The phone is ringing. (answer)"
 ],
 "corrige": ["will win", "It won't rain tomorrow.", "Will they arrive on time?", "I'll answer it."],
 "piege": "No “to” after will: “I will go”, not “I will to go”. And no -s: “She will come”, not “She will comes”."
},
{
 "n": 50, "niveau": "A2", "titre": "Present continuous for future arrangements",
 "intro": "Talk about plans that are already fixed: a meeting, a trip, a dinner with a time and a place.",
 "regle": [
  "Form: am / is / are + verb-ing, with a future time: “I'm meeting Sarah tomorrow.”",
  "Use it for arrangements: you have already organised them, often with other people (a date, a ticket, a booking).",
  "The time word shows it is the future: tonight, tomorrow, on Friday, next week.",
  "Questions about plans often use it: “What are you doing this weekend?”"
 ],
 "formule": "am / is / are + verb-ing + future time",
 "exemples": [
  ["I'm seeing the dentist on Tuesday.", "an appointment"],
  ["We're flying to Toronto next Monday.", "the tickets are booked"],
  ["What are you doing tonight?", "asking about plans"],
  ["She isn't coming to the party on Saturday.", "negative"]
 ],
 "mots": [
  ["appointment", "I have an appointment at 10.", "a fixed time to see someone"],
  ["weekend", "What are you doing this weekend?", "Saturday and Sunday"],
  ["fly", "We're flying to Rome.", "to travel by plane"],
  ["book", "I've booked a table.", "to reserve a place, ticket or table"],
  ["tonight", "I'm working tonight.", "this evening or night"]
 ],
 "exercice": [
  "Complete: I ___ (have) dinner with my parents tonight.",
  "Ask a friend about their plans for Saturday.",
  "Make it negative: They are coming tomorrow.",
  "Choose: (I'm meeting / I meet) the manager at 3 pm tomorrow."
 ],
 "corrige": ["am having", "What are you doing on Saturday?", "They aren't coming tomorrow.", "I'm meeting (a fixed arrangement)"],
 "piege": "Don't forget the future time word: “I'm working tomorrow” is a plan; “I'm working” alone means now."
},
]
