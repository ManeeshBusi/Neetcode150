# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can
# trap after raining.

def trap(height):
    if len(height) < 3:
        return 0

    vol, l, r = 0, 0, len(height)-1
    lmax, rmax = 0, 0

    while l < r:
        lmax, rmax = max(height[l], lmax), max(height[r], rmax)
        if height[l] <= height[r]:
            vol += lmax - height[l]
            l += 1
        else:
            vol += rmax - height[r]
            r -= 1
    return vol
