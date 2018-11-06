import os
import time

run_index = 1
currentdir = os.path.dirname(os.path.realpath(__file__))

while True:
    print('Boot Number: ',run_index)
    os.system('py ' + currentdir + '\\gobot.py')
    run_index = run_index + 1
    time.sleep(5)
    print('\n\n**********************************************************  Re-Booting **********************************************************\n')
    