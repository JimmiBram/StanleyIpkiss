import configparser
import os.path

class Config:
    @staticmethod
    def GetConfigValue(Section, Item, DefaultValue=""):
        if os.path.isfile('config.ini') == False:
            raise Exception("Config.ini file missing")

        co = configparser.ConfigParser()
        co.sections()
        co.read('config.ini')
        if DefaultValue != "":
            return co.get(Section, Item, fallback=DefaultValue)
        else:
            if co.has_section(Section) == False:
                raise Exception("Section %s does not exist in Config.ini" % Section)

            if co.has_option(Section, Item) == False:
                raise Exception("Item %s does not exist in Config.ini" % Section)

            return co[Section][Item]
    
        