#! /usr/bin/python3
# chap13PracProjPdfParanoiaDecrypt.py

import os
import PyPDF2

password = 'bubbles'

for folderName, subfolders, filenames in os.walk('/home/matt/AutomateBook/pdfs'):
	for filename in filenames:
		if filename.endswith('.pdf'):
			pdfFile = open(os.path.join(folderName, filename), 'rb')
			pdfReader = PyPDF2.PdfFileReader(pdfFile)
			if pdfReader.isEncrypted:
				print("Attempting to decrypt " + filename + "...")
				pdfReader.decrypt(password)
				pdfWriter = PyPDF2.PdfFileWriter()
				for pageNum in range(pdfReader.numPages):
					pageObj = pdfReader.getPage(pageNum)
					pdfWriter.addPage(pageObj)
				pdfOutputFile = open(os.path.splitext(os.path.join(folderName, filename))[0] + "_decrypted.pdf", 'wb')
				pdfWriter.write(pdfOutputFile)
				pdfOutputFile.close()
				pdfFile.close()
			else:
				print(filename + " is a pdf but is not encrypted...")
		else:
			print(filename + " is not a pdf")
