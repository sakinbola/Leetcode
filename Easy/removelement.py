# first try edge cases 

# thought process

#  I create an element to track the last. I create an 
# element to track the duplicates. I create an element 
# to iterate. My function ends when the iterator plus 
# the duplicates are less than the last element. If it 
# equals, it goes from the back, it does a while loop 
# from the back, uh, checking for duplicates. When it 
# doesn't have a duplicate anymore, you know that's 
# where you are. You can switch the elements and 
# you're fine. It iterates up, though the answer '
# 'is the length minus the number of duplicates you '
# 'found. It feels very easy. It feels like it should '
# 'make sense, but then'
#  ' I can't even get past a few test cases. 

class Solution(object):
    def removeElement(self, nums, val):
            # Rules return the first k elements are elemnts not equal to val 
            # return k the number of elements not equal to val 

            if len(nums) == 1:
                if nums[0] == val:
                    return 0


            j = len(nums)-1
            # last element in array 
            k = 0
            # counter for duplicates 
            i = 0
            # iterator 
            while i + k  < len(nums) - 1:
                print(i,k)
                if nums[i] == val:
                    while j >= 0 and nums[j] == val:
                        k+=1
                        j-=1
                        print(k)
                    nums[i] = nums[j]
                    nums[j] =  val
                    k+=1
                    j-=1
                

                i+=1
            
            print(nums)
            print(len(nums)-k)

            return len(nums)-k 
                
                

# my approach but better

def removeElement(nums, val):
    i = 0
    j = len(nums) - 1

    while i <= j:
        if nums[i] == val:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1  # Reduce the considered array size from the back
        else:
            i += 1  # This element is good, just move forward

    # After loop ends, all non-val are in front (0 to j), duplicates at the back (j+1 to end)
    # Number of non-duplicates is j+1
    return j + 1


# easiest approach 
class Solution(object):
    def removeElement(self, nums, val):

        # two pointer pattern 
        
        position_insert = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[position_insert] = nums[i]
                position_insert +=1
        
        return position_insert



            
        