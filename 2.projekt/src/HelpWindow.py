"""! @file HelpWindow.py
@brief Contains class used to open tutorial window.
@author xhnato00, xlanro00, xmacho12, xslivk03
"""

from PyQt5 import QtWidgets, uic

from os import path
import sys

# Path to a directory containing project files in pyinstaller package
bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))

# Path to a ui file created in QT Creator
path_to_ui = path.abspath(path.join(bundle_dir, 'HelpWindow.ui'))


class UiHelpWindow(QtWidgets.QMainWindow):
    """! Class used for creation of the tutorial window.
    """

    def __init__(self):
        """! Initialization of UI from file created in QT Creator.
        """
        super(UiHelpWindow, self).__init__()

        uic.loadUi(path_to_ui, self)

        self.show()
