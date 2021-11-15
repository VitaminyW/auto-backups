import sqlite3


class Controller:
    def __init__(self,db_path):
        self.db = sqlite3.connect(db_path)

    def get_structure(self):
        pass

    def update_structure(self):
        pass

if __name__ == '__main__':
    pass