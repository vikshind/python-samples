"""
Write a function to add up squares of all the values in an array
"""
import time


'''
Solution 1 : Bruteforce solution with O(N) time complexity
Solution 2 : Just one liner solution - pytonic way
'''


# Solution 2 : Just one liner solution - pytonic way
def pythonic_sum_squared(arr):
    print("\t\tInput array length : {}".format(len(arr)))
    result = sum([num ** 2 for num in arr])
    print("\t\tOutput : {}".format(result))
    return result


'''
Solution 1 : Bruteforce solution with O(N) time complexity
'''


def sum_squared(arr):
    print("\t\tInput array length : {}".format(len(arr)))
    result = 0
    if arr is None or not isinstance(arr, list):
        print("Invalid input, please pass valid list of integers e.g. [3,4,5]")
    else:
        for i in range(len(arr)):
            if isinstance(arr[i], int):
                result += arr[i] ** 2
            else:
                raise TypeError("Element at index - {}, which is {} as it is not an integer".format(i, arr[i]))

    print("\t\tOutput : {}".format(result))
    return result


# Let's do some testing
# Test 1 : Just to check if functions are returning correct results
print("Test 1 : Check correctness")
input_array = [1, 2, 3, 4, 5]
output = 55
print("Input array      : " + str(input_array))
print("Expected output  : " + str(output))
print("\ta. Bruteforce method :")
assert sum_squared(input_array) == output

print("\tb. Pythonic method :")
assert pythonic_sum_squared(input_array) == output
print("-"*100)

# Test 2 : Check the difference is bruteforce, recursive and pythonic way of implementation of solution
print("Test 2 : Try to find optimized solution")
input_array = list(range(100000))
output = 333328333350000
print("Len(Input array) :" + str(len(input_array)))
print("Expected output  : " + str(output))
print("\ta. Time taken by Bruteforce method :")
start = time.time()
assert sum_squared(input_array) == output
end = time.time()
print("\t\tTime taken : {:.4f}".format(end - start))

print("\tb. Time taken by Pythonic method :")
start = time.time()
assert pythonic_sum_squared(input_array) == output
end = time.time()
print("\t\tTime taken : {:.4f}".format(end - start))
