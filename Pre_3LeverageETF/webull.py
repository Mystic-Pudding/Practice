from selenium import webdriver
brower = webdriver.Chrome('./driver/chromedriver.exe')
nrgu = ["pxd","eog","vlo","mpc","oxy","xom","cvx","psx","cop","hes"]
sum = []

for i in range(len(nrgu)):
    brower.get("https://www.webull.com/quote/nyse-%s" % nrgu[i])
    try:
        search = brower.find_element_by_xpath("//*[@id='app']/section/div[1]/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/span")
        result = (search.text.split(" "))[2].split("%")
        result = float(result[0])
        sum.append(result)
    except:
        pass

brower.close()
result_sum = 0
for i in range(len(sum)):
    result_sum = result_sum + sum[i]
print("개별종목 등락률:",sum)

final_result = ((result_sum/len(sum))*3)

if(final_result>0):
    print("적정 상승률:",(final_result-0.3),"%")
else:
    print("적정 하락률:",(final_result+0.3),"%")
