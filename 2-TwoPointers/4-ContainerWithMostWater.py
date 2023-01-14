# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith
# line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

def maxArea(height):
    ans, l, r = 0, 0, len(height)-1

    while l < r:
        if (height[l] <= height[r]):
            area = height[l] * (r-l)
            l += 1
            while (height[l] < height[l-1] and l < r):
                l += 1
        else:
            area = height[r] * (r-l)
            r -= 1
            while (height[r] < height[r+1] and l < r):
                r -= 1
        if area > ans:
            ans = area

    return ans
