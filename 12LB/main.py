import requests 
from multiprocessing import Pool 
 
def caesar_cipher(text, key): 
    encrypted_text = '' 
    for char in text: 
        if char.isalpha(): 
            shifted = ord(char) + key 
            if char.islower(): 
                if shifted > ord('я'): 
                    shifted -= 32 
                elif shifted < ord('а'): 
                    shifted += 32 
            elif char.isupper(): 
                if shifted > ord('Я'): 
                    shifted -= 32 
                elif shifted < ord('А'): 
                    shifted += 32 
            encrypted_text += chr(shifted) 
        else: 
            encrypted_text += char 
    return encrypted_text 
 
def decrypt_with_key(text_key_pair): 
    text, key = text_key_pair 
    decrypted_text = caesar_cipher(text, -key) 
    return decrypted_text 
 
response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt') 
russian_words = set(response.content.decode('cp1251').splitlines()) 
 
if __name__ == '__main__': 
    encrypted_text = "Привет" 
 
    keys = range(-32, 33) 
 
    text_key_pairs = [(encrypted_text, key) for key in keys] 
 
    with Pool() as pool: 
        decrypted_texts = pool.map(decrypt_with_key, text_key_pairs) 
 
    with open('options.txt', 'w', encoding='utf-8') as file: 
        for key, text in zip(keys, decrypted_texts): 
            if any(word in text.split() for word in russian_words): 
                file.write(f"Key: {key}, Decrypted Text: {text}\n")