import pyautogui, time
time.sleep(5)
print(pyautogui.locateOnScreen('gmail.png'))
'''The four-integer tuple that locateOnScreen() returns has the x-coordinate
of the left edge, the y-coordinate of the top edge, the width, and the height
for the first place on the screen the image was found'''
'''If the image can be found in several places on the screen,
locateAllOnScreen() will return a Generator object, which can be passed
to list() to return a list of four-integer tuples'''
print(list(pyautogui.locateAllOnScreen('webmail2.png')))
