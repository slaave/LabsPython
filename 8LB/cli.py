import tkinter as tk 
from tkinter import filedialog, messagebox 
import os 
from huffman_coder_decoder import * 
from entropy_calculator import calculate_message_characteristics 
 
class HuffmanGUI: 
    def __init__(self, master): 
        self.master = master 
        self.master.title("Huffman Coder/Decoder") 
 
        self.label = tk.Label(master, text="Choose an action:") 
        self.label.pack() 
 
        self.mode = tk.StringVar(value="encode") 
 
        self.encode_radio = tk.Radiobutton(master, text="Encode Unicode Text to Huffman Code", 
variable=self.mode, value="encode") 
        self.encode_radio.pack() 
 
        self.decode_radio = tk.Radiobutton(master, text="Decode Huffman Code to Unicode Text", 
variable=self.mode, value="decode") 
        self.decode_radio.pack() 
 
        self.button = tk.Button(master, text="Perform Action", command=self.perform_action) 
        self.button.pack() 
 
        self.info_label = tk.Label(master, text="") 
        self.info_label.pack() 
 
        master.bind("<Escape>", lambda event: master.quit()) 
 
    def perform_action(self): 
        if self.mode.get() == "encode": 
            file_path = filedialog.askopenfilename(title="Select the original file (Unicode text)") 
            if file_path: 
                huffman_file = filedialog.asksaveasfilename(title="Save Huffman code to", defaultextension=".json") 
                encode_text_to_huffman(file_path, huffman_file) 
                 
                original_size = os.path.getsize(file_path) 
                encoded_size = os.path.getsize(huffman_file) 
 
                entropy_info = calculate_message_characteristics(file_path) 
                average_bits_per_symbol = encoded_size * 8 / entropy_info['alphabet_length'] 
 
                compression_ratio = original_size / encoded_size 
 
                info_str = f"Original Size: {original_size} bytes\nEncoded Size: {encoded_size} bytes\nShannon Entropy: {entropy_info['shannon_entropy']}\nAverage Bits per Symbol: {average_bits_per_symbol}\nCompression Ratio: {compression_ratio}" 
                self.info_label.config(text=info_str) 
                messagebox.showinfo("Huffman Coder/Decoder", "Text successfully encoded and saved.") 
        else: 
            huffman_file = filedialog.askopenfilename(title="Select the Huffman code file") 
            if huffman_file: 
                decoded_file = filedialog.asksaveasfilename(title="Save decoded text to", defaultextension=".txt") 
                decode_huffman_to_text(huffman_file, decoded_file) 
             
                original_size = os.path.getsize(decoded_file) 
 
                entropy_info = calculate_message_characteristics(decoded_file) 
                average_bits_per_symbol = original_size * 8 / entropy_info['alphabet_length'] 
 
                compression_ratio = entropy_info['shannon_entropy'] / average_bits_per_symbol 
 
                info_str = f"Original Size: {original_size} bytes\nShannon Entropy: {entropy_info['shannon_entropy']}\nAverage Bits per Symbol: {average_bits_per_symbol}\nCompression Ratio: {compression_ratio}" 
                self.info_label.config(text=info_str) 
                messagebox.showinfo("Huffman Coder/Decoder", "Text successfully decoded and saved.") 
 
def main(): 
    root = tk.Tk() 
    app = HuffmanGUI(root) 
    root.mainloop() 
 
if __name__ == "__main__": 
    main() 
