#! /usr/bin/python3
# chap12PracProjTxtToSheet.py - Copy contents of text files to a spreadsheet.

import openpyxl
import sys

files = ['rows.txt', 'rowow.txt', 'rowowow.txt']

wb = openpyxl.Workbook()
sheet = wb.active

count = 1
for f in files:
	fo = open(f)
	lst = fo.readlines()
	for i in range(len(lst)):
		sheet.cell(row=i+1, column=count).value = lst[i]
	count += 1

wb.save('txtToSheet.xlsx')
