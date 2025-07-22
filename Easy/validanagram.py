from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        # i instantly think counter hash map make sure there both equal 

        if Counter(s) == Counter(t):
            return True
        else:
            return False 
        
# 55 seconds 