import controllers.wearController as wC
import unittest

class WearControllerTest(unittest.TestCase):

    def testFindWearNameRangeFromValue(self):
        res = wC.findWearNameRangeFromValue(0.01)
        print(res)

        res = wC.findWearNameRangeFromValue(0.0699)
        print(res)

        res = wC.findWearNameRangeFromValue(0.07)
        print(res)

        res = wC.findWearNameRangeFromValue(0.071)
        print(res)










if __name__ == '__main__':
    unittest.main()