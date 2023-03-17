import Tools.ETLData as ETLData

############################################################################
############################### GAME PLAN ##################################
############################################################################
### Add Tooling
# market crawler/buying bot that takes floats into account

# Open new steam accounts per valuable trade
# Trade up bot -> https://automatetheboringstuff.com/chapter18/
# market listing bot w/ steam guard email code fetcher bot

### Continue Trade Up Analysis
# add float cap trade up transition into analysis

# avg max min roi based off of release date for cases

### Findings
# $$$$$$$$$$$ CASES - Chroma 2, PRISMA, Shattered Web

def main():
    ETLData.runEntireDataCollectionAndParsingPipeline()
    
main()

############################################################################
#################### OUTDATED STEAM COMMUNITY API STUFF ####################
############################################################################


###Constants
# driver = None
# STEAM_API_KEY = '66B184C28C703BF06E11FED3B5D07C5F'
# STEAM_MARKET_FEE = .1250
# EURO_TO_DOLLAR = 1.07
# # All Cases - https://www.csgodatabase.com/cases/
# CASES_FILEPATH = 'Data/Cases/'
# CASE_NAMES = [
#     "Revolution Case",
#     "Recoil Case",
#     "Dreams and Nightmares Case",
#     "Operation Riptide Case",
#     "Snakebite Case",
#     "Operation Broken Fang Case",
#     "Fracture Case",
#     "Prisma 2 Case",
#     "Shattered Web Case",
#     "CS20 Case",
#     "Prisma Case",
#     "Chroma Case",
#     "Chroma 2 Case",
#     "Chroma 3 Case",
#     "Clutch Case",
#     "CSGO Weapon Case",
#     "CSGO Weapon Case 2",
#     "CSGO Weapon Case 3",
#     "Danger Zone Case",
#     "eSports 2013 Case",
#     "eSports 2013 Winter Case",
#     "eSports 2014 Winter Case",
#     "Falchion Case",
#     "Gamma Case",
#     "Gamma 2 Case",
#     "Glove Case",
#     "Horizon Case",
#     "Huntsman Weapon Case",
#     "Operation Bravo Case",
#     "Operation Breakout Weapon Case",
#     "Operation Hydra Case",
#     "Operation Phoenix Weapon Case",
#     "Operation Vanguard Weapon Case",
#     "Operation Wildfire Case",
#     "Revolver Case",
#     "Shadow Case",
#     "Spectrum Case",
#     "Spectrum 2 Case",
#     "Winter Offensive Weapon Case"
# ]
# reverseRarityColorMap = {
#     'rgba(75, 105, 255, 1)': 'Mil_Spec Grade',
#     'rgba(136, 71, 255, 1)': 'Restricted',
#     'rgba(211, 44, 230, 1)': 'Classified',
#     'rgba(235, 75, 75, 1)': 'Covert',
#     'rgba(255, 215, 0, 1)': 'Exceedingly Rare'
# }
# weaponWearArr = [
#     'Battle-Scarred',
#     'Well-Worn',
#     'Field-Tested',
#     'Minimal%20Wear',
#     'Factory%20New'
# ]
#
#
# def makeNewWebScrapper():
#     # Chromedriver Selenium Head
#     DRIVER_PATH = os.getcwd() + '\chromedriver.exe'
#     driver: WebDriver = webdriver.Chrome(executable_path=DRIVER_PATH)
#     baseSteamMarketCSGOLink = 'https://steamcommunity.com/market/search?appid=730'
#
#
# def recordWeaponsFromCases(overwrite=False):
#     # Records a STATIC csv of all the weapons in each case
#     makeNewWebScrapper()
#     for case in CASE_NAMES:
#         if (overwrite is False and str(case + '.csv') not in os.listdir('Data/Cases/')) or (overwrite is True):
#             time.sleep(0)
#             searchSteamMarketplace(case)
#             time.sleep(0)
#             selectFirstSteamItem()
#             time.sleep(0)
#             gunsDiv = driver.find_element_by_xpath(
#                 '/html/body/div[1]/div[7]/div[2]/div[2]/div[4]/div/div[2]/div/div[2]/div/div/div[2]/div[3]').find_elements_by_tag_name(
#                 "div")
#             weaponsArray = []
#             for item in gunsDiv:
#                 gunDesc = item.text
#                 if any(x in gunDesc for x in ['|', '!']) and str(gunDesc + '.csv') not in os.listdir('Data/Cases/'):
#                     if '|' in gunDesc:
#                         gun = gunDesc.split('|')[0].strip()
#                         skin = gunDesc.split('|')[1].strip()
#                         rarity = reverseRarityColorMap[item.value_of_css_property('color')]
#                     else:
#                         rarity = reverseRarityColorMap[item.value_of_css_property('color')]
#                         if "Gloves" in gunDesc:
#                             gun = "Gloves"
#                             skin = "Gloves"
#                         else:
#                             gun = "Knife"
#                             skin = "Knife"
#                     weaponsArray.append([gun, case, skin, rarity])
#             df = pd.DataFrame(data=np.array(weaponsArray), columns=['Name', 'Case', 'Skin', 'Rarity'])
#             df.to_csv('Data/Cases/' + case + '.csv', index=False)
#
#
# def getWeaponPriceFromCases(overwrite=False, specificCase=''):
#     # Records a STATIC csv of all weapons
#     # TO DO: add individual case option
#     completedWeapons = pd.read_csv('Data/Weapons/weaponsMiscellaneous.csv').to_numpy()
#     completedWeaponsArr = []
#     weaponsColumns = [
#         'Name',
#         'Case',
#         'Skin',
#         'Rarity',
#         'Battle-Scared Price',
#         'Well-Worn Price',
#         'Field-Tested Price',
#         'Minimal Wear Price',
#         'Factory New Price',
#         'StatTrak™ Battle-Scared Price',
#         'StatTrak™ Well-Worn Price',
#         'StatTrak™ Field-Tested Price',
#         'StatTrak™ Minimal Wear Price',
#         'StatTrak™ Factory New Price'
#     ]
#     for weapon in completedWeapons:
#         entry = str(weapon[0] + ' ' + weapon[2])
#         completedWeaponsArr.append(entry)
#
#     if specificCase == '':
#         for file in os.listdir(CASES_FILEPATH):
#             print("Requesting resources for", file)
#             fileArr = pd.read_csv(str(CASES_FILEPATH) + file).to_numpy()
#             for line in fileArr:
#                 allSingleWeaponsDetails = []
#                 weaponName = line[0]
#                 case = line[1]
#                 skinName = line[2]
#                 rarity = line[3]
#                 if weaponName not in ['Gloves', 'Knife'] and str(
#                         weaponName + ' ' + skinName) not in completedWeaponsArr:
#                     weaponPrices = getPriceOfWeapon(weaponName, skinName)
#                     allDetailsArr = [weaponName, case, skinName, rarity]
#                     for price in weaponPrices:
#                         allDetailsArr.append(price)
#                     allSingleWeaponsDetails.append(allDetailsArr)
#                     df = pd.DataFrame(data=np.array(allSingleWeaponsDetails), columns=weaponsColumns)
#                     df.to_csv('Data/Weapons/weaponsMiscellaneous.csv', index=False, header=False, mode='a')
#                     print("Completed writing", weaponName, skinName, "for the", file.strip('.csv'), '\n')
#     else:
#         print("Requesting resources for", specificCase)
#         fileArr = pd.read_csv(str(CASES_FILEPATH) + specificCase).to_numpy()
#         for line in fileArr:
#             allSingleWeaponsDetails = []
#             weaponName = line[0]
#             case = line[1]
#             skinName = line[2]
#             rarity = line[3]
#             if weaponName not in ['Gloves', 'Knife'] and str(weaponName + ' ' + skinName) not in completedWeaponsArr:
#                 weaponPrices = getPriceOfWeapon(weaponName, skinName)
#                 allDetailsArr = [weaponName, case, skinName, rarity]
#                 for price in weaponPrices:
#                     allDetailsArr.append(price)
#                 allSingleWeaponsDetails.append(allDetailsArr)
#                 df = pd.DataFrame(data=np.array(allSingleWeaponsDetails), columns=weaponsColumns)
#                 df.to_csv('Data/Weapons/weaponsMiscellaneous.csv', index=False, header=False, mode='a')
#                 print("Completed writing", weaponName, skinName, "for the", specificCase.strip('.csv'), '\n')
#
#
# def getPriceOfWeapon(weaponName, skinName):
#     print("Getting prices for", weaponName, skinName)
#     priceArr = []
#
#     def getPrices(statrak=False):
#         statrakString = "StatTrak™"
#         for wear in weaponWearArr:
#             print(
#                 'https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=' + weaponName + "%20|%20" + skinName.replace(
#                     " ", '%20') + "%20(" + wear + ')')
#             if not statrak:
#                 queryResult = requests.get(
#                     'https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=' + weaponName + "%20|%20" + skinName.replace(
#                         " ", '%20') + "%20(" + wear + ')')
#             else:
#                 queryResult = requests.get(
#                     'https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=' + statrakString + '%20' + weaponName + "%20|%20" + skinName.replace(
#                         " ", '%20') + "%20(" + wear + ')')
#             if queryResult.status_code == 429:
#                 print("API REQUESTS OVERLOAD STATUS CODE 429")
#                 sys.exit()
#             if not queryResult.json()['success']:
#                 print("REQUEST JSON RETURNED UNSUCCESSFULLY, STATUS CODE:", queryResult.status_code, queryResult.json())
#                 # if queryResult.status_code != 429:
#                 #     # wait ten minutes if the request limit is broken
#                 #     time.sleep(600)
#                 # Could be a html link conversion error ex. Man-o'-war
#                 priceArr.append(None)
#                 time.sleep(30)
#                 continue
#
#             price = queryResult.json()['lowest_price']
#             if not statrak:
#                 print("Price for", weaponName, skinName, wear.replace('%20', " "), "is", price)
#             else:
#                 print("Price for", statrakString, weaponName, skinName, wear.replace('%20', " "), "is", price)
#             priceArr.append(price)
#             time.sleep(30)
#
#     getPrices(statrak=False)
#     getPrices(statrak=True)
#     return priceArr
#
#
# def selectFirstSteamItem():
#     driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[2]/div[1]/div[4]/div[2]/div[2]/div/div[1]/a[1]').click()
#
#
# def searchSteamMarketplace(searchString):
#     driver.get(baseSteamMarketCSGOLink)
#     marketSearchBar = driver.find_element_by_xpath(
#         '/html/body/div[1]/div[7]/div[2]/div[1]/div[4]/div[2]/div[1]/div/div/div/form/span/span/input[1]')
#     marketSearchBar.send_keys(searchString)
#     marketSearchBar.send_keys(Keys.RETURN)
#

main()
