class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if the number is negative
        if x < 0:
            return False
        
        # Convert the integer to a string
        y = str(x)
        # i am gonna reversing the number as palindlome concept says 
        return y == y[::-1]

# Example usage
s = Solution()
z = s.isPalindrome(121)
print(z)
