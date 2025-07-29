from pathlib import Path
import re

class ConfigParser:
    start_of_config = -1
    end_of_config = -1

    def __init__(self, config_file):
        self.config_file = config_file
        self._directory_mapping = dict()
        self.get_start_of_config()
        self.get_end_of_config()
        self._create_directory_mapping()

    def get_start_of_config(self):
        p = self.config_file
        with p.open() as f:
            for lineno, line in enumerate(f, start=1):
                if line.find("[start]") != -1 and not self._is_line_comment(line):
                    self.start_of_config = lineno
                    return
        raise ValueError("[start] not found in config")
    
    def get_end_of_config(self):
        p = self.config_file
        with p.open() as f:
            for lineno, line in enumerate(f, start=1):
                if line.find("[end]") != -1 and not self._is_line_comment(line):
                    self.end_of_config = lineno
                    return
        raise ValueError("[end] not found in config")

    def get_directory_mapping(self):
        return self._directory_mapping

    def _create_directory_mapping(self):
        p = self.config_file
        with p.open() as f:
            for lineno, line in enumerate(f, start=1):
                if lineno < self.start_of_config + 1:
                    continue;
                if lineno >= self.end_of_config:
                    return
                else:
                    directory = self._parse_directory_from_line(line)
                    file_types = self._parse_filetypes_from_line(line)
                    self._directory_mapping[directory] = set(file_types)


    def _is_line_comment(self, str):
        return str[0] == "#"

    def _parse_directory_from_line(self, str):
        stopping_point = str.find("<-")
        return str[0:stopping_point].strip()

    def _parse_filetypes_from_line(self, str):
        starting_point = str.find("[") + 1
        ending_point = str.find("]") 
        filetypes_str_value = str[starting_point:ending_point].strip()
        array_of_filetypes = re.split(r', ?', filetypes_str_value)
        return array_of_filetypes