# -*- coding: utf-8 -*-
"""
using data structure quad tree

@author: Anvesh
"""


class Range:
    
    def __init__(self,i1,j1,i2,j2):
        self.i1 =i1
        self.j1 =j1
        self.i2 =i2
        self.j2 =j2
        
        

class TreeNode:
    
    def __init__(self,i1,j1,i2,j2,val):
        self.range = Range(i1,j1,i2,j2)
        self.summ = None
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        if val is not None:
            self.secondInit(val)
    
    def secondInit(self,val):
        self.summ = val
    



class RangeSum:
    
    def __init__(self,matrix):
        """Preprocess - TC:O(n^2)"""
        self.root = self.build(0,0,len(matrix)-1,len(matrix[0])-1,matrix) 
        self.width = len(matrix[0])-1
        self.height = len(matrix)-1
                        
    def checkNode(self,node):
        if node is None:
            return 0
        else:
            return node.summ
    
    def build(self,i1,j1,i2,j2,matrix):
        if(i1>i2 or j1 >j2):
            return
        if(i1 == i2 and j1 == j2 ):
            return TreeNode(i1,j1,i1,j1,matrix[i1][j1])
        rowMid = (i1)+((i2-i1)//2)
        colMid = (j1)+((j2-j1)//2)
        node = TreeNode(i1,j1,i2,j2,None)
        node.child1 = self.build(i1,j1,rowMid,colMid,matrix)
        node.child2 = self.build(i1,colMid+1,rowMid,j2,matrix)
        node.child3 = self.build(rowMid+1,j1,i2,colMid,matrix)
        node.child4 = self.build(rowMid+1,colMid+1,i2,j2,matrix)
        node.summ = self.checkNode(node.child1)+self.checkNode(node.child2)+self.checkNode(node.child3)+self.checkNode(node.child4)
        return node
        
    def update(self,i,j,x):
        """TC:log(4) n^2"""
        self.updatAux(i,j,x,self.root)
        
    
    def updatAux(self,x,y,val,node):
        if(node.range.i1==x and node.range.j1==y and node.range.i2==x and node.range.j2==y):
            node.summ = val
            return
        colMid= (node.range.j1)+((node.range.j2-node.range.j1)//2)
        rowMid = (node.range.i1)+((node.range.i2-node.range.i1)//2)
        if(y <= colMid):
            if(x <= rowMid):
                self.updatAux(x,y,val,node.child1)
            elif(x > rowMid):
                self.updatAux(x,y,val,node.child3)
        elif(y >colMid):
            if(x <= rowMid):
                self.updatAux(x,y,val,node.child2)
            elif(x > rowMid):
                self.updatAux(x,y,val,node.child4)
        node.summ = self.get(node.child1)+self.get(node.child2)+self.get(node.child3)+self.get(node.child4)
    
    def get(self,node):
        if node is not None:
            return node.summ
        else:
            return 0
        
    
    def rangeSum(self,x1,y1,x2,y2):
        """TC:log(4) n^2"""
        summ = self.rangeSumAux(x1,y1,x2,y2,self.root)
        return summ
    
    def rangeSumAux(self,x1,y1,x2,y2,node):
        if(node.range.i1==x1 and node.range.j1==y1 and node.range.i2==x2 and node.range.j2==y2):
            return node.summ
        colMid= (node.range.j1)+((node.range.j2-node.range.j1)//2)
        rowMid = (node.range.i1)+((node.range.i2-node.range.i1)//2)
        summ = 0
        if(y2 <= colMid):
            if(x2 <= rowMid):
               summ = self.rangeSumAux(x1,y1,x2,y2,node.child1)
            elif(x1 > rowMid):
               summ = self.rangeSumAux(x1,y1,x2,y2,node.child3)
            else:
               summ = self.rangeSumAux(x1,y1,rowMid,colMid,node.child1)+ self.rangeSumAux(rowMid+1,y1,x2,y2,node.child3)
            
        elif(y1>colMid):
            if(x2 <= rowMid):
               summ = self.rangeSumAux(x1,y1,x2,y2,node.child2)
            elif(x1 > rowMid):
               summ = self.rangeSumAux(x1,y1,x2,y2,node.child4)
            else:
               summ = self.rangeSumAux(x1,y1,rowMid,y2,node.child2)+self.rangeSumAux(rowMid+1,colMid+1,x2,y2,node.child4)
        elif(x2<=rowMid):
            summ = self.rangeSumAux(x1,y1,rowMid,colMid,node.child1)+self.rangeSumAux(x1,colMid+1,rowMid,y2,node.child2)
        elif(x1>rowMid):
            summ = self.rangeSumAux(rowMid+1,y1,x2,colMid,node.child3)+self.rangeSumAux(rowMid+1,colMid+1,x2,y2,node.child4)
        else:
            summ = self.rangeSumAux(x1,y1,rowMid,colMid,node.child1)+self.rangeSumAux(x1,colMid+1,rowMid,y2,node.child2)+self.rangeSumAux(rowMid+1,y1,x2,colMid,node.child3)+self.rangeSumAux(rowMid+1,colMid+1,x2,y2,node.child4)
        return summ
    
     # Only used for printing quad tree::: no logic for range problem: Ignore this method
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
                if node and node.child1:
                    buf.append(node.child1)
                    nextCount += 1
                else:
                    buf.append(None)
                if node and node.child2:
                    buf.append(node.child2)
                    nextCount += 1
                else:
                    buf.append(None)
                if node and node.child3:
                    buf.append(node.child3)
                    nextCount += 1
                else:
                    buf.append(None)
                if node and node.child4:
                    buf.append(node.child4)
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

     
from random import randint        
matrix = [[randint(0, 9) for i in range(3)] for i in range(3)]
print(len(matrix[0]))
print("-------------------")
print(matrix)
print("-------------------")
obj = RangeSum(matrix)
obj.printTree()

print(obj.rangeSum(0,0,1,1))
obj.update(0,1,10)
obj.printTree()
print(obj.rangeSum(0,0,1,1))
