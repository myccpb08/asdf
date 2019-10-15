import requests
from bs4 import BeautifulSoup


# test_url="http://www.bokjiro.go.kr/welInfo/retrieveWelInfoDetail.do?searchIntClId=01&searchCnDivCd=&welInfSno=315&searchGb=01&searchText=&searchSidoCode=&searchCggCode=&searchCtgId=999&pageGb=1&pageUnit=10&pageIndex=1&domainName=&cardListTypeCd=list&welSrvTypeCd=01&age=&hirkQestId=&qestCric=&qestDsr=&searchCondition=&searchKeyword=&intClId=&region1=&region2=&occupation=&occupation4=&pref=&career=&education=&regDate=&searchGbn=&hdHelpLen=1&hdWelHelpId=div_doc_5594691&hdWelHelpNm=%EC%88%98%EA%B8%89%EA%B6%8C%EC%9E%90&hdWelHelpCn=%EC%82%AC%ED%9A%8C%EB%B3%B5%EC%A7%80%EC%82%AC%EC%97%85+%EA%B4%80%EB%A0%A8%EB%B2%95%EC%97%90+%EC%9D%98%ED%95%9C+%EA%B8%89%EC%97%AC+%EB%98%90%EB%8A%94+%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A5%BC+%EB%B0%9B%EC%9D%84+%EC%9E%90%EA%B2%A9%EC%9D%B4+%EC%9E%88%EB%8A%94+%EC%9E%90&hdChcNum=1&key1=315&stsfCn="
# test_url = "http://www.bokjiro.go.kr/welInfo/retrieveWelInfoDetail.do?welInfSno=95"
test_url = "http://www.bokjiro.go.kr/welInfo/retrieveWelInfoDetail.do?welInfSno=315"
resp = requests.get(test_url)
html = BeautifulSoup(resp.content, 'html.parser')
print(html)
# #댓글 전체 수
# pageTotal= html.find('div', {'class':'score_total'}).find('strong').findChildren('em')[1].getText()
# pageTotal = int(pageTotal.replace(',', ''))

# for i in range(1, 101):
#     url = test_url + '&page=' + str(i)
#     get_data(url)


