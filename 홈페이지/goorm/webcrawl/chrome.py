from selenium import webdriver

options=webdriver.ChromeOptions()
options.headless=True
options.add_argument('window-size=1920x1080')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')

browser=webdriver.Chrome('./goorm/webcrawl/chromedriver_win32/chromedriver.exe',
options=options)

url='https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

elem=browser.find_element_by_css_selector('#detected_value > a')

print(elem.text)

browser.get_screenshot_as_file('./goorm/webcrawl/user-agent.png')

