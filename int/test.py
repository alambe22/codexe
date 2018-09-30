#!/usr/bin/python3
from subprocess import call, check_output
from time import time
from json import dumps
import re

dir = "tests/"

class Executable(object):
    def __init__(self, command, desired):
        self.command = command
        time_init = time()
        try:
            self.output = self.exo()
        except Exception as e:
            if Exception == KeyboardInterrupt: raise
            self.output = "Error"
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
        o = check_output(self.command.split(" ")).decode("utf-8").rstrip()
        return str(o)



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
        o[s[1]]["report"] = {}
        exo("sudo stat/codeStat " + s[0] + " " + s[2])
        t = read("report").split("\n")
        for i in t[:-1]:
            j = i.split(" ")
            libraries = []
            libraries += re.findall(r'"(.*?)(?<!\\)"', i)
            o[s[1]]["report"][j[0]] = {
                    "language": j[-1],
                    "lines": j[1],
                    "comments": j[2],
                    "libraries": libraries,
            }
    return o

students = {}
rc = runCommands(getCommands())
for s in rc.keys():
    total = len(rc[s])
    correct = 0
    students[s] = {}
    for i in rc[s].keys():
        if not i == "report":
            correct += rc[s][i]["result"]
            students[s][i] = {
                "time": rc[s][i]["time"],
                #"verbose": ""#rc
            }
    students[s]["report"] = rc[s]["report"]
    students[s]["grade"] = correct / total

print(dumps(students))
