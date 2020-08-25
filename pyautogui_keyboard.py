import pyautogui, time
'''open a new file editor window
and position it in the upper-left corner of your screen so that PyAutoGUI
will click in the right place to bring it into focus.'''
pyautogui.click(100,100)
pyautogui.typewrite('Hello world!')
pyautogui.typewrite('write with a pause',0.25)
pyautogui.typewrite(['a','b','left','left','X','Y'])
#Because pressing the left arrow key moves the keyboard cursor, this will output XYab.
print(pyautogui.KEYBOARD_KEYS) #to see all possible keyboard key strings that PyAutoGUI will accept
'''The 'shift' string refers
to the left shift key and is equivalent to 'shiftleft'. The same applies for
'ctrl', 'alt', and 'win' strings; they all refer to the left-side key.'''
#pressign and releasing the keyboard
pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')
#copy
'''pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')'''
#copy using hotkey
pyautogui.hotkey('ctrl','c')




