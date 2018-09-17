# -*- coding: utf-8 -*-
"""
@author: Anvesh

Using Segment tree data structure built with  array
"""

class RangeSum:
    
    def __init__(self,arr):
        """"
        Building segment tree with array.
        TC: preprocess O(n)
        """
        self.n = len(arr)
        self.segmentTree = [None]*(2*len(arr)-1)
        i = len(arr)-1
        while(i>=0):
            self.segmentTree[len(arr)-1+i] = arr[i]
            i-= 1
        i = len(self.segmentTree)-1
        while(i>0):
            self.segmentTree[(i-1)//2] = self.segmentTree[i-1] + self.segmentTree[i]
            i-= 2
        print(self.segmentTree)#[14 |8, 6 |4, 4, 1, 5 |1,3, 6,-2, 0, 1, 5, 0]
        
    
    def update(self,x,i):
        """ TC:O(log n) """
        i = i+self.n-1
        self.segmentTree[i] = x
        while(i>0):
            if(i%2==1):
                self.segmentTree[(i-1)//2] = self.segmentTree[i] + self.segmentTree[i+1]
            else:
                self.segmentTree[(i-1)//2] = self.segmentTree[i-1] + self.segmentTree[i]
            i = (i-1)//2
        print(self.segmentTree)     
        
    
    def rangeSum(self,i,j):
        """
        If i is in odd/left move to parent ,else if it is in even/right move to next element parent.
        If j is in even/right move to parent ,else if it is in odd/left move to next element parent.
        TC: O(log n)"""
        i = i+self.n-1
        j = j+self.n-1
        summ=0
        while(i<=j):
            if(i%2==0):
                summ += self.segmentTree[i]
                if(i==0):
                    break
                i+=1
            if(j%2==1):
                summ +=self.segmentTree[j]
                j-=1
            i = (i-1)//2
            j = (j-1)//2
        return summ
        
        
        

rangeObj = RangeSum([1,3,6,-2,0,1,5,0])
summ = rangeObj.rangeSum(0,7)
print(summ)
rangeObj.update(10,0)
            
            
    