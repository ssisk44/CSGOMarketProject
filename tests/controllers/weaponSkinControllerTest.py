import unittest
from controllers.weaponSkinController import *
from controllers.rarityController import *
import tools.staticAssets as testAssets


class WeaponSkinControllerTest(unittest.TestCase):
    entry = testAssets.getTestWeaponSkinEntry()
    entries = testAssets.getTestWeaponSkinEntries()

    def testGetAllSkinsForAContainer(self):
        res = getAllSkinsForAContainer("Revolution Case")
        self.assertEqual(len(res), 166, "Should be 166")

    def testGetRarityNameByRarityID(self):
        rarityID = getRarityNameByRarityID(4)
        res = getEntriesByCaseAndRarity('Revolution Case', 4)
        self.assertEqual(len(res), 30, "Should be 30")
        self.assertEqual(res[0][7], '4', 'Should be 4')

    def testGetUniqueWeaponEntriesByCaseAndRarity(self):
        res = getUniqueWeaponEntriesByCaseAndRarity('Revolution Case', 4)
        self.assertEqual(len(res), 3, "Should be 3")

    def testGetFloatRangeFromEntry(self):
        res = getFloatRangeFromEntry(self.entry)
        self.assertEqual(res, [0.0, 0.7], "Should be [0.0, 0.7]")

    def testGetEntriesByWearLevel(self):
        res = getEntriesByWearLevel(self.entries, 'Factory New')
        self.assertEqual(len(res), 1, "Should be 1")

    def getEntriesByRarityLevel(self):
        res = getEntriesByRarityLevel(self.entries, 4)
        self.assertEqual(len(res), 30, "Should be 30")

    def testGetEntries(self):
        res = getEntries(self.entries, 5, 'Factory New', 0, 1)
        self.assertEqual(len(res), 1, "Should be 1")

    def testGetWeaponPrice(self):
        res = getPriceForWeapon('M4A4', "Temukau", "Factory New", 0, 1)
        self.assertEqual(res, 944.0, "Should be 944.0")


if __name__ == '__main__':
    unittest.main()
