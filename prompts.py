""" Module for the game's prompts """

from constants import (TALK, ITEM, INFO, RUN, OPTION_A, OPTION_B, OPTION_C,
                       OPTION_D, OPTION_E, OPTION_F, YES, NO)
from character_classes import Character
from typing import Dict


def decision_prompt(confidence: float, turns: int) -> str:
    """ 
    Return a prompt for the user to decide what they
    want to do.

    """
    prompt = 'What do you want to do?\n'\
             f'Turns left: {turns}\n'\
             f'[{TALK}] - Talk\n'\
             f'[{ITEM}] - Items\n'\
             f'[{INFO}] - Info\n'\
             f'[{RUN}] - Run\n'\
             f'Your Confidence: {confidence}%'

    return prompt


def menu_prompt() -> str:
    """
    Return a prompt for the user to decide if they want
    to play the game or quit.

    """
    prompt = 'Main Menu:\n'\
            f'[{OPTION_A}] - Play the game!\n'\
            f'[{OPTION_B}] - Story\n'\
            f'[{OPTION_C}] - Instructions\n'\
            f'[{OPTION_D}] - Options\n'\
            f'[{OPTION_E}] - Credits\n'\
            f'[{OPTION_F}] - Quit'

    return prompt


def item_prompt(cologne: int, excuses: int) -> str:
    """
    Return a prompt for the user to decide what item to use.

    """
    prompt = 'Items:\n'\
            f'[{OPTION_A}] - Cologne: {cologne}\n'\
            f'[{OPTION_B}] - Washroom Break Excuses: {excuses}\n'\
            f'[{OPTION_C}] - Show Off!\n'\
            f'[{OPTION_D}] - Back'

    return prompt


def yes_no_prompt(message: str) -> str:
    """
    Return a prompt that prints <message> and gives the user
    a Yes/No prompt.

    Occurs whether the user has won/lost.

    """
    prompt = f'{message}\n'\
             f'[{YES}] - Yes\n'\
             f'[{NO}] - No'

    return prompt


def question_format(question: Dict) -> str:
    """
    Return a prompt for the user to decide how to respond to a random question
    from <questions>.

    """
    answers = question.get('Answers')
    print(question.get(sorted(list(question.keys()))[1]))
    prompt = f'[{OPTION_A}] - {answers.get(OPTION_A)}\n'\
             f'[{OPTION_B}] - {answers.get(OPTION_B)}\n'\
             f'[{OPTION_C}] - {answers.get(OPTION_C)}\n'\
             f'[{OPTION_D}] - {answers.get(OPTION_D)}'

    return prompt


def options_prompt() -> str:
    """
    Return a prompt for the user to decide what volume to change or to go
    back to the main menu.

    """

    prompt = 'What would you like to change?\n'\
            f'[{OPTION_A}] - Music Volume\n'\
            f'[{OPTION_B}] - Sound Effect (SE) Volume\n'\
            f'[{OPTION_C}] - Back'

    return prompt


def music_lvl_prompt(music_vol: float) -> str:
    """
    Return a prompt that displays what the current <music_vol> is and
    what is a valid music volume to change to.

    """

    return f'Current Music volume: {music_vol} (from 0.0 to 1.0)'


def sound_lvl_prompt(sound_vol: float) -> str:
    """
    Return a prompt that displays what the current <sound_vol> is and
    what is a valid sound volume to change to.

    """

    return f'Current SE volume: {sound_vol} (from 0.0 to 1.0)'


def credits_prompt(credits_all: str) -> str:
    """
    Return a prompt that displays <credits_all> and gives the user
    the option to go back to the main menu.

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
             '\n\n3. Info gives you the person\'s name and'\
             'personality.\n\n4. Run ends the game prematurely '\
             '(using it results in a loss).\n\nGood Luck!\n\n'\
             f'[{OPTION_A}] - Back'
    return prompt


def story_prompt() -> str:
    """
    Return a prompt that delivers the context surrounding
    the game.

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
