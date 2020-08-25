import time
#Display the program's instructions
print('Press Enter to begin. Afterwards, press wnter to "click" the stopwatch. Press CTRL-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum=1
try:
    while True:
        input()
        lapTime = round(time.time()-lastTime,2)
        totalTime = round(time.time()-startTime,2)
        print('Lap #%s: %s (%s)' %(lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    print('\nDone')
