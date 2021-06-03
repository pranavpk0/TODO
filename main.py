from PyQt5.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.button.clicked.connect(self.add_to_list)
        self.show_at_start()

    def add_to_list(self):
        name = self.entry.text()
        time = self.timeEdit.text()
        date = self.dateEdit.text()
        format_ = "you need to do " + name + " at " + time + ":" + date + "!"
        self.listWidget.addItem(format_)
        with open("file.txt", "a") as f:
            f.write(format_ + "\n")

    def show_at_start(self):
        f = open("file.txt", "r")
        for line in f:
            split = line.split('!')
            i = split[0]
            self.listWidget.addItem(i)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
