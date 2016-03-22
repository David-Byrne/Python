import shutil, os

backup_dest = "C:\\Users\\david\\Desktop\\Backup\\"

def visual_studio():
    source = 'C:\\Users\\david\\Documents\\Visual Studio 2013'

    for folderName, subfolders, filenames in os.walk(source):
        # print('The current folder is ' + folderName)

        for filename in filenames:
            if filename.endswith(".c") or filename.endswith(".h"):
                dest = backup_dest+"VS2013"+folderName[len(source):]
                # copies in the rest of the file structure after what's given in the source

                if not os.path.exists(dest):
                    os.makedirs(dest)  # if the folder structure doesn't already exist create it now

                shutil.copy(folderName + "\\" + filename, dest)  # copies the file into the location


def eclipse():
    source = 'C:\\Users\\david\workspace'

    for folderName, subfolders, filenames in os.walk(source):
        # print('The current folder is ' + folderName)

        for filename in filenames:
            if filename.endswith(".java"):
                dest = backup_dest+"Eclipse"+folderName[len(source):]
                # copies in the rest of the file structure after what's given in the source

                if not os.path.exists(dest):
                    os.makedirs(dest)  # if the folder structure doesn't already exist create it now

                shutil.copy(folderName + "\\" + filename, dest)  # copies the file into the location

eclipse()
visual_studio()
