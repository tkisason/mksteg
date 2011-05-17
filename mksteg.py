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

def to_hex(input):
    return ''.join(['%02x' % ord(x) for x in input])

def to_chr(input):
    return ''.join(['%02s' % chr(int(x,16)) for x in split_n(input,2)])

def rfile(filename):
    return open(filename,"r").read()

def trn(input,fr,to):
    import string
    tr = string.maketrans(fr,to)
    return input.translate(tr)

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

def simple_tr_mapper(cfx,dfx):
    if can_dec(cfx,dfx) == 0:
        return 0
    cst = get_symb_array(cfx)
    dst = get_symb_array(dfx)
    cst = cst[:len(dst)]
    dst = dst[:len(dst)]
    return cst,dst

def encode_data(cfx,dfx,data):
    if len(cfx) <= len(dfx):
        print "[+] carrier data mismatch!"
        return 0
    map = simple_tr_mapper(cfx,dfx)
    print "[+] map0: ",map[0]
    cmap = ''.join(map[0])
    print "[+] cmap: ", to_hex(cmap)
    print "[+] map1: ",map[1]
    dmap = ''.join(map[1])
    print "[+] dmap: ", to_hex(dmap)
    return trn(data,dmap,cmap)
    
if __name__ == '__main__':
    if len(argv) != 4:
        print "[+] usage: CARRIERFILE DATAFILE OUTPUTFILE"
        print "[+] current method: simple probability mapping"
        quit
    else:
        cfx = {} # carrier frequency
        dfx = {} # data frequency
        carrier = open(argv[1],"r").read()
        data = open(argv[2],"r").read()
        output = open(argv[3],"w")
        cfx = freq_an(carrier,cfx)
        dfx = freq_an(data,dfx)
        out = encode_data(cfx,dfx,data)
        if out != 0:
            output.write(out)
            print "[+] message written to OUTFILE"
   
