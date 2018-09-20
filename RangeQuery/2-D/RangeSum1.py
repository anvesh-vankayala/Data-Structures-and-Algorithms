# -*- coding: utf-8 -*-
"""
@author: Anvesh

Naive approach
"""
from random import randint




class RangeSum:
    
    def __init__(self,array):
        self.arr = array
        
    def update(self,x,i,j):
        """TC:O(1)"""
        self.arr[i][j] = x
        
    
    def rangeSum(self,i1,j1,i2,j2):
        """TC:O(n^2)"""
        summ = 0
        column = j1
        while(i1<=i2):
            while(j1<=j2):
                summ += self.arr[i1][j1]
                j1+=1
            j1 = column
            i1+=1
        return summ

    
    
matrix = [[randint(0, 9) for i in range(6)] for i in range(6)]
print(len(matrix[0]))
print(matrix)
obj = RangeSum(matrix)
print(obj.rangeSum(1,1,2,2))
obj.update()