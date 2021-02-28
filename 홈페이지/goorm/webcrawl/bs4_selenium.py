from selenium import webdriver
from selenium.webdriver.common.keys import Keys # key 입력.
import time

basepath='./goorm/webcrawl/'
browser=webdriver.Chrome(basepath+'chromedriver_win32/chromedriver.exe')

# browser.get('http://naver.com')

# browser.back()
# browser.forward()
# browser.refresh()

# 입력 클릭.
# elem=browser.find_element_by_id('query')
# elem.click()
# elem.send_keys('영화')
# elem.send_keys(Keys.ENTER)

# 주소
# elem=browser.find_elemnet_by_tag_name('a')

# for e in elem:
#     print(e.get_attribute('href')) # 주소
#     break

# xpath
browser.get('https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=d')
# elem=browser.find_element_by_class_name('link_txt')
# time.sleep(2)
elem=browser.find_element_by_xpath('//*[@id="randomCategoryCollDetail"]/div[2]/ol[1]/li[2]/div/span[2]/a')
time.sleep(2)
elem.click()

browser.close()

# time.sleep(2)
# browser.quit()
# browser.close()


# elem=browser.find_element_by_css_selector('#account > a').click()
# time.sleep(2)

# browser.find_element_by_css_selector('#id').send_keys('ckdckd01')
# # browser.find_element_by_css_selector('#id').clear()
# time.sleep(2)
# browser.find_element_by_css_selector('#pw').send_keys('bbqabc1236')
# time.sleep(2)

# browser.find_element_by_class_name('btn_global').click()

# time.sleep(5)

# # browser.page_source()
# browser.quit()


