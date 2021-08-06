"""
this module is the wrapper class for PyQt5 liberary, it will help mentain the
accessibility.
"""
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import sys


class window(object):
    def __init__(self):
        self.Window: QWidget = QWidget()
        self.width: int = 500
        self.height: int = 500

    def Geometry(self, width=None, height=None):
        if width and height is not None:
            self.Window.resize(width, height)
            return width, height
        else:
            self.Window.resize(self.width, self.height)

    def title(self, title: str):
        self.Window.setWindowTitle(title)

    def __repr__(self) -> str:
        description = 'Wrapper class for PyQt5'
        return description

    def run(self):
        self.Window.show()


class application(object):
    def __init__(self):
        self.application = QApplication(sys.argv)

    def exit(self):
        sys.exit(self.application.exec())


class button(object):
    def __init__(self, w) -> None:
        """

        :rtype: object
        """
        self.height = 50
        self.width = 120
        self.button = QPushButton()
        self.button.setParent(w)

    def create(self, x, y, title, w, height=None, width=None):
        if height is not None:
            if width is not None:
                self.button.resize(width, height)
            else:
                return None
        else:
            self.button.resize(self.width, self.height)
        self.button.setWindowTitle(title)
        self.button.move(x, y)


    def run(self):
        self.button.show()
