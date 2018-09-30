#!/usr/bin/python3
import json
import sys

def getJ(url):
    with open(url, "r") as read_file:
        return json.load(read_file)

def it(test):
    o = []
    if isinstance(test, dict):
        p = []
        for i in test.keys():
            o += [i, it(test[i])]
        o += p
    else:
        return [test]
    return o

def htmlize(g):
    o = "<ul>"
    if isinstance(g, list):
        for i in g:
            o += htmlize(i)
        return o + "</ul>"
    else:
        return "<li>" + str(g).replace("<","&lt;".replace(">","&gt")) + "</li>"

def out(s, u):
    f = open(u, "w")
    f.write(s)

y = getJ(sys.argv[1])
out(htmlize(it(y)),sys.argv[2])
