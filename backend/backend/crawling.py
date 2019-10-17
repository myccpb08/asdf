import requests
import math
from bs4 import BeautifulSoup


def getList(url):
    resp = requests.get(url)
    html = BeautifulSoup(resp.content, 'html.parser')
    lis = html.findAll('dt', {'class': 'tit'})

    print("{}페이지// url:{}".format(page, url))
    for li in lis:
        codeNum = li.find('a').get('href')[20:-3]
        getService("http://www.bokjiro.go.kr/welInfo/retrieveGvmtWelInfo.do?searchIntClId=&welInfSno={}".format(codeNum))
        # print(codeNum)

def getService(url):
    print(url)



# test_url = "http://www.bokjiro.go.kr/welInfo/retrieveWelInfoDetail.do?welInfSno=95"    #상세보기
test_url="http://www.bokjiro.go.kr/welInfo/retrieveLcgWelInfoList.do?searchSidoCode=&searchCggCode=&searchIntClId=&searchCnDivCd=&searchCtgId=&searchGb=&searchText=&pageUnit=10"
resp = requests.get(test_url)
html = BeautifulSoup(resp.content, 'html.parser')
print(html)

#댓글 전체 수
commandTotal= int(html.find('strong', {'class':'point01'}).getText().replace(',',''))
#페이지 수
pages = math.floor(commandTotal/10)

page = 2
url = test_url + '&pageIndex=' + str(page)
getList(url)

# # 나머지 뺀 페이지
# for page in range(1, pages+1):
#     url = test_url + '&pageIndex=' + str(page)
#     getList(url)
#
# # 나머지 부분
# page = pages+1
# nmg = commandTotal-pages*10
# if nmg != 0:
#     url = test_url + '&pageIndex=' + str(page)
#     getList(url)



