# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

def longestConsecutive(nums):
    longest, numarray = 0, set(nums)

    for num in numarray:
        if num - 1 not in nums:
            length = 1
            while num+length in numarray:
                length += 1
            longest = max(longest, length)

    return longest
