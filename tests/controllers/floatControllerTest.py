import unittest
import controllers.floatController as fC


class WeaponSkinControllerTest(unittest.TestCase):
    def testGetAdjustedFloat(self):
        res = fC.getAdjustedFloat(0, .8, 0.33)
        self.assertEqual(res, 0.264, "Should be 0.264")

        res = fC.getAdjustedFloat(.12, .26, 0.061)
        self.assertEqual(res, 0.13586, "Should be 0.13586")


if __name__ == '__main__':
    unittest.main()
