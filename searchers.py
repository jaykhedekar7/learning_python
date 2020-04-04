# -*- coding: utf-8 -*-
"""
This is a practise script file.
"""

data = [12,21,43,1,2,3,4,55,43,27,7,89,42]

total = sum(data)

#linear data search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
        
#binary search iterative process
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    
    while low<=high:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif mid < target:
            high = mid - 1
        else:
            low = mid + 1
    return False

#binary search recursive
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            binary_search_recursive(data, target, low, mid-1)
        else:
            binary_search_recursive(data, target, mid+1, high)


print(binary_search_recursive(data, 12, 0, len(data)-1))

print(binary_search_iterative(data, 12))