from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        # Move the print statement and return outside the outer loop
        print('No number found')
        return []

# Create an instance of the Solution class
solution = Solution()

# Example input
nums = [3, 2, 4]
target = 6

# Call the twoSum method
result = solution.twoSum(nums, target)  # Corrected extra parenthesis
print(result)  # Output the result