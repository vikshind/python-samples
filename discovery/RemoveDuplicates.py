"""
Remove duplicate chars from a string,
keeping the first occurrence of each character.
"""
from collections import OrderedDict

'''
Solution 1 : Just iterate through each char and keep track of visited characters using Dict Data-Structure.
Solution 2 : Using collections.OrderedDict
'''


# Solution 1 : Just iterate through each char and keep track of visited characters using Dict Data-Structure.
def deduplicate(s):
    result = ""
    if not isinstance(s, str):
        print("Invalid input, please pass on valid string e.g. 'hello beautiful world'")
    else:
        char_dict = {}
        for x in s:
            if not char_dict.__contains__(x):
                char_dict.__setitem__(x, x)
                result += x
    print("de-duplicated string is : {}".format(result))
    return result


'''
Solution 2 : Using collections.OrderedDict
'''


def deduplicate_with_ordered_dict(s):
    return "".join(OrderedDict.fromkeys(s))


# Let's do some testing
# Test 1 : Check the desired result
original_str = "hello beautiful world"
expected_str = "helo bautifwrd"
print("Test 1 : Check correctness of the function with 'original string'={}".format(original_str))
assert deduplicate(original_str) == expected_str
assert deduplicate_with_ordered_dict(original_str) == expected_str
print("-"*100)

# Test 2 : Check in case of 4 blank spaces, it should return only 1 blank space
original_str = "    "
expected_str = " "
print("Test 2 : Check in case of 4 blank spaces, it should return only 1 blank space")
assert len(deduplicate(original_str)) == 1
assert len(deduplicate_with_ordered_dict(original_str)) == 1
print("-"*100)

# Test 3 : Check if it handles TABs as well
original_str = "\ttab\t"
expected_str = "\ttab"
print("Test 3 : Check it handles TABs as well")
assert len(deduplicate(original_str)) == 4
assert len(deduplicate_with_ordered_dict(original_str)) == 4
print("-"*100)

# Test 4 : Check if it handles NewLine characters
original_str = "new\n\n\n\nline"
expected_str = "new\nli"
print("Test 4 : Check if it handles NewLine characters")
assert len(deduplicate(original_str)) == 6
assert deduplicate(original_str) == expected_str
assert deduplicate_with_ordered_dict(original_str) == expected_str
print("-"*100)

# Test 5 : Check if code can handle larger strings with multiple lines.
original_str = "Remove duplicate chars from a string,\n\
keeping the first occurrence of each character."
expected_str = "Remov duplicathrsfng,\nk."
print("Test 5 : Check if code can handle larger strings with multiple lines.")
assert deduplicate(original_str) == expected_str
assert deduplicate_with_ordered_dict(original_str) == expected_str
print("-"*100)
