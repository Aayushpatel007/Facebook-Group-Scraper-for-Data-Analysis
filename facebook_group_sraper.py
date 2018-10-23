# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 11:03:13 2018

@author: aayush
"""


from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time
import csv 
import pandas as pd

usr = "_username_"

pwd = "_password_"
driver = webdriver.Firefox(executable_path='E:\\geckodriver.exe')

# or you can use Chrome(executable_path="/usr/bin/chromedriver")

driver.get("http://www.facebook.org")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
elem.click()
time.sleep(7)
# Enter the the facebook group link 

driver.get("https://www.facebook.com/groups/CipherApp/members/")
time.sleep(5)
i=0;
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
        ele=driver.find_elements_by_xpath("//div[@class='_60ri fsl fwb fcb']/a") 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(15)
        new_height = driver.execute_script("return document.body.scrollHeight")
        names=[]
        links=[]
        if new_height == last_height:
            for values in ele:
                    names.append(values.text)     
                    links.append(values.get_attribute('href'))
                    print(values.text)

                    print(values.get_attribute('href'))
                    i=i+1
                  
            print(i)
            
            break
            
        else:
            last_height = new_height
            
print(names)
print(links)
res=[names,links]
mydfpd=pd.DataFrame(res)
# SAVE FILE TO SPESIFIC DESTINATION

mydfpd.to_csv('E:\\ciphernew.csv',index=False,header=False)            
                                    