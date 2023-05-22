import controllers.wearController as WearModel
import sys

### getWearNameByID
res1 = WearModel.getWearNameByID(0)
res2 = WearModel.getWearNameByID(1)
if res1 != 'Factory New':
    sys.exit("TEST FAILED")
if res2 != 'Minimal Wear':
    sys.exit("TEST FAILED")

### getWearFloatMinMaxByID
res = WearModel.getWearFloatMinMaxByID(1)
if res != [0.07, 0.15]:
    sys.exit("TEST FAILED")

### getWearFloatMinMaxByWearName
res = WearModel.getWearIDByWearName('Minimal Wear')
if res != 1:
    sys.exit("TEST FAILED")










print("WearModelTest PASSED")