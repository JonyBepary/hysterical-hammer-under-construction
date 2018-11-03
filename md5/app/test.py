
import os
# import hashlib
# import time
from hsh import Hasher, HashChecker, file_exists
import sys
print(dir(os))
for root, dirs, files in os.walk(os.getcwd()):
    if root == "/home/jony/PYC/hho/md5/__pycache__":
        continue
    for file in files:
        # print(dirs, file)
        hasher = Hasher()
        sha_hash = hasher.md5(file)
        print("MD5 (" + file + ") :")
        print(sha_hash)
