# Python program for implementation of atoi

# A simple atoi() function


def my_atoi(text):
    res = 0

    # Iterate through all characters of
    # input string and update result
    for i in range(len(text)):
        res = res * 10 + (ord(text[i]) - ord('0'))

    return res


def my_itoa(num) -> str:
    if num == 0:
        return "0"
    is_negative = False
    if num < 0:
        num = -num
        is_negative = True

    digits = 0
    temp_number = num
    while temp_number > 0:
        temp_number = temp_number // 10
        digits += 1

    digs = ['']*digits
    for temp in range(digits - 1, -1, -1):
        digs[temp] = str(num % 10)
        num = num // 10

    result = ""
    if is_negative:
        result = "-"

    return result + "".join(digs)


def itoa(num):
    return str(num)


# Driver program
# Function calls


my_string = "1074"
print(my_atoi(my_string))

number = -420
print(my_itoa(number))
print(itoa(number))
