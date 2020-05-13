# %%
from datetime import datetime
import matplotlib.pyplot as plt
import csv

fn = "pythonExample/csvReport.csv"

with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        print("Row %s = " % csvReader.line_num, row)

# %%
# using list read contents

fn = "pythonExample/csvReport.csv"
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)

print(listReport[0][1])
print(listReport[1][1])


# %%
# using DictReader() Example

fn = "pythonExample/csvPeople.csv"

with open(fn) as csvFile:
    csvDictReader = csv.DictReader(csvFile)
    for row in csvDictReader:
        print(row['first_name'], row['last_name'])


# %%
# Write value to csv file

fn = 'csvWriteExample.csv'
with open(fn, 'w', newline='') as csvFile:  # newline()避免輸出時每個行之間多空一行
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['Name', 'Age', 'City'])
    csvWriter.writerow(['Hung', '35', 'Taipei'])
    csvWriter.writerow(['James', '40', 'Chicago'])


# %%
# Using DictWriter() Example

fn = "dictCsvExample.csv"

with open(fn, 'w', newline='')as csvFile:
    fields = ['Name', 'Age', 'City']
    dictWriter = csv.DictWriter(csvFile, fieldnames=fields)

    dictWriter.writeheader()
    dictWriter.writerow({'Name': 'Hung', 'Age': '35', 'City': 'Taipei'})
    dictWriter.writerow({'Name': 'James', 'Age': '40', 'City': 'Chicago'})


# %%
# Using csv data drew a chart

fn = "pythonExample/TaipeiWeatherJan.csv"

with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)             # 讀取文件下一行
    dates, highTemps, lowTemps = [], [], []  # 設定空串列
    for row in csvReader:
        try:
            currentDate = datetime.strptime(row[0], "%Y/%m/%d")
            highTemp = int(row[1])          # 設定最高溫
            lowTemp = int(row[3])           # 設定最低溫
        except Exception:
            print('有缺值')
        else:
            highTemps.append(highTemp)      # 儲存最高溫
            lowTemps.append(lowTemp)        # 儲存最低溫
            dates.append(currentDate)       # 儲存日期

fig = plt.figure(dpi=80, figsize=(12, 8))   # 設定繪圖區大小
plt.plot(dates, highTemps)                  # 繪製最高溫
plt.plot(dates, lowTemps)                   # 繪製最低溫
fig.autofmt_xdate()                         # 日期旋轉
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()
