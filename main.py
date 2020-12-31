""" Maybe I could do something like this??? """

import sys
import doctest
import re
import pygame as pg
from os.path import abspath
import doctest
from time import sleep
from random import choice, randint
from typing import List, Tuple, Union, Dict
from character_classes import (Character, NormalCharacter, ActiveCharacter,
                               ObjectiveCharacter, NegativeCharacter)
from constants import (OPTION_A, OPTION_B, OPTION_C, OPTION_D, RUN, ITEM, INFO,
                       TALK, USAGE_DEC, COLOGNE_LOWER, COLOGNE_HIGHER,
                       WASHROOM_LOWER, WASHROOM_HIGHER, SHOW_OFF_LOWER,
                       SHOW_OFF_HIGHER, NORMAL, OBJECTIVE, ACTIVE, NEGATIVE,
                       YES, NO, OPTION_E, conf_gain_SE, conf_lose_SE,
                       cologne_SE, slap_SE, invalid_SE, invalid_2_SE, info_SE,
                       toilet_SE, run_SE, select_SE, drum_roll_SE, gunshot_1_SE,
                       gunshot_2_SE, panic2_SE, sounds, OPTION_F)
from questions_list import questions
from prompts import (decision_prompt, menu_prompt, item_prompt, options_prompt,
                     yes_no_prompt, credits_prompt, music_lvl_prompt,
                     question_format, sound_lvl_prompt, instructions_prompt,
                     story_prompt, information_prompt)
from all_credits import credit_str

fst_nmes, last_nmes = [], []
personalities = {NORMAL: [], OBJECTIVE: [], ACTIVE: [], NEGATIVE: []}


# Initializing Files

fst_nms_file = abspath(r'text_files\Names\women_first_names.txt')
lst_nms_file = abspath(r'text_files\Names\last_names.txt')


with open(fst_nms_file) as fst, open(lst_nms_file) as last:
    fst_nmes, last_nmes = fst.read().split('\n'), last.read().split('\n')

bsic_file = abspath(r'text_files\Personalities'\
                            r'\basic_personality.txt')
active_file = abspath(r'text_files\Personalities'\
                              r'\active_personality.txt')
ngtive_file = abspath(r'text_files\Personalities'\
                              r'\negative_personality.txt')
ojctive_file = abspath(r'text_files\Personalities'\
                               r'\objective_personality.txt')

with open(bsic_file) as bsic, open(active_file) as active,\
open(ngtive_file) as ngtive, open(ojctive_file) as objctive:
    for line in bsic:
        personalities.get(NORMAL).append(line.strip())
    for line in ngtive:
        personalities.get(NEGATIVE).append(line.strip())
    for line in active:
        personalities.get(ACTIVE).append(line.strip())
    for line in objctive:
        personalities.get(OBJECTIVE).append(line.strip())


# Initializing Music

pg.init()
music_path = r'Sounds\Music'

# Game Ready

print('Welcome to the game!')
input('Enter any key to start!\n')


def main_game() -> None:
    """
    The main menu of the game.

    """

    menu_choice = ''
    pg.mixer.music.set_volume(0.5)
    music_vol = 0.5
    sound_vol = slap_SE.get_volume()
    select_SE.play()

    while True:
        music_loop(abspath(music_path + '\BGM.wav'), 500, 100)
        menu_options = (OPTION_A, OPTION_B, OPTION_C, OPTION_D, OPTION_E, 
                        OPTION_F)
        menu_choice = prompt_select(menu_prompt(), menu_options).upper()

        while menu_choice.upper() in (OPTION_B, OPTION_C, OPTION_D, OPTION_E):
            select_SE.play()

            if menu_choice.upper() == OPTION_B:
                prompt_select(story_prompt(), OPTION_A)
                select_SE.play()

            elif menu_choice.upper() == OPTION_C:
                prompt_select(instructions_prompt(), OPTION_A)
                select_SE.play()

            elif menu_choice.upper() == OPTION_D:
                music_loop(music_path + r'\new_options_men.wav', 500, 100)
                options = (OPTION_A, OPTION_B, OPTION_C)
                menu_choice = prompt_select(options_prompt(), options).upper()
                while menu_choice.upper() in (OPTION_A, OPTION_B):
                    if menu_choice == OPTION_A:
                        music_vol = music_vol_change(music_vol)
                    elif menu_choice == OPTION_B:
                        sound_vol = sound_vol_change(sound_vol)
                    select_SE.play()
                    menu_choice = prompt_select(options_prompt(), options).upper()
                select_SE.play()
                music_loop(music_path + '\BGM.wav', 500, 100)

            elif menu_choice.upper() == OPTION_E:
                prompt_select(credits_prompt(credit_str), OPTION_A)
                select_SE.play()

            menu_choice = prompt_select(menu_prompt(), menu_options).upper()

        if menu_choice.upper() == OPTION_A:
            person = person_creator()
            battle(person)

        elif menu_choice.upper() == OPTION_F:
            select_SE.play(), print('Quitting...')
            sys.exit()


def music_vol_change(volume: float) -> float:
    """
    Display the current music <volume> and return the valid
    volume that the user has chosen.

    A valid volume must be a float that is between 0 and 1.0
    inclusive.

    """

    music_choice = -1
    select_SE.play()

    while not (0 <= music_choice <= 1.0):
        music_choice = input(f'{music_lvl_prompt(volume)}\n')
        if (not music_choice.replace('.', '0', 1).isdigit()
            or music_choice == '.'):
             music_choice = -1
        music_choice = float(music_choice)

    pg.mixer.music.set_volume(music_choice)
    return music_choice


def sound_vol_change(volume: float) -> float:
    """
    Display the current sound <volume> and return the valid
    volume that the user has chosen.

    A valid volume must be a float that is between 0 and 1.0
    inclusive.

    """

    sound_choice = -1
    select_SE.play()

    while not (0 <= sound_choice <= 1.0):
        sound_choice = input(f'{sound_lvl_prompt(volume)}\n')
        if (not sound_choice.replace('.', '0', 1).isdigit()
            or sound_choice == '.'):
             sound_choice = -1
        sound_choice = float(sound_choice)

    for i in sounds:
        i.set_volume(sound_choice)

    return sound_choice


def battle(person: Character) -> None:
    """
    Begins the actual game, featuring the user 'battling' against
    <person>.

    """

    while True:
        excuses_amt, cologne_amt, confidence, decision = 3, 3, 100, ''
        turns = 15
        msg, question_lst = '', questions(person)
        battle_actions, yes_no = (TALK, ITEM, INFO, RUN), (YES, NO)
        options = (OPTION_A, OPTION_B, OPTION_C, OPTION_D)

        info_SE.play()
        input(f'You are dating:\n{person}\nEnter any button to continue.\n')
        music_loop(music_path + '\godot_loop_w_chatter.wav', 500, 500)

        decision = prompt_select(decision_prompt(confidence, turns),
                                 battle_actions).upper()

        while decision.upper() in battle_actions:

            if decision == TALK:
                select_SE.play()
                turns -= 1
                question_q_and_a = choice(question_lst)
                question_nums = question_pick(question_lst, question_q_and_a)
                if question_nums[0] == 17:
                    gunshot_1_SE.play(1), panic2_SE.play()
                    pg.mixer.music.fadeout(1000)
                decision = prompt_select(question_format(question_q_and_a),
                                         options).upper()
                confidence = talk_effects(decision, person, confidence,
                                          question_nums[0])
                question_lst.pop(question_nums[1])

            elif decision == ITEM:
                select_SE.play()
                decision = prompt_select(item_prompt(cologne_amt, excuses_amt),
                                         options).upper()
                if valid_item_option(cologne_amt, excuses_amt, decision):
                    if decision == OPTION_A:
                        cologne_amt = decrease_item_amt(cologne_amt)
                    elif decision == OPTION_B:
                        excuses_amt = decrease_item_amt(excuses_amt)
                    confidence = item_effect(decision, confidence)

            elif decision == INFO:
                info_SE.play()
                prompt_select(information_prompt(person), OPTION_A)
                select_SE.play()

            if confidence <= 0 or decision == RUN:
                select_SE.play()
                if decision == RUN:
                    msg = 'Are you sure you want to run?'
                    decision = prompt_select(yes_no_prompt(msg), yes_no).upper()
                if decision == YES or confidence <= 0:
                    run_SE.play()
                    decision = game_over_lose().upper()
                    if decision == YES:
                        person, decision = person_creator(), ''
                    else:
                        select_SE.play()
                        return
                elif decision == NO:
                    select_SE.play()
            elif turns <= 0:
                game_over_win(confidence)
                msg = 'Do you want to play again?'
                select_SE.play()
                decision = prompt_select(yes_no_prompt(msg), yes_no).upper()
                if decision == YES:
                    person, decision = person_creator(), ''
                else:
                    select_SE.play()
                    return

            if decision != '':
                decision = prompt_select(decision_prompt(confidence, turns),
                                         battle_actions).upper()


def question_pick(question_lst: List[Dict],
                  question_q_and_a) -> Tuple[int, int]:
    """
    Return the question number of <question_q_and_a> by searching
    for <question_q_and_a> in <question_lst> and return the index
    of said question.

    The 0th index of the tuple is the question number.
    The 1st index of the tuple is the question index.

    """

    options, i = (OPTION_A, OPTION_B, OPTION_C, OPTION_D), 0
    question = sorted(list(question_q_and_a.keys()))[1]

    while (question != sorted(list(question_lst[i].keys()))[1]
           and i <= len(question_lst) - 1):
            i += 1

    if question != sorted(list(question_lst[i].keys()))[1]:
        print('Error 1: Question not found')
        sys.exit()

    return (int(re.search(r'[0-9]+', question).group()), i)


def game_over_lose() -> str:
    """
    Return the user's decision after they have lost the game.

    """

    pg.mixer.music.stop(), pg.mixer.music.unload()
    pg.mixer.music.load(music_path + r'\jingle_07.mp3')
    pg.mixer.music.play()

    print('You became so unconfident that you ran away from the'\
          ' restaurant.\nYou have lost!')

    message = 'Would you like the play again?'
    return prompt_select(yes_no_prompt(message), (YES, NO)).upper()


def game_over_win(confidence: int) -> None:
    """
    Print the reaction of the users' date after they 15 turns have
    passed. Their reaction is determined by the user's total <confidence>
    after these 15 turns.

    """

    pg.mixer.music.stop(), pg.mixer.music.unload()
    pg.mixer.music.load(music_path + r'\results.mp3')
    pg.mixer.music.play()

    input('You have survived all 15 turns!\n')
    select_SE.play()
    input('However, how does your date feel?\n')
    print('Your date says...')
    drum_roll_SE.play(), sleep(4.5), pg.mixer.music.unload()
    nums = win_results_music(confidence)
    pg.mixer.music.load(music_path + r'\{}.mp3'.format(nums[0]))
    pg.mixer.music.play(), input(win_results_text(nums[1]))


def win_results_music(confidence: int) -> Tuple[int, int]:
    """
    Return a tuple that contains (in order):

    - An int that determines what victory song to play
    - An int that the user's <confidence> is greater than or equal to

    There are a limited number of ints that the user's <confidence> can
    be greater than. These are:

    - 90
    - 80
    - 70
    - 60
    - 40
    - 30
    - 20
    - 0

    Each correspond to a unique int in descending order (eg. 90 -> 1,
    80 -> 2, 70 -> 3, etc.), which determines what song to be played. There
    are 8 songs in total.
    
    If there a multiple ints that the user's <confidence> is greater than
    or equal to, use the value that has the greatest key int amongst them.

    >>> win_results_music(81)
    (2, 80)
    >>> win_results_music(90)
    (1, 90)
    >>> win_results_music(-34252)
    (8, 0)
    >>> win_results_music(68)
    (4, 60)

    """

    pg.mixer.music.unload()
    conf_states, i = {90: 1, 80: 2, 70: 3, 60: 4, 40: 5, 30: 6, 20: 7, 0: 8}, 0
    key_lst = sorted(list(conf_states.keys()), reverse=True)
    while confidence < key_lst[i] and i < len(key_lst) - 1:
        i += 1
    return (conf_states.get(key_lst[i]), key_lst[i])


def win_results_text(conf_key: int) -> str:
    """
    Return a string based what <conf_key> matches.

    >>> win_results_text(80).strip()
    'Impressive! I might even consider another date with him in the future!'
    >>> win_results_text(20).strip()
    'Who matched us to date? That was terrible!'
    >>> win_results_text(30).strip()
    'A waste of my time, though I am thankful for the free meal he provided.'
    >>> win_results_text(34).strip()
    ''

    """
    
    conf_states = {90: 'Absolutely amazing! He\'s charming, dashing,'\
                       ' and definitely my type!'\
                       '\nSo handsome, when\'s our next date?',
                   80: 'Impressive! I might even consider another date with '\
                       'him in the future!',
                   70: 'A great partner! It\'s nice to find a man that'\
                       ' shares my interests.',
                   60: 'He\'s much better than the previous men I\'ve dated, '\
                       'I\'ll tell you that much...',
                   40: 'It wasn\'t the best date I\'ve ever had, but it was'\
                       ' far from the worst.',
                   30: 'A waste of my time, though I am thankful for the free'\
                       ' meal he provided.',
                   20: 'Who matched us to date? That was terrible!',
                    0: 'Awful. He was unbearably atrocious. Who knew that such'\
                       ' an absolute and INSANE buffoon ever existed...'}

    if not conf_states.get(conf_key):
        return ''

    return conf_states.get(conf_key) + '\n'


def prompt_select(prompt: str, options: tuple) -> str:
    """ 
    Repeatedly ask the user for a selection, according to <prompt>, until one of
    the determined <options> are received from the user.

    Return the user's input with leading and trailing whitespace removed.

    """

    prompt += '\n'
    selection = input(prompt)
    while (selection.strip().upper() not in options or
           selection.strip().upper() == ''):
        invalid_SE.play()
        selection = input(f'Invalid choice\n{prompt}')

    return selection.strip()


def valid_item_option(cologne: int, excuses: int, decision: str) -> bool:
    """
    Return True or False when the user's <decision> to use an item is valid
    or not.

    <cologne> and <excuses> must not be equal to or less than 0 in order
    to be valid.

    """

    if decision.upper() == OPTION_A and cologne <= 0:
        invalid_2_SE.play()
        print('You don\'t have any cologne left!')
        return False

    elif decision.upper() == OPTION_B and excuses <= 0:
        invalid_2_SE.play()
        print('Your date doesn\'t think that you are actually going to the'\
              ' washroom and forces you to stay put!')
        return False

    return True


def decrease_item_amt(item: int) -> int:
    """
    Return the decreased amount of an <item>, as if it were used.

    """

    return item - USAGE_DEC


def item_effect(decision: str, confidence: int) -> int:
    """
    Increase the <confidence> of the user, depending on their item <decision>.

    """

    amt_gain = 0

    if decision.upper() == OPTION_A:
        cologne_SE.play()
        amt_gain = randint(COLOGNE_LOWER, COLOGNE_HIGHER)
        confidence += amt_gain
        input('You used cologne! You now smell excellent!\n')

    elif decision.upper() == OPTION_B:
        toilet_SE.play()
        amt_gain = randint(WASHROOM_LOWER, WASHROOM_HIGHER)
        confidence += amt_gain
        input('You went to the washroom! Giving yourself a peptalk'\
              ' has worked miracles!\n')

    elif decision.upper() == OPTION_C:
        slap_SE.play()
        amt_gain = randint(SHOW_OFF_LOWER, SHOW_OFF_HIGHER)
        confidence += amt_gain
        input('You unfurl your sleeve, show your date your arm, and'\
              ' slap it as you flex it.\n')
        if amt_gain < 0:
            print('It jiggles upon impact. It\'s safe to say your'\
                  ' date isn\'t very impressed...')
        elif amt_gain > 0:
            print('It is absolutely motionless upon impact. Impressive!')

    elif decision.upper() == OPTION_D:
        select_SE.play()
        return confidence

    confidence_gain_lost(amt_gain)
    return min(confidence, 100)


def person_creator() -> Character:
    """ 
    Return a unique Character class.

    This includes creating the Character's true_pers, pers, name, first_name,
    last_name, and prof.

    """

    behaviour, profile = '', ''
    character_dict = {NORMAL: NormalCharacter,
                      NEGATIVE: NegativeCharacter,
                      ACTIVE: ActiveCharacter,
                      OBJECTIVE: ObjectiveCharacter}
    behaviour = rand_pers()
    profile = character_dict.get(behaviour[0])(rand_nam(), behaviour[0],
                                               behaviour[1])
    return profile


def rand_nam() -> str:
    """
    Create a random name to 'battle.'
    This involves grabbing a random first and last name
    from 'women_first_names.txt' and 'last_names.txt' respectively.

    """

    return choice(fst_nmes) + ' ' + choice(last_nmes)


def rand_pers() -> Tuple[str, str]:
    """
    Assign a random personality to a character.

    Personalities fall into one of four categories:

    - Active
    - Objective
    - Negative
    - Normal

    To spice things up a bit, each category has a list
    of synomnyms that belong to it. Return the category
    and the synonym as a tuple.

    """

    key = choice(list(personalities.keys()))
    value = choice(personalities.get(key))
    return (key, value)


def talk_effects(decision: str, person: Character, confidence: int,
                 question_num: int) -> int:
    """
    Return the user's modified <confidence>, based on their <decision>, their
    randomly chosen <question_index> and their randomly selected <person>.

    """

    decision = decision.upper()
    amt_gain = person.reactions().get(question_num).get(decision)(person)
    if amt_gain == None:
        return 0
    confidence_gain_lost(amt_gain)

    return min(confidence + amt_gain, 100)
    

def confidence_gain_lost(amount_gained_lost: int) -> None:
    """
    Print how much confidence the user has gained or lost, as determined
    by <amount_gained_lost>.

    """

    if amount_gained_lost > 0:
        conf_gain_SE.play()
        input(f'You have gained {amount_gained_lost}% confidence!\n')
    elif amount_gained_lost < 0:
        conf_lose_SE.play()
        input(f'You have lost {abs(amount_gained_lost)}% confidence!\n')
    else:
        input('Nothing interesting happens to your confidence.\n')


def music_loop(song: str, ms_out: int, ms_in: int) -> None:
    """
    Fadeout the current music playing by a certain number of milliseconds,
    represented by <ms_out>. Unload the song, and load and play the
    new <song> for an indefinite amount of times, making it fade in for a
    certain number of milliseconds, represented by <ms_in>.

    """

    pg.mixer.music.fadeout(ms_out), pg.mixer.music.unload()
    pg.mixer.music.load(song), pg.mixer.music.play(-1, 0, ms_in)


main_game()
