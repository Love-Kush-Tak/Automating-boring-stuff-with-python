import pyautogui, time
print('press CTRL-0C to quit')
try:
    while True:
        x,y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x,y))
        positionStr += ' RGB: (' +str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) +')'
        print(positionStr, end='')
        print('\b'*len(positionStr), end='', flush=True)
        time.sleep(2)

except KeyboardInterrupt:
    print('\nDone.')
'''The rjust() string method will right-justify them so
that they take up the same amount of space, whether the coordinate has
one, two, three, or four digits'''
