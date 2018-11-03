import xxhash

with open("/home/jony/PYC/hho/md5/main.js", "r") as fp:
    data = fp.read()
x = xxhash.xxh32(data).hexdigest()
print(x)

# li = list()
# print("start\n")
# for root, dirs, files in os.walk(os.getcwd()):
#     for file in files:
#         if root == "/home/jony/PYC/hho/md5/__pycache__":
#             continue
#
