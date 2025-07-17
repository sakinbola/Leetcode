class Solution(object):

    # thought process i first check for edge cases 
    # then i reduce m and n by 1 to line up with the last element in the arrays     
    # i have the total length of the num2 array including 0's in j 
    # i then while m and n are both greater than 0 iterate from the back
    # if nums2 element is bigger it goes in j , if num1 element is bigger it goes in j / j always increments down
    # when the while loop is done if num1 element so m is finished then its done because
    # num1 is already inn num1 
    # if n >0 then i made the last elements = nums 2 elements 

    # then num1 is printend 
    def merge(self, nums1, m, nums2, n):
        # arrays sorted in increasing order 
        # final array should be in nums1 , nums1 has total length 

        if m==0:
            for i in range(0,len(nums1)):
                nums1[i] = nums2[i]
            return nums1
        
        if n==0:
            return nums1
        
        # edge cases 


        # to do this i will compare nums2 to nums1 i will have a pointer in nums1 moving up to nums2 value if nums2 value is greater it wil be input everyhting will be moved to the right 

        m=m-1
        n=n-1
        j = len(nums1)-1

        while m>=0 and n>=0:
            if nums2[n] > nums1[m]:
                nums1[j] = nums2[n]
                n = n-1
            else:
                nums1[j] =  nums1[m]
                m = m-1
            j-=1
            
        while n >= 0:
                nums1[n] = nums2[n]
                n-=1

        print(nums1)


# same solution but 0ms why ?

class Solution(object):
    def merge(self,nums1,m,nums2,n):
# cant you do this from the back
        i = m - 1
        # pointer for num1 spot in num1
        j = n - 1
        # pointer for num2 spot in num2

        k = m+n-1
        # pointer for last positon in nums1

        while k>=0:
            if i>=0 and j>=0:
                # if nums1[i] == nums2[j]:
                #     nums1[k] =  nums1[i]
                #     k-=1
                #     nums1[k] = nums2[j]
                #     i-=1
                #     j-=1
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i-=1
                else:
                    nums1[k] =  nums2[j]
                    j-=1
            elif j>=0:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        