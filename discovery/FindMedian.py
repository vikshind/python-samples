"""
Write a function to find the median of an array
"""
from statistics import median
import pytest

'''
Solution 1 : My own version to find_median(arr). Assuming input array will be unsorted, 
let's use QuickSort to get sorted array first.

>> Implemented tests using pytest at the bottom

Solution 2 : Directly use statistics.median()
'''


# Solution 1
def find_median(a):
    if a is None or len(a) == 0:
        print("Invalid input, please pass valid list of integers e.g. [2,0,1,3,4,5]")
        raise ValueError("Incorrect input")
    sorted_array = quicksort(a, 0, len(a)-1)
    # check for even case
    n = len(sorted_array)
    if n % 2 != 0:
        return float(a[n // 2])

    return float((a[int((n-1)/2)] + a[int(n / 2)])/2.0)


# In order to find median, input array needs to be sorted first.
# Let's try to use QuickSort for this purpose.
# Below two functions quicksort() and partition() will help us to sort an array quickly.
def partition(nums, left, right):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[right], left
    for i in range(left, right):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[right] = nums[right], nums[ptr]
    return ptr


def quicksort(nums, left, right):
    if len(nums) == 1:  # to terminate recursion.
        return nums
    if left < right:
        pi = partition(nums, left, right)
        quicksort(nums, left, pi - 1)  # Sort the left values
        quicksort(nums, pi + 1, right)  # Sort the right values
    return nums


# Time to perform some testing, In this code lets try to use 'pytest' framework.
def test_error():
    with pytest.raises(ValueError):
        find_median([])


def test_even_numbers():
    arr_even_number = [8, 6, 2, 4, 7, 3, 1, 5]
    assert find_median(arr_even_number) == 4.5
    assert median(arr_even_number) == 4.5


def test_odd_numbers():
    arr_odd_number = [8, 6, 2, 4, 7, 3, 1, 5, 0]
    assert find_median(arr_odd_number) == 4
    assert median(arr_odd_number) == 4
