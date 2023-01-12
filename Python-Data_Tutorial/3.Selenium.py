from selenium import webdriver
from bs4 import BeautifulSoup
#원하는지역 현재날씨 검색
# search_weather=str(input("검색하고싶은 지역:"))
# driver = webdriver.Chrome('./driver/chromedriver')
# driver.get("https://www.naver.com") #chorme 브라우져에서 원하는 주소열기
# #driver.save_screenshot('./003.png') #현재화면 캡쳐
# search=driver.find_element_by_id("query")
# search.clear()
# search.send_keys(search_weather+'날씨')
# # xpath='//*[@id="search_btn"]'
# # driver.find_element_by_xpath(xpath=xpath).click()
# driver.find_element_by_id("search_btn").click() #xpath보다 이 방법이 간단하긴하지만 id가 겹칠땐 xpath가 좋을듯.
# html=driver.page_source
# soup=BeautifulSoup(html,'html.parser')
# raw_list=soup.find_all('p','info_temperature')
# print(search_weather+'현재날씨:'+raw_list[0].find('span',class_='todaytemp').get_text(),raw_list[0].find('span',class_='tempmark').get_text())
# driver.close()

#선거결과 확인
driver = webdriver.Chrome('./driver/chromedriver')
driver.get('http://info.nec.go.kr/')
driver.switch_to_default_content()
driver.switch_to_frame('main')  #frame 옮기는 부분인데 크롬개발자도구에서 source를 확인해보면 프레임을 확인해 볼 수 있음. 페이지가 프레임으로 되어있을떄 사용