from PyQt5 import QtWidgets, QtCore 
import sqlite3 
from sys import exit, argv 
from authentication import User, hash_password 
from database import create_table_users, add_user 
 
class MainWindow(QtWidgets.QMainWindow): 
    def __init__(self): 
        super(MainWindow, self).__init__() 
        self.setWindowTitle("Simple Database") 
        self.setFixedSize(600, 400) 
 
        self.mainFrame = QtWidgets.QFrame() 
        self.mainLayout = QtWidgets.QVBoxLayout() 
 
        self.createButtons() 
        self.createTable() 
 
        self.fillTable() 
 
        self.mainFrame.setLayout(self.mainLayout) 
        self.setCentralWidget(self.mainFrame) 
 
    def createButtons(self): 
        group = QtWidgets.QWidget() 
        group_ly = QtWidgets.QHBoxLayout() 
        group_ly.setContentsMargins(0, 0, 0, 0) 
 
        add_button = QtWidgets.QPushButton("Add Data") 
        add_button.clicked.connect(self.addDataDialog) 
        group_ly.addWidget(add_button) 
 
        del_button = QtWidgets.QPushButton("Delete Data") 
        del_button.clicked.connect(self.deleteData) 
        group_ly.addWidget(del_button) 
 
        group.setLayout(group_ly) 
        self.mainLayout.addWidget(group) 
 
    def createTable(self): 
        self.table = QtWidgets.QTableWidget() 
        self.table.setColumnCount(3) 
        self.table.setHorizontalHeaderLabels(["enter", "user login", "password"]) 
        self.mainLayout.addWidget(self.table) 
 
    def fillTable(self): 
        conn = sqlite3.connect("base.db") 
        cursor = conn.cursor() 
        data = cursor.execute("SELECT * FROM Users").fetchall() 
        conn.close() 
 
        self.table.setRowCount(len(data)) 
 
        for i in range(len(data)): 
            self.table.setCellWidget(i, 0, QtWidgets.QCheckBox()) 
 
            for j in range(3): 
                self.table.setItem(i, j+1, QtWidgets.QTableWidgetItem(str(data[i][j]))) 
 
    def addDataDialog(self): 
        login, ok1 = QtWidgets.QInputDialog.getText(self, 'Enter login', 'Enter the login:') 
        password, ok2 = QtWidgets.QInputDialog.getText(self, 'Enter password', 'Enter the password:') 
 
        if ok1 and ok2: 
            conn = sqlite3.connect("base.db") 
            cursor = conn.cursor() 
            is_admin = "yes" 
            is_admin = is_admin.lower() 
            try:
                cursor.execute("INSERT INTO Users (login, hashed_password, is_admin) VALUES (?, ?, ?)", (login, hash_password(password), 1)) 
            except sqlite3.Error as error: 
                print("Ошибка при попытке добавить пользователя:", error)

            conn.commit() 
            conn.close() 
            self.fillTable() 
 
    def deleteData(self): 
        selected_rows = [] 
        for i in range(self.table.rowCount()): 
            if self.table.cellWidget(i, 0).isChecked(): 
                selected_rows.append(i) 
 
        conn = sqlite3.connect("base.db") 
        cursor = conn.cursor() 
 
        for row in selected_rows: 
            login = self.table.item(row, 1).text() 
 
            cursor.execute("DELETE FROM Users WHERE login = ?", (login,)) 
        conn.commit() 
        conn.close() 
        self.fillTable() 
 
if __name__ == "__main__": 
    app = QtWidgets.QApplication(argv) 
    app.setStyle('Fusion') 
    window = MainWindow() 
    window.show() 
    exit(app.exec_())