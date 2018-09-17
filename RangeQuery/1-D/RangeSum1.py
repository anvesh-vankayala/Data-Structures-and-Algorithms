# -*- coding: utf-8 -*-
"""
@author: Anvesh

adhoc :Naive approach
"""

class RangeSum:
    
    def __init__(self,arr):
        self.intArray = arr
        print(self.intArray)
    
    def update(self,x,i):
        """ TC : O(1) """
        self.intArray[i] = x
        print(self.intArray)
    
    def rangeSum(self,i,j):
        """ TC : O(n) """
        summ =0
        while(i<=j):
            summ = summ+self.intArray[i]
            i+=1
        return summ

""" """
rangesum = RangeSum([2,3,1,0,-1])
rangesum.update(0,2)
summ = rangesum.rangeSum(0,3)
print(summ)


 



            
  