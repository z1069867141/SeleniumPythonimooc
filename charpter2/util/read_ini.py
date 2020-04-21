import configparser

class ReadIni(object):
    def __init__(self,file_path=None,node=None):
        if file_path == None:
            self.file_path = "C:/Users/Akien/Desktop/测试练习笔记/自动化/charpter2/config/local_element.ini"
        else:
            self.file_path = file_path
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(self.file_path)

    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data

# cf = configparser.ConfigParser()
# cf.read(r"C:\Users\Akien\Desktop\测试练习笔记\自动化\charpter2\config\local_element.ini")
# print(cf.get("RegisterElement","user_name"))

if __name__ == "__main__":
    read_ini = ReadIni()
    print(read_ini.get_value("seccodeverify"))
    