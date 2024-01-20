"""
Our first solution to the anagram problem will check the lengths of the strings
and then to see that each character in the first string actually occurs in the second.
If it is possible to “checkoff” each character, then the two strings must be anagrams.
Checking off a character will be accomplished by replacing it with the special Python
value None. However, since strings in Python are immutable, the first step in the
process will be to convert the second string to a list. Each character from the
first string can be checked against the characters in the list and if found,
checked off by replacement.
"""

import time
def anag(s1, s2):

    start = time.time()

    res = False
    s2list = list(s2)

    for letter in s1:
        for j in range(len(s2list)):
            if s2list[j] == letter or s2list[j] == None:
                s2list[j] = None
                res = True
            else:
                res = False

    end = time.time()

    print(s2list)
    print(s2list == None)
    print(res)

    return res, end-start

s1 = 'abcd1xxab'
s2 = 'xdc1aaxbb'
print("Anagram: ", anag(s1, s2))

