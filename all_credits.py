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
        Credit('poopy', 'my bum', 'http://youtube.com/watch?v=7upgaUAcjbc')
    >>> # str(credit) will return the following:
    >>> #'poopy:'
    >>> #'http://youtube.com/watch?v=7upgaUAcjbc'
    >>> #'By my bum.'
    >>> #
    >>> #
    >>> # End of example.
    """
    title: str
    author: str
    link: str

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
        
        self.title = title
        self.link = link
        self.author = author

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

    === Attributes ===
    title: The name of this credit roll (ie. Music, Sound Effects, etc.)

    === Example Use ===
    >>> credit = \
        Credit('poopy', 'my bum', 'http://youtube.com/watch?v=7upgaUAcjbc')
    >>> credit2 = \
        Credit('pee', 'my nonozone', 'https://www.youtube.com/watch?v=iik25wqIuFo')
    >>> creditroll = CreditRoll('Music')
    >>> creditroll.add(credit)
    >>> creditroll.add(credit2)
    >>> # str(creditroll) will return the following
    >>> #'poopy:'
    >>> #'http://youtube.com/watch?v=7upgaUAcjbc'
    >>> #'By my bum.'
    >>> #
    >>> #
    >>> #'pee:'
    >>> #'https://www.youtube.com/watch?v=iik25wqIuFo'
    >>> #'By my nonozone'
    >>> #
    >>> #
    >>> # End of example.
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
        >>> creditroll.credits == []
        True
        >>> creditroll.add(test)
        >>> creditroll.credits != []
        True

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

    # Music

    mus1 = Credit('Sad Song', 'Darkman007', 'https://modarchive.org/')
    mus2 = Credit('Romantic', 'Benjamin Tissot (also known as Bensound)',
                'www.bensound.com')
    mus3 = Credit('Jingles #1-10', 'Zophar\'s Music Domain', 'https://www.zopha'\
                'r.net/music/nintendo-ds-2sf/simple-ds-series-vol-01-the-mahjong')
    mus4 = Credit('Bossa vieja!', 'MadBrain', 'https://modarchive.org/')

    music_credits = CreditRoll('Music')
    all_music = [mus1, mus2, mus3, mus4]
    for i in all_music:
        music_credits.add(i)

    # Code

    code1 = Credit('Clear the Terminal Programmatically!', 'Brōtsyorfuzthrāx',
                'https://stackoverflow.com/questions/2084508/clea'\
                'r-terminal-in-python')
    code_credits = CreditRoll('Code')
    all_code = [code1]
    for i in all_code:
        code_credits.add(i)

    credits_all = [music_credits, code_credits]
    for i in credits_all:
        credit_str += str(i)
    return credit_str

if __name__ == '__main__':
    import doctest
    doctest.testmod()
