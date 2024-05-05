import code
import os
import json
from datetime import datetime
from collections import Counter
from platform import node

class Node: # Определение класса Node для узлов дерева Хаффмана
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

class CodeGenerator: # Определение класса CodeGenerator для генерации кодов Хаффмана
    def __init__(self):
        self.__codes = {} # Инициализация словаря для хранения кодов Хаффмана

    def __huffman_coding(self, freq_dict): # Метод для построения дерева Хаффмана на основе частот символов
        nodes = [Node(sym, freq) for sym, freq in freq_dict.items()] # Создание узлов для символов и их частот
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.freq) # Сортировка узлов по частоте
            left = nodes.pop(0)
            right = nodes.pop(0)
            merged = Node(None, left.freq + right.freq) # Создание объединенного узла
            merged.left = left
            merged.right = right
            nodes.append(merged)
        root = nodes[0] # Получение корневого узла дерева Хаффмана
        self.__generate_codes(root, '') # Генерация кодов Хаффмана для символов

    def __generate_codes(self, node, code): # Рекурсивный метод для генерации кодов Хаффмана
        if node.symbol:
            self.__codes[node.symbol] = code
        else:
            self.__generate_codes(node.left, code + '0') # Рекурсивный вызов для левого потомка с добавлением '0'
            self.__generate_codes(node.right, code + '1') # Рекурсивный вызов для правого потомка с добавлением '1'



    def gen_code(self, file_path):  # Метод для генерации кодов Хаффмана на основе текстового файла
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            freq_dict = dict(Counter(text)) # Создание словаря частот символов из текста
        self.__huffman_coding(freq_dict)
     
        timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        folder_name = os.path.join(os.getcwd(), timestamp)
        os.mkdir(folder_name)
     
        with open(os.path.join(folder_name, 'code.json'), 'w') as json_file:
            json.dump(self.__codes, json_file, ensure_ascii=False, indent=4)

        print("Huffman code generated successfully in folder:", folder_name)


def main():
    cgen = CodeGenerator()
    cgen.gen_code('my_file.txt')

if __name__ == "__main__":
    main()
