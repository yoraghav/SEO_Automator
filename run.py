import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Captaslicer
import cv2


sites = pd.read_csv('1.csv')
clients = pd.read_csv('todaysclients.csv')
clients

def Classified(i,j):
    try:
        s = "Success"
        codes = np.load('citycodes.npy',allow_pickle=True)
        city = clients.City[j]
        for tt in range(len(codes)):
            if(codes[tt][0]==city):
                citycode = codes[tt][1]
                break


        URL = sites.Url[i] + "index.php?view=post&cityid=" + str(citycode) + "&lang=en&catid=" + str(clients.Categorycode[j]) + "&subcatid=" +str(clients.Subcategorycode[j]) +  "&shortcutregion=0"

        driver = webdriver.Chrome()
        driver.get(URL)
        title = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,sites.Textbox[i]))
        )
        title.send_keys(clients.Title[j])
        desc = driver.find_element_by_xpath(sites.Descriptionbox[i])
        desc.send_keys(clients.Description[j])
        desc.send_keys(Keys.RETURN)
        desc.send_keys(clients.Link[j])
        email = driver.find_element_by_xpath(sites.emailbox[i])
        email.send_keys(clients.Email[j])
        flag=0
        ee=1
        while(flag==0):
                try:
                    captchaxpath = "//*[@id=\"content\"]/form/table[1]/tbody/tr[7]/td/table/tbody/tr["+str(ee+1)+"]/td[2]/img"
                    EC.presence_of_element_located((By.XPATH,captchaxpath))
                    captcha = driver.find_element_by_xpath(captchaxpath)
                    file = open("1.png", "wb")
                    file.write(captcha.screenshot_as_png)
                    file.close()
                    decoded = Captaslicer.main()
                    captchabox = driver.find_element_by_xpath(captchaxpath[:captchaxpath.find("img")] + "input")
                    captchabox.send_keys(decoded)
                    flag=1
                except:
                    ee+=1
                    if(ee>15):
                        s="failed"
                        flag=1
        check = driver.find_element_by_xpath("//*[@id=\"content\"]/form/table[3]/tbody/tr[3]/td/input")
        check.click()
        post = driver.find_element_by_xpath(sites.Postbutton[i])
        post.click()
        driver.close()
    except:
        s = "failed"

    print(s," : Link creation of client - ",clients.Sitename[j]," on URL - ",sites.Url[i])
    
for j in range(len(clients)):   
   for i in range(len(sites)):
       Classified(i,j)
