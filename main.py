""" (Not) Super Seducer: The Bootleg Version - The Main File That Runs the Game """

from sys import exit
import doctest
import re
import pygame as pg
import doctest
from time import sleep
from random import choice, randint, shuffle
from typing import List, Tuple, Union, Dict, Callable, Optional
from character_classes import (Character, NormalCharacter, ActiveCharacter,
                               ObjectiveCharacter, NegativeCharacter,
                               person_creator)
from constants import (EASY_TURNS, GAME_OVER_MUSIC, HARD_CONF, HARD_TURNS, MINOR_NEG, MINOR_POS, NORM_CONF, 
                       OPTION_A, OPTION_B, OPTION_C, OPTION_D, RUN, ITEM, INFO,
                       SMALL_NEG, SMALL_POS,
                       TALK, USAGE_DEC, COLOGNE_LOWER, COLOGNE_HIGHER,
                       WASHROOM_LOWER, WASHROOM_HIGHER, SHOW_OFF_LOWER,
                       SHOW_OFF_HIGHER, NORMAL, OBJECTIVE, ACTIVE, NEGATIVE,
                       YES, NO, OPTION_E, conf_gain_small_SE, conf_gain_big_SE, conf_lose_SE,
                       slap_SE, invalid_SE, invalid_2_SE, info_SE, run_SE, select_SE,
                       drum_roll_SE, sounds, OPTION_F, EASY_TURNS, EASY_CONF, 
                       E_COLOGNE_AMT, E_WSHROOM_AMT, NORM_TURNS,
                       NORM_CONF, N_COLOGNE_AMT, N_WSHROOM_AMT, HARD_TURNS,
                       HARD_CONF, H_COLOGNE_AMT, H_WSHROOM_AMT, DIF_EASY,
                       DIF_NORM, DIF_HARD, MENU_MUSIC, JINGLE_PATH, OPTIONS_MUSIC,
                       CREDITS_MUSIC, BATTLE_MUSIC_LST, RESULTS_MUSIC, GAME_OVER_MUSIC, BATTLE_MUSIC_PATH)
from questions_list import questions
from prompts import (decision_prompt, diff_prompt, menu_prompt, item_prompt, music_select_prompt, options_prompt,
                     yes_no_prompt, credits_prompt, music_lvl_prompt,
                     question_format, sound_lvl_prompt, instructions_prompt,
                     story_prompt, information_prompt)
from all_credits import creds
from file_init import game_setup, music_loop, clear_term, q_prompt_select, prompt_select


# Initializing
fst_nmes, last_nmes, personalities = game_setup()
pg.init()

# Game Ready

print('Welcome to (Not) Super Seducer: The Bootleg Version!')
input('Enter any key to start!\n')


def main_game() -> None:
    """
    The main menu of the game.

    """
    menu_choice = ''
    music_vol = 0.5
    diff = DIF_NORM
    credit_str = creds()
    pg.mixer.music.set_volume(music_vol)
    sound_vol = slap_SE.get_volume()
    select_SE.play(), clear_term()

    while True:
        music_loop(MENU_MUSIC, 1000, 500, 0.0)
        menu_options = (OPTION_A, OPTION_B, OPTION_C, OPTION_D, OPTION_E, 
                        OPTION_F)
        menu_choice = prompt_select(menu_prompt(), menu_options).upper()

        while menu_choice.upper() in menu_options:
            select_SE.play(), clear_term()

            if menu_choice.upper() == OPTION_A:
                person = person_creator()
                battle(person, diff)
            
            elif menu_choice.upper() == OPTION_B:
                prompt_select(story_prompt(), OPTION_A)
                select_SE.play()

            elif menu_choice.upper() == OPTION_C:
                prompt_select(instructions_prompt(), OPTION_A)
                select_SE.play()

            elif menu_choice.upper() == OPTION_D:
                music_loop(OPTIONS_MUSIC, 1000, 100, 0.0)
                options = (OPTION_A, OPTION_B, OPTION_C, OPTION_D)
                menu_choice = prompt_select(options_prompt(), options).upper()
                clear_term()
                while menu_choice.upper() in (OPTION_A, OPTION_B, OPTION_C):
                    if menu_choice == OPTION_A:
                        music_vol = vol_change(music_vol, music_lvl_prompt)
                        pg.mixer.music.set_volume(music_vol)

                    elif menu_choice == OPTION_B:
                        sound_vol = vol_change(sound_vol, sound_lvl_prompt)
                        for i in sounds:
                            i.set_volume(sound_vol)

                    elif menu_choice == OPTION_C:
                        dif_choice = ''
                        select_SE.play()
                        dif_choice = prompt_select(diff_prompt(diff), options)
                        if dif_choice.upper() == OPTION_A: diff = DIF_EASY
                        elif dif_choice.upper() == OPTION_B: diff = DIF_NORM
                        elif dif_choice.upper() == OPTION_C: diff = DIF_HARD
                    select_SE.play()
                    menu_choice = prompt_select(options_prompt(), options).upper()
                select_SE.play()
                music_loop(MENU_MUSIC, 1000, 500, 0.0)

            elif menu_choice.upper() == OPTION_E:
                music_loop(CREDITS_MUSIC, 1000, 1000, 0.0)
                menu_choice = prompt_select(credits_prompt(credit_str), OPTION_A)
                menu_choice = ''
                select_SE.play()
                music_loop(MENU_MUSIC, 1000, 500, 0.0)
            
            elif menu_choice.upper() == OPTION_F:
                menu_choice = prompt_select(yes_no_prompt('Are you sure you want to quit?'),
                                            (YES, NO)).upper()
                if menu_choice == YES:
                    clear_term()
                    print('Quitting...')
                    exit()

                select_SE.play()

            menu_choice = prompt_select(menu_prompt(), menu_options).upper()


def vol_change(volume: float, prompt: Callable[[float], str]) -> float:
    """
    Display the current <volume>, displaying the appropriate <prompt> given, 
    and return the valid volume that the user has chosen.

    A valid volume must be a float that is between 0 and 1.0
    inclusive.

    """

    vol_choice = -1
    select_SE.play()

    while not (0 <= vol_choice <= 1.0):
        clear_term()
        vol_choice = input(f'{prompt(volume)}\n')
        if (not vol_choice.replace('.', '0', 1).isdigit()
            or vol_choice == '.'):
             invalid_SE.play()
             vol_choice = -1
        vol_choice = float(vol_choice)

    return vol_choice


def battle(person: Character, diff: str) -> None:
    """
    Begins the actual game, featuring the user 'battling' against
    <person> with <diff>.

    """

    while True:
        select_SE.play(), clear_term()
        battle_track = music_select(BATTLE_MUSIC_LST)

        confidence, turns = NORM_CONF, NORM_TURNS
        excuses_amt, cologne_amt = N_WSHROOM_AMT, N_COLOGNE_AMT
        if diff == DIF_EASY:
            excuses_amt, cologne_amt = E_WSHROOM_AMT, E_COLOGNE_AMT
            confidence, turns = EASY_CONF, EASY_TURNS
        elif diff == DIF_HARD:
            excuses_amt, cologne_amt = H_WSHROOM_AMT, H_COLOGNE_AMT
            confidence, turns = HARD_CONF, HARD_TURNS
        decision, msg = '', ''
        question_lst = questions(person)
        battle_actions, yes_no = (TALK, ITEM, INFO, RUN), (YES, NO)
        options = (OPTION_A, OPTION_B, OPTION_C, OPTION_D)
        cologne_use, bath_use, slap_use = False, False, 0

        input(f'You are dating:\n{person}\nEnter any button to continue.\n')
        music_loop(battle_track, 1000, 0, 0.0)

        decision = prompt_select(decision_prompt(confidence, turns),
                                 battle_actions).upper()

        while decision.upper() in battle_actions:
            clear_term()

            if decision == TALK:
                select_SE.play(), clear_term()
                turns -= 1

                question_q_and_a = choice(question_lst) # {question #: words, answers: {options: words}}
                question_nums = question_pick(question_lst, question_q_and_a)

                random_answers = question_q_and_a.get('Answers')
                if random_answers is None:
                    input('Error 2: answers is None\n')
                    exit()

                random_answers = [answer for answer in random_answers.values()]
                shuffle(random_answers)
                decision = q_prompt_select(question_format(question_q_and_a,
                                                           random_answers),
                                           options, question_q_and_a).upper() ## randomization point ##
                
                confidence = quest_result(decision, person, confidence, question_nums[0], diff)
                cologne_amt = quest_side_effects(cologne_amt, question_nums[0], decision)

                question_lst.pop(question_nums[1]) # use index num to remove question
                cologne_use, bath_use, slap_use = False, False, 0

            while decision == ITEM:
                select_SE.play()
                item_dec = prompt_select(item_prompt(cologne_amt, excuses_amt,
                                                     confidence),
                                                     options).upper()
                if (valid_item_num(cologne_amt, excuses_amt, item_dec)
                    and valid_item_use(cologne_use, bath_use, slap_use,
                                       item_dec)):
                    clear_term()
                    if item_dec == OPTION_A:
                        cologne_amt = decrease_item_amt(cologne_amt)
                        cologne_use = True
                    elif item_dec == OPTION_B:
                        excuses_amt = decrease_item_amt(excuses_amt)
                        bath_use = True
                    elif item_dec == OPTION_C: slap_use += 1
                    confidence = item_effect(item_dec, confidence, diff)
                    if confidence <= 0: decision = ''
                if item_dec == OPTION_D: decision = item_dec

            if decision == INFO:
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
                        pg.mixer.music.fadeout(1000)
                        person, decision = person_creator(), ''
                    else:
                        select_SE.play()
                        music_loop(MENU_MUSIC, 1000, 500, 0.0)
                        return
                elif decision == NO:
                    select_SE.play()
            elif turns <= 0:
                game_over_win(confidence, diff)
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

# def dif_select() -> str:
#     dif_choice = ''
#     select_SE.play()
#     dif_choice = prompt_select(diff_prompt(diff), options)
#     if dif_choice.upper() == OPTION_A: diff = DIF_EASY
#     elif dif_choice.upper() == OPTION_B: diff = DIF_NORM
#     elif dif_choice.upper() == OPTION_C: diff = DIF_HARD
#     select_SE.play()
#     menu_choice = prompt_select(options_prompt(), options).upper()    
#     return 


def music_select(music_lst: List[str]) -> Optional[str]:
    if len(music_lst) < 0:
        return

    i = 0
    options = (OPTION_A, OPTION_B, OPTION_C)
    while True:
        clear_term()
        music_loop(BATTLE_MUSIC_PATH + f'\{music_lst[i]}.wav', 0, 100, 0)
        select_choice = prompt_select(music_select_prompt(music_lst[i]), options)
        if select_choice == OPTION_A:
            info_SE.play(), clear_term()
            return BATTLE_MUSIC_PATH + f'\{music_lst[i]}.wav'
        elif select_choice == OPTION_B:
            if i != len(music_lst) - 1: i += 1
            else: i = 0
        else:
            if i != 0: i -= 1
            else: i = len(music_lst) - 1

def question_pick(question_lst: List[Dict[str, Union[str, Dict[str, str]]]],
                  question_q_and_a) -> Tuple[int, int]:
    """
    Return the question number of <question_q_and_a>
    and return the index of said question.

    The 0th index of the tuple is the question number.
    The 1st index of the tuple is the question index.

    """

    i = 0
    question = sorted(list(question_q_and_a.keys()))[1]

    while (question != sorted(list(question_lst[i].keys()))[1]
           and i <= len(question_lst) - 1):
            i += 1

    if question != sorted(list(question_lst[i].keys()))[1]:
        print('Error 1: Question not found')
        exit()

    return int(re.search(r'[0-9]+', question).group()), i

def game_over_lose() -> str:
    """
    Return the user's decision after they have lost the game.

    """

    pg.mixer.music.stop(), pg.mixer.music.unload()
    pg.mixer.music.load(GAME_OVER_MUSIC)
    pg.mixer.music.play(-1, 0, 200)

    message = 'You became so unconfident that you ran away from the'\
              ' restaurant.\n\nlmao what a wimp\n\n'\
              'Want to play again?'

    return prompt_select(yes_no_prompt(message), (YES, NO)).upper()


def game_over_win(confidence: int, diff: str) -> None:
    """
    Print the reaction of the users' date after a certain number of turns
    have passed. The turn amount is determined by <diff>.
    
    The users' date's reaction is determined by the user's total <confidence>
    after these number of turns.

    """

    user_dec, turn_amt = '', NORM_TURNS
    pg.mixer.music.stop(), pg.mixer.music.unload()
    pg.mixer.music.load(RESULTS_MUSIC), pg.mixer.music.play()

    if diff == DIF_HARD:
        turn_amt = HARD_TURNS
    elif diff == DIF_EASY:
        turn_amt = EASY_TURNS

    input(f'You have survived all {turn_amt} turns as a {diff}!\n')
    select_SE.play()
    input('However, how does your date feel?\n'), clear_term()
    print('Your date says...'), drum_roll_SE.play(), sleep(4.5)
    pg.mixer.music.unload()
    nums = win_results_music(confidence)
    pg.mixer.music.load(JINGLE_PATH + r'\{}.wav'.format(nums[0]))
    pg.mixer.music.play()
    
    while user_dec != 'a':
        user_dec = input(win_results_text(nums[1]) + 'Enter in "a"'\
                                                     ' to continue\n').lower()
        clear_term()


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
    return conf_states.get(key_lst[i]), key_lst[i]


def win_results_text(conf_key: int) -> str:
    """
    Return a string based what <conf_key> matches.

    >>> win_results_text(80).strip()
    'Impressive! I might even consider another date with him in the future!'
    >>> win_results_text(20).strip()
    'Who matched us to date? That was terrible!'
    >>> win_results_text(30).strip()
    'A waste of my time, though I am thankful for the free dinner.'
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
                       ' dinner.',
                   20: 'Who matched us to date? That was terrible!',
                    0: 'Awful. He was unbearably atrocious. Who knew that such'\
                       ' an absolute and INSANE buffoon ever existed...'}

    if not conf_states.get(conf_key):
        return 'Error 1: Missing confidence dialogue'

    return conf_states.get(conf_key) + '\n' * 2


def valid_item_num(cologne: int, excuses: int, item_dec: str) -> bool:
    """
    Return True or False when the user's <decision> to use an item is valid
    or not.

    <cologne> and <excuses> must not be equal to or less than 0 in order
    to be valid.

    """

    if item_dec.upper() == OPTION_A and cologne <= 0:
        invalid_2_SE.play()
        input('You don\'t have any cologne left!\n')
        return False

    elif item_dec.upper() == OPTION_B and excuses <= 0:
        invalid_2_SE.play()
        input('Your date doesn\'t think that you are actually going to the'\
              ' washroom and forces you to stay put!\n')
        return False

    return True


def valid_item_use(cologne_use: bool, bath_use: bool, slap_use: int,
                   item_dec: str) -> bool:
    """
    Return False and the correct message (dependent on <decision>)
    if the user has:

    - <cologne_use> is True (Used the cologne item at least once)
    - <bath_use> is True (Used the bathroom break item at least once)
    - slap_use > 2

    Otherwise, return True.
    """
    if item_dec == OPTION_A and cologne_use:
        invalid_2_SE.play()
        input('Your date remarks of how putrid you smell.\n'\
              'You probably need to wait a while before using your'\
              ' cologne again...')
        return False

    elif item_dec == OPTION_B and bath_use:
        invalid_2_SE.play()
        input('As you get up to leave, your date openly questions'\
              ' whether you have bladder problems or not.\n'\
              'It seems that you need to go to the washroom at a'\
              ' later time...')
        return False

    elif item_dec == OPTION_C and slap_use > 2:
        invalid_2_SE.play()
        input('Your arm is visibly red from all of the slapping you\'ve'\
              ' done!\nYou need to give your arm a rest before attempting'\
              ' to impress your date again.')
        return False

    return True


def decrease_item_amt(item: int) -> int:
    """
    Return the decreased amount of an <item>, as if it were used.

    """

    return item - USAGE_DEC


def item_effect(decision: str, confidence: int, diff: str) -> int:
    """
    Increase the <confidence> of the user, depending on their item <decision>.

    """

    amt_gain = 0

    if decision.upper() == OPTION_A:
        amt_gain = randint(COLOGNE_LOWER, COLOGNE_HIGHER)
        confidence += amt_gain
        input('You used cologne! You now smell excellent!\n')

    elif decision.upper() == OPTION_B:
        amt_gain = randint(WASHROOM_LOWER, WASHROOM_HIGHER)
        confidence += amt_gain
        input('You went to the washroom! Giving yourself a peptalk'\
              ' has worked miracles!\n')

    elif decision.upper() == OPTION_C:
        slap_SE.play()
        amt_gain = randint(SHOW_OFF_LOWER, SHOW_OFF_HIGHER)
        confidence += amt_gain
        input('You unfurl your sleeve and slap your arm as you flex it.\n')
        if amt_gain < 0:
            print('It jiggles upon impact. Your'\
                  ' date doesn\'t seem very impressed...')
        elif amt_gain > 0:
            print('It is absolutely motionless upon impact. Impressive!')

    elif decision.upper() == OPTION_D:
        select_SE.play()
        return confidence

    confidence_gain_lost(amt_gain, diff), clear_term()
    return min(confidence, 100)


def quest_result(decision: str, person: Character, confidence: int,
                 question_num: int, diff: str) -> int:
    """
    Return the user's modified <confidence>, based on their <decision>, their
    randomly chosen <question_index>, and their randomly selected <person>.

    The amount of confidence gained/lost will also be determined by
    the player's <diff> difficulty.

    """
    amt_gain = person.reactions().get(question_num).get(decision.upper())(person)
    confidence_gain_lost(amt_gain, diff)
    return min(amt_gain + confidence, 100)

def quest_side_effects(cologne_use: int, question_num: int, 
                       decision: str) -> int:
    if question_num == 32 and decision == 'B':
        cologne_use += 1
    elif question_num == 36:
        if decision == 'A': cologne_use += 1
        elif decision == 'B' and cologne_use > 0: cologne_use -= 1
    return cologne_use
    

def confidence_gain_lost(amt_gain: int, diff: str) -> None:
    """
    Print how much confidence the user has gained or lost, as determined
    by <amt_gain>.

    """
    amt_gain = conf_gain_adj(amt_gain, diff)

    if amt_gain > 0:
        if amt_gain > 15:
            conf_gain_big_SE.play()
        else:
            conf_gain_small_SE.play()
        input(f'You have gained {amt_gain}% confidence!\n')
    elif amt_gain < 0:
        conf_lose_SE.play()
        input(f'You have lost {abs(amt_gain)}% confidence!\n')
    else:
        input('Nothing interesting happens to your confidence.\n')
    
    clear_term()

def conf_gain_adj(amt_gain: int, diff: str) -> int:
    """
    Return the modified <amt_gain> value after taking note of the
    user's <diff> difficulty.
    """

    if diff == DIF_EASY:
        if amt_gain > 0:
            amt_gain += SMALL_POS

        elif amt_gain < -5:
            amt_gain += MINOR_POS
        elif amt_gain < -10:
            amt_gain += SMALL_POS

    elif diff == DIF_HARD:
        if amt_gain < 0:
            amt_gain += SMALL_NEG
        elif amt_gain > 5:
            amt_gain += MINOR_NEG

    return amt_gain


if __name__ == '__main__':
    main_game()
