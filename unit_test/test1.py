import sys
sys.path.append("..")
from library import config
import os



file_name = '_config.ini'
path = os.path.join(os.environ['HOME'], file_name)
file = os.path.join(os.getcwd(), file_name)


print(int('1') == 1)
config.config_maker()
exit()
# print(config.config_path_ask(path, file))
