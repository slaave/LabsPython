from morse import encode_morse, decode_morse

def main():
    while True:
        choice = input("Выбирите команду:\n1. Перевод В азбуку Морзе.\n2. Перевод ИЗ азбуки Морзе.\n3. Выход\n")
        
        if choice == '1':
            subchoice = input("Выбирите команду:\n1. Ручной ввод.\n2. Ввод из файла.\n")
            if subchoice == '1':
                text = input("Введите текс для кодировки: ")
                encoded_text = encode_morse(text)
                print(f"Обработанный текст: {encoded_text}")
            elif subchoice == '2':
                    path = input("Введите путь к файлу: ")
                    with open(path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        print(content)
                        encoded_text = encode_morse(content)
                        print(f"Обработанный текст: {encoded_text}")
                    subchoice = input("Перезаписть файл?:\n1. Да.\n2. Нет.\n")
                    if subchoice == '1':
                        with open(path, 'w', encoding='utf-8') as file:
                            file.write(encoded_text)
                            print("Файл перезаписан.")
            else:
                print("Некорректный выбор.")

        elif choice == '2':
            subchoice = input("Выбирите команду:\n1. Ручной ввод.\n2. Ввод из файла.\n")
            if subchoice == '1':
                morse_code = input("Введите текс для раскодировки: ")
                decoded_text = decode_morse(morse_code)
                print(f"Обработанный текст: {decoded_text}")
            elif subchoice == '2':
                    path = input("Введите путь к файлу: ")
                    with open(path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        print(content)
                        decoded_text = decode_morse(content)
                        print(f"Обработанный текст: {decoded_text}")
                    subchoice = input("Перезаписть файл?:\n1. Да.\n2. Нет.\n")
                    if subchoice == '1':
                        with open(path, 'w', encoding='utf-8') as file:
                            file.write(decoded_text)
                            print("Файл перезаписан.")
            else:
                print("Некорректный выбор.")

        elif choice == '3':
            print("Завершение работы...")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выбирите команду из списка.")

if __name__ == "__main__":
    main()