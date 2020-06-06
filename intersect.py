
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
    
 
#HashMapSolution:
#Time complexity:O(max(m+n))
#Space Complexity:O(min(m,n))
#Algorithm:
#1.Create hashMap for the bigger array by keeping the lements and its repetition count. This is ensured by making nums1 as alaways bigger one if it is not by input itself  BY SWAPPING.
#2. Now iterate nums in nums2 and see if it exsting in hashMap , if so append to result and decrement its count. 



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # if not nums1 or not nums2 or len(nums1)==0 or len(nums2)==0:
        #     return []
        hashMap=dict()
        res=[]
        if len(nums2)>len(nums1):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        for num in nums1:
            if num not in hashMap:
                 hashMap[num]=0
            hashMap[num]+=1
        for num in nums2:
            # if num in hashMap and hashMap[num]==0 :
            #     hashMap.pop(num)
            if num in hashMap and hashMap[num]>0 :
                res.append(num)
                hashMap[num]-=1
            # else:
            #     hashMap[num]=1
        return res
                

#HBinary Search Solution:
#Time complexity:O(mlogn),n-smaller array length
#Space Complexity:O(min(m,n))
#Algorithm:
#1.Use binary search to search the element present in arr1 in arr2. 



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(nums, num):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2       
                if nums[mid] == num:
                    return mid 
                if nums[mid] > num:
                    right = mid - 1
                elif nums[mid] < num:
                    left = mid + 1
            return -1
            
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        nums1.sort()
        res = []
        for num in nums2:
            index = binary_search(nums1, num)
            if index != -1:
                res.append(nums1[index])
                nums1.pop(index)
                
        return res
        
       
