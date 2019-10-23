
import requests
import json
import math
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import html

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

def unescape(text):
    text = text.strip()
    text = text.replace("&lt;","<")
    text = text.replace("&gt;", ">")
    text = text.replace("&quot;",'"')
    # text = text.replace("\r", '')
    # text = text.replace("\n", '')
    # text = text.replace("\t", '')
    return text

def getService(url):
    resp = requests.get(url)
    parser = BeautifulSoup(resp.content, 'html.parser')
    lis = parser.find('input', {'id': 'welInfDtlCn'})
    # lis = BeautifulSoup(HTMLParser().unescape(str(lis)), 'html.parser')
    lis = html.unescape(str(lis))
    print(lis)
    # print(lis)
    # lis = unescape(str(lis))
    # print(lis)
    lis = BeautifulSoup(lis, 'html.parser')
    # print(lis)
    target = lis.find('li', {'class':'first'}).find('ul', {'class':'bokjiBlit01'})

    # 지원대상
    targetStr=""
    for t in target:
        if "<ul" in str(t):
            temp = str(t).split("<ul")
            temp[0] = temp[0].strip()
            targetStr = targetStr + temp[0][4:]+"&"
        elif str(type(t)) == "<class 'bs4.element.Tag'>":
            targetStr = targetStr + t.getText()+"&"

    print(targetStr)

getService("http://www.bokjiro.go.kr/welInfo/retrieveGvmtWelInfo.do?welInfSno=315")

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

# getService("http://www.bokjiro.go.kr/welInfo/retrieveGvmtWelInfo.do?welInfSno=310")

# getService("http://www.bokjiro.go.kr/welInfo/retrieveWelInfoDetail.do?welInfSno=310")
# getService("http://www.bokjiro.go.kr/welInfo/retrieveGvmtWelInfo.do?searchIntClId=01&searchCtgId=999&welInfSno=237&pageGb=1&domainName=&firstIndex=10&recordCountPerPage=10&cardListTypeCd=list&welSrvTypeCd=01&searchGb=01&searchWelInfNm=&pageUnit=10&key1=list&stsfCn=")
# getService("http://www.bokjiro.go.kr/welInfo/retrieveGvmtWelInfo.do?welInfSno=237")





