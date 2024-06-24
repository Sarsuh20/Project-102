import shutil
import os

from_dir= "C:/Users/Sarva/Downloads"
to_dir= "C:/Users/Sarva/Documents"

list_of_files= os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    root, extention = os.path.splitext(file)
    print(root)
    print(extention)
    if extention == "":
        continue
    if extention in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir+"/"+file
        path2 = to_dir+"/"+"Document_Files"
        path3 = to_dir+"/"+"Document_Files"+"/"+file
        if os.path.exists(path2):
            print("moving"+ file + "....")
            shutil.move(path1 , path3)
        else:
            os.makedirs(path2)
            print("moving"+ file + "....")
            shutil.move(path1, path3)