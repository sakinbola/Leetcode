class Solution(object):
    def isPalindrome(self, s):
        # convert uppercase to lower
        s = s.lower()
        
        # remove all white space
        s = "".join(s.split())

        # remove all non alphanumeric characters 
        new_s = []
        for char in s:
            if char.isalnum():
                new_s.append(char)

        s = "".join(new_s)

        print(s)

        if s == s[::-1]:
            return True 
        else:
            return False


        """
        :type s: str
        :rtype: bool
        """
        