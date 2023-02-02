import csv
from openpyxl import Workbook

wb = Workbook()  # create book
ws = wb.active  # create a sheet

with open('task4.csv', encoding='utf8') as file:
    csvr = list(csv.reader(file, delimiter='-'))

for i in csvr:
    ws.append(i)

ws.delete_cols(3)
wb.save("task5.xlsx")
wb.close()
