from selenium import webdriver
import pyautogui
import time
userid_sendkey=input("user_id:")
userpw_sendkey=input("user_pwd:")

driver = webdriver.Chrome('./driver/chromedriver')
driver.get("https://dcid.dcinside.com/join/login.php?s_url=https%3A%2F%2Fgallog.dcinside.com%2Ftotocaca")
userid = driver.find_element_by_name("user_id")
userpw = driver.find_element_by_name("pw")
userid.clear()
userpw.clear()
userid.send_keys(userid_sendkey)
userpw.send_keys(userpw_sendkey)
btn=driver.find_element_by_class_name("btn_blue.small.btn_wfull")
btn.click()
driver.get("https://gallog.dcinside.com/totocaca/comment")
deletebtns = driver.find_elements_by_class_name("btn_delete.btn_svc.btn_lightgrey.smaller")
find_comment_number=driver.find_element_by_class_name("num").text
find_comment_number=find_comment_number.split('(')
find_comment_number=find_comment_number[1].split(')')
find_comment_number=int(find_comment_number[0])
for i in range(find_comment_number):
    deletebtn = driver.find_element_by_class_name("btn_delete.btn_svc.btn_lightgrey.smaller")
    deletebtn.click()
    pyautogui.press('enter')
    time.sleep(3
    
    )
