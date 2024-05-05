import sqlite3 
from authentication import User, hash_password 
from database import create_table_users, add_user 

DB_PATH = 'base2.db' 
users = [] 

def register(): 
    login = input("Введите логин: ") 
    password = input("Введите пароль: ") 
    is_admin = input("Это администратор? (yes/no): ").lower() == "yes" 
    user = User(login, password, is_admin) 

    try: 
        connection = sqlite3.connect(DB_PATH) 
        cursor = connection.cursor() 
         
        cursor.execute("INSERT INTO Users (login, hashed_password, is_admin) VALUES (?, ?, ?)", 
(login, hash_password(password), int(is_admin))) 
        connection.commit() 
        cursor.close() 
        connection.close() 
         
        users.append(user) 
        print("Пользователь успешно зарегистрирован.") 
         
    except sqlite3.Error as error: 
        print("Ошибка при добавлении пользователя в SQLite:", error) 

def login(): 
    login = input("Введите логин: ") 
    password = input("Введите пароль: ") 

    try: 
        connection = sqlite3.connect(DB_PATH) 
        cursor = connection.cursor() 
         
        cursor.execute("SELECT * FROM Users WHERE login = ?", (login,)) 
        user_data = cursor.fetchone() 
         
        if user_data and user_data[1] == hash_password(password): 
            is_admin = bool(user_data[2]) 
            return User(login, password, is_admin) 
        else: 
            return None 
         
    except sqlite3.Error as error: 
        print("Ошибка при аутентификации через SQLite:", error) 
         
    finally: 
        if connection: 
            connection.close() 

def delete_user(login): 
    try: 
        connection = sqlite3.connect(DB_PATH) 
        cursor = connection.cursor() 

        cursor.execute("SELECT * FROM Users WHERE login = ?", (login,)) 
        user_data = cursor.fetchone() 
         
        if user_data: 
            cursor.execute("DELETE FROM Users WHERE login = ?", (login,)) 
            connection.commit() 
            print("Пользователь успешно удален.") 
        else: 
            print("Пользователь не найден.") 

        

    except sqlite3.Error as error: 
        print("Ошибка при удалении пользователя из базы данных:", error) 

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

def admin_functions(admin): 
    while True: 
        print("1. Вывести список пользователей") 
        print("2. Удалить пользователя") 
        print("3. Добавить пользователя") 
        print("4. Сменить пароль") 
        print("5. Выход из учетной записи") 
        choice = input("Выберите действие: ") 

        if choice == '1': 
            show_all_users() 
        elif choice == '2': 
            login = input() 
            delete_user(login) 
        elif choice == '3': 
            register() 
        elif choice == '4': 
            new_password = input("Введите новый пароль: ") 
            admin.change_password(new_password) 
            print("Пароль изменен.") 
        elif choice == '5': 
            break 
        else: 
            print("Некорректный выбор. Попробуйте снова.") 

def user_functions(user): 
    while True: 
        print("1. Сменить пароль") 
        print("2. Выйти из учетной записи") 
        choice = input("Выберите действие: ") 

        if choice == '1': 
            new_password = input("Введите новый пароль: ") 
            user.change_password(new_password) 
            print("Пароль изменен.") 
        elif choice == '2': 
            break 
        else: 
            print("Некорректный выбор. Попробуйте снова.") 

def main(): 
    create_table_users() 
     
    while True: 
        action = input("1. Зарегистрироваться\n2. Войти в систему\n3. Выход\nВыберите действие: ") 
     
        if action == '1': 
            register() 
        elif action == '2': 
            user = login() 
            if user: 
                print("Вход выполнен успешно.") 
                if user.is_admin: 
                    admin_functions(user) 
                else: 
                    user_functions(user) 
            else: 
                print("Ошибка входа. Проверьте логин и пароль.") 
        elif action == '3': 
            print("Выход...") 
            break 

if __name__ == "__main__": 
    main() 