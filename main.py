
# Project imports
from dictata import Dictata
from gui import GUI
import sys

def main(args):

    d = Dictata(args, "test.json")
    g = GUI(args, d)

    g.show()
    g.run()


if __name__ == "__main__":

    sys.exit( main(sys.argv) )

