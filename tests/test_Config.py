import unittest
from sibase.Config import Config

class test_Config(unittest.TestCase):
    def setUp(self):
        self.func = Config()
 
    def test_1(self):
        self.assertTrue(True)

    def test_2(self):
        self.assertGreaterEqual(int(Config.GetConfigValue("API", "PORT")), 1)

    def tearDown(self):
        print("GONE")
 
if __name__ == '__main__':
    unittest.main()