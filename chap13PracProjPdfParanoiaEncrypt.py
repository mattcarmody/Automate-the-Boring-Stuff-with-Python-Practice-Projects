#! /usr/bin/python3
# chap13PracProjPdfParanoiaEncrypt.py

import os
import PyPDF2

password = 'bubbles'

for folderName, subfolders, filenames in os.walk('/home/matt/AutomateBook/pdfs'):
	for filename in filenames:
		if filename.endswith('.pdf'):
			print("Encrypting... " + filename)
			
			# Encrypt all PDFs
			pdfFile = open(os.path.join(folderName, filename), 'rb')
			pdfReader = PyPDF2.PdfFileReader(pdfFile)
			pdfWriter = PyPDF2.PdfFileWriter()
			for pageNum in range(pdfReader.numPages):
				pageObj = pdfReader.getPage(pageNum)
				pdfWriter.addPage(pageObj)
			pdfWriter.encrypt(password)
			pdfOutputFile = open(os.path.splitext(os.path.join(folderName, filename))[0] + "_encrypted.pdf", 'wb')
			pdfWriter.write(pdfOutputFile)
			pdfOutputFile.close()
			pdfFile.close()
		
			# Attempt to decrypt new file before deleting old one
			pdfFile2 = open(os.path.splitext(os.path.join(folderName, filename))[0] + "_encrypted.pdf", 'rb')
			pdfReader2 = PyPDF2.PdfFileReader(pdfFile2)
			if pdfReader2.decrypt(password):
				print("Deleting original...")
				os.remove(os.path.join(folderName, filename))
			else:
				print("Couldn't open the encrypted version...")
				continue
				
