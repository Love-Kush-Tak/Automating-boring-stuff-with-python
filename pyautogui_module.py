import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print(pyautogui.size())
width, height = pyautogui.size()
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200,100, duration=0.25)
    pyautogui.moveTo(200,200, duration=0.25)
    pyautogui.moveTo(200,200, duration=0.25)
    pyautogui.moveTo(100,200, duration=0.25)
'''pyautogui.moveRel() function moves the mouse cursor relative to
its current position.'''
for i in range(10):
    pyautogui.moveRel(100,0,duration=0.25)
    pyautogui.moveRel(0,100,duration=0.25)
    pyautogui.moveRel(-100,0, duration=0.25)
    pyautogui.moveRel(0,-100, duration=0.25)

#Getting the mouse
print(pyautogui.position())
    
