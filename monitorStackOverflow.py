import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

############################################################################################################
# Configurations
############################################################################################################
# wait for an element to be available (seconds)
IMPLICIT_WAIT = 10

# Sleep duration after every click event (seconds)
SLEEP_DURATION = 1

# Duration (in seconds) to wait before page refresh
REFRESH_WAIT_TIME = 12 * 60 * 60;

# URL
STACK_OVERFLOW_URL = r"https://stackoverflow.com"

# X-Paths
loginButtonXpath = r'/html/body/header/div/ol/li[6]/a[1]'
loginWithGoogleButtonXpath = r'//*[@id="openid-buttons"]/button[1]'
emailTextXpath = r'//*[@id="identifierId"]'
emailNextButtonXpath = r'//*[@id="identifierNext"]/span/span'  
pwdTextXpath = r'//*[@id="password"]/div[1]/div/div[1]/input'
pwdNextButtonXpath = r'//*[@id="passwordNext"]/span/span' 
profileXpath = r'/html/body/header/div/ol/li[2]/a'
reputationXpath = r'//*[@id="top-cards"]/aside[1]/div/div/div[1]/div[1]/div[1]/span[1]'
reputationIncreaseXpath = r'//*[@id="top-cards"]/aside[1]/div/div/div[1]/div[1]/div[1]/span[2]'

# Path of chromedriver
chromeDriverPath = r"C:\Users\m0pxnn\Documents\Selenium\ChromeDriver\chromedriver.exe" 

# Credentials
userEmail = "userEmail@gmail.com"
userPassword = "userPassword"

############################################################################################################
# Main
############################################################################################################
os.environ["webdriver.chrome.driver"] = chromeDriverPath
browser = webdriver.Chrome(executable_path=chromeDriverPath)
browser.implicitly_wait(IMPLICIT_WAIT)

#browser.set_window_position(-2000, 0)
browser.set_window_position(-2000, 0)
print ("Accessing ", STACK_OVERFLOW_URL)
browser.get(STACK_OVERFLOW_URL)
time.sleep(SLEEP_DURATION) 

print ("Login")
loginButton = browser.find_element(By.XPATH, loginButtonXpath);
loginButton.click()
time.sleep(SLEEP_DURATION)

print ("Login using Google credentials")
loginWithGoogleButton = browser.find_element(By.XPATH, loginWithGoogleButtonXpath);
loginWithGoogleButton.click()
time.sleep(SLEEP_DURATION)

print ("Enter eMail")
emailText = browser.find_element(By.XPATH, emailTextXpath);
emailText.send_keys(userEmail)
time.sleep(SLEEP_DURATION)

print ("Click Next button")
emailNextButton = browser.find_element(By.XPATH, emailNextButtonXpath);
emailNextButton.click()
time.sleep(SLEEP_DURATION)

print ("Enter password")
pwdText = browser.find_element(By.XPATH, pwdTextXpath);
pwdText.send_keys(userPassword)
time.sleep(SLEEP_DURATION)

print ("Click Next button")
pwdNextButton = browser.find_element(By.XPATH, pwdNextButtonXpath);
pwdNextButton.click()
time.sleep(SLEEP_DURATION)

print ("\n** %s Logged In ***" % userEmail)

print ("Go to profile")
profile = browser.find_element(By.XPATH, profileXpath);
profile.click()
time.sleep(SLEEP_DURATION)

nextRefresh = datetime.timedelta(seconds=REFRESH_WAIT_TIME)
print ("Page will be refreshed next after", nextRefresh)

while (1):       
    reputation = browser.find_element(By.XPATH, reputationXpath);
    reputationIncrease = browser.find_element(By.XPATH, reputationIncreaseXpath);
    
    print("Timestamp  : ", datetime.datetime.now());
    print("Reputation : ", reputation.text)
    print("Change     : ", reputationIncrease.text)
    
    time.sleep(REFRESH_WAIT_TIME);
    print("\nRefreshing page...")
    browser.refresh();