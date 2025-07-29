from pathlib import Path
from constants.text import DEFAULT_FILE_TEXT

class FileHandler:
    directories_map = dict()

    def __init__(self):
        self.path = Path()
        self.managed_directory = self.path.cwd()
        print(f"file path directory: {self.managed_directory}")

    def use_directory_mapping(self, dir_mapping):
        # handle the creation of folders if they need to be created
        self._handle_directory_mapping_folders(dir_mapping)
        
        # go through all files, move them to correct folders if one is specified

    def get_path(self) -> Path:
        return self.managed_directory

    def get_config_file(self):
        for filePath in self.path.iterdir():
            if filePath.name == "fm-config.txt":
                return filePath
        raise FileNotFoundError("Config not found")

    def create_config_file(self):
        p = Path("fm-config.txt")
        with p.open("w"):
            p.write_text(DEFAULT_FILE_TEXT)

    def _handle_directory_mapping_folders(self, dir_mapping):
        p = Path()

        # iterate through folders in the config, and see if they exist in directory
        for dir in dir_mapping:
            new_dir = Path(f'{p.cwd()}/{dir}')
            new_dir.mkdir(parents=False, exist_ok=True)
            print(new_dir)