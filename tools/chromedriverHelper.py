from selenium import webdriver


def createNewChromeDriver(extensions=True):
    # creates a new chromedriver instance with csgo float extensions
    DRIVER_PATH = '../chromedriver.exe'
    chrome_options = webdriver.ChromeOptions()

    # # load chrome account NOT WORKING
    # chrome_options.add_argument("--user-data-dir=C:/Users/samue/AppData/Local/Google/Chrome/User tmp/Profile 7/")

    # load csgo steam market extensions
    if extensions:
        chrome_options.add_extension('csgofloatmarketchecker.crx')
        chrome_options.add_extension('csgotradersteamtradeenhancer.crx')
        driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=chrome_options)
    else:
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    return driver
