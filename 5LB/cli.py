import os
import json
from huffman_coder import *

def main():
    while True:
        print("1. Кодировать текст из Unicode в код Хаффмана")
        print("2. Декодировать текст из кода Хаффмана в Unicode")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            original_file = input("Введите имя оригинального файла (с текстом в кодировке Unicode): ")
            huffman_file = input("Введите имя файла для сохранения кода Хаффмана (в формате JSON): ")

            encode_text_to_huffman(original_file, huffman_file)

        elif choice == "2":
            huffman_file = input("Введите имя файла с кодом Хаффмана (в формате JSON): ")
            decoded_file = input("Введите имя файла для сохранения декодированного текста (с расширением .txt): ")

            decode_huffman_to_text(huffman_file, decoded_file)

        elif choice == "3":
            print("Завершение работы")
            break

if __name__ == "__main__":
    main()
