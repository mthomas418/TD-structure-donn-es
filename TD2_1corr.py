# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 10:48:43 2025

@author: Thoma
"""

#corrigé#

class polynomial :
    def __init__(self, coeffs):
        self.coeffs=coeffs #liste des coeffs
        
    def __str__(self):
        terms=[]
        for i in range (len(self.coeffs)):
            if self.coeffs[i]!=0:
                terms.append(f"{self.coeffs[i]}x^{i}" if i>0 else f"{self.coeffs[i]}")
        return "+".join(terms) if terms else "0"
    
    def add(self, other):
        max_len=max(len(self.coeffs), len(other.coeffs))
        new_coeffs=[0]*max_len
        
        for i in range(len(self.coeffs)):
            new_coeffs[i]+=self.coeffs[i]
        for i in range(len(other.coeffs)):
            new_coeffs[i]+=other.coeffs[i]
        return polynomial(new_coeffs)
    
#exemples
p1=polynomial([1,2,3])
p2=polynomial([2,3,4])
print (p1.add(p2))
        