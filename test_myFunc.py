import myFunc
import unittest

class testCases(unittest.TestCase):

    def testMyFunc(self):
        self.assertEqual(myFunc.myFunc(1,1),2)


if __name__ == '__main__':
    unittest.main()