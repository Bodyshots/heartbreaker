""" Module for setting up credits """

from typing import Tuple, List

class Credit:
    """
    Create a new Credit.

    === Attributes ===
    title: The name of the work.
    author: The author of the work.
    link: The website where the client may view the work.

    === Example Use ===
    >>> credit = \
        Credit('poopy', 'my bum', 'http://youtube.com/watch?v=7upgaUAcjbc'\
               'license_stuff', 'license_link')
    >>> # str(credit) will return the following:
    >>> #'poopy'
    >>> # my bum
    >>> #'http://youtube.com/watch?v=7upgaUAcjbc'
    >>> #'license_stuff:'
    >>> #'license_link'
    >>> #
    >>> # End of example.
    """
    title: str
    author: str
    link: str
    licensing: str
    licensing_link: str


    def __init__(self, title: str, author: str, link: str, 
                 licensing=None, licensing_link=None):
        """
        Initiaize a new credit, using <category>, <title>, <author>, and
        <link>.

        >>> test = Credit('BGM #04 (Beta Mix) - Simple DS Series '\
            'Vol. 01 - The Mahjong', 'SilvaGunner', 'https://www.youtube.co'\
            'm/watch?v=mXvR7Qvf3cA', 'test', 'testing')
        >>> test.title
        'BGM #04 (Beta Mix) - Simple DS Series Vol. 01 - The Mahjong'
        >>> test.author
        'SilvaGunner'
        >>> test.link
        'https://www.youtube.com/watch?v=mXvR7Qvf3cA'
        >>> test.licensing
        'test'
        >>> test.licensing_link
        'testing'
        """
        
        self.title = title
        self.link = link
        self.author = author
        self.licensing = licensing
        self.licensing_link = licensing_link

    def __str__(self):
        """
        Reorganize how a Credit is printed by presenting the following (in
        order).

        - Title
        - Author
        - Link
        - Licensing
        - Licensing Link

        Each are on its own separate line (multiple if needed).

        """
        credit = '{}, by {}\n{}'.format(self.title, self.author, self.link)
        if self.licensing:
            credit += f'\n{self.licensing}'
        if self.licensing_link:
            if self.licensing:
                credit += ':'
            credit += f'\n{self.licensing_link}'
        return credit + '.\n\n'

class CreditRoll:
    """
    Create a new CreditRoll

    === Attributes ===
    title: The name of this credit roll (ie. Music, Sound Effects, etc.)
    """
    title: str

    def __init__(self, title: str):
        """
        Initialize a CreditRoll

        >>> creditroll = CreditRoll('Music')
        >>> creditroll.credits
        []
        >>> creditroll.title
        'Music'

        """
        self.title = title
        self.credits = []

    def __str__(self):
        """
        Alter the way CreditRoll is normally printed by showing the
        following to the user.

        - Title (of CreditRoll [only once])
        - Credit Information

        """
        return_string = ''
        return_string += f'\n{self.title}:\n'
        for i in self.credits:
            return_string += str(i)
        return return_string[:len(return_string) - 1]

    def add(self, credit: Credit):
        """
        Add <credit> to a CreditRoll's list.

        """
        self.credits.append(credit)

def creds() -> str:
    """ 
    Return a string that details all CreditRolls, which are (in order):

    - Music CreditRoll
    - Sound Effect CreditRoll
    - Code CreditRoll
    """
    credits_all, credit_str = [], ''

    # Battle music

    bat_mus1 = Credit('Leisurely Voice', 'K. Jose', 
                      'https://modarchive.org/index.php?request=view_profile&query=86612',
                      'CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
                      'https://creativecommons.org/publicdomain/zero/1.0/')
    bat_mus2 = Credit('Retrospective', 'm0d',
                      'https://modarchive.org/index.php?request=view_profile&query=69141',
                      'Public Domain Certification',
                      'https://creativecommons.org/licenses/publicdomain/')
    bat_mus3 = Credit('Transmission', 'Drozerix',
                      'https://modarchive.org/index.php?request=view_profile&query=84702',
                      'Public Domain Certification',
                      'https://creativecommons.org/licenses/publicdomain/')
    bat_mus4 = Credit('The Red One', 'm0d',
                      'https://modarchive.org/index.php?request=view_profile&query=69141',
                      'Public Domain Certification',
                      'https://creativecommons.org/licenses/publicdomain/')

    bat_mus_credits = CreditRoll('Battle Music')
    all_bat_mus = [bat_mus1, bat_mus2, bat_mus3, bat_mus4]
    for i in all_bat_mus: bat_mus_credits.add(i)

    # Jingles

    jingle1 = Credit('Spectrum', 'Peak & Drozerix',
                     'https://modarchive.org/index.php?request=view_profile&query=84702',
                     'Public Domain Certification',
                     'https://creativecommons.org/licenses/publicdomain/')
    jingle2 = Credit('Nerve 2.00', 'Drozerix',
                     'https://modarchive.org/index.php?request=view_profile&query=84702',
                     'Public Domain Certification',
                     'https://creativecommons.org/licenses/publicdomain/')
    jingle3 = Credit('A Winter Kiss', 'Drozerix',
                     'https://modarchive.org/index.php?request=view_profile&query=84702',
                     'Public Domain Certification',
                     'https://creativecommons.org/licenses/publicdomain/')
    jingle4 = Credit('Old Dance Thing', 'Katie Cadet',
                     'https://modarchive.org/index.php?request=view_profile&query=84804',
                     'Public Domain Certification',
                     'https://creativecommons.org/licenses/publicdomain/')
    jingle5 = Credit('stranger_-_run.mod', 'Stranger',
                     'https://modarchive.org/index.php?request=view_profile&query=88286',
                     'Public Domain Certification',
                     'https://creativecommons.org/licenses/publicdomain/')
    jingle6 = Credit('4_RNDD!', 'Drozerix',
                     'https://modarchive.org/index.php?request=view_profile&query=84702',
                     'Public Domain Certification',
                     'https://creativecommons.org/licenses/publicdomain/')
    jingle7 = Credit('Viral Legacy', 'Drozerix',
                     'https://modarchive.org/index.php?request=view_profile&query=84702',
                     'Public Domain Certification',
                     'https://creativecommons.org/licenses/publicdomain/')
    jingle8 = Credit('Neon Techno', 'Drozerix',
                     'https://modarchive.org/index.php?request=view_profile&query=84702',
                     'Public Domain Certification',
                     'https://creativecommons.org/licenses/publicdomain/')
    jingle9 = Credit('Cue Ball', 'christofori',
                     'https://modarchive.org/index.php?request=view_profile&query=69248',
                     'Public Domain Certification',
                     'https://creativecommons.org/licenses/publicdomain/')

    jingle_credits = CreditRoll('Jingles')
    all_jingles = [jingle1, jingle2, jingle3, jingle4, jingle5, jingle6, jingle7,
                   jingle8, jingle9]
    for i in all_jingles: jingle_credits.add(i)

    # Other Music

    oth_mus1 = Credit('Past never come back', 'JAM', 'https://modarchive.org/', 
                      'Public Domain Certification',
                      'https://creativecommons.org/licenses/publicdomain/')
    oth_mus2 = Credit('Blue Intermission', 'congusbongus',
                      'https://modarchive.org/index.php?request=view_profile&query=85757',
                      'CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
                      'https://creativecommons.org/publicdomain/zero/1.0/')
    oth_mus3 = Credit('My Street', 'congusbongus', 
                      'https://modarchive.org/index.php?request=view_profile&query=85757',
                      'CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
                      'https://creativecommons.org/publicdomain/zero/1.0/')
    oth_mus4 = Credit('Merrily Strolling', 'K. Jose', 
                      'https://modarchive.org/index.php?request=view_profile&query=86612',
                      'CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
                      'https://creativecommons.org/publicdomain/zero/1.0/')

    oth_music_credits = CreditRoll('Other Music')
    all_oth_music = [oth_mus1, oth_mus2, oth_mus3, oth_mus4]
    for i in all_oth_music: oth_music_credits.add(i)

    # Sound Effects

    se1 = Credit('jsfxr', 'DrPetter, Eric Fredricksen, and Chris McCormick',
                 'https://sfxr.me/', 
                 'Copyright 2011 Eric Fredricksen (Public Domain)',
                 'https://unlicense.org/')
    se2 = Credit('8-Bit Sound Effects Library', 'LittleRobotSoundFactory',
                 'https://opengameart.org/content/8-bit-sound-effects-library',
                 'Copyright 2015 Little Robot Sound Factory',
                 'www.littlerobotsoundfactory.com')
    se3 = Credit('8bit power down', 'JavierZumer',
                 'https://freesound.org/people/JavierZumer/sounds/257221/',
                 'Copyright 2014 JavierZumer (CC by 3.0)',
                 'https://creativecommons.org/licenses/by/3.0/')
    se4 = Credit('Power up', 'komit.wav',
                 'https://freesound.org/people/komit.wav/sounds/402295/',
                 'CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
                 'https://creativecommons.org/publicdomain/zero/1.0/')
    se5 = Credit('Game Die', 'Jofae',
                 'https://freesound.org/people/Jofae/sounds/364929/',
                 'CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
                 'https://creativecommons.org/publicdomain/zero/1.0/')
    se6 = Credit('Error Signal 2', 'Breviceps',
                 'https://freesound.org/people/Breviceps/sounds/445978/',
                 'CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
                 'https://creativecommons.org/publicdomain/zero/1.0/')
    se7 = Credit('Wrong answer.', 'SgtPepperArc360',
                 'https://freesound.org/people/SgtPepperArc360/sounds/341732/',
                 'Copyright 2016 SgtPepperArc360 (CC BY-NC 3.0)',
                 'https://creativecommons.org/licenses/by-nc/3.0/')
    se8 = Credit('Retro game heal sound', 'lulyc',
                 'https://freesound.org/people/lulyc/sounds/346116/',
                 'CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
                 'https://creativecommons.org/publicdomain/zero/1.0/')

    se_credits = CreditRoll('Sound Effects Provided by:')
    se = [se1, se2, se3, se4, se5, se6, se7, se8]
    for i in se: se_credits.add(i)

    # Code

    code1 = Credit('Clear the Terminal Programmatically!', 'Brōtsyorfuzthrāx',
                   'https://stackoverflow.com/questions/2084508/clea'\
                   'r-terminal-in-python')
    code_credits = CreditRoll('Code')
    all_code = [code1]
    for i in all_code: code_credits.add(i)

    credits_all = [bat_mus_credits, jingle_credits, oth_music_credits, se_credits,
                   code_credits]
    for i in credits_all: credit_str += str(i)
    return credit_str

if __name__ == '__main__':
    import doctest
    doctest.testmod()
