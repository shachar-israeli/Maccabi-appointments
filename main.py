
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options



def functionA():
	PATH = "C:\\Users\shach\\OneDrive\\Desktop\\selenuim"

	driver = webdriver.Chrome(PATH + "\\chromedriver.exe")
	# driver.get("https://www.maccabi4u.co.il/14-he/Maccabi.aspx")
	driver.get("https://techwithtim.net")

	# print(driver.title[::-1])
	print(driver.title)

	#search = driver.find_element_by_id("ctl00_ucNavigationBar_ucNavigationBarAreaLeft_ancOnline")
	search = driver.find_element_by_name("s")
	search.send_keys("test")
	search.send_keys(Keys.RETURN)  # press click

	"""
	wait for load what you want
	"""
	try:
		main = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.ID, "main"))
		)

		articles = main.find_elements_by_tag_name("article")
		for article in articles:
			header = article.find_elements_by_class_name("entry-summary")
			print(header.text)

	except Exception as e:
		print(e)

	print(main.text)
	#driver.quit()


def functionB():
	PATH = "C:\\Users\shach\\OneDrive\\Desktop\\selenuim"

	chrome_options = Options()
	chrome_options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(PATH + "\\chromedriver.exe",chrome_options=chrome_options)
	driver.get("https://techwithtim.net/")

	try:
		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located(
				(By.LINK_TEXT, "Python Programming"))
		)
		print(element.text)
		element.click()

		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located(
				(By.LINK_TEXT, "Beginner Python Tutorials"))
		)
		print(element.text)
		element.click()


		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located(
				(By.ID, "sow-button-19310003"))
		)
		print(element.text)
		element.click()

	except Exception as e:
		print("222")
		print(e)


def login_to_maccabi(driver,username,password):

	driver.get("https://www.maccabi4u.co.il/")
	try:
		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located(
				(By.LINK_TEXT, "כניסה ל online"))
		)
		element.click()
		print("switching to the open tab")
		driver.switch_to.window(driver.window_handles[-1])

		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located(
				(By.ID, "identifyWithPasswordCitizenId"))
		)
		element.send_keys(username)

		element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located(
				(By.ID, "password"))
		)
		print(element.text)
		element.send_keys(password)

		driver.find_element_by_class_name("validatePassword").click()

		return driver
	
	except Exception as e:
		print("error in login function")
		print(e)

def search_doctor(driver,doctorFirstName,doctorLastName,city):

	try:

		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ctl00_wcSiteHeaderLobby1_wcSiteHeaderNavigationMenu_rptNavigationMenuHeader_ctl02_lnkHref"))	)
		print(element.text)
		element.click()

		print("gggg")

		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "doctors"))	)
		print(element.text)
		time.sleep(2)
		element.click()

		print("filling deatils")														
		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "doctorLastName"))	)
		element.send_keys(doctorLastName)

		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "doctorFirstName"))	)
		element.send_keys(doctorFirstName)

		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtCities"))	)
		element.send_keys(city)

		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lnkSearch"))	)

		element.click()
		
		print("get info from table:")

		time.sleep(2)

		# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "row"))	)
		# cells =  element.find_elements_by_css_selector("td")
		# print(cells[3].text)

		rows = driver.find_elements_by_class_name("row")
		for row in rows:
			cells =  row.find_elements_by_css_selector("td")
			if cells[3].text:
				print("The closest appointment that available:")
				print(cells[3].text)

	
	except Exception as e:
		print("error in search_doctor function")
		print(e)


if __name__ == '__main__':
	#functionB()
	PATH = "C:\\Users\shach\\OneDrive\\Desktop\\selenuim"
	chrome_options = Options()
	chrome_options.add_argument("--headless")  
	chrome_options.add_experimental_option("detach", True)
	driver = webdriver.Chrome(PATH + "\\chromedriver.exe",chrome_options=chrome_options)

	userID = "20333111"
	password = "yourMaccabiPassword"
	driver = login_to_maccabi(driver,userID,password)

	#search_doctor(driver, doctorFirstName = "גנאדי" , doctorLastName = "יודקביץ" , city = "ירושלים")
	# search_doctor(driver, doctorFirstName = "טים" , doctorLastName = "יעקבי" , city = "ירושלים")
	search_doctor(driver, doctorFirstName = "מריאן" , doctorLastName = "כץ" , city = "ירושלים")
	
