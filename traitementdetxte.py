print("\033c")
from unidecode import unidecode
from random import randint

# =============================================================================================


def ask_file():
    file_path = str()
    while file_path.endswith(".txt") == False:
        file_path = repr(input("Enter a file path of an existing '.txt' file:\n")) # "file_path" will always be raw string if called from "ask_file()"

    try:
        open(file_path)
    except FileNotFoundError:
        print("Yikes!\nThe file path you inserted was not found\nPlease insert a file path of an existing '.txt' file\n\n")
        ask_file()
    return file_path


def rewrite_file(file_path,txt):
    with open(file_path,"r+") as f:
        f.truncate()
        f.write(txt)

def fetch_txt(file_path):
    with open(file_path,"r+") as f:
        txt = f.readlines
    return txt

def fetch_file_name(file_path):
    path = file_path.split("\\")
    return path[-1]

# =========================================================================================================================================


def normalize_text(file_path):
    txt = fetch_txt(file_path)
    txt = unidecode(txt)
    txt = ''.join(i for i in txt if i.isalnum())
    txt = txt.upper()
    rewrite_file(file_path, txt)

def is_in_text(file_path):
    search_txt = input("Enter the phrase you would like to search for:\n")
    txt = fetch_txt(file_path)
    if search_txt in txt:
        print(f"A copy of that text has been found in {fetch_file_name(file_path)}")
    else:
        print(f"No match found in {fetch_file_name(file_path)} for:\n{search_txt}")

def edit_file(file_path): # TO DO
    pass

def cesar_encrypt(file_path):
    txt, key, temp_txt = fetch_txt(file_path), randint(1,25), str()
    try:
        for char in txt:
            temp_txt += str(chr(ord(char)+int(key)))
    except Exception: pass
    rewrite_file(file_path, temp_txt)
    print(f"Caesar cipher done!\n{fetch_file_name(file_path)} has been encrypted using this key:\n{key}")

def vigenere_encrypt(file_path): # TO DO
    pass


# =========================================================================================================================================

def encrypt_file_select(file_path):
    encryption_type = int()
    while encryption_type <= 0 and encryption_type > 2: 
        encryption_type = int(input("What encryption would you like? (1 - 2)\n1 - Cesar\n2 - Vigenere\n"))
    operations[encryption_type + 4](file_path) if encryption_type == 1 else operations[encryption_type + 4](file_path)

def tool_select_menu():

    tool_select = int()

    while tool_select <= 0 and tool_select > 5:
            tool_select = int(input("\
            1 - Normalize Text\n\
            2 - Check text sample in text\n\
            3 - Edit file\n\
            4 - Encrypt files\n\n\
            Enter the tool you want to use (1 - 4):\n\
            "))

    return tool_select

operations = {
    1 : normalize_text,
    2 : is_in_text,
    3 : edit_file,
    4 : encrypt_file_select,
    5 : cesar_encrypt,
    6 : vigenere_encrypt
}

def main():
    tool_select = tool_select_menu()
    file = ask_file()
    operations[tool_select](file)
main()












# searched_txt = "ú, ýÁ, É, Í, Ó, Ú, Ýâ, ê, î, ô, ûÂ, Ê, Î, Ô, Ûã, ñ, õÃ, Ñ, Õä"
# file_path = r"C:\Users\TheOGPC\Desktop\VSCode\Informatique---TD-5\File_Example.txt"
