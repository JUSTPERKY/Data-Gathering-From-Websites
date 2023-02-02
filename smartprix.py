from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


s=Service('C:/Users/USER/OneDrive/Desktop/chromedriver.exe')

driver = webdriver.Chrome(service=s,options=chrome_options)

driver.get('https://www.smartprix.com/tvs')


driver.find_element(by=By.XPATH,value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
#driver.find_element(by=By.XPATH,value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
#time.sleep(2)

old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.find_element(by=By.XPATH,value = '//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == old_height:
        break
    old_height=new_height

html = driver.page_source
with open('smartprixtv.html','w',encoding='utf-8') as f:
    f.write(html)