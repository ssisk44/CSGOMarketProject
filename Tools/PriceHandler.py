import os
import sys
import pandas as pd

def getWeaponPrice(weaponName, skinName, wear, stattrakBool):
    #get weapon price with weapon name, skin, and wear
    weaponsArr = pd.read_csv('../Data/Weapons/weapons.csv').to_numpy().tolist()
    for entry in weaponsArr:
        if entry[0] == weaponName and entry[1] == skinName and entry[3] == wear and entry[5] == stattrakBool:
            return round(entry[16], 2)


def testGetWeaponPrice():
    median = 0.715 # will need to be manually changed
    testMedian = getWeaponPrice('Tec-', 'Avalanche', 'Battle-Scarred')
    print(median == testMedian)
