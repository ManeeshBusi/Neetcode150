# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element 
# is distinct.

def containsDup(nums):
    
    numdict = {}
    for i in nums: 
        if i not in numdict:
            numdict[i] = i
        else:
            return True
    return False

# used hashmap/dictionary since searching in dict is O(1)
# time complexity is O(n) since we traverse through the whole array(worst case)
# space complexity is O(n) since we might have to store every element of the array in it (worst case)