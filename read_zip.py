import zipfile

file_name = "C:\ZipProjectTests\Test1.zip"
try:
    with zipfile.ZipFile(file_name, 'r') as zip:
        for filename in zip.namelist():
            print(filename)
        print(zip.read("ZipProjectTests/new_append.txt"))
except KeyError as error:
    print(error)