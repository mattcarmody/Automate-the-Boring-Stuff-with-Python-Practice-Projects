import PyPDF2

DICTIONARY = '/home/matt/AutomateBookLocal/automate_online-materials/dictionary.txt'
ENCR_FILE = '/home/matt/AutomateBookLocal/pdfs/combinedminutes_encrypted.pdf'
PWD_DEF = "12DEF34"

pdf_reader = PyPDF2.PdfFileReader(open(ENCR_FILE, 'rb'))
dict_content = open(DICTIONARY).read().splitlines()

print("Cracking your security...")
pwd = PWD_DEF

for word in dict_content:
	if pdf_reader.decrypt(word):
		pwd = word
		break
	elif pdf_reader.decrypt(word.lower()):
		pwd = word.lower()
		break

if pwd != PWD_DEF:
    print("Your password is {}".format(pwd))
else:
    print("Either you have a half decent password, which isn't a dictionary word in all caps or lowercase, or the program botched the job")

