import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

user_name= "xyz@rediffmail.com"
password= "pass@123"
driver= webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element(By.ID,"email").send_keys(user_name)
driver.find_element(By.ID,"pass").send_keys(password)
driver.find_element(By.NAME,"login").send_keys(Keys.ENTER)
time.sleep(10)
print("Sample test case successfully completed")
