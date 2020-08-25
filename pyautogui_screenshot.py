import pyautogui
im = pyautogui.screenshot()
print(im.getpixel((0,0)))
print(im.getpixel((50,200)))
print(pyautogui.pixelMatchesColor(50,200,(86,86,86)))
'''given x- and y-coordinates on the screen matches the given color. The
first and second arguments are integers for the x- and y-coordinates, and
the third argument is a tuple of three integers for the RGB color the screen
pixel must match.'''

