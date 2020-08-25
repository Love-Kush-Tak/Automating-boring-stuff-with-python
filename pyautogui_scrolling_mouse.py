import pyautogui, time
time.sleep(5)
pyautogui.scroll(200)
import pyperclip
numbers = ''
for i in range(200):
    numbers = numbers + str(i) +'\n'
pyperclip.copy(numbers)

