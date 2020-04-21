import json
class handle_json:
    def load_json(self):
        with open("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter1\\cookie.json") as fp:
            data = json.load(fp)
        return data

    def get_data(self):
        return self.load_json()
    def write_data(self,data):
        with open("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter1\\cookie.json","w")as fp:
            fp.write(json.dump)

if __name__ == "__main__":
    hand = handle_json()
    print(hand.get_data())