import unittest
from Commands import send

class test_send(unittest.TestCase):

    def setUp(self):
        self.send1 = send(self, "eonshik")
        self.send2 = send(self, "eonshik spykim2003" "-s")
        self.send3 = send(self, "-a")

    def test_name(self):
        self.assertEqual(self.send1.getAccountName(), "eonshik")

    def test_multiple_names(self):
        self.assertEqual(self.send2.getAccountNames(), "eonshik spykim2003")






if __name__ == '__main__':
    unittest.main()
