# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 09:50:20 2025

@author: Thoma
"""

class Tree: 
    
    def __init__(self, label, *children):
        self._label=label
        self._children=tuple(children)
        
    def nb_children(self):
        return len(self.children)
    
    def children(self):
        return self._children
    
    def label(self):
        return self._label
    
    
    def child(self, i):
        c=self.children
        return c[i]
    
    
    def is_leaf (self):
        if len(self.children)==0:
            return True
        return False
    
    def depth(self):
        if self.is_leaf():
            return 0
        else:
            return 1+max(child.depth for child in self._children)
        
    def __str__(self):
        if self.is_leaf():
            return str(self.label)
        return f"{self.label}({','.join(str(child) for child in self.children)})"
    
    def __eq__(self, other):
        if not isinstance (other, Tree):               #vérifier que c'est du même type
            return False
        return self.label==other.label and self.children ==other.children
    
    
    def deriv(self, var: str):
        if self.is_leaf():
            if self._label == var:
                return Tree('1')
            else:
                return Tree('0')
        if self._label == '+':
            return Tree('+', *(child.deriv(var) for child in self._children))
        if self._label == '*':
            # Produit de deux fonctions : f * g => f' * g + f * g'
            if len(self._children) == 2:
                u, v = self._children
                return Tree('+',
                            Tree('*', u.deriv(var), v),
                            Tree('*', u, v.deriv(var)))
        return Tree('0')
    
    
    
    
    
    
    
    
    
    
        
    
    


