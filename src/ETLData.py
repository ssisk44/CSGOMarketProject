import os
from datetime import datetime
import numpy as np
import pandas as pd
import requests
import func.text


class ETLData:
    columnNames = [
        'nameID',
        'market_name',
        'market_hash_name',
        'border_color',
        'image',
        'latest',
        'min',
        'avg',
        'max',
        'mean',
        'median',
        'unstable',
        'unstable_reason',
        'first_seen'
    ]
    allItemTypesMap = {
        'knifeArr': [],
        'patchArr': [],
        'stickerArr': [],
        'graffitiArr': [],
        'weaponArr': [],
        'capsuleArr': [],
        'pinArray': [],
        'musicArr': [],
        'caseArr': [],
        'keyArr': [],
        'agentsArr': [],
        'passArr': [],
        'glovesArr': [],
        'packageArr': []
    }

    def runDBDataETLPipeline(self):
        ### receive all items market data
        allItemData = self.getSteamAPICSGOAllItemData()

        ### enter data into static_data.items
        allItemsSQL = ''
        allItemEntries = []
        for itemEntry in allItemData:
            self.sortItemsIntoItemTypeArray(itemEntry)




        ### create ItemsModel to get items from database
        # TO DO: create items->update prices

        ### grab case data from csgostash
        # if case already in database, dont grab it
        # enter data into static_data.cases

        ### grab weapon float data from csgostash
        # if weaponSkinFloat already in database, dont grab it
        #


    def getSteamAPICSGOAllItemData(self):
        # makes call to STEAM APIS to get data on every item in CS:GO with prices
        resSteamApisMapArray = [
            'nameID',
            'market_name',
            'market_hash_name',
            'border_color',
            'image',
            'prices',
        ]
        resPricesSteamApisMapArray = [
            'latest',
            'min',
            'avg',
            'max',
            'mean',
            'median',
            'unstable',
            'unstable_reason',
            'first_seen'
        ]
        res = requests.get('https://api.steamapis.com/market/items/730/?api_key=' + os.getenv('STEAM_APIS_KEY'))
        allItemsArr = []

        # Parse response json
        for item in res.json()['data']:
            itemArr = []
            for key in resSteamApisMapArray:
                if key == 'prices':
                    for keyPrices in resPricesSteamApisMapArray:
                        itemArr.append(item['prices'][keyPrices])
                else:
                    itemArr.append(item[key])
            allItemsArr.append(itemArr)

        # TO DO: Transition to logging
        print("API data obtained and sorted at:", datetime.now().strftime("%H:%M:%S"))
        return allItemsArr

    def sortItemsIntoItemTypeArray(self, item):
        """ ITEMTYPE SEARCH KEYWORDS
        Knife - Contains "Knife or Daggers"
        Sticker - Contains "Sticker, Legends, Challengers, Contenders"
        Graffiti - contains "Graffiti"
        Weapon - everything left
        Capsule- Contains "Capsule"
        Pin - Contains " Pin"
        Music Kit - Contains "Music Kit"
        Case - Contains "Case" without "Key"
        Agents - Need to create an Agent List
        Pass - Contains " Pass"
        Gloves - Contains "Gloves or Wraps"
        Collection Package - "Collection Package, Souvenir Package"
        """


        if func.text.checkIfContains(item[1], ' | '):
            itemMarketName = item[1]
            itemType = item[1].split(' | ')[0]

            ## add itemMedianPrice if it exists
            if item[10]:
                item = [item[0], itemType, item[1], round(float(str(item[10])), 2)]
            else:
                item = [item[0], itemType, item[1], '']

            ## determine the itemType and add entry to itemType group
            if func.text.checkIfContains(itemType, ['Knife', 'Daggers']):
                # only keep knives with wear in itemMarketName
                if func.text.checkIfContains(itemMarketName, ['(', ')']):
                    item[1] = 'Knife'
                    self.allItemTypesMap['knifeArr'].append(item)
                else:
                    return
            elif func.text.checkIfContains(itemType, ['Patch']):
                item[1] = 'Patch'
                self.allItemTypesMap['patchArr'].append(item)
            elif func.text.checkIfContains(itemType, ["Sticker", "Legends", "Challengers", "Contenders"]):
                item[1] = 'Sticker'
                self.allItemTypesMap['stickerArr'].append(item)
            elif func.text.checkIfContains(itemType, ["Graffiti"]):
                item[1] = 'Graffiti'
                self.allItemTypesMap['graffitiArr'].append(item)
            elif func.text.checkIfContains(itemType, ['Capsule']):
                item[1] = 'Capsule'
                self.allItemTypesMap['capsuleArr'].append(item)
            elif func.text.checkIfContains(itemType, [' Pin']):
                item[1] = 'Pin'
                self.allItemTypesMap['pinArray'].append(item)
            elif func.text.checkIfContains(itemType, ['Music Kit']):
                item[1] = 'Music Kit'
                self.allItemTypesMap['musicArr'].append(item)
            elif func.text.checkIfContains(itemType, ['Case']) and not func.text.checkIfContains(itemType, ['Key']):
                item[1] = 'Case'
                self.allItemTypesMap['caseArr'].append(item)
            elif func.text.checkIfContains(itemType, ['e Key']):
                item[1] = 'Key'
                self.allItemTypesMap['keyArr'].append(item)
            elif func.text.checkIfContains(itemType, [' Pass']):
                item[1] = 'Pass'
                self.allItemTypesMap['passArr'].append(item)
            elif func.text.checkIfContains(itemType, ['Gloves', 'Wraps']):
                item[1] = 'Gloves'
                self.allItemTypesMap['glovesArr'].append(item)
            elif func.text.checkIfContains(itemType, ["Collection Package", "Souvenir Package"]):
                item[1] = 'Package'
                self.allItemTypesMap['packageArr'].append(item)
            else:
                #
                if func.text.checkIfContains(itemMarketName, ['(', ')']):
                    item[1] = 'Weapon'
                    self.allItemTypesMap['weaponArr'].append(item)
                else:
                    item[1] = 'Agent'
                    self.allItemTypesMap['agentsArr'].append(item)

            """
            itemID  itemType  itemName  itemDesc  itemMarketName  itemMedianPrice
            """
            entry = []
            return entry
