#!/usr/bin/env python

def freq_an(input):
    fx = {}
    for elem in input:
        if fx.has_key(elem):
            fx[elem] +=1
        else:
            fx[elem] = 1
    return fx

def entropy(data):
    Hd = 0
    for i in range(256):
        pi = float(data.count(chr(i)))/len(data)
        if pi > 0:
            Hd += - pi * math.log(pi, 2)
    return Hd

def rfile(filename):
    return open(filename,"r").read()

def trn(input,fr,to):
    import string
    return(input.translate(string.maketrans(fr,to)))


