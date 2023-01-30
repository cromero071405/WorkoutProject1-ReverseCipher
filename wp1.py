from pathlib import Path
import sys

def get_original_text(input_file):
    original_text = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            original_text.append(line.replace("\n", ""))
    return original_text


def encrypt_text(input_file):
    original_text = input_file
    encrypted_text = []
    for line in reversed(original_text):
        l = "".join(reversed(line))
        encrypted_text.append(l)
    return encrypted_text
        
         
def write_encrypted_text(output_file, encrypted_text):
    with open(output_file, 'w') as f:
        for line in encrypted_text:
            f.write(line + "\n")


def main():
    if len(sys.argv) == 3:
        original_file = sys.argv[1]
        encrypted_file = sys.argv[2]

        # Creating two path objects from the variables "original_file"
        # and "encrypted_path" of which command line arguments are stored. 
        original_path = Path(original_file)
        encrypted_path = Path(encrypted_file)

        # Checks if user input contains the correct format: Pure Text File
        if original_path.exists():
            if original_path.suffix == ".txt" and encrypted_path.suffix == ".txt":
                original_text = get_original_text(original_path)
                encrypt_original_text = encrypt_text(original_text)
                write_encrypted_text(encrypted_file, encrypt_original_text) 
            else:
                print("Invalid File Formats, Please Try Again.")
                main()
    else:
        pass


if __name__ == "__main__":
    main()
        
        

        
