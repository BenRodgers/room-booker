#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from datetime import datetime, timedelta
from selenium.webdriver.support.select import Select
import time

#ChromeDriver
driver = webdriver.Chrome()
#Get URL for booking study room
driver.get("https://auth.uq.edu.au/idp/module.php/core/loginuserpass.php?AuthState=_27d25f50646299b675576623a0cfafc8b2c2bbf12e%3Ahttps%3A%2F%2Fauth.uq.edu.au%2Fidp%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Fsciauth.scientia.com%252FMetadata%252FSamlMetadata%26cookieTime%3D1559521197%26RelayState%3DTzRKnQV_FCBMYyqytruXA7FCYEPUNwqu-ttNxgKrgC0ajc5hnCc4b_EV8QSTjIpHLTWQVFhG4vGgW2Fkdl8g9gYzpYbG93wVqGCy61qSn5tZHVP4QkXnVq5vNraxnFdJFZfY1ko6xgQs8qN_J8yHdvwoxXPuDMTG1MKLMJ6D34d1nzW-OuKY41w_MvZ1f_XE3NvF_Mq2hvCFiKCPyNwXAEKyV4znrroOYjWfVYbMyazqK9Kh8C0iS05Nmiwpu1iSArK2gxvoykzHQREL5xm7qpFHx6ZKO8oPsbcHloThKDaggwhPxKc17e5j6B2owPbK3RriXTMwddtwgyll7vKzEy_OpUuqMJZY0xSsbkAK12u9yPR4NRNGz10xCVhm6_wgVIDfbLKLXcsG7UnBWARuxjCZW02KW02m9ZJfdXzruuJ6K5VLvXJhfzN2JOiUWNRUaczXw1p7RutFTSwEIzj9sv4kwyJokewcFSrKPYb_RmVv11hVfDH9w1KpoMIPyBBO")

try:
    #Get username/password from external file
    with open('config.json', 'r') as f:
        config = json.load(f)
    #Input the username/password
    driver.find_element_by_id("username").send_keys(config['user']['name'])
    driver.find_element_by_id("password").send_keys(config['user']['password'])
    driver.find_element_by_name("submit").click()

    #Click on library rooms
    element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="ember1099"]')))
    element.click()


    #Show more results
    element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="ember1460"]')))
    element.click()

    #Click on 303F
    element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="ember1709"]'))).click()

    #Day View
    element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="ember1893"]/div/div[1]/div[1]/button[3]'))).click()

    #Skip forward 8 days.

    for i in range(8):
        element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ember1893"]/div/div[1]/div[3]/button[2]'))).click()

    Bookingtime = datetime.now() + timedelta(days = 7)
    startHour = Bookingtime.hour
    endHour = startHour + 3

    #Start time tow
    row = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="ember1893"]/div/div[2]/div/ul/li[2]/div[1]/span[{0}]'.format((str(startHour+1)))))).click()

    #End Time
    select_end = Select(driver.find_element_by_xpath('//*[@id="ember2032"]/select'))
    select_end.select_by_index(endHour+1)

    #Write a booking title
    driver.find_element_by_xpath('//*[@id="ember1969"]/div/input').send_keys("Booking Team");

    book = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="ember2076"]/div/span'))).click()
    
    time.sleep(10);
    driver.quit();

#Quit if there are any issues
except:
    driver.quit();
