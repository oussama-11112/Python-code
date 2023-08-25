import os

PARENT_FOLDER = os.getcwd()
CURRENT_FOLDER = os.path.join(PARENT_FOLDER, "folders")

print("the path of the parent folder is: ", PARENT_FOLDER)
print("the path of the current folder is: ", CURRENT_FOLDER)


import os

parent_path = os.getcwd()
current_path = os.path.join(parent_path, "OUSSAMA")
idk_path = os.path.join(current_path, "sub folder1")

print("Parent: ", parent_path)
print("Current", current_path)

#create a new folder
