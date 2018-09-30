#!/usr/bin/python3
from subprocess import call, check_output
from time import time

dir = "tests/"

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

    def exo(self):
        """executes string as command with output"""
        return check_output(self.command.split(" ")).decode("utf-8").rstrip()



def exo(c):
    """executes string as command with output"""
    return check_output(c.split(" ")).decode("utf-8").rstrip()

def read(url):
    """reads string as url and returns file contents"""
    with open(url, 'r') as file:
        return file.read()

def getCommands():
    return exo("ls " + dir).split("\n")


def runCommands(cList):
    o = {}
    students = []
    for i in read("images").rstrip().split("\n"):
        t = i.split(":$:")
        students += [[t[0],t[1],t[2]]]
        o[t[1]] = {}
    for f in cList:
        if f[0] != ".":
            text = [x for x in read(dir + f).split("\n")[:-1] if not x[0] == "#"]
            args = text[0]
            expected = text[1:]
            for i in students:
                k = Executable("sudo docker run --rm " + i[0] + " bash /" + i[2] + "/run.sh " + args, expected)
                o[i[1]][f] = k.dict
    for s in students:
        exo("sudo stat/codeStat " + s[0] + " " + s[2])
        o[s[1]]["report"] = read("report")
    return o


def expOut(inst, arg=""):
    o = {}
    for i in [x for x in inst.split("\n")[:-1] if not x[0] == "#"]:
        k = i.split(":$:")
        try:
            o[k[0]] = Executable(k[0] + " " + arg, k[1].split("|:|")).dict
        except IndexError:
            raise TypeError("Instruction file incorrectly formatted")
    return o

d = runCommands(getCommands())
for i in d.keys():
    print(i)
    print("Output: " + str(d[i]["output"]))
    print("Correct: " + str(d[i]["desired"]))



"""t = expOut(read("commands"), "Hello world!")
for k in t.keys():
    print(k)
    print(t[k])"""
