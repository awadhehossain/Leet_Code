class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        #Convert all digits to a string and join them to form the number string
        num_str = ""
        for digit in digits:
            num_str += str(digit) 

        #Convert string to integer
        number = int(num_str)

        #Add 1 to the number
        number += 1

        #Convert the result back to string
        new_num_str = str(number)

        #Convert each character back to integer and store in a list
        result = []
        for ch in new_num_str:
            result.append(int(ch))

        return result

