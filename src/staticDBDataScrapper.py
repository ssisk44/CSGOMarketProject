import os
import time
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
from tools.chromedriverHelper import createNewChromeDriver
import database.query as Query
from controllers.caseController import getAllContainers
from controllers.caseController import getContainerIndexByName
from controllers.rarityController import getRarityIDByRarityName
import sys
import tools.fileHandler as FileHandler
import tools.PriceHandler as PriceHandler

"""
    This file is meant to enter data into the db as a single time event... do not use after initial data population
"""
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
    count = 0  ### FUTURE ERROR HERE
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
    sql = "INSERT INTO static_data.cases (c_id, c_name, c_is_collection, c_link) VALUES "
    count = 39  ### FUTURE ERROR HERE
    for entry in response:
        count += 1
        sql += "('" + str(count) + "','" + entry[0] + "'," + "1,'" + entry[1] + "'),"
    sql = sql[:-1] + ';'
    Query.executeSingularQuery(sql)


def weaponSkinDataToDB(debug=False, specificCases=None, specificCount=0):
    allCaseData = getAllContainers()

    # allows for inserting previously erroring out entries :)
    newCaseData = []
    if specificCases is not None:
        # start at a specific case
        if len(specificCases) == 1:
            newCaseData = allCaseData[specificCases[0]:]
        # select specific cases to perform
        else:
            for index in specificCases:
                newCaseData.append(allCaseData[index])
        allCaseData = newCaseData


    count = 0
    if specificCount:
        count = specificCount

    for container in allCaseData:
        allContainerSkinEntryData = []
        ws_case_name = container[1]
        # isCase to determine Stattrak or Souvenir, case or collection
        isCase = not container[2]
        caseLink = container[3]
        print("Beginning data acquisition for:", ws_case_name)

        # visit case link and get each weapon link
        driver = createNewChromeDriver(False)
        driver.get(caseLink)

        if isCase:
            response = driver.execute_script('''
                const res = document.getElementsByClassName('col-lg-4 col-md-6 col-widen text-center');
                let retArr = [];
                for(let i = 0; i < res.length; i++){
                    const weapon = res[i];
                    let weaponInfo = weapon.getElementsByTagName('a');
                    if (weaponInfo.length > 0){
                        let knifeCardCheck = res[i].getElementsByClassName('stattrak');
                        if (knifeCardCheck.length > 0){
                            const weaponName = weaponInfo[0].innerHTML;
                            const weaponSkin = weaponInfo[1].innerHTML;
                            const weaponLink = weaponInfo[3].href;
                            const weaponRarity = weapon.getElementsByClassName('quality')[0].innerText.split(' ')[0];
                            retArr.push([weaponName, weaponSkin, weaponLink, weaponRarity]);
                        }  
                    }
                }
                return retArr;
            ''')
        else:
            response = driver.execute_script('''
                            const res = document.getElementsByClassName('col-lg-4 col-md-6 col-widen text-center');
                            let retArr = [];
                            for(let i = 0; i < res.length; i++){
                                const weapon = res[i];
                                let weaponInfo = weapon.getElementsByTagName('a');
                                // prevent empty weapon cards and souvenir cases 
                                if (weaponInfo.length > 3){
                                    const weaponName = weaponInfo[0].innerHTML;
                                    const weaponSkin = weaponInfo[1].innerHTML;
                                    const weaponLink = weaponInfo[3].href;
                                    const weaponRarity = weapon.getElementsByClassName('quality')[0].innerText.split(' ')[0];
                                    retArr.push([weaponName, weaponSkin, weaponLink, weaponRarity]);
                
                                }
                            }
                            return retArr;
                        ''')

        for weapon in response:
            ws_wp_name = weapon[0].replace("'", "")
            ws_name = weapon[1].replace("'", "")
            ws_link = weapon[2].replace("'", "")
            ws_r_id = getRarityIDByRarityName(weapon[3].replace("'", ""))
            driver.get(str(ws_link))

            floatCaps = driver.execute_script("""
                const floats = document.getElementsByClassName('marker-value-wrapper');
                const min = floats[0].innerText;
                const max = floats[1].innerText;
                return [min, max];
            """)
            ws_min_float = floatCaps[0]
            ws_max_float = floatCaps[1]

            weaponSkinData = driver.execute_script("""
                const res = document.getElementsByClassName('btn-group-sm btn-group-justified');
                let retArr = [];
                for(let i = 2; i < 12; i++){
                    let weaponWearEntry = res[i];
                    let entryText = weaponWearEntry.getElementsByTagName('span');
                    let entry = [];
                    for(let j = 0; j < entryText.length; j++){
                        const e = entryText[j].innerText;
                        console.log(entryText[j]);
                        entry.push(e);
                    }
                    retArr.push(entry);
                }
                return retArr;
            """)
            for weaponSkin in weaponSkinData:
                # some weapons dont have souv or stat options
                if len(weaponSkin) > 0:
                    # if the float is not possible skip this entry
                    ws_median_price = weaponSkin[-1].replace('$', '').replace(',', '')
                    if ws_median_price == 'Not Possible':
                        continue
                    elif ws_median_price == 'No Recent Price':
                        ws_median_price = '-0.01'

                    count += 1
                    ws_is_stattrak = 0
                    ws_is_souvenir = 0
                    if len(weaponSkin) == 3:
                        if isCase:
                            ws_is_stattrak = 1
                        else:
                            ws_is_souvenir = 1
                    ws_w_name = weaponSkin[-2]

                    if debug:
                        print([count, ws_case_name, ws_name, ws_wp_name, ws_w_name, ws_min_float, ws_max_float, ws_r_id,
                               ws_is_stattrak, ws_is_souvenir, ws_median_price])
                    allContainerSkinEntryData.append(
                        [count, ws_case_name, ws_name, ws_wp_name, ws_w_name, ws_min_float, ws_max_float, ws_r_id,
                         ws_is_stattrak, ws_is_souvenir, ws_median_price])

        def insertCaseDataIntoDB():
            sql = "INSERT INTO static_data.weapon_skins (ws_id, ws_case_name, ws_name, ws_wp_name, ws_w_name, ws_min_float, ws_max_float, ws_r_id, ws_is_stattrak, ws_is_souvenir, ws_median_price) VALUES "
            for entry in allContainerSkinEntryData:
                sql += "(" + str(entry[0]) + ",'" + str(entry[1]) + "','" + str(entry[2]) + "','" + str(
                    entry[3]) + "','" + str(
                    entry[4]) + "'," + str(entry[5]) + "," + str(entry[6]) + "," + str(entry[7]) + ",'" + str(
                    entry[8]) + "','" + str(entry[9]) + "','" + str(entry[10]) + "'),"

            sql = sql[:-1] + ';'
            Query.executeSingularQuery(sql)


        insertCaseDataIntoDB()
        print("Data successfully inserted for:", ws_case_name, "! \n")
        driver.close()

# same index as last entry in DB for parameter 3
weaponSkinDataToDB(False, [getContainerIndexByName('2021 Mirage')], 6122)
