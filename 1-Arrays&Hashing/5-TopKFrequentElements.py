# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent(nums, k):

    counter = {}
    freq = [[] for i in range(len(nums) + 1)]

    for i in nums:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    for n, c in counter.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

# used hashmap to store the element and number of times it occurs. this is O(n)
# then in an array of arrays created before (freq), pushed the element into the array at index that is equal to it's frequency
# looped in reverse through frequency and appended k elements into the answer array
