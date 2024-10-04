import myFunc
import unittest

class MyUnitTest(unittest.TestCase()):

    def myTest(self):
        self.assertEqual(myFunc(1,1),2)


if __name__ == '__main__':
    unittest.main()