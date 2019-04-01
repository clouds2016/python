# -*- coding:gbk -*-

import subprocess
prop = subprocess.Popen(['ipconfig'], stdout=subprocess.PIPE)
while True:
    line = prop.stdout.readline()
    if not line:
        break
    print(line, end='')

if prop.poll() is None:
    print("Program is running")
if prop.poll() > 0:
    print('Program is exit and error')
if prop.poll() < 0:
    print('program is killed')
if prop.poll() == 0:
    print('program is ok and exit')
