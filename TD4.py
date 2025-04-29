# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 09:46:20 2025

@author: Thoma
"""


import matplotlib.pyplot as plt
from time import perf_counter


class hashtable :
    
    def __init__(self, size=10, function=None):
        self.size=size
        self.function=function if function else self.hash_naive
        self.table=[[] for i in range (size)]
    
    def hash_naive(self, x):
        return sum(ord(c) for c in x)
    
    
    def put(self, key, value):
        index=self.function(key)%self.size
        for i, (k,v) in enumerate(self.table[index]):
            if k == key:
               self.table[index][i] = (key, value)
               return
        self.table[index].append((key, value))

            
    def get(self, key):
        index=self.function(key)%self.size
        for k,v in self.table[index]:
            if k==key:
                return v
        return None
    
    def repartition(self):
        y = [len(self.table[index]) for index in range(self.size)]
        N = len(y)
        x = range(N)
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()
    
    def resize(self):
        old_table = self.table
        self.size *= 2
        self.count = 0
        self.table = [[] for _ in range(self.size)]
        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)
                
            
if __name__=="__main__":
    h=lambda s:sum([ord(c) for c in s])
    h2=lambda s:sum([ord(s[i])*33**i for i in range(len(s))])
    def hash_wikipedia(key):
        hash = 0
        for c in key:
            hash += ord(c)
            hash += (hash << 10)
            hash ^= (hash >> 6)
            hash += (hash << 3)
            hash ^= (hash >> 11)
            hash += (hash << 15)
        return hash
    

    T=hashtable(100,h)
    T.put('abc',197)
    T.put('ab',200)
    print(T.table)
    T.put('abc',220)
    print(T.table)
    print(T.get('abc'))
    T2=hashtable(5,h)
    T2.put('abc',197)
    T2.put('a',200)
    T2.put('b',200)
    T2.put('aba',200)
    T2.put('cab',200)
    T2.put('acb',200)
    T2.put('bac',200)
    print(T2.table)
    print(T2.repartition())
    L=list()
    f=open("C:\\Users\\Thoma\\frenchssaccent.dic","r")
    for ligne in f:
        L.append(ligne[0:len(ligne)-1])
    f.close()
    T=hashtable(320,h2)
    for i in range (0,len(L),6):
        T.put(L[i],len(L[i]))
    T.repartition()
    
    
    
    
    
        
        
            
    
        

        
        
        
ht = hashtable()
print(ht.hash_naive('abc'))
ht.put('abc', 3)
ht.put('cab', 5)  # collision probable
ht.put('aaa', 10)
print("ht.get('abc'):", ht.get('abc'))
print("ht.get('aaa'):", ht.get('aaa'))




        