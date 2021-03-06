import unittest


class Test28(unittest.TestCase):
    def testcases(self):
        self.assertTrue(True and True)
        self.assertFalse(False and True)
        self.assertFalse(1 == 1 and 2 == 1)
        self.assertTrue("test" == "test")
        self.assertTrue(1 == 1 or 2 != 1)
        self.assertTrue(True and 1 == 1)
        self.assertFalse(False and 0 != 0)
        self.assertTrue(True or 1 == 1)
        self.assertFalse("test" == "testing")
        self.assertFalse(1 != 0 and 2 == 1)
        self.assertTrue("test" != "testing")
        self.assertFalse("test" == 1)
        self.assertTrue(not (True and False))
        self.assertFalse(not (1 == 1 and 0 != 1))
        self.assertFalse(not (10 == 1 or 1000 == 1000))
        self.assertFalse(not (1 != 10 or 3 == 4))
        self.assertTrue(not ("testing" == "testing" and "zed" == "Cool Guy"))
        self.assertTrue(1 == 1 and (not ("testing" == 1 or 1 == 0)))
        self.assertFalse("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
        self.assertFalse(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))


if __name__ == '__main__':
    unittest.main()
