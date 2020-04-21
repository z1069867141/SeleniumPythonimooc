import unittest
import os

class Runcase(unittest.TestCase):
    def test_case01(self):
        case_path = os.path.join(os.getcwd(),'case')
        suit = unittest.defaultTestLoader.discover(case_path,'unittest*.py')
        unittest.TextTestRunner().run(suit)


if __name__ == "__main__":
    unittest.main()