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