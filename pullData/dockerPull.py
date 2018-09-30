#!/usr/bin/env python3
import os
import sys

if(len(sys.argv) != 3):
    print('usage: dockerPull.py students.txt labNum')
    exit(0)

dockerhub = 'beardlessbeard/'

file = open(sys.argv[1])
lines = file.read().split('\n')
lines.pop()

for student in lines:
    student = dockerhub + student + '_lab' + sys.argv[2]
    print(student)
    os.system('sudo docker pull ' + student)

