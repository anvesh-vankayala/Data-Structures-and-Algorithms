## Sort Colors


# Dutch National Flag Approach.


# How 3 pointers are used : 
## index 0 to  low - 1 : 0's  
## index low to mid - 1 : 1's
## index mid to high : unsorted part of list.
## index high + 1 to n - 1 : 2's

 # Time Complexity : O(n)
 # Space Complexity : O(1)

from typing import List


def sortColors(nums: List[int]) -> None:
        low = mid = 0
        high = len(nums)-1
        
        def swap(li,ele1, ele2):
            li[ele2], li[ele1] = li[ele1], li[ele2]
            return li

        while mid < high+1:
            if nums[mid] == 0:
                nums = swap(nums,mid,low)
                mid+=1
                low+=1
            elif nums[mid] == 1:
                mid+=1
            elif nums[mid] == 2:
                nums = swap(nums,mid,high)
                high-=1
        return nums


print(sortColors([2,0,2,1,1,0]))  
print(sortColors([2,0,1]))  
        
        
        