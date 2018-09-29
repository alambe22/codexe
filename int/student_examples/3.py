#!/usr/bin/python3
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

delay_print("Hello world! ")
