import shutil, os


def backup(source, destination, valid_extensions, excluded_files):

    for folderName, subfolders, filenames in os.walk(source):
        # print('The current folder is ' + folderName)

        for filename in filenames:
            if filename.endswith(valid_extensions) and filename not in excluded_files:
                dest = destination+folderName[len(source):]
                # copies in the rest of the file structure after what's given in the source

                if not os.path.exists(dest):
                    os.makedirs(dest)  # if the folder structure doesn't already exist create it now

                shutil.copy(folderName + "\\" + filename, dest)  # copies the file into the location


backup("C:\\Users\\david\workspace", "C:\\Users\\david\\Desktop\\Backup\\Eclipse", (".java",), ())
backup("C:\\Users\\david\\Documents\\Visual Studio 2013", "C:\\Users\\david\\Desktop\\Backup\\VS2013",
       (".c", ".cpp", ".h", ".txt", ".dat", ".csv"), ("stdafx.h", "targetver.h", "stdafx.cpp", "ReadMe.txt"))
backup("C:\\Users\\david\\Documents\\Visual Studio 2015", "C:\\Users\\david\\Desktop\\Backup\\VS2015",
       (".c", ".cpp", ".h", ".txt", ".dat", ".csv"), ("stdafx.h", "targetver.h", "stdafx.cpp", "ReadMe.txt"))