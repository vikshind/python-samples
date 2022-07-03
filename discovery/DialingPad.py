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


class DialingPad:
    dial_pad = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    '''
    Returns the letters representing dialed sequence of digits on a phone
    e.g.
    "226222" == "bmc"
    "8884445577726" == "vikram"
    '''
    def get_letters(self, digits):
        result = ""
        PATTERN_STR = r'(\d)\1*'
        pattern = re.compile(PATTERN_STR)
        # find all matches to groups
        for match in pattern.finditer(digits):
            # extract words
            group = match.group()
            letter = self.__get_letter(group)
            result += letter
        return result

    '''
    This method helps in identifying correct letter to pick up for sequence of digit pressed
    e.g. 2 == 'a', 22 == 'b', 222=='c', 2222 == 'a'
    and  9 == 'w', 99 == 'x', 999=='y', 9999 == 'z', 99999 == 'w'
    '''
    def __get_letter(self, group):
        letters = self.dial_pad.get(group[0])
        if letters is None:
            return ""
        idx = 0
        num_letters = len(letters)
        grp_length = len(group)
        if grp_length > num_letters:
            idx = (grp_length % num_letters) - 1
        else:
            idx = grp_length - 1
        return letters[idx]


# Driver Code
if __name__ == "__main__":
    dp = DialingPad()

    # Test for correctness of the code
    assert dp.get_letters("226222") == "bmc"
    assert dp.get_letters("8884445577726") == "vikram"

    # Some interesting test case, where one can just keep on dialing same key on phone's dialing pad
    assert dp.get_letters("222222222") == "c"
    assert dp.get_letters("99999") == "w"

    # '0' and '1' has no char representation
    assert dp.get_letters("111") == ""
    assert dp.get_letters("0") == ""

