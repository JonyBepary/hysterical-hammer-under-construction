import platform
import os
import configparser


file_name = '_config.ini'
config = configparser.ConfigParser(strict=False)
path = os.path.join(os.environ['HOME'], file_name)




def config_set(Header, Attribute, Value, file=None):
    try:
        config.read(file)
        config.set(Header, Attribute, Value)
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
    # try:
    #     with open(file, 'w') as fp:
    #         config.write(fp)
    # except TypeError:
    #     try:
    #         with open(path, 'w') as fp:
    #             config.write(fp)
    #     except KeyError as e:
    #         return KeyError
    except FileNotFoundError:
        print("{} This File Not Found\n".format(file))
        return FileNotFoundError

    # uncomment for testing
    # cpu = config["JEKYLL"]["CPU_ARCHITECTURE"]
    # file = config['JEKYLL']['FILE_SKIPPING']
    # print("cpu: {}  file: {}".format(cpu, file))


def config_path_ask(path, file=None):
    config_ui('No _config.ini detected in current directory!!!\nWhich config you want to use', ['Universal at [Default]: ', 'Make a New One at: '], [path, file])
    cmd = input("Enter a Option (1-2): ")
    if cmd == '2':
        return False
    else:
        return os.path.isfile(path)


def config_get(Header, Attribute, file=None):
    if os.path.isfile(file) != False:
        try:
            config.read(file)
            con_str = config[Header][Attribute]
            return config[Header][Attribute]
        except KeyError:
            print('KeyError')
            return KeyError
        except TypeError:
            print("TypeError in config.py and get config file bound")
            return TypeError
    elif config_path_ask(path, file):
        try:
            config.read(path)
            con_str = config[Header][Attribute]
            return config[Header][Attribute]
        except KeyError as e:
            print('KeyError')
            return KeyError
        except FileNotFoundError:
            print("{} This File Not Found\n".format(file))
            return FileNotFoundError
        except TypeError:
            print("TypeError in config.py and get config path bound")
            return TypeError
    else:
        config_maker(file)
    # uncomment for testing
    # cpu = config["JEKYLL"]["CPU_ARCHITECTURE"]
    # file = config['JEKYLL']['FILE_SKIPPING']
    # print("cpu: {}  file: {}".format(cpu, file))


# Function Example
# ['JEKYLL']['CPU_ARCHITECTURE']

def config_file_maker(file=None):
    text = """; 'target_location' directory can be separated by comma
; 'file_database'  used to store hash generated
; 'file_skipping' for check file integrity & skip if it's already optimized
; 'cpu_architecture' this variable used durning hashing. set value 64 for x64 and 32 for x86 architecture. you can see your cpu architecture by entering "$ getconf LONG_BIT" command
;'overwrite' used to replace current file to optimized file

"""
    with open(file, 'w') as fp:
        fp.write(text)
        # fp.write("[SITE]")
    return fp.close()


def config_ui(text, list1, list2=None, list3=None, list4=None):
    print(text)
    if list2 == None:
        for i, value in enumerate(list1):
            print('{}. {} {} {} {}'.format(i + 1, value, "", "", ""))
    elif list3 == None:
        for i, value in enumerate(list1):
            print('{}. {} {}'.format(i + 1, value, list2[i], "", ""))
    elif list4 == None:
        for i, value in enumerate(list1):
            print('{}. {} {}'.format(i + 1, value, list2[i], list3[i], ""))
    else:
        for i, value in enumerate(list1):
            print('{}. {} {}'.format(i + 1, value, list2[i], list3[i], list4[i]))
    return 0


    # jpeg_optim_quality = input("jpegoptim quality (0 - 100): ")
def config_decision(cmd, section, attribute, values, default=None, file=None):
    for i, value in enumerate(values):
        print(value)
        if cmd == str(i + 1):
            config_set(section, attribute, value, file)
            return value
    if default != None:
        config_set(section, attribute, default, file)
        return default


def config_maker(file_dir=None):
    if file_dir == None:
        file = os.path.join(os.getcwd(), file_name)
    else:
        file = os.path.join(file_dir, file_name)
    config_file_maker(file)
    config.add_section('SITE')
    ####### Target folder ########
    section = 'SITE'
    attribute = 'target_location'
    values = ['_site', 'static', "Custom"]
    config_ui("Target folder: ", values, ["JEKYLL", "GHOST", ""], )
    cmd = input("Your Command (1-3): ")
    ext = config_decision(cmd, section, attribute, values, values[1], file)
    if ext == values[2]:
        folder = input("Your Custom folder name: ")
        config_set(section, attribute, folder, file)

    config_set(section, 'file_database', "filehash.db", file)
    cmd = input("skip optimized file (y/N): ")
    if (cmd == 'N') | (cmd == 'n'):
        config_set('SITE', 'file_skipping', 'False', file)
    else:
        config_set('SITE', 'file_skipping', 'True', file)
    cmd = input("overwrite optimized file (y/N): ")
    if (cmd == 'N') | (cmd == 'n'):
        config_set('SITE', 'overwrite', 'False', file)
    else:
        config_set('SITE', 'overwrite', 'True', file)
    ####### Target CPU_ARCHITECTURE for hashing:  ########
    section = 'SITE'
    attribute = 'target_location'
    values = ['X86', 'X64', 'Detect from System']
    config_ui("CPU_ARCHITECTURE for hashing: ", values)
    cmd = input("CPU_ARCHITECTURE (1-3): ")
    ext = config_decision(cmd, section, attribute, values, values[2], file)

    config.add_section('IMAGE')

    ####### Target jpeg encoder for optimizing jpeg file:  ########
    section = 'IMAGE'
    attribute = 'jpg_encoder'
    values = ['MOZJPEG', ' LIBJPEG-TURBO', 'Custom']
    config_ui("jpeg encoder for optimizing jpeg file: ", values)
    cmd = input("jpeg_enocoder (1-3): ")
    ext = config_decision(cmd, section, attribute, values, values[1], file)
    if ext == values[2]:
        folder = input("Your Custom folder name: ")
        config_set(section, attribute, folder, file)

    ####### Target jpeg programs for optimizing jpeg file:  ########
    section = 'IMAGE'
    attribute = 'jpg_program'
    values = ['jpegtran', 'jpegoptim', 'jpegtran', 'jpegrescan', 'Custom']
    config_ui("jpeg program for optimizing jpeg file: ", values)
    cmd = input("jpeg_program (1-5): ")
    ext = config_decision(cmd, section, attribute, values, values[1], file)
    if ext == 'jpegoptim':
        jpeg_optim_quality = input("jpegoptim quality (0 - 100): ")
        config_set(section, 'jpgoptim_quality', jpeg_optim_quality, file)
    elif ext == values[4]:
        jpg_program = input("Your Custom jpg_program name: ")
        config_set(section, attribute, jpg_program, file)

    ####### Target png programs for optimizing png file:  ########
    section = 'IMAGE'
    attribute = 'png_program'
    values = ['pingo', 'optipng', 'advpng', 'pngout', 'Custom']
    config_ui("png program for optimizing png file: ", values)
    cmd = input("png_program (1-5): ")
    ext = config_decision(cmd, section, attribute, values, values[0], file)
    if ext == values[4]:
        png_program = input("Your Custom png_program name: ")
        config_set(section, attribute, png_program, file)

    ####### Target gif programs for optimizing gif file:  ########
    section = 'IMAGE'
    attribute = 'gif_program'
    values = ['gifsicle', 'gifsicle_lossy', 'Custom']
    config_ui("gif program for optimizing gif file: ", values)
    cmd = input("gif_program (1-5): ")
    ext = config_decision(cmd, section, attribute, values, values[1], file)
    gif_quality = input("gifsicle quality (0 - 100): ")
    config_set(section, 'gif_quality', gif_quality, file)
    if ext == values[2]:
        gif_program = input("Your Custom gif_program name: ")
        config_set(section, attribute, gif_program, file)

    ####### Target svg programs for optimizing svg file:  ########
    section = 'IMAGE'
    attribute = 'svg_program'
    values = ['svgcleaner', 'Custom']
    config_ui("svg program for optimizing svg file: ", values)
    cmd = input("svg_program (1-2): ")
    ext = config_decision(cmd, section, attribute, values, values[0], file)
    if ext == values[1]:
        svg_program = input("Your Custom svg_program name: ")
        config_set(section, attribute, svg_program, file)

    # cXXXXXXXXXXXXc
    with open(file, 'a') as fp:
        config.write(fp)
    return fp.close()


# print(config_set('SITE', 'CPU_ARCHITECTURE', '32'))
# print(config_get('SITE', 'CPU_ARCHITECTURE'))
