
# import Import WebDriver from selenium and other dependencies 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://google.com/"

driver = webdriver.Chrome()  # create driver object for specific browser
driver.maximize_window()    # maximize the browser window
driver.get(url)             # hit the url

driver.find_element(By.NAME, "q").send_keys("Datantar") # Locate element and send the data for search
time.sleep(3)   
driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)  # Locate element button search and hit ENTER
time.sleep(3)

#driver.close()
print("Sample test case successfully completed")
