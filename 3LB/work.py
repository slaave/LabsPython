import math

def power(text):
    txt_power = len(set(text.lower()))
    return txt_power

def hartli(txt_power):
    h_max = math.log2(txt_power)
    return h_max

def shennon(text):
    probabilities = [text.count(symbol) / len(text) for symbol in set(text)]
    h_sr = -sum(p * math.log2(p) for p in probabilities)
    return h_sr

def izb(h_max, h_sr):
    d = ((h_max - h_sr)  / h_max) * 100
    return d

def report(text):
    power_text = power(text)
    h_max = hartli(power_text)
    h_sr = shennon(text)
    d = izb(h_max, h_sr)
    print(f"Мощность алфавита: {power_text}")
    print(f"Энтропия Хартли: {h_max}")
    print(f"Энтропия Шеннона: {h_sr}")
    print(f"Избыточность алфавита: {d}")
