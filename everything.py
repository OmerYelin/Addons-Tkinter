__version__ = "0.1"


class help:
    help = "Just call 'characters', 'colors' or 'fonts'."

    update = """The 'Everything' module currently have characters, colors and fonts.
Next update will have languages (partially)."""


class characters:
    digits = r'0123456789'
    lowercase = r'abcdefghijklmnopqrstuvwxyz'
    uppercase = r'ABCDEFJHIJKLMNOPQRSTUVWXYZ'
    symbols = r',.!#$%*'
    all_symbols = r'`~!@#$%^&*()_-=+/?.,"'


class colors:
    def __init__(self):
        self.BLUE = 'BLUE'
        self.GREEN = 'GREEN'
        self.BLACK = 'BLACK'
        self.WHITE = 'WHITE'
        self.RED = 'RED'
        self.YELLOW = 'YELLOW'
        self.BROWN = 'BROWN'
        self.GRAY = 'GRAY'
        self.CYAN = 'CYAN'
        self.DARK_RED = 'DARK_RED'
        self.PINK = 'PINK'
        self.DARK_BLUE = 'DARK_BLUE'
        self.DARK_GREEN = 'DARK_GREEN'
        self.LIGHT_BLUE = 'LIGHT_BLUE'
        self.LIGHT_GREEN = 'LIGHT_GREEN'
        self.MAGENTA = 'MAGENTA'
        self.PURPLE = 'PURPLE'
        self.LIGHT_RED = 'LIGHT_RED'
        self.DARK_PURPLE = 'DARK_PURPLE'
        self.LIGHT_PURPLE = 'LIGHT_PURPLE'
        self.AQUA = 'AQUA'
        self.ORANGE = 'ORANGE'
        self.LIME = 'LIME'
        self.NAVY = 'NAVY'
        self.finish = 'More colors will be added soon.'

    def __str__(self):
        print("Available colors:")
        print(self.BLUE)
        print(self.GREEN)
        print(self.BLACK)
        print(self.WHITE)
        print(self.RED)
        print(self.YELLOW)
        print(self.BROWN)
        print(self.GRAY)
        print(self.CYAN)
        print(self.DARK_RED)
        print(self.PINK)
        print(self.DARK_BLUE)
        print(self.DARK_GREEN)
        print(self.LIGHT_BLUE)
        print(self.LIGHT_GREEN)
        print(self.MAGENTA)
        print(self.PURPLE)
        print(self.DARK_RED)
        print(self.DARK_PURPLE)
        print(self.LIGHT_PURPLE)
        print(self.AQUA)
        print(self.ORANGE)
        print(self.LIME)
        print(self.NAVY)
        return self.finish

    BLUE = 'blue'
    GREEN = 'green'
    BLACK = 'black'
    WHITE = 'white'
    RED = 'red'
    YELLOW = 'yellow'
    BROWN = 'brown'
    GRAY = 'gray'
    CYAN = 'cyan'
    DARK_RED = 'darkred'
    PINK = 'pink'
    DARK_BLUE = 'darkblue'
    DARK_GREEN = 'darkgreen'
    LIGHT_BLUE = 'lightblue'
    LIGHT_GREEN = 'lightgreen'
    MAGENTA = 'magenta'
    PURPLE = 'purple'
    LIGHT_RED = 'lightred'
    DARK_PURPLE = 'darkpurple'
    LIGHT_PURPLE = 'lightpurple'
    AQUA = 'aqua'
    ORANGE = 'orange'
    LIME = 'lime'
    NAVY = 'navy'


class fonts:
    ARIAL = 'arial'
    HELVETICA = 'helvetica'
    COURIER = 'courier'
    AHARONI = 'aharoni'
    BROADWAY = 'broadway'
    CAMBRIA = 'cambria'
    COMIC_SANS = 'comic sans MS'
    FIXEDSYS = 'Fixedsys'
    CALIBRI = 'Calibri'
    UBUNTU = 'Ubuntu'
    SANS_SERIF = 'microsoft sans serif'
    TIMES_NEW_ROMAN = 'Times New Roman'
    ROMAN = 'Roman'

    class bold:
        ARIAL = 'arial', 'bold'
        HELVETICA = 'helvetica', 'bold'
        COURIER = 'courier', 'bold'
        AHARONI = 'aharoni', 'bold'
        BROADWAY = 'broadway', 'bold'
        CAMBRIA = 'cambria', 'bold'
        COMIC_SANS = 'comic sans MS', 'bold'
        FIXEDSYS = 'Fixedsys', 'bold'
        CALIBRI = 'Calibri', 'bold'
        UBUNTU = 'Ubuntu', 'bold'
        SANS_SERIF = 'microsoft sans serif', 'bold'
        TIMES_NEW_ROMAN = 'Times New Roman', 'bold'
        ROMAN = 'Roman', 'bold'

    class italic:
        ARIAL = 'arial', 'italic'
        HELVETICA = 'helvetica', 'italic'
        COURIER = 'courier', 'italic'
        AHARONI = 'aharoni', 'italic'
        BROADWAY = 'broadway', 'italic'
        CAMBRIA = 'cambria', 'italic'
        COMIC_SANS = 'comic sans MS', 'italic'
        FIXEDSYS = 'Fixedsys', 'italic'
        CALIBRI = 'Calibri', 'italic'
        UBUNTU = 'Ubuntu', 'italic'
        SANS_SERIF = 'microsoft sans serif', 'italic'
        TIMES_NEW_ROMAN = 'Times New Roman', 'italic'
        ROMAN = 'Roman', 'italic'
