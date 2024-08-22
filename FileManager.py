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
        try:
            with open(json_file_path, 'w') as file:
                json.dump(list_of_dicts, file, indent = 4)
        except Exception as e:
            print(f"An error occurred while writing JSON to the file {json_file_path}: {e}")
        
    def add_to_json(self, data, json_file_path):
        try:
            json_data = self.read_json(json_file_path)
            if json_data is None:
                json_data = []
            json_data.append(data)
            self.write_json(json_data, json_file_path)
        except Exception as e:
            print(f"An error occurred while adding data to the JSON file {json_file_path}: {e}")

        

            