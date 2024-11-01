# problem link
# https://www.geeksforgeeks.org/problems/second-largest3735/1

"""
Given an array arr, return the second largest element from an array. If the second largest element doesn't exist then return -1.
Difficulty : Easy
"""

from typing import List

def find_second_largest(arr: List[int])-> int:
    if len(arr)< 2:
        return -1
    largest = second_largest = float('-inf')
    for val in arr:
        if val > largest:
            second_largest = largest
            largest = val
        elif largest > val > second_largest:
            second_largest = val
    return second_largest if second_largest != float('-inf') else -1

if __name__ == "__main__":
    arr = [-1, -5, 6, 2, 4, 0, 3]
    print(find_second_largest(arr))
