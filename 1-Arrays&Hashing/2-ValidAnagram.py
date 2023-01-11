# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using 
# all the original letters exactly once.

def isAnagram(s, t):
    
    if len(s) != len(t):
        return False
    
    mydict = {}
    
    for i in s:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1
        
    for j in t:
        if j not in mydict:
            return False
        else:
            mydict[i] -= 1
            
    return all(x==0 for x in mydict.values())

# Hashmap used because creating new key value pair and accessing it is O(1).
# create a count for each letter in one of the strings. Iterate through other string and subtract from value if letter is
# present in the dictionary's keys
# check if all elements in dictionary are zero.
# Time and Space Complexity is O(n)
