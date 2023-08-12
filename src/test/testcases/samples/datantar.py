import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "http://datantar.link/"

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()
print(driver.title)
print("Sample test case successfully completed")
