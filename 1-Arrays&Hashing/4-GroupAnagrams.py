# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.

def groupAnagrams(strs):
    srts = [''.join(sorted(word)) for word in strs]
    ans = {}

    for i, w in enumerate(srts):
        if w in ans:
            ans[w].append(strs[i])
        else:
            ans[w] = [strs[i]]

    return ans.values()

# sorted(string) in this case takes a word/string and sorts all the letters and returns a list of letters.
# enumerate(list) will return (index, value) in the loop
