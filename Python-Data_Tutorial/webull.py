from selenium import webdriver
# import pyautogui
driver = webdriver.Chrome('./driver/chromedriver')
driver.get('https://www.webull.com/quote/nyse-%s' % "xom")

search = driver.find_element_by_class_name("jssazadn6")
print(search)
# search = driver.find_element_by_class_name("inputId")
# search.send_keys("oxy")

# pyautogui.press("enter")
# userid = driver.find_element_by_id("name")
# userpw = driver.find_element_by_id("pwd")
# userid.clear()
# userpw.clear()
# userid.send_keys(userid_sendkey)
# userpw.send_keys(userpw_sendkey)
# btn = driver.find_element_by_class_name("btn_login")
# btn.click()
# driver.close()