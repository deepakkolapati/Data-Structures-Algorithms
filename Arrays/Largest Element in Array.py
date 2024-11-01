# problem link
# https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0

"""
Given an array arr[]. The task is to find the largest element and return it.
Difficulty : Easy
"""

from typing import List

def find_largest(arr: List[int]) -> int:
    """
    Finds and returns the largest element in an array.

    :param arr: List of integers.
    :return: The largest integer in the list. Returns -1 if the list is empty.
    """
    if len(arr) == 0:
        return -1
    max_val = arr[0]
    for val in arr[1:]:
        if val > max_val:
            max_val = val
    return max_val

if __name__ == "__main__":
    arr = [2,5,1,10,2,4,0,7]
    print(find_largest(arr))