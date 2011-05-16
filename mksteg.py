#!/usr/bin/env python
from sys import argv

def freq_an(input,fxp):
    if len (fxp) == 0:
        fx = {}
    else:
        fx = fxp
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

def can_dec(cfx,dfx):
    if len(cfx) >= len(dfx):
        return 1
    else:
        print "[+] data/carrier mismatch"
        return 0

def sort_dict(x):
    import operator
    sorted_x = sorted(x.iteritems(), key=operator.itemgetter(1),reverse=True)
    return sorted_x

def get_symb_array(x):
    x = sort_dict(x)
    y = []
    for key in x:
        y.append(key[0])
    return y

def clean_maps(x):
    x = x.remove("\n")
    return x.remove("\t")
    

def simple_dict_mapper(cfx,dfx):
    if can_dec(cfx,dfx) == 0:
        return 0
    cst = get_symb_array(cfx)
    dst = get_symb_array(dfx)
    dst = dst[:len(cst)]
    mapper = {}
    for i in range(len(dst)):
        mapper[cst[i]] = dst[i]
    return mapper

def simple_mapper(cfx,dfx):
    if can_dec(cfx,dfx) == 0:
        return 0
    cst = get_symb_array(cfx)
    dst = get_symb_array(dfx)
    cst = cst[:len(dst)]
    dst = dst[:len(dst)]
    return cst,dst



cfx = {} # carrier frequency
dfx = {} # data frequency

carrier = open(argv[1],"r").read()
data = open(argv[2],"r").read()
#output = open(argv[3],"w")

cfx = freq_an(carrier,cfx)
dfx = freq_an(data,dfx)

print simple_mapper(cfx,dfx)

   
