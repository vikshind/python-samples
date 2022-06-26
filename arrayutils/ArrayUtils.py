class ArrayUtils:
    # methods

    def print_array(self, my_array):
        print("Printing array: ")
        buffer = ""
        for i in range(0, len(my_array)):
            buffer = buffer + str(my_array[i]) + " "
        print(buffer)

    def print_reverse(self, my_array):
        if isinstance(my_array, list):
            print("Array in reverse order: ")
            # Loop through the array in reverse order
            buffer = ""
            for i in range(len(my_array) - 1, -1, -1):
                buffer = buffer + str(my_array[i]) + " "
            print(buffer)
        else:
            print("Input is not an array")

    def reverse(self, my_array):
        rev = ''
        for i in range(len(my_array), 0, -1):
            rev = rev.join(str(my_array[i-1]))
        return rev


def main():
    # Initialize array
    arr = [1, 2, 3, 4, 5, 0]
    # Instantiate arrayUtils
    array_util = ArrayUtils()

    # Try out different methods of ArrayUtils.
    array_util.print_array(arr)
    array_util.print_reverse(arr)
    array_util.reverse(arr)
    print(arr)


if __name__ == "__main__":
    main()