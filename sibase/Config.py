import configparser

@staticmethod
def GetConfigValue(Section, Item):
    co = configparser.ConfigParser()
    co.sections()
    co.read('config.ini')
    return co[Section][Item]