import shutil, os

source = 'C:\\Users\\david\workspace'

for folderName, subfolders, filenames in os.walk(source):
    # print('The current folder is ' + folderName)

    for filename in filenames:
        if filename.endswith(".java"):
            dest = "C:\\Users\\david\\Desktop\\temp"+folderName[len(source):]
            # copies in the rest of the file structure after what's given in the source

            if not os.path.exists(dest):
                os.makedirs(dest)  # if the folder structure doesn't already exist create it now

            shutil.copy(folderName + "\\" + filename, dest)  # copies the file into the location
