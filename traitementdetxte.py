# print("\033c")
from unidecode import unidecode

def ask_file():
    file_path = repr(input("Enter file path\n"))
    try:
        open(file_path)
    except FileNotFoundError:
        print("Yikes!\nThe file path you inserted was not found\nPlease insert a file path of an existing file'.txt' file\n\n")
        ask_file()
    return file_path

def normalize_text(txt = ask_file()):
    with open(txt,"r+") as f:
        txt = f.readlines
        txt = unidecode(txt)
        txt = ''.join(i for i in txt if i.isalnum())
        txt = txt.upper()
        f.truncate()
        f.write(txt)


def is_in_text(txt = ask_file(),search_txt = input("Enter the phrase you would like to search for:\n")):
    pass


def edit_file(txt = ask_file()):
    pass

def cesar_encrypt(txt):
    pass

def vigenere_encrypt(txt):
    pass

def encrypt_file(txt = ask_file()):
    encryption_type = int()
    while encryption_type <= 0 and encryption_type > 2: 
        encryption_type = int(input("What encryption would you like? (1 - 2)\n1 - Cesar\n2 - Vigenere\n"))
    operations[encryption_type + 4](txt) if encryption_type == 1 else operations[encryption_type + 4](txt)





operations = {
# ======================
    1 : normalize_text,
    2 : is_in_text,
    3 : edit_file,
    4 : encrypt_file,
# ======================
    5 : cesar_encrypt,
    6 : vigenere_encrypt
}

tool_select = int()
files = list()

def main():

    while tool_select <= 0 and tool_select > 5:
        tool_select = int(input("\
        1 - Normalize Text\n\
        2 - Check text sample in text\n\
        3 - Edit file\n\
        4 - Encrypt files\n\n\
        Enter the tool you want to use (1 - 4):\n\
        "))

    print(operations[tool_select])
    operations[tool_select]()
main()












# searched_txt = "ú, ýÁ, É, Í, Ó, Ú, Ýâ, ê, î, ô, ûÂ, Ê, Î, Ô, Ûã, ñ, õÃ, Ñ, Õä"
# file_path = "C:\Users\TheOGPC\Desktop\VSCode\Informatique---TD-5\File_Example.txt"
