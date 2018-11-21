import os
import sys

try:
    import xxhash
except ModuleNotFoundError:
    print("'xxhash' library not installed in this system !!! \nYou can install using 'pip install xxhash' this command.\nYou can visit 'https://pypi.org/project/xxhash/' for mor information\n")
    exit()

try:
    from library.file_controler import main_file_strike
except ModuleNotFoundError:
    try:
        from file_controler import main_file_strike
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



def hash_saver(hash1):
    pass


def is_hash_equal(hash1, hash2):
    return hash1 == hash2


def File_Probe(file):

    # for root, dirs, files in os.walk(os.getcwd()):
    #     for file in files:
    #         if root == os.path.join(os.getcwd(), "__pycache__"):
    #             continue
    #         # print(os.path.join(os.getcwd(), "__pycache__"))
    xxhash = hasher(file)
    # print(file, " : ", xxhash)
    return main_file_strike(xxhash)


def Check_Probe(file):

    # for root, dirs, files in os.walk(os.getcwd()):
    #     for file in files:
    #         if root == os.path.join(os.getcwd(), "__pycache__"):
    #             continue
    #         # print(os.path.join(os.getcwd(), "__pycache__"))
    xxhash = hasher(file)
    # print(file, " : ", xxhash)
    return main_file_strike(xxhash)



# File_Probe("/home/jony/hho/assets/css/media.css")
