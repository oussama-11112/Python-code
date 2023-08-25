# file is closed by "with" statement

with open(
    r"C:\Users\LENOVO\Nouveau dossier (1)\Dossier python\Day 6\text.txt", "r"
) as name_file:
     content = name_file.read()
     print(content)

#we need to close:

name_file = open(
     r"C:\Users\LENOVO\Nouveau dossier (1)\Dossier python\Day 6\text.txt", "r"
)



try:
    with open(
        r"C:\Users\LENOVO\Nouveau dossier (1)\Dossier python\Day 6\text.txt", "r"
    ) as name_file:
        content = name_file.read()
        print(content)
except FileNotFoundError:
    print("File doesn't exist")
except SyntaxError:
    print("make sure to use the 'r' for windows.")



