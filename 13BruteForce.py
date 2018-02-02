#! /usr/bin/python3
# chap13PracProjBruteForce.py

import PyPDF2

dictionary = '/home/matt/AutomateBook/automate_online-materials/dictionary.txt'
encryptedFile = '/home/matt/AutomateBook/pdfs/combinedminutes_encrypted.pdf'
pdfReader = PyPDF2.PdfFileReader(open(encryptedFile, 'rb'))

dictFile = open(dictionary)
dictList = dictFile.read().splitlines()

for word in dictList:
	if pdfReader.decrypt(word):
		print(word)
		break
	if pdfReader.decrypt(word.lower()):
		print(word.lower())
		break

