"""
### Merge Sort ###

Merge sort is a divide-and-conquer algorithm that divides a list into two
halves, sorts each half, and then merges the sorted halves to produce a single
sorted list. The merge sort is a stable sort, meaning that the relative order
of equal elements is preserved in the sorted list. It's the most reliable sorting
algorithm and is often used as the default sorting algorithm in many programming
languages.

Complexity: O(nlogn)
"""

def mergeSort(values):
  # The base case for the recursion is when the list has zero or one element
  if len(values) <= 1:
    return values
  # We divide the list into two halves
  middle_index = len(values) // 2
  # We then recursively call merge_sort on the two sub-lists
  left_values = mergeSort(values[:middle_index])
  right_values = mergeSort(values[middle_index:])
  # We then merge the two sorted sub-lists
  sorted_values = []
  left_index = 0
  right_index = 0
  # We iterate over the two sub-lists and merge them by always 
  # selecting the smallest element
  while left_index < len(left_values) and right_index < len(right_values):
    if left_values[left_index] < right_values[right_index]:
      sorted_values.append(left_values[left_index])
      left_index += 1
    else:
      sorted_values.append(right_values[right_index])
      right_index += 1
  # We then append the remaining elements to the sorted list
  sorted_values += left_values[left_index:]
  sorted_values += right_values[right_index:]
  return sorted_values

if __name__ == "__main__":
  # Example: 5 _> 2 3 9 2 2
  n = int(input())
  values = list(map(int, input().split()))
  # Result: 2 2 2 3 9
  print(' '.join(map(str, mergeSort(values))))