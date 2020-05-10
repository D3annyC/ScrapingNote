import csv

fn = 'pythonExample/csvPeople.csv'

with open(fn, 'r') as csvFile:
    csvReader = csvFile
    listReport = list(csvReader)
    for row in listReport:
        print(listReport)
        print(row)
