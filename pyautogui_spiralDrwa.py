'''PyAutoGUI provides the pyautogui.dragTo() and pyautogui.dragRel()
functions
to drag the mouse cursor to a new location or a location relative
to its current one'''
'''The arguments for dragTo() and dragRel() are the
same as moveTo() and moveRel(): the x-coordinate/horizontal movement, the
y-coordinate/vertical movement, and an optional duration of time'''
#Dragging the mouse
import pyautogui, time
time.sleep(5)
pyautogui.click()
distance = 200
while distance >0:
    pyautogui.dragRel(distance,0,duration=0.2)
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance,0, duration=0.2)
    distance = distance - 5
    pyautogui.dragRel(0,-distance, duration=0.2)
