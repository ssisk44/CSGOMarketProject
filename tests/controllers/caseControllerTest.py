from controllers.caseController import *

res1 = getAllContainerNames(1)
if len(res1) != 37:
    print("TEST FAILED")

res2 = getAllContainerNames()
if len(res2) != 76:
    print("TEST FAILED")