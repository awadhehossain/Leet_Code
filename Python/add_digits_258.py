class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while num >= 10:
            total = 0
            for digit in str(num):
                total += int(digit)  
            num = total  
        return num 
