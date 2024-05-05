import math 
 
def calculate_message_characteristics(file_name): 
    with open(file_name, "r", encoding="utf-8") as file: 
        text = file.read().lower() 
 
    alphabet_length = len(set(filter(str.isalpha, text))) 
    max_entropy = math.log2(alphabet_length) 
     
    probabilities = {char: text.count(char) / len(text) for char in set(filter(str.isalpha, text))} 
    shannon_entropy = sum([-prob * math.log2(prob) for prob in probabilities.values()]) 
     
    redundancy = ((max_entropy - shannon_entropy) / max_entropy) * 100 
     
    print("Мощность алфавита: ", alphabet_length) 
    print("Энтропия Хартли: ", max_entropy) 
    print("Энтропия Шеннона: ", shannon_entropy) 
    print("Избыточность алфавита: {:.2f}%".format(redundancy)) 

    return {
        'alphabet_length': alphabet_length,
        'max_entropy': max_entropy,
        'shannon_entropy': shannon_entropy,
        'redundancy': redundancy
    }