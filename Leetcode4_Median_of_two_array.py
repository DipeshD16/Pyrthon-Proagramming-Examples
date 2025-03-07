'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1) #store the length of nums1
        y = len(nums2) #store the length of nums2
    
    #this function ensures that num1 is shorter array if num2 is smaller then it swaps both the array
        if x>y:
            return self.findMedianSortedArrays(nums2, nums1)
    #low and high defines the search range for partitioning nums1
    #binary search will be applied to nums1 within this range  
        low = 0
        high =x
    #performs partitioning
    #px is the partitioning index for nums1
    #py is the partitioning index for nums2

        while low <=high:
            px = (low +high)//2
            py = ((x+y+1)//2) - px #the formula ensures the left half contains (x+y+1)/2 elements

            maxLeftX = float('-inf') if px == 0 else nums1[px-1] #largest elements in the left half nums 1
            minRightX = float('inf') if px==x else nums1[px]     #smallest elements in the right half of num1

            maxLeftY = float('-inf') if py == 0 else nums2[py-1] #largest element in the left half of nums2
            minRightY = float('inf') if py == y else nums2[py]   #smallest elements in the right half of nums2
            #check partioning
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                #compute the median
                if (x+y)%2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                else:
                    return max(maxLeftX, maxLeftY)
            #adjust search range if partition is correct
            elif maxLeftX > minRightY:
                high = px-1
            else:
                low = px+1




