from pathlib import Path

DEFAULT_FILE_TEXT = """
# Welcoem to the file handler template. 
# Between the [start] and [end] brackets, you can clarify which directories will handle specific file types.

# Use the following syntax:
# [start]
# name_of_folder <- [.file_type, .another_file_type]
# name_of_folder <- [.file_type, .another_file_type]
# [end] 

# The rest of the document will be parsable from here on out
# Lines with a # are ignored, please remove these for your directory structure entries. 

rules:
[start]
[end]"""

class FileHandler:
    sub_directories = []

    def __init__(self):
        self.path = Path()
        self.managed_directory = self.path.cwd()
        print(f"file path directory: {self.managed_directory}")

    def get_path(self) -> Path:
        return self.managed_directory

    def get_subdirs(self):
        for subdir in self.path.iterdir():
            if subdir.is_dir():
                self.sub_directories.append(subdir)

    def get_config_file(self):
        for file in self.path.iterdir():
            if file.name == "fm-config.txt":
                return file
        raise FileNotFoundError("Config not found")

    def create_config_file(self):
        p = Path("fm-config.txt")
        with p.open("w"):
            p.write_text(DEFAULT_FILE_TEXT)
