import os
import PyPDF2

password = 'bubbles'

for folder_name, subfolders, files in os.walk('/home/matt/AutomateBookLocal/pdfs'):
	for _file in files:
		if _file.endswith('.pdf'):
			pdf_file = open(os.path.join(folder_name, _file), 'rb')
			pdf_reader = PyPDF2.PdfFileReader(pdf_file)
			if pdf_reader.isEncrypted:
				print("Attempting to decrypt {}...".format(_file))
				pdf_reader.decrypt(password)
				pdf_writer = PyPDF2.PdfFileWriter()
				for page_num in range(pdf_reader.numPages):
					pdf_writer.addPage(pdf_reader.getPage(page_num))
				pdf_output_file = open("{}_decrypted.pdf".format(os.path.splitext(os.path.join(folder_name, _file))[0]), 'wb')
				pdf_writer.write(pdf_output_file)
				pdf_output_file.close()
			else:
				print("{} is a pdf but is not encrypted...".format(_file))
			pdf_file.close()
		else:
			print("{} is not a pdf".format(_file))
