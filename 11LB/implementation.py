def caesar_cipher(text, key, n): 
    encrypted_text = '' 
    for char in text: 
        if char.isalpha(): 
            shifted = ord(char) + key 
            if char.islower(): 
                if shifted > ord('z'): 
                    shifted -= 26 
                elif shifted < ord('a'): 
                    shifted += 26 
            elif char.isupper(): 
                if shifted > ord('Z'): 
                    shifted -= 26 
                elif shifted < ord('A'): 
                    shifted += 26 
            encrypted_text += chr(shifted) 
        else: 
            encrypted_text += char 
    return encrypted_text 
 
def decryption(text, key, n): 
    decrypted_text = '' 
    for char in text: 
        if char.isalpha(): 
            shifted = ord(char) - key 
            if char.islower(): 
                if shifted > ord('z'): 
                    shifted -= 26 
                elif shifted < ord('a'): 
                    shifted += 26 
            elif char.isupper(): 
                if shifted > ord('Z'): 
                    shifted -= 26 
                elif shifted < ord('A'): 
                    shifted += 26 
            decrypted_text += chr(shifted) 
        else: 
            decrypted_text += char 
    return decrypted_text 

def encryption_worker(queue, key, n): 
    while True: 
        text = queue.get() 
        if text is None: 
            break 
        encrypted_text = caesar_cipher(text, key, n) 
        decrypted_text = decryption(encrypted_text, key, n) 
        print(f"Зашифрованный текст: {encrypted_text} - {text}\n") 
        print(f"Раcшифрованный текст: {decrypted_text} — {encrypted_text}")