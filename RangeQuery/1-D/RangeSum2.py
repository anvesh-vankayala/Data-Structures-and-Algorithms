# -*- coding: utf-8 -*-
"""
@author: Anvesh

adhoc : cummulative sum approach
"""

class RangeSum:
    
    def __init__(self,arr):
        """Tc: preprocess O(n)"""
        self.intArray = arr
        self.cummSum =  [None]*(len(arr))
        self.cummSum[0]=arr[0]
        for i in range(1,len(arr)-1):
            self.cummSum[i] = arr[i]+self.cummSum[i-1]
        print(self.cummSum)
        
    def update(self,x,i):
        """TC: O(n)"""
        self.intArray[i] = x
        for i in range(1,len(self.intArray)):
            self.cummSum[i] = self.intArray[i]+self.cummSum[i-1]
        print(self.intArray,'', self.cummSum)
        
    def rangeSum(self,i,j):
        """Tc : O(1)"""
        if i ==0:
            return self.cummSum[j]
        return self.cummSum[j]-self.cummSum[i-1]
    
    
rangesum = RangeSum([2,3,1,0,-1])
rangesum.update(10,2)
summ = rangesum.rangeSum(0,2)
print(summ)