""" Module for all questions """

from random import choice
from typing import List, Dict
from character_classes import person_creator
from reactions import Character
from file_init import (first_names_lst, last_names_lst, personalities_dict, 
                       file_lst_return)

def questions(person: Character) -> List[Dict]:
    """ 
    Return a dictionary of questions that the user has to answer randomly,
    occasionally referring to <person> when talking about the user's
    date.

    """
    sad = file_lst_return('tragedies')
    gud_people = file_lst_return('good_peeps_i_think')
    chosen_console = choice(file_lst_return('consoles'))

    rand_prof1, rand_prof2 = '', ''
    while rand_prof1 == person.prof or rand_prof1 == '': 
        rand_prof1 = person.rand_prof()[:-1]
    while rand_prof2 == person.prof or rand_prof2 == '':
        rand_prof2 = person.rand_prof()[:-1]

    rand_pers1, rand_pers2 = '', ''
    personalities = personalities_dict()
    del personalities[person.true_pers]
    personality_key_list = list(personalities.keys())
    rand_pers1 = choice(personalities[choice(personality_key_list)])
    rand_pers2 = choice(personalities[choice(personality_key_list)])

    gud_peeps = []
    while len(gud_peeps) != 3:
        gud_peep = choice(gud_people)
        if gud_peep not in gud_peeps: gud_peeps.append(gud_peep)

    questions = [
        {
            'Question 0': 'Suddenly, your phone starts to ring. What do you do?',
             'Answers': {'A': '"Sorry, my wives are expecting"',
                         'B': 'Hang up and focus on your date',
                         'C': '"Can you shut up for a sec?"',
                         'D': 'Keep it ringing for the next 30 seconds'}
        },
        {
            'Question 1': f'You realize that you and {person.first_name}'\
                          ' are running out of things to talk about. What\'s'\
                          ' a nice topic to keep the conversation going?',
             'Answers': {'A': f'{choice(sad)}',
                         'B': 'Nothing',
                         'C': 'Your gambling addiction',
                         'D': 'Exercise'}
        },
        {
            'Question 2': f'{person.first_name} begins to choke on some ribs!'\
                          ' What do you do?',
             'Answers': {'A': 'Call 911',
                         'B': 'Perform the Heimlich Maneuver',
                         'C': 'SCREAM',
                         'D': 'Continue talking'}
        },
        {
            'Question 3': f'You and {person.first_name} notice that the '
                          'restaurant is getting progressively louder.\nIn'\
                          ' fact, it\'s getting harder for you and your date'\
                          ' to actually speak to each other without shouting!\n\n'\
                          ' What do you do?',
             'Answers': {'A': 'Demand the entire restaurant to be quiet',
                         'B': 'Attempt to speak to your date anyways',
                         'C': '"Thank God it\'s loud in here. Now I'\
                                ' don\'t get to hear you speak"',
                         'D': 'Try to make a joke out of the situation'}
        },
        {
            'Question 4': f'{person.first_name} weakly fiddles with her fork.'\
                          ' It seems like something\'s bothering her.'\
                          ' What do you do?',
             'Answers': {'A': '"Sucks to suck"',
                         'B': 'Lean in for a kiss',
                         'C': 'What\'s wrong?',
                         'D': 'Fiddle with your fork as well'}
        },
        {
            'Question 5': f'{person.first_name} asks: "How are you?"'
                           '\nHow do you respond?',
             'Answers': {'A': 'Say nothing',
                         'B': '"Healthy. Thanks for asking"',
                         'C': '"You too"',
                         'D': '"Fine, like a sharp point baby"'}
        },
        {
            'Question 6': 'One of the restaurant\'s waiters accidentally trips'\
                          ' and spills a glass of wine on your shirt! What do '\
                          'you do in response?',
             'Answers': {'A': 'Punch him',
                         'B': '"Epic."',
                         'C': 'Continue talking to your date',
                         'D': 'Take off your shirt and put it back on once it'\
                              ' dries'}
        },
        {
            'Question 7': f'{person.first_name} asks: "So, what makes you unique?"',
             'Answers': {'A': '"nothing lol"',
                         'B': 'Proceed to brag about how much you lift',
                         'C': '"Next question please"',
                         'D': 'Reflect the question back onto her'}
        },
        {
            'Question 8': f'{person.first_name} asks: "What do you do in'\
                           ' your spare time?"',
             'Answers': {'A': '"By the time this date is done, babe, '\
                              'we won\'t have any"',
                         'B': 'Stumble over your words and fail to give an'\
                              ' answer',
                         'C': '"your mom"',
                         'D': '"Fap"'}
        },
        {
            'Question 9': f'As you\'re talking to {person.first_name} a man'\
                           ' comes to your table demanding that you leave '\
                           f'{person.first_name} alone. Apparently this man is'\
                           ' your date\'s ex!\nHow do you respond?',
             'Answers': {'A': 'Punch him before he gets the first blow.'
                              ' Then, proceed to beat him up',
                         'B': '"You dated her???"',
                         'C': '"Don\'t worry, we\'re really just friends',
                         'D': 'Cry'}
        },
        {
            'Question 10': f'{person.first_name} asks: "Are you a virgin?"',
             'Answers': {'A': 'Outright admit to it',
                         'B': '"I\'ve been saving my virginity for you baby"',
                         'C': 'Proceed to talk about your experiences',
                         'D': '"What does that mean?"'}
        },
        {
            'Question 11': 'A blind old woman accidentally drops her wallet'\
                           ' near your table. What do you do?',
             'Answers': {'A': 'Grab her wallet, trip the old lady, and attempt to'\
                              ' steal the rest of her belongings',
                         'B': 'Get the wallet and try to give it back to her',
                         'C': 'Close your eyes and also try to find her wallet',
                         'D': '"Ma\'am, you dropped your wallet. It\'s right'\
                              ' over there"'}
        },
        {
            'Question 12': 'After going on a rant about what she hates, '\
                           f'{person.first_name} politely asks you'\
                            ' about what ticks you off the most.'\
                            ' What do you say?',
             'Answers': {'A': f'"I HATE {person.prof}s"',
                         'B': '"Myself"',
                         'C': '"You"',
                         'D': '"i\'m not a clock lmao"'}
        },
        {
            'Question 13': f'You haven\'t notified {person.first_name} of'\
                            ' this yet, but you\'ve been quietly watching this'\
                            ' mysterious child spy on you from a couple of'\
                            f' tables back.\nAs {person.first_name} talks, you'\
                            ' think of ways to get rid of this annoying bugger.',
             'Answers': {'A': 'Stare back at him',
                         'B': 'Bodyslam the child',
                         'C': 'Shout at the kid',
                         'D': 'Nothing. He really isn\'t bothering anyone'}
        },
        {
            'Question 14': 'After observing her for a while, you realize that'\
                          f' {person.first_name} may actually be someone you '\
                           'knew from your childhood!\nWhat should you do to'
                           ' remind her about yourself?',
             'Answers': {'A': '"Remember the kid who threw up in your mother\'s'\
                              ' bed after eating an entire sleeve of Oreos?"',
                         'B': '"Hey, remember me from your childhood?"',
                         'C': 'Try to do something she would only recognize',
                         'D': 'Attempt to communicate telepathically to her'}
        },
        {
            'Question 15': f'Once again, {person.first_name} and you have run'\
                            ' out of things to talk about. What can you do to'\
                            ' pass the time?',
             'Answers': {'A': f'Test your physical strength against {person.first_name}',
                         'B': f'Challenge {person.first_name} to a game of intellect',
                         'C':  'just walk past time lol',
                         'D':  'Show her your abs'}
        },
        {
            'Question 16': f'{person.first_name} is reminded of a video she '
                            'just watched recently. Turns out, you\'ve watched'\
                            ' the exact same video.\nYou plan to use'
                            ' it for further conversation. How do you go about'
                            ' speaking to her about it?',
             'Answers': {'A': '"Oh, isn\'t that where they do [insert thing'\
                              ' here]?"',
                         'B': 'Don\'t bother and keep listening to her',
                         'C': 'Smirk and cross your arms while saying'\
                              ' "That video SUCKS"',
                         'D': 'Suggest that she watches your Youtube channel'}
        },
        {
            'Question 17': 'Suddenly, an armed robbery ensues and you and'\
                          f' {person.first_name} are forced to hide. How '\
                           'do you handle this situation?',
             'Answers': {'A': 'Try to steal the money for yourself',
                         'B': f'Offer {person.first_name} as a hostage',
                         'C': 'RUN',
                         'D': 'Continue staying down'}
        },
        {
            'Question 18': '"Who do you admire the most in life?" your date'\
                           ' asks you.',
             'Answers': {'A': 'The person who made this game',
                         'B': gud_peeps.pop(),
                         'C': gud_peeps.pop(),
                         'D': gud_peeps.pop()}
        },
        {
            'Question 19': f'As you\'re chatting with {person.first_name},'\
                            ' an, apparently, lifelong friend approaches your table and'\
                            ' goes on about your experiences you shared '\
                            'together. How do you respond?',
             'Answers': {'A': 'Let him talk. Sending him away would be rude',
                         'B': 'Beat them up',
                         'C': 'Steer the conversation towards a ' 
                              'different topic',
                         'D': 'Tell him to buzz off'}
        },
        {
            'Question 20': f'As a hypothetical, {person.first_name} wonders'\
                            ' what you would do when you encounter a homeless'\
                            ' person on the side of the road.',
             'Answers': {'A': '"Homeless? Tell them to just get a house"',
                         'B': 'Steal their belongings',
                         'C': 'Give them some money',
                         'D': '"I, too, am homeless"'}
        },
        {
            'Question 21': f'To test your intelligence, {person.first_name}'\
                            ' poses the following math question:\n'\
                            '"Find the antiderivative of\n'
                            'dy/dx = e^(2y)(2x-x^2),'
                            ' where y(0) = 3.1510690248564.\n\nThen, find '\
                            'x when y = -ln(209484)/2. Ensure your final '\
                            'answer is in the real numbers."',
             'Answers': {'A': '"what"',
                         'B': 'Try to answer the question',
                         'C': 'How about I give you a math question?',
                         'D': 'Ignore them and continue eating your food'}
        },
        {
            'Question 22': 'Your date decides to go to the washroom.\nWhat'\
                           ' do you do?',
            'Answers': {'A': 'Join them',
                        'B': 'Wait patiently for their return',
                        'C': 'Eat their food while you wait',
                        'D': 'Use this as an opportunity to take a break'}
        },
        {
            'Question 23': f'While talking with {person.first_name}, you'\
                            ' realize that you accidentally left your oven'\
                            ' on.\n\nIn short, your house is in danger of'\
                            ' burning down!\n\nWhat do you do?',
            'Answers': {'A': '"SHIT MY HOUSE IS BURNING DOWN"',
                        'B': 'Hope that your house will be alright when'\
                             ' you get back',
                        'C': 'Call one of your buds to turn it off',
                        'D': 'Postpone your date to quickly head back and'\
                             ' turn it off'}
        },
        {
            'Question 24':  'Thanks to your waning attention span,'\
                           f' you space out while {person.first_name}'\
                            ' asks you a question.\n\What is your response?',
            'Answers': {'A': '"Yes"',
                        'B': '"No"',
                        'C': '"Huh?"',
                        'D': '"Sorry, I wasn\'t paying attention."'}
        },
        {
            'Question 25':  f'{person.first_name} tells you to spell'\
                             ' "ICUP".',
            'Answers': {'A': '"Seriously?"',
                        'B': 'Spell it out',
                        'C': '"How do you spell it?"',
                        'D': '"No"'}
        },
        {
            'Question 26':  'Your date asks you how they look today.',
            'Answers': {'A': '"Bloody gorgeous"',
                        'B': '"Pretty good"',
                        'C': '"Your outfit SUCKS"',
                        'D': '"This is a text-based video game.'\
                             ' I literally don\'t know."'}
        },
        {
            'Question 27':  '"Do you eat ass?"',
            'Answers': {'A': '"Of course I do!"',
                        'B': '"Do you?"',
                        'C': '"What?"',
                        'D': '"No"'}
        },
        {
            'Question 28':  'Movie discussion time! Your date fervently'\
                            ' talks about the Lord of the Rings trilogy'\
                            ' and asks about your favourite quote from'\
                            ' the series.',
            'Answers': {'A': '"Obstacles do not exist to be surrendered'\
                             ' to, but only to be broken"',
                        'B': '"I believe in one thing only, the power'\
                             ' of human will"',
                        'C': '"All\'s well that ends better"',
                        'D': '"Inactivity is death"'}
        },
        {
            'Question 29':  f'{person.first_name} looks visibly bored! You'\
                             ' try to tell a joke to lighten the mood, but'\
                             ' what should the joke be about?',
            'Answers': {'A': 'Cars',
                        'B': 'Shakespeare',
                        'C': 'Kidney stones',
                        'D': 'Water'}
        },
        {
            'Question 30':  '"Would you kill a puppy for ten million US dollars?"',
            'Answers': {'A': '"Hell yeah"',
                        'B': '"Dumb question. Next"',
                        'C': '"Nah"',
                        'D': '"A puppy, no. A different animal though..."'}
        },
        {
            'Question 31':  'Though your food is of excellent quality, you'\
                            ' suddenly realize your wallet isn\'t as so.'\
                            ' You\'re too poor to pay for both '\
                           f'{person.first_name}\'s meal as well as yours!\n\n'\
                            'What do you do?',
            'Answers': {'A': f'Persuade {person.first_name} to split the'\
                              ' bill.',
                        'B': f'Pickpocket {person.first_name}',
                        'C': 'Create art',
                        'D': 'Make more money'}
        },
        {
            'Question 32':  'Out of the corner of your eye, you spot a big,'\
                            ' red, jolly man munching down on some cookies'\
                            ' and milk. Slowly, it all clicks together...\n\n'\
                            'It\'s clearly Santa Claus! How do you act in this'\
                            ' situation?',
            'Answers': {'A': '"Eat a salad, fat man"',
                        'B': '"HOLY SHIT"',
                        'C': 'Yeah right',
                        'D': 'FUCK SANTA CLAUS'}
        },
        {
            'Question 33':  f'{person.first_name} asks you about work.'\
                             '\nWhat\'s your job?',
            'Answers': {'A': '"A plumber"',
                        'B': '"I\'m unemployed"',
                        'C': '"A lawyer"',
                        'D': '"A coach"'}
        },
        {
            'Question 34':  '"As part of a team, what role do you prefer?"',
            'Answers': {'A': '"A leader"',
                        'B': '"I\'m pretty much the idea guy"',
                        'C': '"Just your average worker"',
                        'D': '"I work alone"'}
        },
        {
            'Question 35':  'Your chair is terribly uneven and has been'\
                            ' bugging you for a while now.\n\n'\
                            'What do you do about this ordeal?',
            'Answers': {'A':  'Use your table cloth to level the chair',
                        'B':  'Get another chair from a nearby table',
                        'C':  'Continue ignoring it',
                        'D': f'Ask {person.first_name} to switch chairs with you'}
        },
        {
            'Question 36':  f' You touch your pockets and seem to be missing'\
                             ' something.\n\nIt seems like you\'ve been pickpocketed!\n\n'\
                             'Indeed, out of the corner of your eye, you see'\
                             ' a man walking rapidly. What do you do?',
            'Answers': {'A': 'Confront the man',
                        'B': 'Begrudingly continue on with your date',
                        'C': 'Get some compensation',
                        'D': 'Cope'}
        },
        {
            'Question 37':  '"If you had to describe yourself in one word'\
                           f' what would it be?", {person.first_name} asks.',
            'Answers': {'A': '"No one can be explained in one word"',
                        'B': '"poggers"',
                        'C': '"Pathetic"',
                        'D': '"Pretty cool"'}
        },
        {
            'Question 38':  f'{person.first_name} is feeling a bit bored and'\
                             ' asks you for a random fact about yourself\n\n'\
                             'What do you say?',
            'Answers': {'A': '"IMO, you\'re pretty hot"',
                        'B': '"Fun fact: I volunteered at an animal shelter once."',
                        'C': '"It isn\'t much, but I\'ve been going to the gym'\
                              ' a lot more recently."',
                        'D': '"I\'m too busy to know anything pretty unique."'}
        },
        {
            'Question 39':  'Out of the corner of your eye you spot a police officer'\
                            'wheel clamping your illegally parked car down!\n\n'\
                            'What do you do?',
            'Answers': {'A': 'Persuade the officer to look the other way',
                        'B': 'I didn\'t need my car anyways',
                        'C': 'Try to get the wheel clamp off',
                        'D': 'Actually, I parked in a legal spot'}
        },
        {
            'Question 40':   f'"What do you think about the {chosen_console}?',
            'Answers': {'A': f'"the {chosen_console} fucking sucks lmao"',
                        'B': '"What\'s that?"',
                        'C': '"It\'s alright"',
                        'D': '"Pretty based ngl"'}
        },
        {
            'Question 41':  '"Tell me your age without saying it", says\n'\
                            f'{person.first_name}.',
            'Answers': {'A': '"Y\'all remember strawberry clock?"',
                        'B': 'Type your age on your phone and show it to'\
                            f' {person.first_name}',
                        'C': '"amogus haha"',
                        'D': '"Never ask someone their age, idiot"'}
        },
        {
            'Question 42':  'I know where you live',
            'Answers': {'A': '192.24.63.179',
                        'B': 'monkaS',
                        'C': 'Cthulhu fhtagn! Ph\'nglui mglw\'nfah '\
                             'Cthulhu R\'lyeh wgah\'nagl fhtagn', #(alternatively, player's Name here)
                        'D': '42.4338° N, 83.9845° W'}
        },
        {
            'Question 43':  'El no sabe Pepelaugh',
            'Answers': {'A': 'Clueless',
                        'B': 'What?',
                        'C': 'Si',
                        'D': 'Isn\'t this a dating game?'}
        },
        {
            'Question 44':  '"What says the most about a person?" your date asks',
            'Answers': {'A': '"Their personality"',
                        'B': '"Their looks"',
                        'C': '"What their room looks like"',
                        'D': '"How they act under pressure"'}
        },
        {
            'Question 45':  f'"What are you really proud of?", {person.first_name} asks',
            'Answers': {'A': '"My intellect"',
                        'B': '"My \"grind\""',
                        'C': '"There\'s nothing to be proud of..."',
                        'D': '"Eh, myself in general"'}
        },
        {
            'Question 46':  'Your date asks: "What would you spend a million dollars on?"',
            'Answers': {'A': '"Training equipment!"',
                        'B': '"Student loans!"',
                        'C': '"Gambling!"',
                        'D': '"I would never be able to get a million dollars in the first place..."'}
        },
        {
            'Question 47':  f'"What\'s your favourite holiday?", {person.first_name} asks',
            'Answers': {'A': '"Christmas"',
                        'B': '"Valentine\'s Day"',
                        'C': '"Halloween"',
                        'D': '"Leg Day"'}
        },
        {
            'Question 48':  f'{person.first_name} asks: "Are you the type of guy to do'\
                             ' things on the fly?"',
            'Answers': {'A': '"Yes"',
                        'B': '"No"',
                        'C': '"It depends"',
                        'D': '"Are you?"'}
        },
        {
            'Question 49':  '"Do you remember my last name?", your date asks',
            'Answers': {'A':  '"No"',
                        'B': f'"{person.first_name}"',
                        'C': f'"{person.last_name}"',
                        'D': f'"{choice(last_names_lst())}"'}
        },
        {
            'Question 50':  'Your date asks: "What do you care the least about?"',
            'Answers': {'A': '"You"',
                        'B': '"To be honest, myself"',
                        'C': '"My regrets"',
                        'D': '"Society"'}
        },
        {
            'Question 51':  '"Do you remember my first name?", your date asks',
            'Answers': {'A':  '"No"',
                        'B': f'"{person.first_name}"',
                        'C': f'"{person.last_name}"',
                        'D': f'"{choice(first_names_lst())}"'}
        },
        {
            'Question 52':  '"Do you remember what my job is?", your date asks',
            'Answers': {'A':  '"No"',
                        'B': f'"A {rand_prof1}"',
                        'C': f'"A {rand_prof2}"',
                        'D': f'"A {person.prof}"'}
        },
        {
            'Question 53':  '"How would you describe me?", your date asks',
            'Answers': {'A':  '"I don\'t know lmao"',
                        'B': f'"{rand_pers1}"',
                        'C': f'"{rand_pers2}"',
                        'D': f'"{person.pers}"'}
        }
    ]
    return questions

if __name__ == '__main__':
    from character_classes import person_creator
    questions(person_creator())
