""" Module for all questions """

from random import choice, randint
from typing import List, Dict
from reactions import Character
from file_init import file_lst_return
import doctest
import os

def questions(person: Character) -> List[Dict]:
    """ 
    Return a dictionary of questions that the user has to answer randomly,
    occasionally referring to <person> when talking about the user's
    date.

    """
    sad = file_lst_return('tragedies')
    gud_people = file_lst_return('good_peeps_i_think')

    gud_peeps = []
    while len(gud_peeps) != 3:
        gud_peep = choice(gud_people)
        if gud_peep not in gud_peeps:
            gud_peeps.append(gud_peep)

    questions = [
        {
            'Question 0': 'Suddenly, your phone starts to ring. What do you do?',
             'Answers': {'A': '"Sorry, my wives are expecting"',
                         'B': 'Patiently hang up and focus on your date',
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
                         'D': 'Continue talking, despite the rude interruption'}
        },
        {
            'Question 3': f'You and {person.first_name} notice that the '
                          'restaurant is getting progressively louder.\nIn'\
                          ' fact, it\'s getting harder for you and your date'\
                          ' to actually speak to each other without shouting!'\
                          ' What do you do?',
             'Answers': {'A': 'Stand up and DEMAND the entire restaurant to'\
                              ' be quiet',
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
             'Answers': {'A': 'Politely shake his hand in approval and proceed'\
                              ' to engage in fisticuffs',
                         'B': 'Sincerely say "Epic. My favourite flavour!"',
                         'C': 'Continue talking to your date',
                         'D': 'Take off your shirt and put it back on once it'\
                              ' dries'}
        },
        {
            'Question 7': f'{person.first_name} asks: "So, what makes you unique'\
                          ' from the previous men I\'ve dated?"',
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
             'Answers': {'A': 'Winners are always first! Stand up and punch him'\
                              ' before he gets the first blow. Then, proceed to'\
                              ' beat him up',
                         'B': '"You dated her???"',
                         'C': '"Don\'t worry, we\'re really just friends"',
                         'D': 'Cry'}
        },
        {
            'Question 10': f'{person.first_name} asks: "Are you a virgin?"',
             'Answers': {'A': 'Outright admit to it',
                         'B': '"I\'ve been saving my virginity for you baby"',
                         'C': 'Lie and proceed to talk about your experiences',
                         'D': '"What does that mean?"'}
        },
        {
            'Question 11': 'A blind old woman accidentally drops her wallet'\
                           ' near your table. What do you do?',
             'Answers': {'A': 'Grab her wallet, trip the old lady, and attempt to'\
                              ' steal the rest of her belongings',
                         'B': 'Get the wallet and try to give it back to her',
                         'C': 'Pretend to be blind by closing your eyes and also'\
                              ' try to find her wallet',
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
                         'B': 'BODYSLAM the child at his table',
                         'C': '"HEY YOU, STOP LOOKING AT US!"',
                         'D': 'Nothing. He really isn\'t bothering anyone'}
        },
        {
            'Question 14': 'After observing her for a while, you realize that'\
                           f' {person.first_name} may actually be a childhood '\
                            'friend! What should you do to remind her?',
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
             'Answers': {'A': f'Challenge {person.first_name} to an'\
                               ' arm-wrestling match',
                         'B': f'Play chess with {person.first_name}',
                         'C': 'just walk past time lol',
                         'D': '"Look at these ABS, babe"'}
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
                         'C': 'Smirk, cross your arms, and say "That video'\
                              ' SUCKS"',
                         'D': 'Suggest that she watches your Youtube channel'}
        },
        {
            'Question 17': 'Suddenly, an armed robbery ensues and you and'\
                          f' {person.first_name} are forced to hide. How '\
                           'do you handle this situation?',
             'Answers': {'A': 'Tackle the intruder and try to steal the '\
                              'money for yourself',
                         'B': f'Offer {person.first_name} as a hostage to'\
                              ' get out without being harmed',
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
                            ' a lifelong friend approaches your table and'\
                            ' goes on about your experiences you shared '\
                            'together. How do you respond?',
             'Answers': {'A': 'Let him talk. Sending him away would be rude',
                         'B': 'FISTICUFFS. NOW',
                         'C': 'Try to steer the conversation towards a ' 
                              'different topic',
                         'D': 'Tell him to buzz off'}
        }
    ]
    return questions
