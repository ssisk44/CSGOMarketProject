from controllers.weaponSkinController import *
from controllers.rarityController import *

res1 = getAllSkinsForAContainer("Revolution Case")
if len(res1) != 166:
    print("TEST FAILED")

rarityID = getRarityNameByRarityID(4)
res2 = getEntriesByCaseAndRarity('Revolution Case', 4)

res3 = getUniqueWeaponEntriesByCaseAndRarity('Revolution Case', 4)
if len(res3) != 3:
    print("TEST FAILED")

res4 = getFloatRangeFromEntry([21, 'Revolution Case', 'Duality', 'AWP', 'Factory New', 0.0, 0.7, '4', 1, 0, 139.68])
if res4 != [0.0, 0.7]:
    print("TEST FAILED", res4)

entries = [[1, 'Revolution Case', 'Temukau', 'M4A4', 'Factory New', 0.0, 0.8, '5', 1, 0, 944.0], [2, 'Revolution Case', 'Temukau', 'M4A4', 'Minimal Wear', 0.0, 0.8, '4', 1, 0, 382.62], [3, 'Revolution Case', 'Temukau', 'M4A4', 'Field-Tested', 0.0, 0.8, '3', 1, 0, 90.0]]
res5 = getEntriesByWearLevel(entries, 'Factory New')
res6 = getEntriesByRarityLevel(entries, 4)


res7 = getEntries(entries, 5, 'Factory New', 0, 1)
print(res7)