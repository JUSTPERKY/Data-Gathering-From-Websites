from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


s=Service('C:/Users/USER/OneDrive/Desktop/chromedriver.exe')

driver = webdriver.Chrome(service=s,options=chrome_options)
driver.maximize_window()

driver.get('https://coinmarketcap.com/currencies/polygon/historical-data/')

#The Below code is to accept cookie policy
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cmc-cookie-policy-banner__close"))).click()
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)
num=0
max_num=43
while num<max_num:
    driver.find_element(by=By.XPATH,value = '//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div/div[1]/p[1]/button').click()
    time.sleep(1)
    num+=1
    #print(num)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    if num == max_num:
        break
#After automation you can store the whole webpage as .html file
html = driver.page_source
with open('cmcpolygon.html','w',encoding='utf-8') as f:
    f.write(html)

