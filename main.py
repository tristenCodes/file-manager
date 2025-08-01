import file_handler
import config_parser

handler = file_handler.FileHandler()


def main():
    handler.get_path()

    try:
        handler.get_config_file()
    except:
        handler.create_config_file()

    parser = config_parser.ConfigParser(handler.get_config_file())
    dir_mapping = parser.get_directory_mapping()
    handler.use_directory_mapping(dir_mapping)



if __name__ == "__main__":
    main()
