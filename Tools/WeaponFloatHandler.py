import time
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import Tools.FileHandler as FileHandler
import Tools.PriceHandler as PriceHandler

wearArray = [
    'Factory New',
    'Minimal Wear',
    'Field-Tested',
    'Well-Worn',
    'Battle-Scarred'
]
wearRangeMap = {
    'Factory New': [0.000000000000000000000000000, 0.06999999284744262695312500],
    'Minimal Wear': [0.070000000298023223876953125, 0.14999999105930328369140625],
    'Field-Tested': [0.150000005960464477539062500, 0.37999999523162841796875000],
    'Well-Worn': [0.380000025033950805664062500, 0.44999998807907104492187500],
    'Battle-Scarred': [0.450000017881393432617187500, 1.00000000000000000000000000]
}
weaponArr = [
    'CZ75-Auto',
    'Desert Eagle',
    'Dual Berettas',
    'Five-SeveN',
    'Glock-18',
    'P2000',
    'P250',
    'R8 Revolver',
    'Tec-9',
    'USP-S',
    'AK-47',
    'AUG',
    'AWP',
    'FAMAS',
    'G3SG1',
    'Galil AR',
    'M4A1-S',
    'M4A4',
    'SCAR-20',
    'SG 553',
    'SSG 08',
    'MAC-10',
    'MP5-SD',
    'MP7',
    'MP9',
    'PP-Bizon',
    'P90',
    'UMP-45',
    'MAG-7',
    'Nova',
    'Sawed-Off',
    'XM1014',
    'M249',
    'Negev'
]
urlPrefix = 'https://csgostash.com/weapon/'

def getLinksOfWeapons(self):
    allWeaponsLinkArr = []
    for weapon in self.weaponArr:
        # Make a GET request to fetch the raw HTML content
        html_content = requests.get(self.urlPrefix + weapon).text

        # Parse the html content
        soup = BeautifulSoup(html_content, "lxml")
        allLinkDivs = soup.find_all("div", class_='well result-box nomargin')
        for entry in allLinkDivs:
            if entry.find('a'):
                skin = entry.find('h3').text
                links = entry.find_all("a", href=True)
                link = links[3]['href']
                allWeaponsLinkArr.append([weapon, skin, link])
    df = pd.DataFrame(data=np.array(allWeaponsLinkArr), columns=['Weapon', 'Skin', 'Link'])
    df.to_csv('Data/Float/floatLinks.csv', index=False)
    return allWeaponsLinkArr

def getFloatRangesOfAllWeapons():
    linkArr = pd.read_csv('../Data/Float/floatLinks.csv').to_numpy().tolist()
    newLinkArray = []
    for entry in linkArr:
        print("Beginning", entry[0], entry[1])
        link = entry[2]
        html_content = requests.get(link).text
        soup = BeautifulSoup(html_content, "lxml")
        floatCapsArr = soup.find_all('div', class_='marker-value cursor-default')
        entry.append(floatCapsArr[0].text)
        entry.append(floatCapsArr[1].text)
        newLinkArray.append(entry)
        print(entry, '\n')
        time.sleep(0)
    FileHandler.writeDFToFilepathAsCSV(newLinkArray, ['Weapon', 'Skin', 'Link', 'Low Float Cap', 'High Float Cap'], '../Data/Float/floatCaps.csv')

def convertArrayOfFloatBounds(floatArr, minOutcomeRange, maxOutcomeRange):
    # TO DO: AUTO FIND BOUNDS
    # only outcome float caps matter when trading up skins, return new skin float and wear
    newFloat = (sum(floatArr)/len(floatArr) * (maxOutcomeRange-minOutcomeRange)) + minOutcomeRange
    for wear in wearArray:
        wearRange = wearRangeMap[wear]
        wearMin = wearRange[0]
        wearMax = wearRange[1]
        if wearMin <= newFloat <= wearMax:
            return [newFloat, wear]

def getFloatCapsByWeaponNameSkinName(weaponName, skinName):
    floatArr = pd.read_csv('Data/Float/floatCaps.csv').to_numpy().tolist()
    for floatEntry in floatArr:
        if weaponName == floatEntry[0] and skinName == floatEntry[1]:
            return [floatEntry[3], floatEntry[4]]

def getTradeUpFloat(outcomeWeaponName, outcomeSkinName, tradeUpAverageFloat: float):
    floatRange = getFloatCapsByWeaponNameSkinName(outcomeWeaponName, outcomeSkinName)
    newFloat = (tradeUpAverageFloat * (floatRange[1] - floatRange[0])) + floatRange[0]
    for wear in wearArray:
        wearRange = wearRangeMap[wear]
        wearMin = wearRange[0]
        wearMax = wearRange[1]
        if wearMin <= newFloat <= wearMax:
            price = PriceHandler.getWeaponPrice(outcomeWeaponName, outcomeSkinName, wear)
            return [newFloat, wear, price]
