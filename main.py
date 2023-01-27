import main_class, zip_class, os, re

def check_path(paths):
    is_dir_list = []
    for my_path in paths:
        is_dir_list.append(os.path.isdir(my_path))
    # return os.path.exists(my_path), is_dir_list
    return True, is_dir_list

if __name__ == '__main__':
    i = zip_class.Zip
    path = "C:\ZipProjectTests\Trans_ebays","C:\ZipProjectTests\\new_append.txt"

    # path_exists, is_dir_list = check_path(path)
    # if path_exists:
    #     i.zip_dir(path, compress=True, compress_level=1, _is_dir=is_dir_list)
