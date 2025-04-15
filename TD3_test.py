# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 10:17:32 2025

@author: Thoma
"""

import unittest 
from TD3 import Tree


class TestTree(unittest.TestCase):
    
    
    def test_base_methods(self):
        t = Tree('a')
        print ("voici l'arbre :", t)
        self.assertEqual(t.label(), 'a')
        self.assertEqual(t.nb_children(), 0)
        self.assertTrue(t.is_leaf())
        
    def test_depth(self):
        t=Tree('f', Tree('a'), Tree('b'))
        self.assertEqual(t.depth(), 1)
        
    def test_str(self):
        t=Tree('f', Tree('a'), Tree('b'))
        self.assertEqual(str(t), "f(a,b)")
        
    def test_eq(self):
        t1=Tree('f', Tree('a'), Tree('b'))
        t2=Tree('f', Tree('a'), Tree('b'))
        self.assertEqual(t1,t2)
        
        
    def test_deriv(self):
        expr = Tree('+',
                    Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X'))),
                    Tree('*', Tree('5'), Tree('X')),
                    Tree('7'))
        d = expr.deriv('X')
        simplified = d.simplify()
        self.assertEqual(str(simplified), "+(+(3*(1*X+X*1),5*1),0)".replace(" ", ""))  # Non-simplifié
        
        
        

         
 
         
    
        
    