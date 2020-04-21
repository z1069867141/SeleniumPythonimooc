import sys
sys.path.append("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2")
from util.excel_util import ExcelUtil
from keyword_selenium.actionMethod import ActionMethod

class KeywordCase(object):
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil("C:\\Users\\Akien\\Desktop\\测试练习笔记\\自动化\\charpter2\\config\\keyword.xls")
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                is_run = handle_excel.get_col_value(i,3)
                if is_run == "yes":
                    method = handle_excel.get_col_value(i,4)
                    send_value = handle_excel.get_col_value(i,5)
                    handle_value = handle_excel.get_col_value(i,6)
                    except_result_method = handle_excel.get_col_value(i,7)
                    except_result_value = handle_excel.get_col_value(i,8)
                    self.run_method(method,send_value,handle_value)    
                    if except_result_value != "":
                        except_value = self.get_except_result_value(except_result_value)
                        if except_value[0] == 'text':
                            result_value = self.run_method(except_result_method)
                            print(result_value)
                            print(except_value[1])
                            if except_value[1] in result_value:
                                handle_excel.write_value(i,"pass")
                                print("pass")
                            else:
                                handle_excel.write_value(i,'fail')
                                print("fail")
                        elif except_value[0] == "element":
                            result_value = self.run_method(except_result_method,except_value[1])
                            if result_value:
                                handle_excel.write_value(i,'pass')
                                print("pass")
                            else:
                                handle_excel.write_value(i,'fail')
                                print("fail")
                        else:
                            print("没有else")
                    else:
                        print("预期结果为空")

        # 拿到行数
        # 循环行数，去执行每一行的case
        # 是否执行
            # 拿到执行操作
            # 拿到操作值
            # 拿到输入数据
            # 是否有输入数据
                # 执行方法(输入数据，操作元素)
            # 没有输入数据
                # 执行方法（操作元素)

    # 获取预期结果值
    def get_except_result_value(self,data):
        return data.split("=")
                
    def run_method(self,method,send_value='',handle_value=''):
        #print(method,send_value,handle_value)
        method_value = getattr(self.action_method,method)
        if send_value != "" and handle_value != "":
            result_value = method_value(handle_value,send_value)
        elif send_value == "" and handle_value != "":
            result_value = method_value(handle_value)
        elif send_value != "" and handle_value == "":
            result_value = method_value(send_value)
        else:
            result_value = method_value()
        return result_value


if __name__ == "__main__":
    a = KeywordCase()
    a.run_main()
    # from selenium import webdriver
    # driver = webdriver.Chrome()
    # driver.get('https://www.incnjp.com/member.php?mod=jionxc')
    # print(driver.title)