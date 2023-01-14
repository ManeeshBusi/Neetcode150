# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they
# add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def twoSum(numbers, target):

    # dict = {}
    # i = 0
    # while i < len(numbers):
    #     if (target-numbers[i] in k):
    #         return [k[target - numbers[i]] + 1, i + 1]
    #     dict[numbers[i]] = i
    #     i += 1

    l, r = 0, len(numbers)-1
    while l < r:
        if (numbers[l]+numbers[r] > target):
            r -= 1
        if (numbers[l]+numbers[r] < target):
            l += 1
        if (numbers[l]+numbers[r] == target):
            return [l+1, r+1]
