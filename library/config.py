import os
import configparser


file_name = '_config.ini'
config = configparser.ConfigParser()
path = os.path.join(os.getcwd(), file_name)


def config_set(Header, Attribute, Value, file=None):
    try:
        config.read(file)
        config.set(Header, Attribute, Value)
        return True
    except KeyError as e:
        return KeyError
    except TypeError:
        try:
            config.read(path)
            config.set(Header, Attribute, Value)
            return True
        except KeyError as e:
            return KeyError
        except FileNotFoundError:
            print("{} This File Not Found\n".format(file))
        return FileNotFoundError
    except FileNotFoundError:
        print("{} This File Not Found\n".format(file))
        return FileNotFoundError
    try:
        with open(file, 'w') as fp:
            config.write(fp)
    except TypeError:
        try:
            with open(path, 'w') as fp:
                config.write(fp)
        except KeyError as e:
            return KeyError
    except FileNotFoundError:
        print("{} This File Not Found\n".format(file))
        return FileNotFoundError

    # uncomment for testing
    # cpu = config["JEKYLL"]["CPU_ARCHITECTURE"]
    # file = config['JEKYLL']['FILE_SKIPPING']
    # print("cpu: {}  file: {}".format(cpu, file))



def config_get(Header, Attribute, file=None):
    try:
        config.read(file)
        con_str = config[Header][Attribute]
        return config[Header][Attribute]
    except KeyError as e:
        return KeyError
    except TypeError:
        try:
            config.read(path)
            con_str = config[Header][Attribute]
            return config[Header][Attribute]
        except KeyError as e:
            return KeyError
        except FileNotFoundError:
            print("{} This File Not Found\n".format(file))
            return FileNotFoundError
        pass
    except FileNotFoundError:
        print("{} This File Not Found\n".format(file))
        return FileNotFoundError

    # uncomment for testing
    # cpu = config["JEKYLL"]["CPU_ARCHITECTURE"]
    # file = config['JEKYLL']['FILE_SKIPPING']
    # print("cpu: {}  file: {}".format(cpu, file))


# Function Example
# ['JEKYLL']['CPU_ARCHITECTURE']
# print(config_set('SITE', 'CPU_ARCHITECTURE', '32'))
# print(config_get('SITE', 'CPU_ARCHITECTURE'))
