from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import sys
from YoutubeDownloader.QGUI import GUICLASS


# without the wrapper:

def main0():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(200, 100)
    w.setWindowTitle('Hello world')
    w.show()
    button = QPushButton("hi")
    button.setParent(w)
    button.resize(120, 50)
    button.move(0, 0)
    button.show()
    sys.exit(app.exec())


# with the wrapper
def main():
    app2 = GUICLASS.application()
    w2 = GUICLASS.window()
    w2.Geometry(400, 400)
    w2.title("Hello world")
    button = GUICLASS.button(w2)
    button.create(0, 0, "hi", w2, 120, 50)
    button.run()
    w2.run()
    app2.exit()


if __name__ == '__main__':
    main()
