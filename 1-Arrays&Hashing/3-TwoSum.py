# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    
    freq = {}
    
    for i in range(len(nums)):
        num = target - nums[i]
        if num in freq:
            return [freq[num], i]
        freq[nums[i]] = i

# hashmap is used. 
# time complexity is O(n) since we are iterating through the array only once
# Space complexity is O(n) since we might have to create an entry for each element in nums
    