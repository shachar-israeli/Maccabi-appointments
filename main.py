
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
from loginDetails import login_details

DEBUG_MODE = True
PATH = "C:\\Users\shach\\OneDrive\\Desktop\\selenuim\\Maccabi-appointments"

def print_steps(str):
    if DEBUG_MODE:
        print(str)

def init():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("detach", True)
    return webdriver.Chrome(PATH + "\\chromedriver.exe", chrome_options=chrome_options)


def login_to_maccabi(driver, username, password):

    driver.get("https://www.maccabi4u.co.il/")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "כניסה ל online")))
        element.click()
        print_steps("switching to the open tab")
        driver.switch_to.window(driver.window_handles[-1])

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "identifyWithPasswordCitizenId")))
        element.send_keys(username)

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(				(By.ID, "password"))		)
        print_steps(element.text)
        element.send_keys(password)

        driver.find_element_by_class_name("validatePassword").click()
        return driver

    except Exception as e:
        print("error in login function")
        print(e)

def search_doctor(driver, doctorFirstName, doctorLastName, city):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.ID, "ctl00_ctl00_wcSiteHeaderLobby1_wcSiteHeaderNavigationMenu_rptNavigationMenuHeader_ctl02_lnkHref"))	)
        print_steps(element.text)
        element.click()
        print_steps("clicked the search")

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "doctors"))	)
        print_steps(element.text)
        time.sleep(2)
        element.click()

        print_steps("filling deatils")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "doctorLastName"))	)
        element.send_keys(doctorLastName)

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "doctorFirstName"))	)
        element.send_keys(doctorFirstName)

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "txtCities"))	)
        element.send_keys(city)

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "lnkSearch"))	)
        element.click()
        print_steps("get info from table:")

        time.sleep(2)
        return driver

    except Exception as e:
        print("error in search_doctor function")
        print(e)

def get_nearest_appointment(driver):
    try:
        rows = driver.find_elements_by_class_name("row")
        for row in rows:
            cells = row.find_elements_by_css_selector("td")
            if cells[3].text:
                print("The closest appointment that available:")
                print(cells[3].text)

    except Exception as e:
        print("error in get_nearest_appointment:")
        print(e)    

if __name__ == '__main__':

    driver = init()
    userID, password = login_details()
    driver = login_to_maccabi(driver, userID, password)

    #search_doctor(driver, doctorFirstName = "גנאדי" , doctorLastName = "יודקביץ" , city = "ירושלים")
    # search_doctor(driver, doctorFirstName = "טים" , doctorLastName = "יעקבי" , city = "ירושלים")
    driver = search_doctor(driver, doctorFirstName="מריאן", doctorLastName="כץ", city="ירושלים")
    get_nearest_appointment(driver)