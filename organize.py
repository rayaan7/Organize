import os
import shutil

from_dir ="C:/Users/AshRa/Downloads"
to_dir = "C:/Users/AshRa/OneDrive/Desktop/Python/downloadedImages"

list_of_files = os.listdir(from_dir)
# print(list_of_files)

for filename in list_of_files:
    name,extension= os.path.splitext(filename)
    print(name)
    # print(extension)
    if extension == "":
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = from_dir + '/' + filename
        path2 = to_dir + '/' + "Image_files"
        path3 = to_dir + '/' + "Image_files" + '/' + filename
        print(path1)

        if os.path.exists(path2):
            shutil.move(path1,path3)
            print("moved")
            
        else:
            os.makedirs(path2) 
            shutil.move(path1,path3)
            print("moved after creating")


