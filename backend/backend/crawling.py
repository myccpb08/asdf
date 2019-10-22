
import requests
import json
from bs4 import BeautifulSoup

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def getList(url):
    resp = requests.get(url)
    html = BeautifulSoup(resp.content, 'html.parser')
    lis = html.findAll('dt', {'class': 'tit'})

    # print("{}페이지// url:{}".format(page, url))
    for li in lis:
        codeNum = li.find('a').get('href')[20:-3]
        getService("http://www.bokjiro.go.kr/welInfo/retrieveGvmtWelInfo.do?searchIntClId=&welInfSno={}".format(codeNum))
        # print(codeNum)

def getService(url):
    print(url)

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
        # category = Category.objects.create(id= categoryNum, name=name)
        # category.save()

    response = requests.post(API_URL + 'crawling/category/', data=json.dumps(request_data), headers=headers)
    print(response.text)



# test_url = "http://www.bokjiro.go.kr/welInfo/retrieveWelInfoDetail.do?welInfSno=95"    #상세보기
# test_url="http://www.bokjiro.go.kr/welInfo/retrieveLcgWelInfoList.do?searchSidoCode=&searchCggCode=&searchIntClId=&searchCnDivCd=&searchCtgId=&searchGb=&searchText=&pageUnit=10"
# categories = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16"]
# for category in categories:
#     test_url="http://www.bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do?searchIntClId={}&pageUnit=10&pageIndex=1".format(category)
# test_url="http://www.bokjiro.go.kr/welInfo/retrieveGvmtWelInfo.do?searchIntClId=01&searchCtgId=999&welInfSno=283&pageGb=1&domainName=&firstIndex=0&recordCountPerPage=10&cardListTypeCd=list&welSrvTypeCd=01&searchGb=01&searchWelInfNm=&pageUnit=10&key1=list&stsfCn="

#
# #댓글 전체 수
# commandTotal= int(html.find('strong', {'class':'point01'}).getText().replace(',',''))
# #페이지 수
# pages = math.floor(commandTotal/10)
#
# page = 2
# url = test_url + '&pageIndex=' + str(page)
# getList(url)

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

def main():
    putCategory()
    # test_url = "http://www.bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do?searchIntClId=01&pageUnit=10&pageIndex=1"
    # resp = requests.get(test_url)
    # html = BeautifulSoup(resp.content, 'html.parser')
    # lis = html.find('div', {'class': 'catBoxIn'}).findAll('a')

if __name__ == "__main__":
    main()

