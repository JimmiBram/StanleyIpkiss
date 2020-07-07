import configparser

class SICore:
    def __init__(self, dbpath = ""):
        self.dbpath = dbpath
        self._load_configurations()

#Properties

    # @property
    # def instance_name(self) -> str:
    #     return _get_instance_name(self.estimator)

#Internal Functions

    def _load_configurations(self):
        self.config = configparser.ConfigParser()
        self.config.sections()
        self.config.read('config.ini')
        if self.dbpath == "":
            self.dbpath = self.config["DEFAULT"]["DataPath"]


    def MaskValue(self, Value):
        return 123

    def MaskFloatValue(self, Value):
        return float(self.MaskData(Value))