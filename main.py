# Author: przewnic
# Tram Simulation

from tram_model.TramSystem import TramSystem
from MainWindow import MainWindow
from PyQt5 import QtWidgets
import sys


def main():
    """ Creation of new app with MainWindow
        Start of program loop
    """
    app = QtWidgets.QApplication(sys.argv)
    tram_system = TramSystem()
    window = MainWindow(tram_system)
    WIDTH = 1100
    HEIGHT = 800
    window.resize(WIDTH, HEIGHT)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
