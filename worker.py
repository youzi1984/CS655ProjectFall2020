# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:46:19 2020

@author: yuqi
"""


import socket
from hashlib import md5
from string import ascii_letters
from itertools import permutations
from itertools import product
from time import time
all_letters=ascii_letters

def decrypt_md5(md5_value, n, i):

    if len(md5_value)!=32:
        print('error')
        return

    md5_value=md5_value.lower()
    k = float(52 / n)
    for j in range(int(round(k * i)), int(round(k * i + k))):
        print("Checking password starting with "+str(ascii_letters[j]))
        for item in product(list(all_letters), repeat=4):
        # for item in permutations(all_letters,4):
            item=ascii_letters[j]+''.join(item)
            # print('.',end='')
            if md5(item.encode()).hexdigest()==md5_value:
                return item
    return "None"

s = socket.socket()
s.connect(('172.17.2.13', 9007))
print(s.recv(1024).decode(encoding='utf8'))
#sentence = s.recv(1024).decode
#print(sentence.decode(encoding='utf8'))


while True:
    sentence = s.recv(1024)
    print("Receive the message from job server:")
    print(sentence)
    md5_value, n, seq = sentence.split( )
    n = int(n)
    seq = int(seq)
    #md5_value = md5_value.decode(encoding='utf-8')
    #n = int(n.decode(encoding='utf8'))
    #k = int(k.decode(encoding='utf8'))
    print("md5= "+str(md5_value))
    print("n= "+str(n))
    print("seq= "+str(seq))
    
    start = time()
    result=decrypt_md5(md5_value, n, seq)
    if result and result!="None":
        print('\n Success: '+md5_value+'==>'+result)
    print('Time used:',time()-start)
    
#    ans = input("input anthing:")
#    ans += "\n"
    ans = result
    s.send(ans.encode())
