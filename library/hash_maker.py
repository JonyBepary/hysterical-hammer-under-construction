'''For hashing and other stuf
File_Probe(file):
Check_Probe(file):'''
import os
import sys

try:
    import xxhash
except ModuleNotFoundError:
    print("'xxhash' library not installed in this system !!! \nYou can install using 'pip install xxhash' this command.\nYou can visit 'https://pypi.org/project/xxhash/' for mor information\n")
    exit()

try:
    from library.file_controler import main_file_strike, check_strike
except ModuleNotFoundError:
    try:
        from file_controler import main_file_strike, check_strike
    except ModuleNotFoundError:
        print("'file_controler' library Not Found in this system !!! \nYou can check if all files are installed correctly.\n\n")
        exit()



def hasher(file):
    try:
        with open(file, "r") as fp:
            data = fp.read()
            # print("data: ", data)
        x = xxhash.xxh64(data).hexdigest()
        # print(x)
        return x
    except FileNotFoundError:
        print("File Not Found!!! Please Check if ({0}) path is Valid!!!".format(file))
        return FileNotFoundError
    except UnicodeDecodeError:
        with open(file, "rb") as fp:
            data = fp.read()

        x = xxhash.xxh64(data).hexdigest()
        # print(x)
        return x


def File_Probe(file):
    xxhash = hasher(file)
    # print('File_Probe')
    # print("file_controler cwd: ", os.getcwd())
    return main_file_strike(xxhash)


def Check_Probe(file):
    # print('File_check')
    # print("file_controler cwd: ", os.getcwd())
    xxhash = hasher(file)
    # print(file, ':', xxhash)
    return check_strike(xxhash)



# File_Probe("/home/jony/hho/assets/css/media.css")
