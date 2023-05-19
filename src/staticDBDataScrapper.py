import os
import time
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
from tools.seleniumHelper import createNewChromeDriver
import database.query as Query
from models.CaseModel import getAllContainers
import sys
import tools.FileHandler as FileHandler
import tools.PriceHandler as PriceHandler

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
baseURL = 'https://csgostash.com/'
baseWeaponUrl = 'https://csgostash.com/weapon/'


# get all case/collection data
def caseLinksToDB():
    driver = createNewChromeDriver(False)
    driver.get(baseURL)
    driver.fullscreen_window()
    time.sleep(3)
    response = driver.execute_script('''
        const res = document.getElementsByClassName('dropdown-menu navbar-dropdown-small')[0].getElementsByTagName('li');
        let retArr = [];
        // remove last 3 non-case name items
        for(let i = 0; i < res.length - 3; i++){
            const li = res[i];
            const a = li.getElementsByTagName('a');
            if(a.length>0){
                const caseName = a[0].innerText;
                const href = a[0].getAttribute('href');
                const link = href ? href.trim() : '';
                retArr.push([caseName, link]);
            }
        }
        return retArr;
    ''')
    driver.close()
    sql = "INSERT INTO static_data.case (c_id, c_name, c_is_collection, c_link) VALUES "
    count = 0 ### FUTURE ERROR HERE
    for entry in response:
        count += 1
        sql += "('" + str(count) + "','" + entry[0] + "'," + "0,'" + entry[1] + "'),"
    sql = sql[:-1] + ';'
    Query.executeSingularQuery(sql)

def collectionsLinksToDB():
    driver = createNewChromeDriver(False)
    driver.get(baseURL)
    driver.fullscreen_window()
    time.sleep(3)
    response = driver.execute_script('''
            const res = document.getElementsByClassName('dropdown-menu navbar-dropdown-small')[1].getElementsByTagName('li');
            let retArr = [];
            for(let i = 0; i < res.length; i++){
                const li = res[i];
                const a = li.getElementsByTagName('a');
                if(a.length>0){
                    const collectionName = a[0].innerText;
                    const href = a[0].getAttribute('href');
                    const link = href ? href.trim() : '';
                    retArr.push([collectionName, link]);
                }
            }
            return retArr;
        ''')
    driver.close()
    sql = "INSERT INTO static_data.case (c_id, c_name, c_is_collection, c_link) VALUES "
    count = 39 ### FUTURE ERROR HERE
    for entry in response:
        count += 1
        sql += "('" + str(count) + "','" + entry[0] + "'," + "1,'" + entry[1] + "'),"
    sql = sql[:-1] + ';'
    Query.executeSingularQuery(sql)

def weaponSkinDataToDB():
    allCaseData = getAllContainers()

    allWeaponSkinEntryData = []
    for container in allCaseData:
        caseIndex = container[0]
        caseName = container[1]
        caseIsCollection = container[2]
        caseLink = container[3]


        print(container)

    sql = "INSERT INTO static_data.weaponSkins () VALUES "
    count = 0  ### FUTURE ERROR HERE
    for entry in allWeaponSkinEntryData:
        count += 1
        sql += "('" + str(count) + "','" + entry[0] + "'," + "1,'" + entry[1] + "'),"
    sql = sql[:-1] + ';'
# for each weapon in case hyperlink
weaponSkinDataToDB()
