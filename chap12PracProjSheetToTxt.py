#! /usr/bin/python3
# chap12PracProjSheetToTxt.py - Copy contents of text files to a spreadsheet.

import openpyxl

files = ['rows2.txt', 'rowow2.txt', 'rowowow2.txt']

wb = openpyxl.load_workbook('txtToSheet.xlsx')
sheet = wb.active

for j in range(1, sheet.max_column+1):
	fileHere = open(files[j-1], 'w')
	for i in range(1, sheet.max_row+1):
		if sheet.cell(row=i, column=j).value:
			fileHere.write(sheet.cell(row=i, column=j).value)
	fileHere.close
