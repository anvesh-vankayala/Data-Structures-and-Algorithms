# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 12:48:24 2018

@author: Anvesh
"""

class RangeSum:
    array = []
    actualLength=0
    def __init__(self,arr):
        RangeSum.actualLength = len(arr)-1
        array = [None]*(2*len(arr)-1)
        i=2*len(arr)-2
        j=len(arr)-1
        while(j>=0):
            array[i]=arr[j]
            j= j-1
            i= i-1
        k = len(array)-1
        while(k >=0):
            array[int((k-1)/2)] = array[k-1]+array[k]
            k=k-2
        RangeSum.array = array
        print(RangeSum.array)
                      
            
    def rangeSum(self,i,j):
        return RangeSum.auxilery(0,RangeSum.actualLength+i,RangeSum.actualLength+j)
    
    
    def auxilery(sum,i,j):
        if(i==j):
            return sum
        if(i%2!=0):
            sum = sum+RangeSum.array[i]
        else:
            sum = sum+RangeSum.array[i]
        if(j%2==0):
            sum = sum+RangeSum.array[j]
        else:
            sum = sum+RangeSum.array[j]
        i = int((i-1)/2)
        j = int((j-1)/2)
        return RangeSum.auxilery(sum,i,j)
        
        
        
        
        
        
    def update(self,i,value):
        print("update array value")
        
        
#         46     
#    16          20
# 5,    11,   10    10
#2, 3, 5, 6, 9, 1, 0, 10
rangeObj = RangeSum([2,3,5,6,9,1,0,10])
sume = rangeObj.rangeSum(0,3)
print(sume)
#rangeObj.update(2,3)
#print(rangeObj.array)
#sume = rangeObj.rangeSum(1,4)
#print(sume)
