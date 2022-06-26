def binary_search(low, high, condition):
    while low <= high:
        mid = (low+high)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        else:
            low = mid + 1
    return -1

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid+1] == target:
                return 'right'
            else:
                return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


def search_range(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    return first_and_last_position(nums, target)

print(search_range([2,2], 2))

# class Solution(object):
#     pass
#
# if __name__ == "__main__":
#     solution = Solution()
#     search_range([2,2], 2)
