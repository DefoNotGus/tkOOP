#dbOOP
#By Gustavo
import os

class Dataset:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                pass  # Create an empty file if it doesn't exist

    def add_data(self, data):
        with open(self.filename, 'a') as f:
            f.write(data + '\n')

    def remove_data(self, data):
        with open(self.filename, 'r') as f, open(self.filename + '.tmp', 'w') as tmp:
            for line in f:
                if line.strip() != data:
                    tmp.write(line)
        os.replace(self.filename + '.tmp', self.filename)

    def modify_data(self, old_data, new_data):
        with open(self.filename, 'r') as f, open(self.filename + '.tmp', 'w') as tmp:
            for line in f:
                if line.strip() == old_data:
                    tmp.write(new_data + '\n')
                else:
                    tmp.write(line)
        os.replace(self.filename + '.tmp', self.filename)

    def get_data(self):
        with open(self.filename, 'r') as f:
            return f.readlines()