import zipfile

#not workings

file_name = "C:\ZipProjectTests\Test1.zip"
with zipfile.ZipFile(file_name, 'r') as zip:
    zip.setpassword(b"secret")