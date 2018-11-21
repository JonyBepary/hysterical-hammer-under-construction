import os
import configparser

config = configparser.ConfigParser()
path = os.path.join(os.getcwd(), '_config.ini')
try:
    config.read(path)
except Exception as e:
    raise e

cpu = config['SITE']['CPU_ARCHITECTURE']  # 'secret-key-of-myapp'
file = config['SITE']['FILE_SKIPPING']

print("cpu: {}  file: {}".format(cpu, file))

config.set("SITE", "FILE_SKIPPING", "False")
file = config['SITE']['FILE_SKIPPING']

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
