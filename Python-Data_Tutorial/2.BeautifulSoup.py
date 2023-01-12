from os import sep
import urllib
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlopen,Request
import re 
import pandas as pd 
from tqdm import tqdm_notebook
#html파일 tutorial
# page=open("./data/03. test_first.html","r").read()
# soup=BeautifulSoup(page, 'html.parser')
# print(soup.prettify()) #html all contents
# print(list(soup.children))
#print(soup.find_all('p'))
#soup.find_all('p', class_='outer-text') #class가 outer-text인 부분 찾음.
#soup.find_all(id="first") #id가 first인 태그 
#print(soup.find('p').next_sibling.next_sibling)#제일처음 나타난 p 태그를 찾아줌. 다음p 태그를 보고싶으면 next_sibling을 붙이면 됨.

# for each_tag in soup.find_all('p'): #태그안에 있는 택스트 가져오기 
#     print(each_tag.get_text())

# links=soup.find_all('a')  #링크주소 가져오기 
# for each in links:
#     href=each['href']
#     text=each.string
#     print(text+'->'+href)

#naver 환율정보 획득
# url="https://finance.naver.com/marketindex/"
# page=urlopen(url)
# soup=BeautifulSoup(page,'html.parser')
# # print(soup.prettify())
# print('USD:'+soup.find_all('span',class_='value')[0].string)

#Chicago 샌드위치 정보획득
# url=Request("https://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/",headers={'User-Agent': 'Mozilla/5.0'})
# page=urlopen(url)
# soup=BeautifulSoup(page,'html.parser')
# # print(soup.find_all('div',class_='sammy'))
# html=soup.find_all('div',class_="sammy")[0]
# # print(html.find(class_='sammyRank').get_text())
# # print(html.find(class_='sammyListing').get_text())
# # html_split=html.find(class_='sammyListing').get_text()
# # print(re.split(('\n|\r\n'),html_split))
# # print(html.find('a')['href'])
# rank=[]
# main_menu=[]
# cafe_name=[]
# url_add=[]
# list_soup=soup.find_all('div',class_='sammy')

# for item in list_soup:
#     rank.append(item.find(class_='sammyRank').get_text())
#     html_split=item.find(class_='sammyListing').get_text()
#     main_menu.append(re.split(('\n|\r\n'),html_split)[0])
#     cafe_name.append(re.split(('\n|\r\n'),html_split)[1])
#     url_add.append(html.find('a')['href'])
# # print(rank[:5],main_menu[:5],cafe_name[:5],url_add[:5])
# print(len(rank))
# data={"Rank":rank,"Menu":main_menu,"Cafe":cafe_name,"URL":url_add}
# df=pd.DataFrame(data,columns=['Rank','Cafe','Menu','URL'])
# df.to_csv('./test.csv',sep=',',encoding='UTF-8')

#NAVER 영화 평점 확인
url="https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20210526"
page=urlopen(url)
soup=BeautifulSoup(page,'html.parser')
# print(soup.find_all('div','tit5')[0].a.string) #제목
print(soup.find_all('td','point')[0].get_text())
date= pd.date_range('2021-05-01',periods=20,freq='D')
# print(date)
movie_date=[]
movie_name=[]
movie_point=[]
for today in tqdm_notebook(date):
    html= "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date={date}"
    response=urlopen(html.format(date=urllib.parse.quote(today.strftime('%Y%m%d'))))
    soup=BeautifulSoup(response,'html.parser')
    end=len(soup.find_all('td','point'))
    movie_date.extend([today for n in range(0,end)])
    movie_name.extend([soup.find_all('div','tit5')[n].a.string for n in range(0,end)])
    movie_point.extend([soup.find_all('td','point')[n].string for n in range(0,end)])
    print(movie_name)
movie=pd.DataFrame({'date':movie_date,'name':movie_name,'point':movie_point})
exit()