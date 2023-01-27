import zipfile
from zipfile import ZipFile
import os


def main():
    directory = "C:\ZipProjectTests\Trans_ebays"


    # ---------------------------------------------------------------
    # MULTI DIRECTORIES
    # zipfile.ZIP_STORED
    with ZipFile(f"C:\ZipProjectTests\Trans_ebays.zip", 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=None) as zip:
        for root, directories, files in os.walk(directory):
            for file in files:
                zip.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file),  os.path.join(directory, '..')))
    # ---------------------------------------------------------------


    #---------------------------------------------------------------
    #SINGLE FILE
    # zipfile.ZIP_STORED
    # with ZipFile(f"C:\ZipProjectTests\\new_append.zip", 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=None) as zip:
    #     # for file in file_paths:
    #     zip.write("C:\ZipProjectTests\\new_append.txt", "new_append")
    # ---------------------------------------------------------------


if __name__ == '__main__':
    main()
