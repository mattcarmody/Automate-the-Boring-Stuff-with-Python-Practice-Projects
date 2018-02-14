#  A simple stopwatch program with pretty output.
#  Output is copied to the clipboard at the end.

import pyperclip
import time

# Display the program's instructions.
print('Press ENTER to begin. Then, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input() # press Enter to begin.
print('Started.')
start_time = time.time() # get the first lap's start time
last_click = start_time
lap_num = 1
cum_text = ''

# Start tracking the lap times.
try:
    while True:
        input() # press Enter to 'click' lap.
        lap_time = round(time.time() - last_click, 2)
        total_time = round(time.time() - start_time, 2)
        new_text = 'Lap #{}: {} ({})'.format(str(lap_num).rjust(2), str(total_time).rjust(5), str(lap_time).rjust(5))
        print(new_text, end='')
        cum_text += '{}\n'.format(new_text)
        lap_num += 1
        last_click = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    pyperclip.copy(cum_text)
    print('\nDone. Text copied to clipboard.')
