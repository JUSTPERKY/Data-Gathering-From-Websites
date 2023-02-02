from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

s = Service("C:/Users/USER/OneDrive/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service = s,options=chrome_options)

driver.get('https://coinmarketcap.com/')
time.sleep(2)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

driver.find_element(by=By.XPATH,value='//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[6]/div[1]/div/ul/li[10]').click()
time.sleep(2)
driver.find_element(by=By.XPATH,value='//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[6]/div[1]/div/ul/li[10]').click()
time.sleep(2)