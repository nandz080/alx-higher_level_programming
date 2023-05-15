#!/usr/bin/python3

def max_integer(my_list=[]):
    # Check if the list is empty
    if len(my_list) == 0:
        return None
    
    # Initialize the maximum value to the first element of the list
    max_value = my_list[0]
    
    # Iterate over the remaining elements of the list
    for num in my_list[1:]:
        # Update the maximum value if a larger number is found
        if num > max_value:
            max_value = num
    
    return max_value
