import json

class FileManager:
    def load_data(self, filename):
        try:
            with open(filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(f"The file {filename} not found")
            return None

    def save_data(self, filename, data):
        try:
            with open(filename, "w") as file:
                file.write(data)
        except Exception as e:
            print(f"An error occurred while writing to the file {filename}: {e}")
        
    def read_json(self, json_file_path):
        try:
            with open(json_file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"The file {json_file_path} not found.")
            return None
        
    def write_json(self, list_of_dicts, json_file_path):
        pass
        # TODO:
        # Implement a process that writes a list of dictionaries from list_of_dicts to the `json_file_path` file

    def add_to_json(self, data, json_file_path):
        pass
        # TODO:
        # Implement a process that gets the dictionary in the data variable and adds it to the JSON `json_file_path`

            