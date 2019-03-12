import unittest
from Commands import send

class test_send(unittest.TestCase):

    def setUp(self):
        self.send1 = send("eonshik")
        self.send2 = send("eonshik spykim2003" "-s")
        self.send3 = send("-a")

    def test_name(self):
        self.assertEqual(self.send1.getAccountName(), "eonshik")

    def test_multiple_names(self):
        self.assertEqual(self.send2.getAccountNames(), "eonshik spykim2003")

    def test_speicific_option(self):
        with self.assertRaises(ValueError):






            if __name__ == '__main__':
                 unittest.main()
