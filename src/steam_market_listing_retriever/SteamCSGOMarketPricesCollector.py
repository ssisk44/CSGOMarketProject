import os
import sys
import time
import random
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tools.seleniumHelper import createNewChromeDriver

"""
This file is designed to conduct ACTUAL steam market listing price recon and retrieval
"""

# Variables
steam_login_link = 'https://store.steampowered.com/login/'
alphabetListLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetListCapital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def main():
    load_dotenv() # makes environment variables obtainable
    getMarketListings('UMP-45', 'Wild Child', True, 'Field-Tested')





def logIntoGmail():
    None


def logIntoSteamAccount():
    # getting driver and opening steam login site
    # need to open a new tab
    driver = createNewChromeDriver(extensions=True)
    driver.get(steam_login_link)
    time.sleep(5)

    # which account is this logging into
    accountUsername = os.getenv('STEAM_MAIN_ACCOUNT_USERNAME')
    accountPassword = os.getenv('STEAM_MAIN_ACCOUNT_PASSWORD')

    # input steam login information
    usernameInput = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[6]/div/div[1]/div/div/div/div[2]/div/form/div[1]/input')
    usernameInput.send_keys(accountUsername)
    time.sleep(getRandomSleepTime())
    passwordInput = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[6]/div/div[1]/div/div/div/div[2]/div/form/div[2]/input')
    passwordInput.send_keys(accountPassword)
    time.sleep(getRandomSleepTime())
    passwordInput.send_keys(Keys.RETURN)
    return driver

def getMarketListings(weaponName, skinName, statTrakBool, wear):
    driver = logIntoSteamAccount()
    # what if verification pops up?
    # if codeinsert class (newlogindialog_SegmentedCharacterInput_1kJ6q) is present
    # log into chrome
    # get first email
    # get code

    time.sleep(25)
    statTrakStr = ''
    if statTrakBool:
        statTrakStr = 'StatTrak™'

    weaponCountUrl = 'https://steamcommunity.com/market/search?appid=730&q='+ weaponName + '+' + statTrakStr + '+' + skinName
    driver.get(weaponCountUrl)
    time.sleep(getRandomSleepTime())
    weaponWearCounts= driver.execute_script('''
        names = document.getElementsByClassName('market_listing_item_name');
        var namesArr = [];
        for (var i=0, max=names.length; i < max; i++) {
            wearParens = names[i].innerText.split('(').at(-1);
            namesArr.push(wearParens.substring(1, wearParens.length-1));
        }
        
        counts = document.getElementsByClassName('market_listing_num_listings_qty');
        var countArr = [];
        for (var i=0, max=counts.length; i < max; i++) {
            countArr.push(counts[i].innerText);
        }
        
        return [namesArr, countArr];
    ''')
    print(weaponWearCounts[0], weaponWearCounts[1])

    # go to desired weapon listing url
    url='https://steamcommunity.com/market/listings/730/'+statTrakStr+' '+weaponName+' | '+skinName + ' (' + wear + ')?cc=us?l=english?query=&start=0&count=100'
    driver.get(url)
    time.sleep(5)

    def getListingsOnCurrentPage():
        floats = driver.execute_script('''
            const allFloats = document.getElementsByTagName('csgofloat-item-row-wrapper');
            let floatArr = []
            for (let i = 0; i < allFloats.length; i++) {
                let float = allFloats[i].shadowRoot.textContent;
                floatArr.push(float.substring(45,61));
            }
            return floatArr;
        ''')
        time.sleep(1)

        prices = driver.execute_script('''
            const allPrices = document.getElementsByClassName('market_listing_price market_listing_price_with_fee')
            let pricesArr = []
            for (let i = 0; i < allPrices.length; i++) {
                let price = allPrices[i].innerText;
                pricesArr.push(price);
            }
            return pricesArr;
        ''')
        time.sleep(1)

        itemsList = []
        for index in range(0, len(prices)):
            thisPriceStr = ''
            for symbol in prices[index]:
                if symbol in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    thisPriceStr += str(symbol)
            thisFloat = floats[index]
            thisPrice = str(thisPriceStr[0:-2])+'.'+str(thisPriceStr[-2:])
            itemsList.append([thisPrice, thisFloat])
        return itemsList
    res = getListingsOnCurrentPage()
    print(statTrakStr, weaponName, skinName, wear)
    print(res)


    # what if all the items arent on one page? or total element counter (obtained from first script) is greater than current element count (100s)
    # pagerElement = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div[2]/div[1]/div[4]/div[1]/div[3]/div[4]/div[3]/div[1]/span[3][@class="pagebtn"]')
    # print(pagerElement.text)




def getRandomSleepTime():
    return round(random.uniform(1.01, 4.00), 3)


main()