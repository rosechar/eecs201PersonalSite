from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get("https://rosechar.github.io/updates")
updates = driver.find_elements(By.ID, 'update')
links = driver.find_elements_by_link_text('read...')
for update in updates:
    print(update.text.split('\n')[0])
for link in links:
    url = link.get_attribute('href')
    driver2 = webdriver.Chrome()
    driver2.get(url)
    if ("404" in driver2.page_source):
        print('this url is invalid:' + url)
        driver2.close()
        driver.close()
        exit(1)
    driver2.close()
driver.close()