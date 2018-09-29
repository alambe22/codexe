#!/usr/bin/python3
from subprocess import call, check_output
from time import time

class Executable(object):
    def __init__(self, command, desired):
        self.command = command
        time_init = time()
        try:
            self.output = self.exo()
        except Exception as e:
            if Exception == KeyboardInterrupt: raise
            self.output = e
        self.time = time() - time_init
        self.desired = desired
        self.result = self.output in desired
        self.dict = {
            "command": self.command,
            "output": self.output,
            "time": self.time,
            "desired": self.desired,
            "result": self.result
        }

    def ex(self):
        """executes string as command without output"""
        call(self.command.split(" "))

    def exo(self):
        """executes string as command with output"""
        return check_output(self.command.split(" ")).decode("utf-8").rstrip()



def read(url):
    """reads string as url and returns file contents"""
    with open(url, 'r') as file:
        return file.read()



def expOut(inst, arg=""):
    o = {}
    for i in inst.split("\n")[:-1]:
        k = i.split(":$:")
        try:
            o[k[0]] = Executable(k[0] + " " + arg, k[1].split("|:|")).dict
        except IndexError:
            raise TypeError("Instruction file incorrectly formatted")
    return o



print(expOut(read("commands"), "Hello world!"))
