from os.path import abspath
from constants import NORMAL, OBJECTIVE, ACTIVE, NEGATIVE, invalid_SE
from typing import Tuple, List, Dict
import subprocess, platform
import pygame as pg

def first_names_lst() -> List[str]:
    """
    Return a list of women first names from
    "women_first_names.txt"
    """
    with open(abspath(r'text_files\Names\women_first_names.txt')) as fst:
        return fst.read().split('\n')

def last_names_lst() -> List[str]:
    """
    Return a list of women first names from
    "last_names.txt"
    """
    with open(abspath(r'text_files\Names\last_names.txt')) as lst:
        return lst.read().split('\n')

def personalities_dict() -> List[str]:
    """
    Return a list of available personalities
    """
    personalities = {NORMAL: [], OBJECTIVE: [], ACTIVE: [], NEGATIVE: []}

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
        for line in bsic: personalities.get(NORMAL).append(line.strip())
        for line in ngtive: personalities.get(NEGATIVE).append(line.strip())
        for line in active: personalities.get(ACTIVE).append(line.strip())
        for line in objctive: personalities.get(OBJECTIVE).append(line.strip())
    
    return personalities

def game_setup() -> Tuple[List[str], List[str], Dict[str, str]]:
    """
    Return the objects necessary for the game to function.

    These are (in order):
    - First names
    - Last names
    - Personalities

    """
    return (first_names_lst(), last_names_lst(), personalities_dict())


def file_lst_return(name: str) -> List[str]:
    """
    Open <name> in text_files\Other and return a list of its entries.
    """
    with open(abspath(r'text_files\Other'
                      f'\{name}.txt')) as pro_txt:
            content_lst = pro_txt.read().split('\n')
    return content_lst


def music_loop(song: str, ms_out: int, ms_in: int, start: float) -> None:
    """
    Fadeout the current music playing by a certain number of milliseconds,
    represented by <ms_out>. Unload the song, and load and play the
    new <song> at <start> (in seconds) for an indefinite amount of times.

    The new song fades in for a certain number of milliseconds, 
    represented by <ms_in>.

    """

    pg.mixer.music.fadeout(ms_out)
    pg.mixer.music.unload()
    pg.mixer.music.load(song)
    pg.mixer.music.play(-1, start, ms_in)


def clear_term() -> None:
    """
    Clear the user's screen for Windows, Linux, and MacOS only.

    Credit to Brōtsyorfuzthrāx here:
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python

    """
    if platform.system()=="Windows":
        subprocess.Popen("cls", shell=True).communicate()
    else:
        print("\033c", end="")


def _decision_select(prompt: str, options: tuple) -> str:
    clear_term()
    prompt += '\n'
    decision = input(prompt)
    while (decision.strip().upper() not in options or
           decision.strip().upper() == ''):
        invalid_SE.play(), clear_term()
        decision = input(f'Invalid choice\n{prompt}')
    return decision.strip().upper()


def q_prompt_select(prompt: str, options: tuple, question_q_and_a):
    user_choices = question_q_and_a.get('Answers')
    if user_choices is None:
        input('Error 2: answers is None\n')
        exit()

    decision = _decision_select(prompt, options).upper()
    decision_index = prompt.index(f'[{decision}]')
    if prompt[decision_index:].find('\n') == -1:
        selected_ans = prompt[decision_index:]
    else:
        selected_ans = prompt[decision_index:prompt.index('\n', decision_index)]
    selected_ans = selected_ans[selected_ans.index('-') + 2:]

    for option, answer in user_choices.items():
        if answer == selected_ans:
            return option

    input('Error 3: Selected answer not found')
    exit()


def prompt_select(prompt: str, options: tuple) -> str:
    """ 
    Repeatedly ask the user for a decision, according to <prompt>, until one of
    the determined <options> are received from the user.

    Return the user's input with leading and trailing whitespace removed.

    """
    return _decision_select(prompt, options)
