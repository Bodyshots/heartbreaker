from os.path import abspath
from constants import NORMAL, OBJECTIVE, ACTIVE, NEGATIVE
from typing import Tuple, List, Dict

def game_setup() -> Tuple[List[str], List[str], Dict[str, str]]:
    """
    Return the objects necessary for the game to function.

    These are (in order):
    - First names
    - Last names
    - Personalities

    """
    fst_nmes, last_nmes = [], []
    personalities = {NORMAL: [], OBJECTIVE: [], ACTIVE: [], NEGATIVE: []}

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
    return (fst_nmes, last_nmes, personalities)

def file_lst_return(name: str) -> List[str]:
    """
    Open <name> in text_files\Other and return a list of its entries.
    """
    with open(abspath(r'text_files\Other'
                      f'\{name}.txt')) as pro_txt:
            content_lst = pro_txt.read().split('\n')
    return content_lst
