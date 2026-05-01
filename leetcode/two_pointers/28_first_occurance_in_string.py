'''
Given two strings needle and haystack, return the 
index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Notes:
1. The needle has to be countingsly inside of the the haystack
2. the needle has to be a word 
3. pointer 'start' has to keep tabs of the first occurance
4. pointer end has to read and record each char that is a match to the 
    haystack
5. must output the start index if not found then output -1
'''

def needle_search(haystack, needle):
	n_len = len(needle)
	h_len = len(haystack)
	
	for start in range(h_len - n_len + 1):
		for end in range(n_len):
			if haystack[start + end] != needle[end]:
				break
			if end == n_len - 1:
				return start

	return -1

result = needle_search('racecar', 'car')
print(result)