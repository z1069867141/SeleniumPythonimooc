import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
image = Image.open("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\code1.png")
text = pytesseract.image_to_string(image)
print(text)

# r = ShowapiRequest("http://route.showapi.com/1274-2","152723","6bf4ca3f0b344e0d82fb920553cc1230" )
# r.addFilePara("imgFile", r"C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\code1.png")
# res = r.post()
# text = res.json()["showapi_res_body"]["texts"][0]
# print(text) # 返回信息