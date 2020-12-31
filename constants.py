import pygame as pg
from os.path import abspath

pg.init()
# Battle Options

OPTION_A = 'A'
OPTION_B = 'B'
OPTION_C = 'C'
OPTION_D = 'D'
OPTION_E = 'E'
OPTION_F = 'F'

# Menu Options

RUN = 'R'
ITEM = 'I'
INFO = 'N'
TALK = 'T'
YES = 'Y'
NO = 'N'

# Item Usage and Lower Bounds and Higher Bounds for Items

USAGE_DEC = 1
COLOGNE_LOWER, COLOGNE_HIGHER = 5, 15
WASHROOM_LOWER, WASHROOM_HIGHER = 15, 25
SHOW_OFF_LOWER, SHOW_OFF_HIGHER = -30, 20

# Reactions

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

# Personalities

NORMAL = 'Normal'
OBJECTIVE = 'Objective'
ACTIVE = 'Active'
NEGATIVE = 'Negative'


# Sounds

conf_lose_SE = pg.mixer.Sound(abspath(r'Sounds\SE\437.wav'))
conf_gain_SE = pg.mixer.Sound(abspath(r'Sounds\SE\conf_gain.wav'))
cologne_SE = pg.mixer.Sound(abspath(r'Sounds\SE\cologne.wav'))
slap_SE = pg.mixer.Sound(abspath(r'Sounds\SE\slap.wav'))
invalid_SE = pg.mixer.Sound(abspath(r'Sounds\SE\invalid.wav'))
invalid_2_SE = pg.mixer.Sound(abspath(r'Sounds\SE\invalid_2.wav'))
slam_SE = pg.mixer.Sound(abspath(r'Sounds\SE\break_table.wav'))
select_SE = pg.mixer.Sound(abspath(r'Sounds\SE\snd_item.wav'))
toilet_SE = pg.mixer.Sound(abspath(r'Sounds\SE\toilet.wav'))
run_SE = pg.mixer.Sound(abspath(r'Sounds\SE\snd_escaped.wav'))
info_SE = pg.mixer.Sound(abspath(r'Sounds\SE\snd_heal_c.wav'))
fight_SE = pg.mixer.Sound(abspath(r'Sounds\SE\fight.wav'))
table_slam_SE = pg.mixer.Sound(abspath(r'Sounds\SE\table_slam.wav'))
drum_roll_SE = pg.mixer.Sound(abspath(r'Sounds\SE\drum_roll.wav'))
gunshot_1_SE = pg.mixer.Sound(abspath(r'Sounds\SE\gunshot.wav'))
gunshot_2_SE = pg.mixer.Sound(abspath(r'Sounds\SE\gunshot_2.wav'))
panic_SE = pg.mixer.Sound(abspath(r'Sounds\SE\crowd_panic.wav'))
panic2_SE = pg.mixer.Sound(abspath(r'Sounds\SE\crowd_panic2.wav'))
cough_SE = pg.mixer.Sound(abspath(r'Sounds\SE\cough.wav'))

# Making all sounds have a consistent volume of around 0.4

sound_vol = 0.4

sounds = [conf_gain_SE, conf_lose_SE, cologne_SE, slap_SE, invalid_SE, slam_SE,
          info_SE, toilet_SE, invalid_2_SE, run_SE, select_SE, fight_SE,
          table_slam_SE, drum_roll_SE, gunshot_1_SE, gunshot_2_SE, panic_SE,
          panic2_SE, cough_SE]

for i in sounds:
    i.set_volume(sound_vol)
