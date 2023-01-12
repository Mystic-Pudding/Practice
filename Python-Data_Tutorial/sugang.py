from selenium import webdriver
userid_sendkey = '2019038046'
userpw_sendkey = '2019038046'
driver = webdriver.Chrome('./driver/chromedriver')
driver.get('https://eisa.cbnu.ac.kr/atlecLogin')
userid = driver.find_element_by_id("name")
userpw = driver.find_element_by_id("pwd")
userid.clear()
userpw.clear()
userid.send_keys(userid_sendkey)
userpw.send_keys(userpw_sendkey)
btn = driver.find_element_by_class_name("btn_login")
btn.click()
driver.close()