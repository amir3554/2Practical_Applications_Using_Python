import openpyxl 
from pathlib import Path

import openpyxl.chart

file = openpyxl.load_workbook(Path.home() /  Path('Desktop', 'tests', 'employees.xlsx'))

sheet = file['Sheet1']

names = openpyxl.chart.Reference(sheet, max_col=1, min_col=1, max_row=1 , min_row=6)
data  = openpyxl.chart.Reference(sheet, max_col=2, min_col=2, max_row=1 , min_row=6)

My_chart = openpyxl.chart.BarChart() # لاستدعاء الرسم البياني بار تشارت
#My_chart = openpyxl.chart.LineChart()
#My_chart = openpyxl.chart.PieChart()
# SEARTCH ON GOOGLE openpyxl charts

My_chart.title = 'Amir Chart'

My_chart.add_data(data=data)
My_chart.set_categories(names)

sheet.add_chart(My_chart, 'A10')

file.save(filename= Path.home() /  Path('Desktop', 'tests', 'employees.xlsx'))
