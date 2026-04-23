# # Binary Search 
# arr_1 = list(range(1, 101))

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     print(right)

#     while left <= right:
#         mid = (left + right) // 2
#         mid_value = arr[mid]

#         if mid_value == target:
#             return mid
#         elif mid_value < target:
#             left = mid + 1 
#         else:
#             right = mid - 1
    
#     return -1

# result = binary_search(arr_1, 56)
# print(result)

# 1.1 List of names
'''
Suppose you have a sorted list of 128 names, and you’re searching 
through it using binary search. What’s the maximum number of steps 
it would take?

Answer: 7 because 2^7 equals 128 names
'''

# 1.2 Double the size
'''
“Suppose you double the size of the list. What’s the maximum number of steps now?”

Answer: 8 steps max for double the size of the array
'''

# 1.3 Phone number in the phone book
'''
You have a name, and you want to find the person’s phone number in the 
phone book.”

Answer: O(log n)
'''

# 1.4
'''
“You have a phone number, and you want to find the person’s name in the 
phone book. (Hint: You’ll have to search through the whole book!)”


Answer: O(n)
'''
