from selenium import webdriver
from selenium.webdriver.common.keys import Keys

while True:
    driver = webdriver.Chrome(r"C:\Users\Admin\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get("https://www.google.com")
    driver.find_element_by_name("q").send_keys("You just got hacked")
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')  
    driver.get("https://www.google.com")
    driver.find_element_by_name("q").send_keys("You just got hacked")
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')  

