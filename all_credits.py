class Credit:
    """
    Create a credit for a credit roll

    """

    def __init__(self, title: str, author: str, link: str):
        """
        Initiaize a new credit, using <category>, <title>, <author>, and
        <link>.

        >>> test = Credit('BGM #04 (Beta Mix) - Simple DS Series '\
            'Vol. 01 - The Mahjong', 'SilvaGunner', 'https://www.youtube.co'\
            'm/watch?v=mXvR7Qvf3cA')
        >>> test.title
        'BGM #04 (Beta Mix) - Simple DS Series Vol. 01 - The Mahjong'
        >>> test.author
        'SilvaGunner'
        >>> test.link
        'https://www.youtube.com/watch?v=mXvR7Qvf3cA'

        """
        
        self.title, self.link, self.author = title, link, author

    def __str__(self):
        """
        Reorganize how a Credit is printed by presenting the following (in
        order).

        - Title
        - Link
        - Author

        Each are on its own separate line (multiple if needed).

        """
        return '{}:\n{}\nBy {}.\n\n'.format(self.title, self.link, self.author)

class CreditRoll:
    """
    Create a new CreditRoll

    """

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
        - Title (of a Credit)
        - Link
        - Author

        """
        return_string = ''
        return_string += f'\n{self.title}:\n'
        for i in self.credits:
            return_string += str(i)
        return return_string[:len(return_string) - 1]

    def add(self, credit: Credit):
        """
        Add <credit> to a CreditRoll's list.

        >>> test = Credit('BGM #04 (Beta Mix) - Simple DS Series '\
            'Vol. 01 - The Mahjong', 'SilvaGunner', 'https://www.youtube.co'\
            'm/watch?v=mXvR7Qvf3cA')
        >>> creditroll = CreditRoll('Music')
        >>> creditroll.add(test)

        """
        self.credits.append(credit)


credits_all = []

# Music

mus1 = Credit('BGM #04 (Beta Mix) - Simple DS Series Vol. 01 - The Mahjong',
              'SilvaGunner', 'https://www.youtube.com/watch?v=mXvR7Qvf3cA')
mus2 = Credit('Sad song', 'Darkman007', 'http://darkman007.untergrund.net'\
              '/chiptune.php, from the album "Chiptunes 2012"')
mus3 = Credit('Jingles #1-10', 'Zophar\'s Music Domain', 'https://www.zopha'\
              'r.net/music/nintendo-ds-2sf/simple-ds-series-vol-01-the-mahjong')
mus4 = Credit('Turnabout Jazz Soul - Track 8 - Godot - The Fragrance of '\
              'Dark Coffee', 'Capcom, provided by Bloogeyz', 'https://www.yo'\
              'utube.com/watch?v=HMnrl0tmd3k')

music_credits = CreditRoll('Music')
all_music = [mus1, mus2, mus3, mus4]
for i in all_music:
    music_credits.add(i)

credits_all.append(music_credits)

# Sound Effects

se1 = Credit('Item and Confidence Gain/Loss', 'Jagex, provided by'\
             ' Enzo Willems', 'https://www.youtube.com/watch?v=w9IsTb9yPoQ')
se2 = Credit('Invalid and Breaking Table Noises', 'Valve, provided by'\
             ' Darkrai64', 'https://www.youtube.com/playlist?list=PLNl6VjQ8'\
             'AltzVT3vDkenZx3NcaC3fpgtG')
se3 = Credit('Slap and Table Slam', 'All Sounds', 'https://youtu.be/NJesYXP71'\
             '44?t=21 and https://youtu.be/0HwyOSfaOPc?t=50 respectively.')
se4 = Credit('Escape, Select, and Information Select', 'Toby Fox, provided '\
             'by carpathia808', 'https://www.youtube.com/watch?v=dkk6t9iywKA')
se5 = Credit('Toilet Flush', 'JonGallagher1', 'https://www.youtube.com/watch'\
             '?v=hwxNVnPKaPE')
se6 = Credit('Invalid Item Use', 'CorrectAndWrong', 'https://www.youtube.co'\
             'm/watch?v=worclOeTALw')
se7 = Credit('Restaurant Chatter', 'The Corner of Ambient Sounds & ASMR',
             'https://www.youtube.com/watch?v=Knt974Y3Cqc')
se8 = Credit('Drum Roll', 'Gaming Sound FX', 'https://www.youtube.com/'\
             'watch?v=Ek56AgxwybI')
se9 = Credit('Woman Coughing', 'Visual & Sound FX', 'https://www.youtube.com'\
             '/watch?v=ORLWyWQteV0')
se10 = Credit('Gunshots', 'Fesliyanstudios', 'https://www.fesliyanstudios.'\
              'com/royalty-free-sound-effects-download/gun-shooting-300')
se11 = Credit('Crowd Scream 1', 'Dadda Digital', 'https://www.youtube.com/'\
              'watch?v=5Irt2ABKeqc')
se12 = Credit('Crowd Scream 2', 'euronews', 'https://www.youtube.com'\
              '/watch?v=yDJvnWgREQw')

se_credits = CreditRoll('Sound Effects')
all_se = [se1, se2, se3, se4, se5, se6, se7, se8, se9, se10, se11, se12]
for i in all_se:
    se_credits.add(i)

credits_all.append(se_credits)

credit_str = ''
for i in credits_all:
    credit_str += str(i)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
