from zipfile import ZipFile
import os

def get_all_file_path(dic):

    file_path = []

    for root, directories, files in os.walk(dic):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_path.append(filepath)


    return file_path

def main():
    directory = "C:\ZipProjectTests\Test2"

    file_paths = get_all_file_path(directory)

    print("Following files will be zipped")
    for i in file_paths:
        print(i)


    with ZipFile(f"{directory}.zip", 'w') as zip:
        for file in file_paths:
            zip.write(file)

    print("All files zipped!")


if __name__ == '__main__':
    main()
