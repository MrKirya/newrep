# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3
import sys

from PyQt6.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def __init__(self):
        self.db_cursor = None
        self.db_connection = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 314)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_save = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(170, 170, 171, 41))
        self.btn_save.setStyleSheet("background-color: rgb(255, 123, 237);")
        self.btn_save.setObjectName("btn_save")
        self.lol_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.lol_label.setGeometry(QtCore.QRect(180, 20, 151, 41))
        self.lol_label.setStyleSheet("background-color: rgb(178, 186, 199);")
        self.lol_label.setObjectName("lol_label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 100, 331, 41))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.btn_show = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_show.setGeometry(QtCore.QRect(170, 220, 171, 41))
        self.btn_show.setObjectName("btn_show")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.db_connection = sqlite3.connect('mydatabase.db')
        self.db_cursor = self.db_connection.cursor()

        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS texts (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)''')
        MainWindow.setStatusBar(self.statusbar)

        self.btn_save.clicked.connect(self.save_text)
        self.btn_show.clicked.connect(self.show_text)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def save_text(self):

        text = self.lineEdit.text()
        if text:
            self.db_cursor.execute("INSERT INTO texts (text) VALUES (?)", (text,))
            self.db_connection.commit()
            self.lineEdit.setText('')
        else:
            QMessageBox.warning(self, 'Error', 'Empty string')


    def show_text(self):
        self.db_cursor.execute("SELECT text FROM texts ORDER BY id DESC LIMIT 1")
        result = self.db_cursor.fetchone()
        if result:
            text = result[0]
            self.lineEdit.setText(text)
        else:
            QMessageBox.warning(self, 'Error', 'No text found in database')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text Editor"))
        self.btn_save.setText(_translate("MainWindow", "Сохранить"))
        self.lol_label.setText(_translate("MainWindow", "Directed by Robert.D.Wide"))
        self.btn_show.setText(_translate("MainWindow", "Показать"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
