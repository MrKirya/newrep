import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox
import sqlite3

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle('My Window')

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(260, 30)

        self.save_button = QPushButton('Save', self)
        self.save_button.move(20, 70)
        self.save_button.clicked.connect(self.save_text)

        self.show_button = QPushButton('Show', self)
        self.show_button.move(180, 70)
        self.show_button.clicked.connect(self.show_text)

        self.db_connection = sqlite3.connect('mydatabase.db')
        self.db_cursor = self.db_connection.cursor()

        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS texts
                             (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)''')

    def save_text(self):
        text = self.textbox.text()
        if text:
            self.db_cursor.execute("INSERT INTO texts (text) VALUES (?)", (text,))
            self.db_connection.commit()
            self.textbox.setText('')
        else:
            QMessageBox.warning(self, 'Error', 'Empty string')

    def show_text(self):
        self.db_cursor.execute("SELECT text FROM texts ORDER BY id DESC LIMIT 1")
        result = self.db_cursor.fetchone()
        if result:
            text = result[0]
            self.textbox.setText(text)
        else:
            QMessageBox.warning(self, 'Error', 'No text found in database')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
