# Initialize variables
sum_of_odds = 0
count_of_odds = 0

# Loop through numbers from 1 to 1000
for num in range(1, 1001):
    if num % 2 != 0:  # Check if the number is odd
        sum_of_odds += num
        count_of_odds += 1

# Calculate the average
average_of_odds = sum_of_odds / count_of_odds

# Print the results
print("Sum of all odd numbers between 1 and 1000:", sum_of_odds)
print("Average of all odd numbers between 1 and 1000:", average_of_odds)
