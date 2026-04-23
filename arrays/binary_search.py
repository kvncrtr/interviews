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