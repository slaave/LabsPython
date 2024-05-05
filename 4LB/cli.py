import os
from huffman import CodeGenerator

def main():
    cgen = CodeGenerator()
    
    while True:
        print("\n1. Generate Huffman code for a text file")
        print("2. Clear code generation history")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            file_path = input("Enter the path of the text file: ")

            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                cgen.gen_code(file_path)
            else:
                print("The specified file does not exist or is empty.")
        
        elif choice == '2':
            confirm = input("Do you really want to clear code generation history? (y/n): ")
            if confirm.lower() == 'y':
                folders = [f for f in os.listdir() if os.path.isdir(f)]
                for folder in folders:
                    if folder.startswith('20'):
                        folder_path = os.path.join(os.getcwd(), folder)
                        for the_file in os.listdir(folder_path):
                            file_path = os.path.join(folder_path, the_file)
                            try:
                                if os.path.isfile(file_path):
                                    os.unlink(file_path)
                            except Exception as e:
                                print(e)
                        try:
                            os.rmdir(folder_path)
                        except Exception as e:
                            print(e)
                            print("Code generation history cleared.")
  
        elif choice == '3':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
