from work import report
import os

def main():
    while True:
        choice = input("\nВыбирите команду:\n1. Ручной ввод.\n2. Из файла.\n3. Выход\n")
        
        if choice == '1':
            text = input("Введите текст:\n")
            report(text)

        elif choice == '2':
            path = input("Введите путь к файлу: ")
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if content:
                        print(content)
                        report(content)
                    else:
                        print("Файл пустой. Пожалуйста, укажите файл с содержимым.")    
            else:
                print("Файл не найден. Пожалуйста, укажите существующий путь к файлу.")
                
        elif choice == '3':
            print("Завершение работы...")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выбирите команду из списка.")

if __name__ == "__main__":
    main()