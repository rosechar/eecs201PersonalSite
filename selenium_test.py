from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rosechar.github.io/updates")
updates = driver.find_elements(By.ID, 'update')
print(updates)
driver.close()