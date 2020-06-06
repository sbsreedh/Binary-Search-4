
#Two pointers Solution:
#Time complexity:O(log(m+n))
#Space Complexity:O(k), k is the number of elements being returned. 
#Algorithm:
#1. Initialise two pointers ptr1 ptr2 pointing on first element in each array given, 
#2. Compare the elements, 
######if they are equal append them to result
######increment the pointer whose value is lesser. 
#3. return the resultant array

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result=[]
        ptr1=0
        ptr2=0
        while ptr1<len(nums1) and ptr2<len(nums2):
            if nums1[ptr1]<nums2[ptr2]:
                ptr1+=1
            elif nums1[ptr1]>nums2[ptr2]:
                ptr2+=1
            
            else:
                nums1[ptr1]==nums2[ptr2]
                result.append(nums1[ptr1])
                ptr1+=1
                ptr2+=1
            
        return result
