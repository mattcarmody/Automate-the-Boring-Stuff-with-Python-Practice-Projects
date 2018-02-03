import re

def regex_strip(target, snip):
    if len(snip):    # If user passed a criteria, snip it.
        front_input_re = re.compile(r'^{}'.format(re.escape(snip)))
        back_input_re = re.compile(r'{}$'.format(re.escape(snip)))
        trimmed = front_input_re.sub('', target)
        trimmed = back_input_re.sub('', trimmed)
        return trimmed        
    else:   # Else, take off white space
        front_white_re = re.compile(r'^\s*')
        back_white_re = re.compile(r'\s*$')
        trimmed = front_white_re.sub('', target)
        trimmed = back_white_re.sub('', trimmed)
        return trimmed
        
target = str(input('What would you like stripped?'))
snip = str(input('And what would you like taken off? Press only Enter if white space.'))
print(regex_strip(target, snip))
