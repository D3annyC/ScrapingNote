import json

fn = 'pythonExample/populations.json'

with open(fn, 'r') as fnObj:
    getDatas = json.load(fnObj)

for getData in getDatas:
    if getData['Year'] == '2010':
        cName = getData['Country Name']
        cCode = getData['Country Code']
        population = int(float(getData['Numbers']))
        print('國家代碼＝ ', cCode,
              '國家名稱＝ ', cName,
              '2010總人口＝ ', population)
