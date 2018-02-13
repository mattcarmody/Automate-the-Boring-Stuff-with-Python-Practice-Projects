import os
import PyPDF2

password = 'bubbles'

for folder_name, subfolders, files in os.walk('/home/matt/AutomateBookLocal/pdfs'):
    for _file in files:
        if _file.endswith('.pdf'):
            print("Encrypting... {}".format(_file))
            
            # Encrypt all PDFs
            pdf_file = open(os.path.join(folder_name, _file), 'rb')
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            pdf_writer = PyPDF2.PdfFileWriter()
            if not pdf_reader.isEncrypted:
                for page_num in range(pdf_reader.numPages):
                    page_obj = pdf_reader.getPage(page_num)
                    pdf_writer.addPage(page_obj)
                pdf_writer.encrypt(password)
                pdf_output_file = open("{}_encrypted.pdf".format(os.path.splitext(os.path.join(folder_name, _file))[0]), 'wb')
                pdf_writer.write(pdf_output_file)
                pdf_output_file.close()
            else:
                print("{} is already encrypted.".format(_file))
                pdf_file.close()
                continue
            pdf_file.close()
		
			# Attempt to decrypt new file before deleting old one
            pdf_file_new = open("{}_encrypted.pdf".format(os.path.splitext(os.path.join(folder_name, _file))[0]), 'rb')
            pdf_reader_new = PyPDF2.PdfFileReader(pdf_file_new)
            if pdf_reader_new.decrypt(password):
                print("Deleting original...")
                os.remove(os.path.join(folder_name, _file))
            else:
                print("Couldn't open the encrypted version...")
                continue
            pdf_file_new.close()
            
