#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create an empty list to store the results
    result = []
    
    # Iterate over the elements of the original list
    for num in range(len(my_list)):
        # Check if the number is divisible by 2
        if my_list[num] % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    
    return result
