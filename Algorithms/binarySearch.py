"""
### Binary Search ###

Binary search is a divide-and-conquer algorithm that select the middle element
of a sorted array and compares it to the target value. If the target value is
less than the middle element, the algorithm searches the left subarray. If the
target value is greater than the middle element, the algorithm searches the
right subarray. If the target value is equal to the middle element, the
algorithm returns the index of the middle element. The algorithm continues 
this process until the target value is found or the subarray is empty.

This algorithm is a very efficient way to search for a target value in a sorted
array. For example, an array of 1,000,000 elements can be searched in just 20
steps using binary search, compared to 1,000,000 steps using a linear searh
(which searches each element in the array one by one).

Complexity: O(logn)
"""

def binary_search(collection, target):
  first = 0
  last = len(collection) - 1
  while first <= last:
    midpoint = (first + last) // 2
    if collection[midpoint] == target:
      return midpoint
    elif collection[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1
  return -1

if __name__ == "__main__":
  # Example: 5 _> 1 5 8 12 13 _> 8
  n = int(input())
  collection = list(map(int, input().split()))
  target = int(input())
  # Result: 2
  print(binary_search(collection, target))
  
