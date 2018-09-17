# -*- coding: utf-8 -*-
"""
@author: Anvesh

Using segment tree data structure built with (pointer based segment tree)

"""


class Range:
    
    def __init__(self,l,r):
        self.l=l
        self.r=r
        

class TreeNode:
    
    def __init__(self,val,l,r):
        self.summ = None
        self.left = None
        self.right = None
        self.key = Range(l,r)
        if val is not None:
            self.secondInit(val)
    
    def secondInit(self,val):
        self.summ = val
        
        
    
class RangeSum:
    
    def __init__(self,arr):
        self.array = arr
        self.root = self.build(0,len(arr)-1,arr)
        print(self.root)
        
        
    def build(self,l,r,arr):
        """TC: O(n) """
        if(l>r):
            return None
        if(l==r):
            return TreeNode(arr[l],l,r)
        m = (l+r)//2
        temp = TreeNode(None,l,r)
        temp.left = self.build(l,m,arr)
        temp.right = self.build(m+1,r,arr)
        temp.summ = temp.left.summ + temp.right.summ
        return temp
        
    def update(self,x,i):        
        self.root =  self.updateAux(self.root,x,i)
        return
    
    
    def updateAux(self,node,x,i):
        """TC:O(log n)"""
        if(i==node.key.l and i==node.key.r):
            node.summ = x
            return x
        if(i<=node.left.key.r):
            self.updateAux(node.left,x,i)
        elif(i>=node.right.key.l):
            self.updateAux(node.right,x,i)
        node.summ = node.left.summ + node.right.summ
        return node
        
    def rangeSum(self,i,j):
        
        return self.rangeSumAux(self.root,i,j)
      
    def rangeSumAux(self,node,i,j):
        """TC:O(log n)"""
        if(node is None):
            return
        summe =0
        if(i==node.key.l and j==node.key.r):
            return node.summ
        if(i>=node.left.key.l and j<=node.left.key.r):
            summe = self.rangeSumAux(node.left,i,j)
        elif(i>=node.right.key.l and j<=node.right.key.r):
            summe = self.rangeSumAux(node.right,i,j)
        else:#((i>=node.left.key.l and j>node.left.key.r) or (i<node.right.key.l and j<=node.right.key.r)):
            summe= self.rangeSumAux(node.left,i,node.left.key.r)+self.rangeSumAux(node.right,node.left.key.r+1,j)
        return summe
       
       
          
    # Only used for printing::: no logic for range problem
    def printTree(self):
        buf = []
        output = []
        root = self.root
        if not root:
            print ('$')
        else:
            buf.append(root)
            count = 1
            nextCount = 0
            while count > 0:
                node = buf.pop(0)
                if node:
                    output.append(node.summ)
                    count -= 1
                else:
                    output.append('$')
                if node and node.left:
                    buf.append(node.left)
                    nextCount += 1
                else:
                    buf.append(None)
                if node and node.right:
                    buf.append(node.right)
                    nextCount += 1
                else:
                    buf.append(None)
                if count == 0:
                    print (output)
                    output = []
                    count = nextCount
                    nextCount = 0
            # print the remaining all empty leaf node part
            for i in range(len(buf)):
                output.append('$')
            print (output)


rangeObj = RangeSum([1,3,5,1,4,-2,0,-1])
rangeObj.printTree()
summ = rangeObj.rangeSum(0,7)
print('range summ: --------- ',summ)
rangeObj.update(0,7)
rangeObj.printTree()
summ = rangeObj.rangeSum(0,7)
print('range summ: --------- ',summ)



