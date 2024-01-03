def check_sum(num_list):
    for first_num in range(len(num_list)):
        for second_num in range(first_num, len(num_list)):
            if num_list[first_num] + num_list[second_num] == 0:
                print(f"Pair found: {num_list[first_num]} and {num_list[second_num]}")
                return True  # Return True if sum is zero for any pair of numbers
    return False  # Return False if no such pair is found

# Example usage
numbers = [2, -2, 3, -3, 5]
result = check_sum(numbers)
print(result)
    

"""
implement the check_sum() 
function which takes in a list 
and returns True if the sum of two numbers in the list is zero. 
If no such pair exists, return False.
"""