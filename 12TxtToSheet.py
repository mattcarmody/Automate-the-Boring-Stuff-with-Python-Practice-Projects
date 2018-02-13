# Copy contents of text files to a spreadsheet.

import openpyxl

files = [file1, file2, file3]

wb = openpyxl.Workbook()
sheet = wb.active

for j, _file in enumerate(files):
	content = open(_file).readlines()
	for i in range(len(content)):
		sheet.cell(row=i+1, column=j+1).value = content[i]

wb.save('txtToSheet.xlsx')
