#! python3
# 14excelToCsv.py - Converts all Excel files in a directory to csv files.

import csv, openpyxl, os
from openpyxl.utils import get_column_letter

# Loop through all files in directory.
for file in os.listdir('C:\\Users\\Papa\\Documents\\mattPython\\'):
    # Skip any non-Excel files.
    if file.endswith('.xlsx'):
        wb = openpyxl.load_workbook('C:\\Users\\Papa\\Documents\\mattPython\\' + file)
        # Loop through all the sheets in each Excel file.
        for sheet in wb.get_sheet_names():
            # Create a CSV file for this sheet.
            csvFile = open(file[:-5] + '_' + sheet + '.csv', 'w', newline='')
            # Create the CSVwriter object for this file.
            csvWriter = csv.writer(csvFile)
            # Need a sheet object.
            sheetObj = wb.get_sheet_by_name(sheet)
            print('Loading rows & columns & cells for ' + file)
            # Loop through each row.
            for row in range(1, sheetObj.max_row+1):
                rowData = []
                # Loop through each cell in the row.
                for column in range(1, sheetObj.max_column+1):
                    # Append each cell in the row.
                    rowData.append(sheetObj[get_column_letter(column) + str(row)].value)
                # Append row to csvFile.
                csvWriter.writerow(rowData)
            # Save/close? CSV file.
            csvFile.close()
            
