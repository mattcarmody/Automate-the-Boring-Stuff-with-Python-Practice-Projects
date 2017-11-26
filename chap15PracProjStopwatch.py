#! python3
# chap15PracProjStopwatch.py -  A simple stopwatch program with pretty output.
#       Output is copied to the clipboard at the end.

import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Then, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() # press Enter to begin.
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1
text = ''

# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).rjust(5), str(lapTime).rjust(5)), end='')
        text += ('Lap #' + str(lapNum).rjust(2) + ': ' + str(totalTime).rjust(5) +' (' + str(lapTime).rjust(5) + ')\n')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    pyperclip.copy(text)
    print('\nDone. Text copied to clipboard.')
