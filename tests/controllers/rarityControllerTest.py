import controllers.rarityController as RarityModel
import sys

res1 = RarityModel.getRarityNameByRarityID(0)
res2 = RarityModel.getRarityNameByRarityID(1)
if res1 != 'Covert':
    sys.exit("TEST FAILED")
if res2 != 'Classified':
    sys.exit("TEST FAILED")


res1 = RarityModel.getRarityIDByRarityName('Covert')
res2 = RarityModel.getRarityIDByRarityName('Consumer Grade')
if res1 != 0:
    sys.exit("TEST FAILED")
if res2 != 5:
    sys.exit("TEST FAILED")


print("RarityModelTest PASSED")