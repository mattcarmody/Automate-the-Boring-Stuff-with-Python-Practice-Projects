#! python3
# chap7PracProjRegexStrip.py - Recreating strip() with Regex.

import re

def regexStrip(target, snip):
    if len(snip):    # If user passed a criteria, snip it.
        fcustRegex = re.compile(r'^' + re.escape(snip))
        bcustRegex = re.compile(re.escape(snip) + r'$')
        trimmed = fcustRegex.sub('', target)
        trimmed = bcustRegex.sub('', trimmed)
        return trimmed        
    else:            # Else, take off white space
        fspaceRegex = re.compile(r'^\s*')
        bspaceRegex = re.compile(r'\s*$')
        trimmed = fspaceRegex.sub('', target)
        trimmed = bspaceRegex.sub('', trimmed)
        return trimmed
        
target = str(input('What would you like stripped?'))
snip = str(input('And what would you like taken off? Press only Enter if white space.'))
newTarget = regexStrip(target, snip)
print(newTarget)
