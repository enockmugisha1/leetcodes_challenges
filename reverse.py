class Solution:
    def reverse(self, x: int) -> int:
        # Convert the integer to a string
        y = str(x)
        
        # Check if the number is negative
        if y[0] == '-':
            # Reverse the string without the negative sign and convert back to int
            reversed_y = '-' + y[:0:-1]  # Reverse excluding the first character
        else:
            # Reverse the string and convert back to int
            reversed_y = y[::-1]

        # Convert the reversed string back to an integer
        reversed_int = int(reversed_y)

        # Handle integer overflow if needed (depending on your requirements)
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0  # Return 0 if it overflows

        return reversed_int

# Example usage
solution = Solution()
z = solution.reverse(123)
print(z)  # Output: 321

z_negative = solution.reverse(-123)
print(z_negative)  # Output: -321
