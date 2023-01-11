# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums
# except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExceptSelf(nums):

    arrlength = len(nums)
    sol = [1] * arrlength
    pre, post = 1, 1

    for i in range(arrlength):
        sol[i] *= pre
        pre = pre * nums[i]
        sol[arrlength - i - 1] *= post
        post = post * nums[arrlength - i - 1]

# make solution array of 1s with length equal to input
# make pre, post variables to denote product of all elements pre current element and post current element
# loop through array
# solution array element should be product of pre and post. pre of 0 element is nothing so 1.
# multiple pre with current input element so that the pre of next element would have the current element in its pre
# solution array element with index arrlength -i -1 is multiplied with post. post in first iteration is 1 and arrlength-i-1
# element in first iteration is last element. since last element has no post it's post is 1
# as we go through the array we calculate pre by multiplying current element with pre and post by multiplying the complementary
# arrlength - i - 1 element with post
