class Solution(object):
    def search(self, nums, target):
        # thinking merge sort instantly splitting the repeadetly dont really know how the code looks
        # o of n soluiong ovbiosuly 

        left = 0
        right = len(nums) - 1


        while left <= right: 
            mid = left + ((right - left)//2) 
            print(mid)

            if nums[mid] == target:
                return mid      
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid +1
            

        return -1 

                
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        