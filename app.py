import sys
from Qt.QtWidgets import QApplication
from Dewins.ui.Windows.WindowMain import MainWindow


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()

    code = app.exec()
    #TODO save or do exiting after closing window
    exit(code)

if __name__ == "__main__":
    main()