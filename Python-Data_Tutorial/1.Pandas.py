import pandas as pd 
cctv_seoul = pd.read_csv("./data/01. CCTV_in_Seoul.csv", encoding='utf-8')
print(cctv_seoul.head()) #show first 5 line
print(cctv_seoul.columns)   #show first line
cctv_seoul.rename(columns={cctv_seoul.columns[0] : '구별'},inplace=True)
print(cctv_seoul.columns)  

# pop_seoul = pd.read_excel("./data/01. population_in_Seoul.xls", encoding='utf-8') # basic
pop_seoul = pd.read_excel('./data/01. population_in_Seoul.xls', header=2,parse_cols='B,D,G,J,N',encoding='utf-8') # add option
pop_seoul.rename(columns={pop_seoul.columns[0] : "구별",pop_seoul.columns[1]:'인구수',pop_seoul.columns[2]:'한국인',pop_seoul.columns[3]:'외국인',pop_seoul.columns[4]:'고령자'},inplace=True)
print(pop_seoul.head())

