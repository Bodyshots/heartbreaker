from random import randint, choice
from constants import (NORMAL, OBJECTIVE, ACTIVE, NEGATIVE, 
                       EXTREME_NEG, LARGE_NEG, MED_NEG, SMALL_NEG, NEUTRAL,
                       SMALL_POS, MED_POS, LARGE_POS, EXTREME_POS, MINOR_NEG,
                       MINOR_POS, slap_SE, slam_SE, fight_SE, table_slam_SE,
                       run_SE, cough_SE, gunshot_2_SE, panic_SE)
import pygame as pg
from os import path

pg.init()

class Character:
    """
    Create a new character

    """

    def __init__(self, name: str, true_pers: str=NORMAL, 
                 personality:str='Indifferent'):
        """
        Initialize a new Character, using <name>, <true_pers>, and
        <personality>.

        >>> pandemonica = Character('Pandemonica')
        >>> pandemonica.name
        'Pandemonica'
        >>> pandemonica.pers
        'Indifferent'
        >>> pandemonica.first_name
        'Pandemonica'

        """
    
        self.name, self.pers = name, personality
        self.true_pers, space = true_pers, name.find(' ')

        prof = self.rand_prof()
        prof = prof[:len(prof) - 1]
        self.prof = prof

        if space >= 0:
            self.first_name, self.last_name = name[:space], name[space + 1:]
        else:
            self.first_name = name

    def __str__(self):
        """
        Display the known information about the character to the user
        once printed.

        """

        return '{}\nPersonality: {}'.format(self.name, self.pers)

    def rand_prof(self):
        """
        Return a random profession after reading a text file of professions.

        """

        with open(path.abspath(r'text_files\Other'
                               r'\professions.txt')) as pro_txt:
            profession = pro_txt.read().split('\n')
        return choice(profession)


# General Reactions


def revulsion(person: Character) -> int:
    """
    Return a negative integer, simulating the user's reaction to
    <person>'s disgust of the user.

    """

    print(f'Revolted, {person.first_name} backs away from you.')
    return randint(LARGE_NEG, MED_NEG)


def slap(person: Character) -> int:
    """
    Return a negative integer, simulating the user's reaction to
    <person> slapping the user.

    """

    slap_SE.play()
    input(f'Deeply insulted, {person.first_name} slaps you.\n')
    print('I guess she didn\'t like that...')
    return randint(LARGE_NEG, MED_NEG)


def unimpressed(person: Character) -> int:
    """
    Return a negative integer, simulating the user's reaction to
    <person> being unimpressed with the user's actions.

    """

    print(f'{person.first_name} doesn\'t seem very impressed.')
    return randint(MED_NEG + MINOR_NEG, MED_NEG)


def distasteful(person: Character) -> int:
    """
    Return a negative integer, simulating the user's reaction to the
    generally negative response from <person>.

    """

    print(f'{person.first_name} gives you a distasteful look.')
    return randint(MED_NEG, SMALL_NEG)


def confusion(person: Character) -> int:
    """
    Return a positive/negative integer, simulating the user's reaction to
    the confused response from <person>.

    """

    print(f'{person.first_name} is wildly confused and doesn\'t know what'\
          ' to make of the situation.')
    return randint(SMALL_NEG, MINOR_NEG)


def funny(person: Character) -> int:
    """
    Return a positive/negative integer, simulating the user's reaction to
    <person> laughing at/with the user.

    """

    print(f'{person.first_name} laughs.')
    input(f'"I\'ll admit, that\'s pretty funny."\n')
    print('You also chuckle, but are unable to tell if her laughs are at or'\
          ' with you.')
    return randint(MINOR_NEG, MINOR_POS)


def sincere_laugh(person: Character) -> int:
    """
    Return a positive integer, simulating the user's reaction to
    <person> laughing with the user.

    This is a more generalized version of the funny function (haha).

    """

    print(f'{person.first_name} laughs. The good thing is that you can tell'
           ' that it\'s sincere! Nice going!')
    return randint(MINOR_POS, SMALL_POS)



def understanding(person: Character) -> int:
    """
    Return a positive integer, simulating an empathetic/sympathetic response
    from <person>.

    """

    print(f'{person.first_name} seems to somehow understand your feelings.')
    return randint(MINOR_POS, SMALL_POS)


def loves_energy(person: Character) -> int:
    """
    Return a positive integer, simulating the user's reaction to <person>'s
    adoration for the "energy" the user outputs.

    This function is typically reserved for ActiveCharacter classes.

    """

    print(f'{person.first_name} loves your energy!')
    return randint(MINOR_POS, SMALL_POS)


def lack_energy(person: Character) -> int:
    """
    Return a negative integer, simulating the user's reaction to <person>
    disapproving of the user's lack of energy.

    This function is typically reserved for ActiveCharacter classes.

    """

    print(f'{person.first_name} visibly approves of your lack of energy.')
    return randint(SMALL_NEG, MINOR_NEG)


def appreciate(person: Character) -> int:
    """
    Return a positive integer, simulating the user's reaction to
    <person> appreciating the user's actions.

    """

    print(f'{person.first_name} appreciates your response.')
    return randint(MINOR_POS, SMALL_POS)


def honesty(person: Character) -> int:
    """
    Return a positive integer, simulating the user's reaction to
    <person> valuing the user's honesty.

    """

    print(f'{person.first_name} appears to value your honesty.')
    return randint(MINOR_POS, SMALL_POS)


def impressed(person: Character) -> int:
    """
    Return a positive integer, simulating the user's reaction to the
    impressed response from <person>.

    """

    print(f'You have, somehow, made {person.first_name} admire you a bit more.')
    return randint(SMALL_POS, MED_POS)


def badass(person: Character) -> int:
    """
    Return a positive integer, simulating the user's reaction to the very
    impressed response from <person>.

    """

    print(f'{person.first_name} is so thoroughly impressed that she thinks'\
           ' you\'re badass!')
    return randint(SMALL_POS, MED_POS)


def pathetic(person: Character) -> int:
    """
    Return a tiny positive/negative integer, simulating the user's response
    to <person> taking pleasure in their uselessness
    (a mixed response really).

    This function is reserved for NegativeCharacter classes.

    """

    print(f'{person.first_name} takes pleasure in how pathetic you look.'\
               ' You don\'t really know how to feel.')
    return randint(NEUTRAL, MINOR_POS)


# Functions that use other functions


def person_is_profession(person: Character) -> int:
    """
    Return the user's reaction to <person>'s reaction, after <person>
    reveals that she occupies the user's professsion, <prof> that the
    user insulted.

    If <person>'s true_pers is OBJECTIVE then return the output of 
    unimpressed(person). If <person>'s true_pers is NEGATIVE, then
    print some text and return a positive int. Otherwise, return the
    output of slap(person).

    """

    print(f'It turns out, {person.first_name} IS a {person.prof}.')
    if person.true_pers == OBJECTIVE:
        return unimpressed(person)
    elif person.true_pers == NEGATIVE:
        input(f'Nevertheless, {person.first_name} expresses delight'\
               ' in finally having someone to rant about her job to.\n')
        print('I guess she doesn\'t like her job too much...')
        return randint(SMALL_POS, MED_POS)
    return slap(person)


def crowd_silence() -> None:
    """
    Print the awkwardness of crowd silence.

    """

    pg.mixer.music.fadeout(1000)
    input('The restaurant is stunned into silence.\n')
    input('Quickly, the staff try to escort you out of the establishment,'\
          ' but you quickly apologize and sit back down.\n')


def crowd_silence_effects(person: Character) -> int:
    """
    Return a large negative integer, simulating the user's reaction to
    <person>'s response after the restaurant is silenced by the user's actions.

    """

    crowd_silence()

    if person.true_pers == ACTIVE:
        print(f'Despite this, {person.first_name} admires your courage!')
        print('A win/lose situation for your confidence, I guess?')
        pg.mixer.music.play(-1, 0, 2000)
        return randint(MED_NEG, MED_POS)
    input(f'{person.first_name} covers her head in shame.\n')
    pg.mixer.music.play(-1, 0, 2000)
    return randint(EXTREME_NEG, LARGE_NEG)


def crowd_silence_child_B(person: Character) -> int:
    """
    If <person>'s true_pers is NEGATIVE or ACTIVE, return a positive
    integer. Otherwise, return a negative integer.

    This function should only be used in OPTION_B of question 13.

    """

    slam_SE.play(), crowd_silence()
    input(f'{person.first_name} is flushed with embarrassment.\n')
    pg.mixer.music.play(-1, 0, 2000)
    input('Later, after most of the restaurant stop looking at you,'\
          ' you explain why you ABSOLUTELY had to bodyslam the child to'\
         f' {person.first_name}.\n')

    input('"I see..." your date ponders.\n')

    if person.true_pers == NEGATIVE:
        print('"Serves him right then."')
        return randint(MINOR_POS, SMALL_POS)

    elif person.true_pers == ACTIVE:
        print(f'{person.first_name} admires your bravery!')
        return randint(MINOR_POS, SMALL_POS)
    
    print('"Are you alright? Mentally, not physcially."')
    return randint(EXTREME_NEG, LARGE_NEG)


def choke(person: Character) -> None:
    """
    Print the user's date successfully coughing out the food
    she was choking on.

    """
    cough_SE.play()
    input(f'{person.first_name} successfully coughs out the piece of her ribs'\
           ' she was choking on!\n')


def choke_neg(person: Character) -> int:
    """
    Return a negative integer, simulating the user's reaction to <person>'s
    response to the user after she coughs out her eaten ribs.

    """

    choke(person)

    print(f'However, despite your efforts, {person.first_name} fails to'\
           ' mention that you actually helped in anyway.')
    return randint(MED_NEG, SMALL_NEG)


def choke_pos(person: Character) -> int:
    """
    Return a positive integer, simulating the user's reaction to <person>'s
    response to the user after she coughs out her eaten ribs.

    """
    choke(person)

    print(f'{person.first_name} appreciates your help!')
    return randint(SMALL_POS, MED_POS)


def choke_neg_pos(person: Character) -> int:
    """
    Return a positive integer, simulating the user's reaction to <person>
    admiring how useless the user is when <person> is choking.

    This function is reserved for NegativeCharacter classes.

    """
    
    choke(person)

    input('"I could\'ve died and you decide to do that?"\n')
    input('"The futility of your actions just now..."\n')
    print('"It sort of turns me on..."')
    return randint(MINOR_POS, SMALL_POS)



def weights(person: Character) -> int:
    """
    If <person>'s true_pers is ACTIVE, return a positive integer. Otherwise,
    return the output of unimpressed(person) that is lower than what
    is typically expected of the function.

    """

    input('You can only lift 10 pounds.\n')

    if person.true_pers == ACTIVE:
        print(f'Nevertheless, {person.first_name} treasures your effort!')
        return randint(MINOR_POS, SMALL_POS)
    return unimpressed(person) + MINOR_NEG


def lies(person: Character) -> int:
    """
    If the user gets lucky, return the output of badass(person). Otherwise,
    return the output of unimpressed(person).

    Furthermore, if <person>'s true_pers method is OBJECTIVE, return
    unimpressed(person), as well.

    """

    if person.true_pers == OBJECTIVE or randint(0, 20) >= 7:
        print('The more you lied, the deeper the hole you dug became.'\
              ' Eventually, you got caught up in your lies...')
        return unimpressed(person)
    print('Through your masterful lies, you have managed to somehow'\
          f' convince {person.first_name} that you\'re actually'\
           ' "cooler" than you are!')
    return badass(person)


def fap_confused(person: Character) -> int:
    """
    Return an integer simulating the user's reaction to <person> being
    unfamiliar with the term "fap."

    """

    confusion(person)
    print('Perhaps it\'s best that she doesn\'t know what "fap" means...')
    return randint(NEUTRAL, MINOR_POS)


def event_remembers_B(person: Character) -> int:
    """
    If the user gets lucky, return the output of remembers(person).
    Otherwise, return the output of not_remember().

    Furthermore, if <person>'s true_pers method is OBJECTIVE, then
    return the output of not_remember(), as well.

    """

    if randint(NEUTRAL, 23) >= 17 or person.true_pers == OBJECTIVE:
        return not_remember()
    return remembers(person)


def event_remembers_C(person: Character) -> int:
    """
    If the user gets lucky, return the output of confusion(person).
    Otherwise, return the output of distasteful(person).

    """
    with open(path.abspath(r'text_files\Other\memories.txt')) as mem_txt:
        mems = mem_txt.read().split('\n')
    memory = choice(mems)
    print(f'{memory}')

    if randint(0, 20) >= 15:
        return distasteful(person)
    return confusion(person)


def event_blind_C(person: Character) -> int:
    """
    If <person>'s true_pers is NEGATIVE, then return some
    integer. Otherwise, if they are not OBJECTIVE, then
    return the output of distasteful(person) and return the
    output of confusion(person) if they are.

    """

    print('You pretend to be blind. It\'s safe to say that neither'\
          ' of you actually manage to find the wallet.')
    if person.true_pers == NEGATIVE:
        input(f'{person.first_name} laughs at how useless you are.')
        return randint(NEUTRAL, MINOR_POS)
    if person.true_pers != OBJECTIVE:
        return distasteful(person)
    return confusion(person)


def event_blind_D(person: Character) -> int:
    """
    If <person>'s true_pers is NORMAL or ACTIVE, then return
    the output of understanding(person). Otherwise, print a message
    and return the output of distasteful(person).
    
    """

    input('Blind people can\'t actually see what you\'re referring to...\n')
    if person.true_pers == NORMAL:
        return understanding(person)
    elif person.true_pers == NEGATIVE:
        return pathetic(person)
    print(f'Despite your true intentions, ', end='')
    return distasteful(person)


def chess(person: Character) -> int:
    """
    Return a positive integer simulating the user's reaction to
    <person>'s response to the user challenging them to a chess match.

    This function is reserved for ObjectiveCharacter classes.

    """

    table_slam_SE.play()
    print(f'You pull out a chess set and challenge {person.first_name} '\
           'to a match. Surprisingly, you put up quite a fight.')
    return impressed(person)


def event_video_A(person: Character) -> int:
    """
    Return a negative integer simulating the user's reaction to
    <person>'s response to the user explicitly saying
    "[insert thing here]." What a PSYCHO.

    """

    input(f'{person.first_name} doesn\'t really know what you mean when you'\
           ' explicitly say "[insert thing here]."\n')
    return confusion(person)


# Unique Functions


def not_remember() -> int:
    """
    Return a large negative integer simulating the user's devastating reaction
    to their date not remembering the user.

    """

    print('"Sorry, I don\'t know you," she says.')
    return randint(LARGE_NEG, MED_NEG)


def fight(person: Character) -> int:
    """
    If <person>'s true_pers is ACTIVE, return a neutral/positive integer
    after showing some text. Otherwise, return a considerable negative integer
    after showing some text.

    """

    fight_SE.play()
    if person.true_pers == ACTIVE:
        input('Although you painfully lose your fight against the man,'\
          f' {person.first_name} seems to appreciate your effort.\n')
        return randint(NEUTRAL, MINOR_POS)
    elif person.true_pers == NEGATIVE:
        input(f'As you lay on the floor, you {person.first_name} giggles'\
               ' at your misfortune.\n')
        print('That didn\'t feel very nice.')
        return randint(MED_NEG, SMALL_NEG)
    input('Expectedly, you lose your fight against the man. Your adversary'\
         f' nor your date seem very pleased.\n')
    return randint(LARGE_NEG, MED_NEG)


def remembers(person: Character) -> int:
    """
    Return a small negative integer simulating the user's reaction
    after <person> remembers the user, but doesn't actually appreciate
    the user's presence.

    """

    print(f'Thankfully, {person.first_name} remembers you.')
    if person.true_pers == NEGATIVE:
        input(f'{person.true_pers} laughs.\n')
        input(f'She\'s probably thinking about how stupid you were in the'\
               ' past, rather than your "fond" memories with each'\
               ' other...\n')
        return randint(NEUTRAL, MINOR_POS)
    elif person.true_pers == NORMAL:
        input('"I do! I\'m actually glad I got to see you again!"\n')
        input('"People really do change, huh?"\n')
        input('"It\'s just..."\n')
        input('"I\'d rather not remind myself of how you were back'\
              ' then..."\n')
        input('"Sorry."\n')
        print('Ouch.')
        return randint(SMALL_NEG, MINOR_NEG)
    input('However, she doesn\'t seem very pleased about it...\n')
    return randint(MED_NEG, SMALL_NEG)


def event_blind_A(person: Character) -> int:
    """
    Return a negative integer simulating the user's reaction after
    underestimating a "blind old woman."

    """
    input('It turns out, the blind old woman was actually an undercover'\
          ' agent trying to lure criminals into taking advantage of her.\n')
    input('Immediately, you get tackled by the old woman and are read'\
          f' your rights.\nIt is only until {person.first_name} somehow'\
          ' explains that you thought the agent was an "old friend" that'\
          ' you are released from custody.\n')
    if person.true_pers == NEGATIVE:
        return pathetic(person)
    return randint(EXTREME_NEG, LARGE_NEG)


def event_blind_B(person: Character) -> int:
    """
    Return a negative integer simulating the user's reaction after
    the people around the user accuse the user of stealing.

    """
    input('After picking up the wallet, you are accused of stealing'\
          ' the "poor old woman\'s wallet" and are placed under '\
          'citizen\'s arrest.\n')
    input('Even though you eventually explain the situation and'\
          f' sit back down, you notice that {person.first_name} has had'\
          ' her head down on the table for the entire ordeal.\n')
    if person.true_pers == NEGATIVE:
        print(f'Taking into account {person.true_pers}\'s personality, '\
               'it\'s probably safe to assume that it\'s due to laughter'\
               ' rather than embarassment...')
        return randint(NEUTRAL, MINOR_POS)
    return randint(EXTREME_NEG, LARGE_NEG)


def event_video_C(person: Character) -> int:
    """
    Return a positive integer simulating the user's reaction to
    <person> enjoying arguing with the user.

    This function is reserved for ActiveCharacter and NegativeCharacter
    classes.

    """

    print(f'You and {person.first_name} argue for a while. For some'\
           ' reason, she seems to like arguing with you!')
    return randint(MINOR_POS, SMALL_POS)


def arm_wrestle(person: Character) -> int:
    """
    Return a positive integer simulating the user's reaction to
    <person> enjoying the arm-wrestling match with the user.

    This function is reserved for ActiveCharacter classes.

    """

    table_slam_SE.play()
    print(f'You challenge {person.first_name} to an'\
           ' arm-wrestling match. Although you lose,'\
          f' {person.first_name} appreciates your enthusiasm!')
    return randint(SMALL_POS, MED_POS)


def event_friend_ignore(person: Character) -> int:
    """
    Return a negative integer simulating the user's reaction
    to <person> not being very pleased with the user's history.

    If <person>'s true_pers is NORMAL, return a positive integer
    instead.

    """

    input('Your supposed "friend" ignores your presence and keeps talking.\n')
    input('He goes on to explain how you were telling him of your'\
          ' plan to vomit on a person\'s bed years ago by consuming an entire '
          'sleeve of Oreos.\n')
    if person.true_pers == NORMAL:
        input(f'{person.true_pers} gives you a sympathetic look.\n')
        print('At least she understands how hard it is to not vomit on'\
              ' other peoples\' beds.')
        return randint(MINOR_POS, SMALL_POS)
    return unimpressed(person)


def event_friend_buzz_neg(person: Character) -> int:
    """
    Return a positive integer simulating the user's reaction
    to <person> being impressed with the user's mannerisms.

    This function is unique to NegativeCharacter and
    ActiveCharacter classes and should only be used for
    OPTION_D in question 19.

    """
    if person.true_pers == ACTIVE:
        input('The fact that you tried to rudely send you friend off'\
              f' has apparently angered {person.first_name} that she'\
              ' gives you a black eye.')
        print('You should probably file assault charges.')
        return randint(MED_NEG, SMALL_NEG)

    input(f'Oddly enough, {person.first_name} joins in. The both of you'\
           ' harass your friend to the point of tears.\n')
    input('He runs away crying. How despicable..\n')
    print(f'Just the way {person.first_name} likes it.')
    return randint(SMALL_POS, MED_POS)


def event_fight_win(person: Character) -> int:
    """
    If <person>'s true_pers is ACTIVE, return the output of
    badass(person). Otherwise, return a considerable negative
    integer after printing some text.

    """

    fight_SE.play()
    input('Unexpectedly, you win the fight against your friend.\n')

    if person.true_pers == ACTIVE:
        return badass(person)
    input(f'Despite this, {person.first_name} is mortified,'\
           ' especially with all of the people looking at you and her.\n')
    return randint(LARGE_NEG, MED_NEG)


def event_robbery_A(person: Character) -> int:
    """
    If the user is (un)lucky or if <person>'s true_pers is not ACTIVE,
    then return an extremely large negative integer. Otherwise, return
    moderately sized positive integer.

    Text must be printed throughout this entire process.

    """

    gunshot_2_SE.play(), panic_SE.play()
    if randint(0, 100) >= 95:
        print('You somehow manage to tackle the intruder and steal the'\
              ' money he was carrying.')
        input('Unluckily for you, having taken the place of the intruder,'\
              ' you are placed under citizen\'s arrest and are sentenced to'\
              f'{randint(5, 13)} years in prison.\n')
        input(f'By the time you meet {person.first_name} and arrange another'\
               ' date, she has completely forgotten who you were.\n')
        pg.mixer.music.play(-1, 0, 2000)
        return EXTREME_NEG

    input('Though you got shot, you at least managed to distract the intruder'\
          ' so the others in the restaurant could wrestle the gun away from'\
          ' him.\n')
    input('Luckily, you receive proper medical attention just in time'\
          ' for you to continue your date in a different restaurant.\n')

    if person.true_pers == ACTIVE:
        print(f'{person.first_name} praises your fearlessness and daring'\
               ' nature.')
        pg.mixer.music.play(-1, 0, 2000)
        return MED_POS

    pg.mixer.music.play(-1, 0, 2000)
    input(f'However, {person.first_name} questions your sanity for 30 minutes\n'
           'straight once you meet each other.')
    return EXTREME_NEG


def event_robbery_B(person: Character) -> int:
    """
    If <person>'s true_pers is NORMAL, then return the output
    of understanding(person). Otherwise, return the output of
    distasteful(person)

    """

    input('Technically, both of you are already hostages.\n')
    fight_SE.play()
    input('So, the intruder just whacks you unconscious.\n')
    pg.mixer.music.play(-1, 0, 2000)
    input('After regaining consciousness, you realize that you\'re still '
          f'in the restaurant with {person.first_name}, for some reason.\n')
    input('Apparently you just dozed off in the middle of your date with'\
          f' {person.first_name}. Great work.\n')
    if person.true_pers == NORMAL:
        return understanding(person)
    return distasteful(person)
    

def event_robbery_C(person: Character) -> None:
    """
    Print the user running away from the restaurant, and <person> in
    particular, and return None to make the user lose the game.

    """

    run_SE.play()
    input(f'You run, leaving {person.first_name} to live another day\n')
    input('You know what that means...\n')


def event_robbery_D(person: Character) -> int:
    """
    If <person>'s true_pers is ACTIVE, return a negative integer.
    If <person>'s true_pers is NORMAL or OBJECTIVE, return a
    positive integer.
    Otherwise, return a negative integer.

    """

    input('You decide to stay down to avoid getting shot.\n')
    input('Fortunately, the police arrive just in time to make '\
          'negotiations with the robber and send him off on his merry way.\n')
    pg.mixer.music.play(-1, 0, 2000)
    input(f'You continue eating with {person.first_name} to discuss the'\
          ' event.\n')
    if person.true_pers == ACTIVE:
        print(f'{person.first_name} appears severely disappointed in your'\
               ' lack of heroism.')
        return randint(MED_NEG, SMALL_NEG)
    elif person.true_pers in (NORMAL, OBJECTIVE):
        print(f'{person.first_name} appreciates how you reacted'\
               ' during that situation!')
        return randint(SMALL_POS, MED_POS)
    input(f'{person.first_name} mockingly remarks about you apparently pissing'\
           ' your pants throughout the whole ordeal.\n')
    print('Although not true, her mockery of you still stings a bit...')
    return randint(SMALL_NEG, MINOR_NEG)

def abs_muscles(person: Character) -> int:
    """
    If <person>'s true_pers is NEGATIVE, return the output of
    pathetic(person). If <person>'s true_pers is ACTIVE, then return
    a positive integer. Otherwise, return a negative integer.

    """

    slap_SE.play()
    input(f'You reveal your grotesque stomach to {person.first_name} and'\
           ' slap it, for some reason.\n')
    input('It jiggles upon impact.\n')

    if person.true_pers == NEGATIVE:
        return pathetic(person)

    elif person.true_pers == ACTIVE:
        print(f'{person.first_name} admires what effort you try to put into'\
               ' your body!')
        return randint(MINOR_POS, SMALL_POS)

    print(f'{person.first_name} is disgusted.')
    return randint(MED_NEG, SMALL_NEG)
