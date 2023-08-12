from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()



driver.find_element(By.ID, "id")
driver.find_element(By.NAME, "name")
driver.find_element(By.XPATH, "xpath")
driver.find_element(By.LINK_TEXT, "link text")
driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")
driver.find_element(By.TAG_NAME, "tag name")
driver.find_element(By.CLASS_NAME, "class name")
driver.find_element(By.CSS_SELECTOR, "css selector")

