#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep, gmtime, strftime
import os
import sys

f = open(".credentials", "r")
username = f.readline()
password = f.readline()

browser = webdriver.Firefox()
browser.get("https://login.bolha.com/")
sleep(0.1)


user_name=browser.find_element_by_xpath('//*[@id="username_"]')
password=browser.find_element_by_xpath('//*[@id="password_"]')
user_name.send_keys('beanonymous1997')
password.send_keys('oLqW9Ir0')
login_button = browser.find_element_by_xpath('//*[@id="signin_submit"]')
login_button.click()
print("Login complete!")
sleep(0.5)

def deactivate():
    browser.get("https://moja.bolha.com/oglasi")
    sleep(0.5)

    try:
        try:
            deactivate_all = browser.find_elements_by_xpath('/html/body/div[5]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/table/tbody/tr[7]/td/div/div[1]/input')[0]
        except:
            deactivate_all = browser.find_elements_by_xpath('/html/body/div[5]/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/table/tbody/tr[3]/td/div/div[1]/input')[0]
        deactivate_all.click()
        deactivate_button = browser.find_element_by_xpath('//*[@id="deactivateBulk"]')
        sleep(2)
        deactivate_button.click()
        sleep(2)
        browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/a[2]').click()
        browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/a').click()
        sleep(0.2)
        browser.find_element_by_xpath('/html/body/div[5]/header/div[3]/a/span').click()
        sleep(0.2)
        browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/a').click()
        print("all items disabled")
    except:
        print("No items to disable")


def sell_dragunov():
    
    browser.get('http://objava-oglasa.bolha.com/')
    browser.find_element_by_link_text("Rekreacija, šport").click()
    sleep(0.2)
    browser.find_element_by_link_text("Airsoft, paintball").click()
    sleep(0.2)
    browser.find_element_by_link_text("Puške").click()
    sleep(5)
    
    browser.find_element_by_xpath('/html/body/section/div/div[3]/div/table/tbody/tr[2]/td/div[3]/div[2]/div/div/div/div/div[4]/form').click()

    description = " Zaradi neuporabe prodajam 2 leti staro vzmetno airsoft puško SVD Dragunov in originalen daljnogled. Puška je 'ful metal' razen kopita in kopiška."
    description += " Puška in daljnogled bi potrebovala nekaj servisa, saj zaradi padca ne več tako natančna kot je bila. Zraven dodam še vrečko BB-jev. \n"
    description += "Prevzem možen  v Ljubljani \n Kontakt: +386 30 668 197 (Benjamin)"
    price = "120"
    title = 'Airsoft puška SVD Dragunov + daljnogled'


    title_box = browser.find_element_by_xpath('//*[@id="cNaziv"]')
    title_box.send_keys(title)
    sleep(0.2)

    description_box = browser.find_element_by_xpath('//*[@id="cOpis"]')
    description_box.send_keys(description)
    sleep(0.2)

    price_box = browser.find_element_by_xpath('//*[@id="nCenaStart"]')
    price_box.send_keys(price)
    sleep(0.2)

    offer_type = browser.find_element_by_xpath('//*[@id="OptProdamfix"]')
    offer_type.click()


    picture_box = browser.find_element_by_xpath('//*[@id="dragandrophandler"]/div[2]/div[2]/input')
    time = 1
    picture_box.send_keys('/home/benjamax/Desktop/178_1480066214_1.jpg')
    sleep(0.2)
    picture_box.send_keys('/home/benjamax/Desktop/19.6.2017-prakticni.jpg')

    while True:
        loading_image = browser.find_element_by_xpath('//*[@id="loader"]') 
        display_size = loading_image.size
        size = display_size.get('width')
   
        if size == 0:
            browser.find_element_by_xpath('//*[@id="step11"]').click()
            sleep(0.2)
            break
        else:
            status = "Uploading picture" + "." * time
            print(status)
            sys.stdout.write("\033[F") 
            time += 1
            sleep(1)

    button_next = browser.find_element_by_xpath('//*[@id="next"]')
    button_next.click()


    

def sell_lenovo():
    browser.get('http://objava-oglasa.bolha.com/')
    browser.find_element_by_link_text("Računalništvo").click()
    sleep(0.2)
    browser.find_element_by_link_text("Prenosni računalniki in oprema").click()
    sleep(0.2)
    browser.find_element_by_link_text("IBM, Lenovo").click()
    sleep(5)
    
    browser.find_element_by_xpath('/html/body/section/div/div[3]/div/table/tbody/tr[2]/td/div[3]/div[2]/div/div/div/div/div[4]/form').click()

    description = " Prodajam HP Pavilion G6: Procesor asdada adsadasdasdasa. \n ewqeqeqwe weqeq"
    price = "300"
    title = 'Lenovo g510 prenosnik'


    title_box = browser.find_element_by_xpath('//*[@id="cNaziv"]')
    title_box.send_keys(title)
    sleep(0.2)

    description_box = browser.find_element_by_xpath('//*[@id="cOpis"]')
    description_box.send_keys(description)
    sleep(0.2)

    price_box = browser.find_element_by_xpath('//*[@id="nCenaStart"]')
    price_box.send_keys(price)
    sleep(0.2)

    offer_type = browser.find_element_by_xpath('//*[@id="OptProdamfix"]')
    offer_type.click()


    picture_box = browser.find_element_by_xpath('//*[@id="dragandrophandler"]/div[2]/div[2]/input')
    time = 1
    picture_box.send_keys('/home/benjamax/Desktop/178_1480066214_1.jpg')
    sleep(0.2)
    picture_box.send_keys('/home/benjamax/Desktop/19.6.2017-prakticni.jpg')

    while True:
        loading_image = browser.find_element_by_xpath('//*[@id="loader"]') 
        display_size = loading_image.size
        size = display_size.get('width')
   
        if size == 0:
            browser.find_element_by_xpath('//*[@id="step11"]').click()
            sleep(0.2)
            break
        else:
            status = "Uploading picture" + "." * time
            print(status)
            sys.stdout.write("\033[F") 
            time += 1
            sleep(1)

    button_next = browser.find_element_by_xpath('//*[@id="next"]')
    button_next.click()






deactivate()
#sell_item()
#deactivate()

browser.close()