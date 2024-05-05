import os 
import json 
import math 
 
def calculate_frequencies(text): 
    frequencies = {} 
    for char in text: 
        if char in frequencies: 
            frequencies[char] += 1 
        else: 
            frequencies[char] = 1 
    return frequencies 
 
def build_huffman_tree(frequencies): 
    tree = list(frequencies.items()) 
    while len(tree) > 1: 
        tree.sort(key=lambda x: x[1]) 
        left = tree.pop(0) 
        right = tree.pop(0) 
        for symbol in left[0]: 
            frequencies[symbol] = '0' + frequencies[symbol] 
        for symbol in right[0]: 
            frequencies[symbol] = '1' + frequencies[symbol] 
        tree.append((left[0] + right[0], left[1] + right[1])) 
    return frequencies 
 
def encode_text_to_huffman(original_file, huffman_file): 
    with open(original_file, "r", encoding="utf-8") as file: 
        text = file.read() 
     
    frequencies = calculate_frequencies(text) 
    encoding = build_huffman_tree({key: '' for key in frequencies.keys()}) 
     
    encoded_text = "" 
    for char in text: 
        encoded_text += encoding[char] 
     
    with open(huffman_file, "w", encoding="utf-8") as file: 
        json.dump({"encoded_text": encoded_text, "encoding": encoding}, file) 
        print("Текст успешно закодирован и сохранен в файле {}.".format(huffman_file)) 
 
def decode_huffman_to_text(huffman_file, decoded_file): 
    with open(huffman_file, "r", encoding="utf-8") as file: 
        decoded_data = json.load(file) 
        encoded_text = decoded_data["encoded_text"] 
        decoding = decoded_data["encoding"] 
     
    decoded_text = "" 
    temp = "" 
    for bit in encoded_text: 
        temp += bit 
        for symbol, code in decoding.items(): 
            if code == temp: 
                decoded_text += symbol 
                temp = "" 
                break 
     
    with open(decoded_file, "w", encoding="utf-8") as file: 
        file.write(decoded_text) 
     
    print("Текст успешно декодирован и сохранен в файле {}.".format(decoded_file)) 
 
