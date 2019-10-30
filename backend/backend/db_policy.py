from openpyxl import  load_workbook
import requests
import json

# API_URL = 'http://localhost:8000/api/'
# headers = {'content-type': 'application/json'}
#
# load = load_workbook("services.xlsx", data_only=True)
# load = load['serviceSheet']
#
# policies = {'policies': []}
#
# for row in load.rows:
#     row_value = []
#     for cell in row:
#         row_value.append(cell.value)
#
#     policies['policies'].append({
#         'id':row_value[0],
#         'title': row_value[1],
#         'brief': row_value[2],
#         'target': row_value[3],
#         'criteria': row_value[4],
#         'content': row_value[5],
#         'supply_way': row_value[6],
#         'procedure': row_value[7],
#         'site': row_value[8]
#     })
#
# del policies['policies'][0]
# requests.post(API_URL + 'crawling/policy/', data=json.dumps(policies), headers=headers)

str = "|생계·의료·주거·교육급여 수급자, 의료급여법에 의한 수급권자, 타법에 의한 수급권자*에게 지원합니다.&타법에 의한 수급권자@이재민@의상자 및 의사자의 유족@입양아동(18세미만)@국가유공자@중요무형문화재의 보유자@북한이탈주민@5ㆍ18 민주화운동 관련자@노숙인|의료급여수급권자 중에서 급여대상의 본인부담금 기준액을 초과한 자에게 지원합니다.|국민기초생활보장법에 의한 의료급여 수급권자는 1종 수급권자와 2종 수급권자로 구분하여 지원합니다."
# str = str.replace("|","\n○ ")
# str = str.replace("&","\n  - ")
# str = str.replace("@","\n    ＊ ")
# str = str.replace("+","\n        ")

temp=""
for i in range(0, len(str)):
    if(str[i]=="|"):
        temp+="\n○ "
    elif(str[i]=="&"):
        temp+="<br>  -  "
    elif (str[i] == "@"):
        temp += "\n    ＊ "
    elif (str[i] == "+"):
        temp += "\n        "
    else:
        temp+=str[i]
print(temp)
