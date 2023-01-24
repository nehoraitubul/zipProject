import zipfile
import warnings


file_name = "C:\ZipProjectTests\Test2.zip"
try:
    with zipfile.ZipFile(file_name, 'a') as zip:
        zip.printdir()
        try:
            warnings.filterwarnings("error")
            zip.write("C:\ZipProjectTests\\new_append.txt")
            zip.printdir()
        except UserWarning as erorr:
            print(erorr)
            usr_inp = input("its look like this file is already exist, please press 1 if you want to force this process or 0 to terminate")
            if usr_inp == "1":
                warnings.resetwarnings()
                warnings.filterwarnings('ignore')
                zip.write("C:\ZipProjectTests\\new_append.txt")
                zip.printdir()
except (FileNotFoundError, PermissionError) as error:
    print(error)

