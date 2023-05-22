import os
import time
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import sys
import tools.fileHandler as FileHandler
import tools.PriceHandler as PriceHandler

wearArray = [
    'Factory New',
    'Minimal Wear',
    'Field-Tested',
    'Well-Worn',
    'Battle-Scarred'
]
wearRangeMap = {
            'Factory New': [0.00, 0.0699999999999999999999999999999999999],
            'Minimal Wear': [0.07, 0.149999999999999999999999999999999999],
            'Field-Tested': [0.15, 0.379999999999999999999999999999999999],
            'Well-Worn': [0.38, 0.449999999999999999999999999999999999],
            'Battle-Scarred': [0.45, 1.00]
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

def getFloatCapsByWeaponNameSkinName(weaponName, skinName, pathToFloatCaps):
    floatArr = pd.read_csv(pathToFloatCaps).to_numpy().tolist()
    for floatEntry in floatArr:
        if weaponName == floatEntry[0] and skinName == floatEntry[1]:
            return [floatEntry[3], floatEntry[4]]


def getTradeUpFloat(outcomeWeaponName, outcomeSkinName, tradeUpAverageFloat: float):
    floatRange = getFloatCapsByWeaponNameSkinName(outcomeWeaponName, outcomeSkinName, '../tmp/Float/floatCaps.csv')
    newFloat = (tradeUpAverageFloat * (floatRange[1] - floatRange[0])) + floatRange[0]
    for wear in wearArray:
        wearRange = wearRangeMap[wear]
        wearMin = wearRange[0]
        wearMax = wearRange[1]
        if wearMin <= newFloat <= wearMax:
            return wear

def getAverageValueOfTradeUp(priceMap, uniqueWeapons, averageFloat):
    profit = 0
    for weapon in uniqueWeapons:
        resultTradeUpWear = getTradeUpFloat(weapon[0], weapon[1], averageFloat)
        price = priceMap[weapon[1]][resultTradeUpWear]
        profit += price
    averageProfit = profit / len(uniqueWeapons)
    return averageProfit
