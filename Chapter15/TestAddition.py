import unittest

class TestAddition(unittest.TestCase):
    def setUp(self):
        print('Setting up the test')

    def tearDown(self):
        print('Tearing down the test')

    def test_twoPlusTwo(self):
        total = 2 + 2
        self.assertEqual(4, total)
    def test_threePlusThree(self):
        total = 3 + 3
        self.assertEqual(6, total)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)



