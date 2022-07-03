"""
Convert a number to string using the standard phone keyboard:

    1   | 2 abc | 3 def
--------+-------+--------
  4 ghi | 5 jkl | 6 mno
--------+-------+--------
  7 pqrs| 8 tuv | 9 wxyz
--------+-------+--------
        | 0     |

assert phone_string("226222") == "bmc"
"""
import re

phone_dial_pad = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


def phone_string(s):
    # Validate input using regular expression.
    # (development by contract, validate input and then only process it)
    validate_input(s)

    result = ""
    num_str = str(s)
    i = 0
    while i < len(num_str):
        key = num_str[i]
        j = i+1

        # below method get_letter() takes care of finding right letters
        # this even considers if that digit is pressed multiple time
        # e.g. if '2' is pressed 1, 4, 7, 10.... times, this should represent letter 'a'

        j, letter = get_letter(j, key, num_str)
        result += letter

        i = j   # We need to adjust 'i' as 'j' might have advanced ahead to 'i'
    print("result = " + result)
    return result


'''
This method helps in identifying correct letter to pick up for sequence of digit pressed
e.g. 2 == 'a', 22 == 'b', 222=='c', 2222 == 'a'
and  9 == 'w', 99 == 'x', 999=='y', 9999 == 'z', 99999 == 'w'

It returns the index (in the origin string) and the letter at that index
'''


def get_letter(j, key, num_str):
    # 'v' will represent exact vertex of a letter on a key
    # e.g. v == 1, where key == 2  ('abc') then it will represent letter 'b'

    v = 0
    while j + v < len(num_str) and key == num_str[j + v]:
        v += 1
        if (key in ['7', '9'] and v > 3) or (key not in ['7', '9'] and v > 2):
            j += v
            v = 0
        print("key: {}, j : {}, v : {}".format(key, j, v))
    j += v
    letters_on_key = phone_dial_pad.get(num_str[j-1])
    letter = ""
    if letters_on_key is not None:  # this condition is added to eliminate '0' and '1'
        letter = letters_on_key[v]
    return j, letter


def validate_input(s):
    if s is None or not isinstance(s, str):
        print("Invalid input, please enter digits on phone dialing pad")
        raise ValueError("Invalid Input, please enter digits on phone dialing pad")
    # Use regX to check if input number contains only numbers
    if not re.match('^\\d*$', s):
        print("Make sure input string contains only numbers")
        raise ValueError("Make sure input string contains only numbers")

    return True


# Test for correctness of the code
assert phone_string("226222") == "bmc"
assert phone_string("8884445577726") == "vikram"

# Some interesting test case, where one can just keep on dialing same key on phone's dialing pad
assert phone_string("222222222") == "c"
assert phone_string("99999") == "w"

# '0' and '1' has no char representation
assert phone_string("111") == ""
assert phone_string("0") == ""
