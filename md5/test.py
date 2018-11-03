import os
import sys
import xxhash
from file_controler import main_file_strike


def hasher(file):
    try:
        with open(file, "r") as fp:
            data = fp.read()
        x = xxhash.xxh32(data).hexdigest()
        # print(x)
        return x
    except FileNotFoundError:
        print("File Not Found!!! Please Check if ({0}) path is Valid!!!".format(file))


def hash_saver(hash1):
    pass


def is_hash_equal(hash1, hash2):
    return hash1 == hash2


def File_Probe():

    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if root == os.path.join(os.getcwd(), "__pycache__"):
                continue
            # print(os.path.join(os.getcwd(), "__pycache__"))
            xxhash = hasher(file)
            main_file_strike(xxhash)




li = list()
print("start\n")

File_Probe()
# print(is_hash_equal(hasher("/home/jony/PYC/hho/md5/main.js"), hasher("/home/jony/PYC/hho/md5/main.min.js")))




# file = "/home/jony/PYC/hho/md5/maidn.js"
# hasher = Hasher()
# sha_hash = hasher.md5(file)
# print("MD5 (" + file + ") :")
# print(sha_hash)
