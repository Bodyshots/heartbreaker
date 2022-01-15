import pygame as pg
import os
from os.path import abspath, join

pg.init()

def _music_file_checker(file: str) -> bool:
    """
    Return True if <file> is a playable music file for Pygame.
    Return False otherwise.
    """
    try:
        pg.mixer.music.load(file)
    except pg.error:
        return False
    return True

### Battle Options

OPTION_A = 'A'
OPTION_B = 'B'
OPTION_C = 'C'
OPTION_D = 'D'
OPTION_E = 'E'
OPTION_F = 'F'
OPTION_G = 'G'

# Turn Amounts
EASY_TURNS = 20
NORM_TURNS = 15
HARD_TURNS = 0

# Confidence Amounts
EASY_CONF = 100
NORM_CONF = 50
HARD_CONF = 100

# Difficulties
DIF_EASY = 'Gigachad'
DIF_NORM = 'Normie'
DIF_HARD = 'Weeb'

### Menu Options

RUN = 'R'
ITEM = 'I'
INFO = 'N'
TALK = 'T'
YES = 'Y'
NO = 'N'
PASSWORD = 'What a Weebachad'

### Item Usage and Lower Bounds and Higher Bounds for Items

USAGE_DEC = 1

# Easy
E_COLOGNE_AMT = 2
E_WSHROOM_AMT = 2

# Normal
N_COLOGNE_AMT = 1
N_WSHROOM_AMT = 1

# Hard
H_COLOGNE_AMT = 0
H_WSHROOM_AMT = 0

# Chances
COLOGNE_LOWER, COLOGNE_HIGHER = 5, 15
WASHROOM_LOWER, WASHROOM_HIGHER = 15, 25
SHOW_OFF_LOWER, SHOW_OFF_HIGHER = -30, 20

### Reactions Gains

EXTREME_NEG = -40
LARGE_NEG = -30
MED_NEG = -20
SMALL_NEG = -10
MINOR_NEG = -5
NEUTRAL = 0
MINOR_POS = 5
SMALL_POS = 10
MED_POS = 20
LARGE_POS = 30
EXTREME_POS = 40

### Personalities

NORMAL = 'Normal'
OBJECTIVE = 'Objective'
ACTIVE = 'Active'
NEGATIVE = 'Negative'

### Sounds Effects and Music

MUSIC_PATH = r'Sounds\Music'
BATTLE_MUSIC_PATH = MUSIC_PATH + r'\battle_music'
BATTLE_MUSIC_INTROS_PATH = BATTLE_MUSIC_PATH + r'\starters'
JINGLE_PATH = r'Sounds\Music\Jingles'
DEFAULT_MUSIC_VOL = 0.5

## Sound Effects
conf_lose_SE = pg.mixer.Sound(abspath(r'Sounds\SE\conf_down.wav'))
conf_gain_small_SE = pg.mixer.Sound(abspath(r'Sounds\SE\conf_gain_small.wav'))
conf_gain_big_SE = pg.mixer.Sound(abspath(r'Sounds\SE\conf_gain_big.wav'))
slap_SE = pg.mixer.Sound(abspath(r'Sounds\SE\slap.wav')) 
invalid_SE = pg.mixer.Sound(abspath(r'Sounds\SE\invalid_1.wav'))
invalid_2_SE = pg.mixer.Sound(abspath(r'Sounds\SE\invalid_2.wav'))
slam_SE = pg.mixer.Sound(abspath(r'Sounds\SE\slam.wav'))
select_SE = pg.mixer.Sound(abspath(r'Sounds\SE\select.wav'))
# mine, 
# https://sfxr.me/#34T6Pm17mG7E5zsjYtk4fB9fptUZXL4pjq4zJk98BGwo5jU3wf3WkbV5wTiwSxuGEcRMkxT8NV3MDARFJFTNMJNURzZhzBC9tvmyGTdTBTv7QZyjHx1gpawLb
run_SE = pg.mixer.Sound(abspath(r'Sounds\SE\run.wav'))
info_SE = pg.mixer.Sound(abspath(r'Sounds\SE\menu_1.wav'))
fight_SE = pg.mixer.Sound(abspath(r'Sounds\SE\fight.wav'))
drum_roll_SE = pg.mixer.Sound(abspath(r'Sounds\SE\drum_roll.wav'))
gunshot_SE = pg.mixer.Sound(abspath(r'Sounds\SE\gunshots.wav'))

## Music
MENU_MUSIC = MUSIC_PATH + r'\Past Never Come Back.wav'
OPTIONS_MUSIC = MUSIC_PATH + r'\Blue Intermission.wav'
CREDITS_MUSIC = MUSIC_PATH + r'\My Street.wav'
RESULTS_MUSIC = JINGLE_PATH + r'\results.wav'
GAME_OVER_MUSIC = MUSIC_PATH + r'\Merrily Strolling.wav'

BATTLE_MUSIC_LST, BATTLE_MUSIC_FULL_NMES = [], []
directory_items = os.listdir(abspath(BATTLE_MUSIC_PATH))
for item in directory_items:
    item_path = join(abspath(BATTLE_MUSIC_PATH), item)
    if _music_file_checker(item_path): 
        BATTLE_MUSIC_LST.append(item[:item.rindex('.')])
        BATTLE_MUSIC_FULL_NMES.append(item)

BATTLE_MUSIC_INTRO_LST, BATTLE_MUSIC_INTRO_FULL_NMES = [], []
directory_items = os.listdir(abspath(BATTLE_MUSIC_INTROS_PATH))
for item in directory_items:
    item_path = join(abspath(BATTLE_MUSIC_INTROS_PATH), item)
    if _music_file_checker(item_path): 
        BATTLE_MUSIC_INTRO_LST.append(item[:item.rindex('.') - 6])
        BATTLE_MUSIC_INTRO_FULL_NMES.append(item)

# Making all sounds have a consistent volume of around 0.5

sound_vol = 0.5

sounds = [conf_lose_SE, conf_gain_small_SE, conf_gain_big_SE, slap_SE, invalid_SE, slam_SE,
          info_SE, gunshot_SE, invalid_2_SE, run_SE, select_SE, fight_SE, drum_roll_SE]

for i in sounds:
    i.set_volume(sound_vol)
