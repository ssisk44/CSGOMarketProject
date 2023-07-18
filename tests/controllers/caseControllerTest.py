from controllers.caseController import *
import unittest

class CaseControllerTest(unittest.TestCase):
    res1 = getAllContainerNames(1)
    if len(res1) != 37:
        print("TEST FAILED")

    res2 = getAllContainerNames()
    if len(res2) != 76:
        print("TEST FAILED")


if __name__ == '__main__':
    unittest.main()