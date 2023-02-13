import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from main import file_parser


class MainWindow(QDialog):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        loadUi("style/gui.ui", self)
        self.browse.clicked.connect(self.open_dir_dialog)
        self.checkBox.stateChanged.connect(self.checked)
        self.button.clicked.connect(self.button_clicked)

        self.name_directory = ""
        self.is_normalize = False

    def open_dir_dialog(self):
        directory = QFileDialog.getExistingDirectory(self, 'Select a folder:', 'D:\\')
        if directory:
            self.label_2.setText(directory)
            self.name_directory = directory

    def checked(self):
        self.is_normalize = str(self.checkBox.isChecked())

    def button_clicked(self):
        out_text = file_parser(self.name_directory, self.is_normalize)
        print(out_text)
        self.label.setText(out_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()

    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setWindowTitle("Clean Folder")
    widget.setWindowIcon(QtGui.QIcon("style/cleaning.png"))
    widget.setFixedSize(450, 350)
    widget.show()

    sys.exit(app.exec_())
