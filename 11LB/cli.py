import queue 
import threading 
from implementation import caesar_cipher, decryption, encryption_worker 
 
def main(): 
    q = queue.Queue() 
 
    while True: 
        choice = input("Введите '1' для ничала работы, '0' для выхода: ") 
        if choice == '1': 
            key = int(input("Введите ключ шифра Цезаря: ")) 
            n = int(input("Введите размер алфавита (n >= 1104): ")) 
            text = input("Введите текст для шифрования: ") 
            encryption_thread = threading.Thread(target=encryption_worker, args=(q, key, n)) 
            encryption_thread.start() 
            q.put(text) 
        elif choice == '0': 
            q.put(None) 
            encryption_thread.join() 
            break 
        else: 
            print("Неверный выбор. Пожалуйста, попробуйте снова.") 
 
if __name__ == "__main__": 
    main()