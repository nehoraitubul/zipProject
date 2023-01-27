import zipfile, os
import main_class

class Zip(main_class.Main):

    def zip_dir(*args, compress=False, compress_level=None, store_path='default', _is_dir):
        print(args)

        compress = "zipfile.ZIP_DEFLATED" if compress else "zipfile.ZIP_STORED"

        for integer, path in enumerate(args):
            if _is_dir[integer]:

                with zipfile.ZipFile("%s.zip" % path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=compress_level) as zip:
                    for root, directories, files in os.walk(path):
                        for file in files:
                            zip.write(os.path.join(root, file),
                                      os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))



    def extract(self, *args):
        pass