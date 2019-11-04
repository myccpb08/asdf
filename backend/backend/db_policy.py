from openpyxl import  load_workbook
import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

load = load_workbook("services.xlsx", data_only=True)
load = load['serviceSheet']

policies = {'policies': []}

for row in load.rows:
    row_value = []
    for cell in row:
        row_value.append(cell.value)

    policies['policies'].append({
        'id':row_value[0],
        'title': row_value[1],
        'brief': row_value[2],
        'target': row_value[3],
        'criteria': row_value[4],
        'content': row_value[5],
        'supply_way': row_value[6],
        'procedure': row_value[7],
        'site': row_value[8]
    })

del policies['policies'][0]
requests.post(API_URL + 'crawling/policy/', data=json.dumps(policies), headers=headers)
