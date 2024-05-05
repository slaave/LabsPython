import sqlite3 
from authentication import hash_password 
 
DB_PATH = 'base.db' 
users = [] 
 
def create_table_users(): 
    try: 
        connection = sqlite3.connect(DB_PATH) 
        cursor = connection.cursor() 
         
        cursor.execute("""CREATE TABLE IF NOT EXISTS Users (login TEXT PRIMARY KEY, 
hashed_password TEXT, is_admin INTEGER)""") 
        connection.commit() 
         
    except sqlite3.Error as error: 
        print("Ошибка при создании таблицы Users:", error) 
         
    finally: 
        if connection: 
            connection.close() 
 
def add_user(login, password, is_admin): 
    try: 
        connection = sqlite3.connect(DB_PATH) 
        cursor = connection.cursor() 
         
        cursor.execute("INSERT INTO Users (login, hashed_password, is_admin) VALUES (?, ?, ?)", 
                       (login, hash_password(password), int(is_admin))) 
        connection.commit() 
         
        print("Пользователь успешно добавлен в базу данных.") 
         
    except sqlite3.Error as error: 
        print("Ошибка при добавлении пользователя в SQLite:", error) 
         
    finally: 
        if connection: 
            connection.close() 
 
def show_all_users(): 
    try: 
        connection = sqlite3.connect(DB_PATH) 
        cursor = connection.cursor() 
 
        cursor.execute("SELECT login FROM Users") 
        all_users = cursor.fetchall() 
 
        if len(all_users) > 0: 
            print("Список зарегистрированных пользователей:") 
            for user in all_users: 
                print(user[0]) 
        else: 
            print("Нет зарегистрированных пользователей.") 
 
    except sqlite3.Error as error: 
        print("Ошибка при выводе списка пользователей:", error) 
 
    finally: 
        if connection: 
            connection.close() 
 
def delete_user(login): 
    try: 
        connection = sqlite3.connect(DB_PATH) 
        cursor = connection.cursor() 
 
        cursor.execute("DELETE FROM Users WHERE login = ?", (login,)) 
        connection.commit() 
        print("Пользователь успешно удален.") 
 
    except sqlite3.Error as error: 
        print("Ошибка при удалении пользователя из базы данных:", error) 
 
    finally: 
        if connection: 
            connection.close()