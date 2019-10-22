
import requests
import json
import math
from bs4 import BeautifulSoup

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def getList(url):
    resp = requests.get(url)
    html = BeautifulSoup(resp.content, 'html.parser')
    lis = html.findAll('dt', {'class': 'tit'})
    for li in lis:
        codeNum = li.find('a').get('href')[26:-2]
        # getService("http://www.bokjiro.go.kr/welInfo/retrieveGvmtWelInfo.do?searchIntClId=&welInfSno={}".format(codeNum)) #ui들어간거
        getService("http://www.bokjiro.go.kr/welInfo/retrieveWelInfoDetail.do?welInfSno={}".format(codeNum))

def getService(url):
    resp = requests.get(url)
    html = BeautifulSoup(resp.content, 'html.parser')
    print(url)
    print(html)

#카테고리 넣기!
def putCategory():
    test_url = "http://www.bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do?searchIntClId=01&pageUnit=10&pageIndex=1"
    resp = requests.get(test_url)
    html = BeautifulSoup(resp.content, 'html.parser')
    lis = html.find('div', {'class': 'catBoxIn'}).findAll('a')

    request_data = {'categories':[]}
    #url로 만들어서 날리기
    for li in lis:
        categoryNum = li.get('href')[29:-7]
        name = li.get('title')
        request_data['categories'].append({
            'id': categoryNum,
            'name': name
        })
        categoryCode.append(categoryNum)

    requests.post(API_URL + 'crawling/category/', data=json.dumps(request_data), headers=headers)



# categoryCode = []
# putCategory()

# categoryCode=["16"] #나중에 지우기
#
# for code in categoryCode:
#     test_url = "http://www.bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do?searchIntClId={}&pageUnit=10".format(code)
#     resp = requests.get(test_url)
#     html = BeautifulSoup(resp.content, 'html.parser')
#
#     #댓글 전체 수
#     commandTotal = int(html.find('em').getText()[6:-2].replace(',',''))
#     lis = html.find('div', {'class': 'catBoxIn'}).findAll('a')
#
#     #페이지 수
#     pages = math.floor(commandTotal/10)
#     # 나머지 뺀 페이지
#     for page in range(1, pages+1):
#         url = test_url + '&pageIndex=' + str(page)
#         getList(url)
#
#     # 나머지 부분
#     page = pages+1
#     nmg = commandTotal-pages*10
#     if nmg != 0:
#         url = test_url + '&pageIndex=' + str(page)
#         getList(url)

getService("http://www.bokjiro.go.kr/welInfo/retrieveWelInfoDetail.do?welInfSno=237")
getService("http://www.bokjiro.go.kr/welInfo/retrieveWelInfoDetail.do?welInfSno=315")






