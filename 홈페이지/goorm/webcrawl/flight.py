from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

basepath='./goorm/webcrawl/'
browser=webdriver.Chrome(basepath+'chromedriver_win32/chromedriver.exe')
browser.maximize_window()

url='https://flight.naver.com/flights/'
browser.get(url)

# 선택
browser.find_element_by_link_text('가는날 선택').click()

# 이번달 27 선택
browser.find_elements_by_link_text('29')[0].click()
browser.find_elements_by_link_text('30')[0].click()

time.sleep(2)

# 선택
browser.find_element_by_xpath('//*[@id="l_1"]/div/div[2]/a[2]').click()
time.sleep(2)

# 제주
browser.find_element_by_xpath('//*[@id="l_1"]/div/div[2]/div[2]/table[1]/tbody/tr[1]/td[1]/a').click()
time.sleep(2)

# 검색
browser.find_element_by_link_text('항공권 검색').click()

try:
    elem=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
except:
    browser.quit()

# 검색.
elem=browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
print(elem.text)

browser.quit()