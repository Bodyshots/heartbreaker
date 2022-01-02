""" Module for the game's prompts """

from constants import (TALK, ITEM, INFO, RUN, OPTION_A, OPTION_B, OPTION_C,
                       OPTION_D, OPTION_E, OPTION_F, YES, NO, DIF_EASY,
                       DIF_NORM, DIF_HARD)
from character_classes import Character
from typing import Dict, List


def decision_prompt(confidence: float, turns: int) -> str:
    """ 
    Return a prompt for the user to decide what they want to do, displaying
    the user's <confidence> and the number of <turns> they have left.

    """
    prompt = 'What do you want to do?\n'\
             f'Turns left: {turns}\n\n'\
             f'[{TALK}] - Talk\n'\
             f'[{ITEM}] - Items\n'\
             f'[{INFO}] - Info\n'\
             f'[{RUN}] - Run\n'\
             f'Your Confidence: {confidence}%'

    return prompt


def menu_prompt() -> str:
    """
    Return a prompt for the user to decide if they want to play the game or
    quit.

    """
    prompt = 'Main Menu:\n\n'\
            f'[{OPTION_A}] - Play the game!\n'\
            f'[{OPTION_B}] - Story\n'\
            f'[{OPTION_C}] - Instructions\n'\
            f'[{OPTION_D}] - Options\n'\
            f'[{OPTION_E}] - Credits\n'\
            f'[{OPTION_F}] - Quit'

    return prompt


def item_prompt(cologne: int, excuses: int, confidence: int) -> str:
    """
    Return a prompt for the user to decide what item to use, displaying
    the user's <confidence> and the user's number of <cologne> and <excuses>.

    """
    prompt = f'Your Confidence: {confidence}%\n'\
              'Items:\n\n'\
             f'[{OPTION_A}] - Cologne: {cologne}\n'\
             f'[{OPTION_B}] - Washroom Break Excuses: {excuses}\n'\
             f'[{OPTION_C}] - Show Off!\n'\
             f'[{OPTION_D}] - Back'

    return prompt


def yes_no_prompt(message: str) -> str:
    """
    Return a prompt that prints <message> and gives the user a Yes/No prompt.

    Occurs whether the user has won/lost.

    """
    prompt = f'{message}\n'\
             f'[{YES}] - Yes\n'\
             f'[{NO}] - No'

    return prompt


def question_format(questions: Dict, answers: List[str]) -> str:
    """
    Return a prompt for the user to decide how to respond to a random question
    from <questions>.

    """
    options = (OPTION_A, OPTION_B, OPTION_C, OPTION_D)
    i = 0

    prompt = f'{(questions.get(sorted(list(questions.keys()))[1]))}\n\n'
    for answer in answers:
        prompt += f'[{options[i]}] - {answer}\n'
        i += 1

    return prompt.rstrip()


def options_prompt() -> str:
    """
    Return a prompt for the user to decide what volume to change or to go
    back to the main menu.

    """

    prompt = 'What would you like to change?\n\n'\
            f'[{OPTION_A}] - Music Volume\n'\
            f'[{OPTION_B}] - Sound Effect (SE) Volume\n'\
            f'[{OPTION_C}] - Back'

    return prompt


def music_lvl_prompt(music_vol: float) -> str:
    """
    Return a prompt that displays what the current <music_vol> is and what is
    a valid music volume to change to.

    """

    return f'Current Music volume: {music_vol} (from 0.0 to 1.0)'


def sound_lvl_prompt(sound_vol: float) -> str:
    """
    Return a prompt that displays what the current <sound_vol> is and what is
    a valid sound volume to change to.

    """

    return f'Current SE volume: {sound_vol} (from 0.0 to 1.0)'


def credits_prompt(credits_all: str) -> str:
    """
    Return a prompt that displays <credits_all> and gives the user the option to
    go back to the main menu.

    """

    return f'{credits_all}\n[{OPTION_A}] - Back'


def instructions_prompt() -> str:
    """
    Return a prompt that shows how to play the game.

    """
    prompt = 'Instructions:\n\n'\
             'Your goal is to survive 15 turns of your date with the highest'\
             ' confidence possible.\nYour confidence acts as both your health'\
             ' and score; when it reaches 0, it\'s game over.\n\nWhen '\
             'beginning the game, you\'ll be confronted with your date\'s'\
             ' name and personality.\nAfter that, the game begins. You\'ll'\
             ' have a host of decisions to choose from.'\
             '\n\nThese are as follows:\n1. Talk\n2. Items\n3. Info\n'\
             '4. Run\n\n1. Talk is where the main meat of the game is and is'\
             ' the only way to reduce the number of turns you have left.\n'\
             'Upon selecting this option, you\'ll be presented with a'\
             ' certain situation and 4 options to choose from.\n\nThis is '\
             'where your date\'s personality becomes vital to your '\
             'progression.\n\nDepending on their personality, they may '\
             'like or dislike certain options more than others, increasing '\
             'or decreasing your confidence respectively.\nBe sure to select '\
             '"the most correct option" out of the bunch to proceed gracefully'\
             ' to your next turn.\n\nOnce you decide to talk'\
             ' to your date, there\'s no turning back. Just like a real one '\
             '(I think)!\n\n2. Items are to increase your confidence and vary'\
             ' in effectiveness.\nThe "Show Off!" option is a wildcard.'\
             ' It\'s the only "item" that can also decrease your confidence.\n'\
             'It may even cause you to lose the game in some situations.'\
             ' Show off wisely!\n\nInfo and Run are a bit self-explanatory:'\
             '\n\n3. Info gives you the person\'s name and '\
             'personality.\n\n4. Run ends the game prematurely '\
             '(resulting in a loss).\n\nGood Luck!\n\n'\
             f'[{OPTION_A}] - Back'
    return prompt


def story_prompt() -> str:
    """
    Return a prompt that delivers the context surrounding the game.

    """
    prompt = 'Story:\n\n'\
             'Pressured by your family, you are desperate to find at least '\
             'someone to date.\nThankfully, after numerous no-shows from '\
             'your dating partners, one of your friends decide to give you a '\
             'helping hand.\nHowever, even after setting up the venue for your '\
             'date, he refuses to give out more than a simple description about'\
             ' the person your\'re dating!\n\nApparently, it\'s to keep the '\
             'whole occasion a "surprise."\n\nBy only knowing your date\'s'\
             ' personality, it seems that you\'ll just have to survive the'\
             ' events that unfold in a proper and gentlemanlike manner.\n\n'\
             f'[{OPTION_A}] - Back'
    return prompt


def information_prompt(person: Character) -> str:
    """
    Return a prompt that details the information of <person>.

    """

    return f'Information:\n{person}\n[{OPTION_A}] - Back'


def diff_prompt() -> str:
    """
    Show a list of difficulties that the user can
    choose from. These are:

    - Gigachad (DIF_EASY)
    - Normal (DIF_NORMAL)
    - Weeb (DIF_HARD)
    """
    prompt = 'Select your difficulty below.\n\n'\
            f'[{OPTION_A}] - Gigachad\n'\
            f'[{OPTION_B}] - Normie\n'\
            f'[{OPTION_C}] - Weeb\n\n'\
            'Difficulty levels determine the number of '\
            'turns and confidence gains/losses throughout the date.'

    return prompt

def jukebox_prompt(song: str) -> str:
    prompt = f'Current song: {song}\n'\
             f'[{OPTION_A}] - Next\n'\
             f'[{OPTION_B}] - Back\n'\
             f'[{OPTION_C}] - Exit\n\n'
    return prompt

def music_select_prompt(song: str) -> str:
    prompt = f'Select a song:\n{song}\n\n'\
             f'[{OPTION_A}] - Select\n'\
             f'[{OPTION_B}] - Next song\n'\
             f'[{OPTION_C}] - Previous song\n'
    return prompt

def select_play_prompt() -> str:
    prompt = f"Select a mode:\n\n"\
             f'[{OPTION_A}] - Random\n'\
             f'[{OPTION_B}] - Select Character (requires password)\n'\
             f'[{OPTION_C}] - Back\n'
    return prompt

def enter_password_prompt() -> str:
    prompt = "Enter the password (obtained by completing random mode"\
             "on Weeb mode with a confidence of 80 or higher)\n"\
             "Alternatively, enter \"A\" to go back to the select screen.\n\n"\
             "Password: "
    return prompt

def select_personality_prompt() -> str:
    prompt = f"Select a personality type:\n\n"\
             f'[{OPTION_A}] - Normal\n'\
             f'[{OPTION_B}] - Active\n'\
             f'[{OPTION_C}] - Negative\n'\
             f'[{OPTION_D}] - Objective\n'\
             f'[{OPTION_E}] - Random\n'
    return prompt

def name_select() -> str:
    prompt = f"Give a name for this character:\n"\
             f'[{OPTION_A}] - Manually\n'\
             f'[{OPTION_B}] - Randomly\n'
    return prompt

def confirm_character(person: Character) -> str:
    prompt = f"Your character is:\n{person}\n"\
             f"True personality: {person.true_pers}\n"\
             f"Continue?\n"\
             f'[{OPTION_A}] - Yes\n'\
             f'[{OPTION_B}] - No'
    return prompt
