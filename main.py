import main_class, zip_class, os, re

def check_path(my_path):
    return os.path.exists(my_path)


if __name__ == '__main__':
    i = zip_class.Zip
    # path = "C:\ZipProjectTests\Trans_ebays","C:\ZipProjectTests\\new_append.txt"
    path = "C:\ZipProjectTests\Trans_ebays"

    path_exists = check_path(path)
    if path_exists:
        i.zip_dir(path, compress=True, compress_level=1)
