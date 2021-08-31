from PyQt5.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.add_button.clicked.connect(self.add_to_list)
        self.del_button.clicked.connect(self.removesel)
        self.clear_all.clicked.connect(self.remove_all)

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

    def remove_and_finish(self):
        # REMOVING SELECTED ONE
        listItems = self.listWidget.selectedItems()
        # if not listItems:
        #     return
        for item in listItems:
            self.listWidget.takeItem(self.listWidget.row(item))

        # UPDATEING FILE
        items = [self.listWidget.item(x).text() for x in range(self.listWidget.count())]
        items_str = str(items)

        items_st = items_str.strip("[")
        items_st = items_st.strip("]")
        items_st = items_st.strip("'")

        with open("file.txt", "w") as f:
            f.write(str(items_st))

    def removesel(self):
        self.remove_and_finish()

    def remove_all(self):
        self.listWidget.clear()
        with open("file.txt", "w") as f:
            f.write('')


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
