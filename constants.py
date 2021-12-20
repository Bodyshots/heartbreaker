import pygame as pg
from os.path import abspath

pg.init()

### Battle Options

OPTION_A = 'A'
OPTION_B = 'B'
OPTION_C = 'C'
OPTION_D = 'D'
OPTION_E = 'E'
OPTION_F = 'F'
OPTION_G = 'G'

# Turn Amounts
EASY_TURNS = 15
NORM_TURNS = 12
HARD_TURNS = 8

# Confidence Amounts
EASY_CONF = 100
NORM_CONF = 50
HARD_CONF = 25

# Difficulties (default is DIF_NORM)
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

### Sounds and Music

MUSIC_PATH = r'Sounds\Music'
JINGLE_PATH = r'Sounds\Music\Jingles'

conf_lose_SE = pg.mixer.Sound(abspath(r'Sounds\SE\437.wav')) # done
conf_gain_SE = pg.mixer.Sound(abspath(r'Sounds\SE\conf_gain.wav')) # done
cologne_SE = pg.mixer.Sound(abspath(r'Sounds\SE\cologne.wav')) # done
slap_SE = pg.mixer.Sound(abspath(r'Sounds\SE\slap.wav')) 
invalid_SE = pg.mixer.Sound(abspath(r'Sounds\SE\invalid.wav')) # done
invalid_2_SE = pg.mixer.Sound(abspath(r'Sounds\SE\invalid_2.wav')) # done
slam_SE = pg.mixer.Sound(abspath(r'Sounds\SE\break_table.wav')) # done
select_SE = pg.mixer.Sound(abspath(r'Sounds\SE\snd_item.wav')) # done
toilet_SE = pg.mixer.Sound(abspath(r'Sounds\SE\toilet.wav')) # done
run_SE = pg.mixer.Sound(abspath(r'Sounds\SE\snd_escaped.wav')) # done
info_SE = pg.mixer.Sound(abspath(r'Sounds\SE\snd_heal_c.wav')) # done
fight_SE = pg.mixer.Sound(abspath(r'Sounds\SE\fight.wav'))
table_slam_SE = pg.mixer.Sound(abspath(r'Sounds\SE\table_slam.wav'))
drum_roll_SE = pg.mixer.Sound(abspath(r'Sounds\SE\drum_roll.wav'))
gunshot_2_SE = pg.mixer.Sound(abspath(r'Sounds\SE\new sound effects\gunshots - LittleRobotSoundFactory.wav'))

# Making all sounds have a consistent volume of around 0.5

sound_vol = 0.5

sounds = [conf_gain_SE, conf_lose_SE, cologne_SE, slap_SE, invalid_SE, slam_SE,
          info_SE, toilet_SE, invalid_2_SE, run_SE, select_SE, fight_SE,
          table_slam_SE, drum_roll_SE]

for i in sounds:
    i.set_volume(sound_vol)
