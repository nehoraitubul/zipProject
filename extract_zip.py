import zipfile

file_name = "C:\ZipProjectTests\Test2.zip"
if zipfile.is_zipfile(file_name):
    with zipfile.ZipFile(file_name, 'r') as zip:
        zip.printdir()

        print("Extracting all the files now...")
        zip.extractall(path="C:\ZipProjectTests")
        print("Done")
else:
    print("The file is not zip file")

