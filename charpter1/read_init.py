import configparser
class ReadIni():
    def __init__(self):
        self.data = self.load_ini()

    def load_ini(self):
        cf = configparser.ConfigParser()
        cf.read("./config/LocalElement.ini")
        return cf

    def get_value(self,key):
        return self.data.get("element",key)

if __name__ == "__main__":
    read_ini = ReadIni()
    print(read_ini.get_value("username"))