import configparser

class SiCore:
    def __init__(self, dbpath):
        self.instance = "NEW"
        self.dbpath = dbpath
        
    
    def _load_configurations(self):
        self.config = configparser.ConfigParser()
        self.config.sections()
        self.config.read('config.ini')
        self.dbpath = self.config["DEFAULT"]["DataPath"]

