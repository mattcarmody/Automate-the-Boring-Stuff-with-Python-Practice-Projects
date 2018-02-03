import re

# Read in text from file and create a list of all the words.
txt_file = open('madLibsFeed.txt')
file_content = txt_file.read()
txt_words = list(file_content.split())
txt_file.close()

# Define regex to recognize placeholders in list.
mad_lib_regex = re.compile(r'''(
    ADJECTIVE |
    VERB |
    NOUN |
    ADVERB
    )''', re.VERBOSE)
mo = mad_lib_regex.findall(file_content)

# Call for user input words and use them to replace placeholders.
for i in range(len(txt_words)):
    if mad_lib_regex.match(txt_words[i]):
        if txt_words[i].endswith('.'):
            sub = input("Enter your own {}: ".format(txt_words[i][:-1].lower()))
            sub += '.'
        elif txt_words[i].endswith(','):
            sub = input("Enter your own {}: ".format(textWords[i][:-1].lower()))
            sub += ','
        else:
            sub = input("Enter your own {}: ".format(textWords[i].lower()))
        txt_words[i] = sub
    else:
        continue
       
new_sentence = ' '.join(txt_words)

new_file = open('madLibsOutput.txt', 'w')
new_file.write(str(new_sentence))
new_file.close()

print(new_sentence)
