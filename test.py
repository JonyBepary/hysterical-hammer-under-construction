import os
import configparser

config = configparser.ConfigParser()
path = os.path.join(os.getcwd(), '_config.ini')
config.read(path)

cpu = config['JEKYLL']['CPU_ARCHITECTURE']  # 'secret-key-of-myapp'
file = config['JEKYLL']['FILE_SKIPPING']

print("cpu: {}  file: {}".format(cpu, file))

config.set("JEKYLL", "FILE_SKIPPING", "False")
file = config['JEKYLL']['FILE_SKIPPING']

print("cpu: {}  file: {}".format(cpu, file))





# import json
# with open("_config.json", "r") as fp:
#     config = json.load(fp)

# print(config)



# []
# TARGET_LOCATION = "/_site"
# FILE_DATABASE = "filehash.db"
# FILE_SKIPPING = True
# CPU_ARCHITECTURE = 64
