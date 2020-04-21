import unittest


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有case执行之前的前置")
    
    @classmethod
    def tearDownClass(cls):
        print("所有case执行之后的后置")

    def setUp(self):
        print("case执行之前的前置")

    def tearDown(self):
        print("case执行之后的后置")

    @unittest.skip("不执行第一条")
    def test01(self):
        print("第一条case")

    def test02(self):
        print("第二条case")

if __name__ == "__main__":
    # nittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase("test01"))
    unittest.TextTestRunner().run(suite)