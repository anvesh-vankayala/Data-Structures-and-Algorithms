# -*- coding: utf-8 -*-
"""
Using data structure K-D tree

@author: Anvesh
"""

class Range:
    def __init__(self,i1,j1,i2,j2):
        
        self.i1 = i1
        self.j1 = j1
        self.i2 = i2
        self.j2 = j2
        
class TreeNode:
    
    def __init__(self,i1,j1,i2,j2,val):
        
        self.range = Range(i1,j1,i2,j2)
        self.summ=None
        self.left=None
        self.right=None
        
        if val is not None:
            self.secondInit(val)
        
    def secondInit(self,val):
        self.summ = val
    
class RangeSum:
    
    def __init__(self,matrix):
        self.root = self.build(0,0,len(matrix)-1,len(matrix[0])-1,1,matrix)
   
    def checkNode(self,node):
        if node is None:
            return 0
        else:
            return node.summ
    
    def build(self,i1,j1,i2,j2,level,matrix):
        if(i1>i2 or j1>j2):
            return
        if(i1==i2 and j1==j2):
            return TreeNode(i1,j1,i2,j2,matrix[i1][j1])
        node = TreeNode(i1,j1,i2,j2,None)
        cutType = level%2 #if odd level column cut and if it is even level row cut
        if(cutType ==1):
            cutAt = (j1)+(j2-j1)//2
            node.left = self.build(i1,j1,i2,cutAt,level+1,matrix)
            node.right = self.build(i1,cutAt+1,i2,j2,level+1,matrix)
        else:
            cutAt = (i1)+(i2-i1)//2
            node.left = self.build(i1,j1,cutAt,j2,level+1,matrix)
            node.right = self.build(cutAt+1,j1,i2,j2,level+1,matrix)
        node.summ = self.checkNode(node.left) + self.checkNode(node.right)
        return node
    
    def rangeSum(self,i1,j1,i2,j2):
        summ = self.rangeSumAux(i1,j1,i2,j2,1,self.root)
        return summ
    
    def rangeSumAux(self,x1,y1,x2,y2,level,node):
        if(x1 == node.range.i1 and y1 == node.range.j1 and x2 == node.range.i2 and y2 == node.range.j2):
            return node.summ
        if(level%2 ==1):
            cutAt = (node.range.j1)+(node.range.j2-node.range.j1)//2
            if(y2<=cutAt):
                summ = self.rangeSumAux(x1,y1,x2,y2,level+1,node.left)
            elif(y1> cutAt):
                summ = self.rangeSumAux(x1,y1,x2,y2,level+1,node.right)
            else:
                summ = self.rangeSumAux(x1,y1,x2,cutAt,level+1,node.left)+ self.rangeSumAux(x1,cutAt+1,x2,y2,level+1,node.right)
        else:
            cutAt = (node.range.i1)+(node.range.i2-node.range.i1)//2
            if(x2<=cutAt):
                summ = self.rangeSumAux(x1,y1,x2,y2,level+1,node.left)
            elif(x1> cutAt):
                summ = self.rangeSumAux(x1,y1,x2,y2,level+1,node.right)
            else:
                summ = self.rangeSumAux(x1,y1,cutAt,y2,level+1,node.left)+ self.rangeSumAux(cutAt+1,y1,x2,y2,level+1,node.right)
        return summ
        
    
    def update(self,x,y,val):
        self.updateAux(x,y,val,1,self.root)
        return
    
    def updateAux(self,x,y,val,level,node):
        if(node.range.i1 == x and node.range.i2 == x and node.range.j1 == y and node.range.j2 == y):
            node.summ = val
            return
        if(level%2 ==1):
            cutAt = (node.range.j1)+(node.range.j2-node.range.j1)//2
            if(y<=cutAt):
                self.updateAux(x,y,val,level+1,node.left)
            elif(y> cutAt):
                self.updateAux(x,y,val,level+1,node.right)
        else:
            cutAt = (node.range.i1)+(node.range.i2-node.range.i1)//2
            if(x<=cutAt):
                self.updateAux(x,y,val,level+1,node.left)
            elif(x> cutAt):
                self.updateAux(x,y,val,level+1,node.right) 
        node.summ = self.checkNode(node.left)+self.checkNode(node.right)
        
    
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




from random import randint        
matrix = [[randint(0, 9) for i in range(3)] for i in range(3)]
print(len(matrix[0]))
print("-------------------")
print(matrix)
print("-------------------")
obj = RangeSum(matrix)
obj.printTree()

print(obj.rangeSum(0,0,1,1))
obj.update(1,1,1)
obj.printTree()
print(obj.rangeSum(0,0,1,1))

        
        
        
            
            
        
        
        
    