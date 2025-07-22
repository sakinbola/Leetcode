class Solution(object):
    def isValid(self, s):
        # so instantly think stack question / in and out question 
        # you can count unlimited opening brackets but in that same order you need to count closing brackets 

        if len(s) == 1:
            return False 
        closing_char = [")","]","}"]

        stack_char = []
        for i in s:
            if i in closing_char:
                if len(stack_char) == 0:
                    return False
                element = stack_char.pop()
                print(element,i)

                if element == "(" and i == ")":
                    pass
                elif element == "[" and i == "]":
                    pass
                elif element == "{" and i == "}": 
                    pass
                else:
                    return False
            else:            
                stack_char.append(i)
            
        if len(stack_char) > 0:
            return False
        
        return True 

            
        """
        :type s: str
        :rtype: bool
        """

# beat 5.18 eeeee