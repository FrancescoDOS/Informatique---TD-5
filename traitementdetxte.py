print("\033c")
from unidecode import unidecode

def normalize_text(txt):
    txt = unidecode(txt)
    txt = ''.join(i for i in txt if i.isalnum())
    txt = txt.upper()

def is_in_text(txt,search_txt):
    if search_txt in txt:
        print("Copy Found")
    else:
        print("Copy Not Found")

operations = {
    1 : normalize_text,
    2 : is_in_text,
    3 : edit_files,
    4 : encrypt_file
}

tool_select = int()
files = list()

total_files = int(input("How meany files are do you wany to work with?\n"))
for _ in range(total_files):
    files.append(input("Enter the path of the files(s)"))

while tool_select == int and tool_select > 0 and tool_select < 5:
    tool_select = int(input("\
    1 - Normalize Text\n\
    2 - Check text sample in text\n\
    3 - Edit files\n\
    4 - Encrypt files\n\n\
    Enter the tool you want to use (1 - 4):\n\
    "))

operations[tool_select]()

# txt = "à, è, ì, ò, ùÀ, È, Ì, Ò, Ùá, é, í, ó, ú, ýÁ, É, Í, Ó, Ú, Ýâ, ê, î, ô, ûÂ, Ê, Î, Ô, Ûã, ñ, õÃ, Ñ, Õä, ë, ï, ö, ü, ÿ Ä, Ë, Ï, Ö, Ü, Ÿ åÅæÆœŒçÇðÐøØß¿¡•◦‣ ∙♥©®ø£¢¥€$₩₤"
# searched_txt = "ú, ýÁ, É, Í, Ó, Ú, Ýâ, ê, î, ô, ûÂ, Ê, Î, Ô, Ûã, ñ, õÃ, Ñ, Õä"
# file_path = "C:\Users\TheOGPC\Desktop\VSCode\Informatique---TD-5\File_Example.txt"
