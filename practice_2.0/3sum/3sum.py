from typing import List

# TC : 
# For two loops : O(n^2) - Fixing one () element and checking for other two
# For sorting : O(n . log(n))
# For checking duplicates : O(n) - Checking for duplicates in the inner loop

# SC : 
# For sorting : O(n) - Sorting the list
# For op_li : O(n) - Storing the result
def threeSum(li: List[int]) -> List[List[int]]:
    op_li = []
    if len(li) < 3: return []
    if all(x == 0 for x in li): return [[0, 0, 0]]
    
    li = sorted(li) ## TC : O(n . log(n))
    
    for i in range(len(li)):
        if i>0 and li[i] == li[i-1]: continue
        j = i+1
        k = len(li)-1
        
        while j<k:
            res = -(li[j]+ li[k])
            if li[i] == res:
                op_li.append([li[i],li[j],li[k]])
                j+=1
                k-=1
                while j<k and li[j] == li[j-1] : j+=1
                while j<k and li[k] == li[k+1] : k-=1
            elif li[i] < res:
                k-=1
            else: # li[i] > res
                j+=1
             
    return op_li
    
# print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([3,0,-2,-1,1,2]))