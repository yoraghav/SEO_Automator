
#import urllib.request
#from selenium import webdriver
#
#driver = webdriver.Chrome()
#driver.get("https://nextfreeads.com/captcha.image.php?992")
#
#with open('1.png', 'wb') as file:
#   l = driver.find_element_by_xpath('//html/body/img')
#   file.write(l.screenshot_as_png)
#driver.close()

import requests
import Captaslicer
import cv2

for i in range(10):
    response = requests.get("https://nextfreeads.com/captcha.image.php?504")
    file = open("1.png", "wb")
    file.write(response.content)
    file.close()
    img = cv2.imread("1.png")
    print(Captaslicer.main(img))
    

