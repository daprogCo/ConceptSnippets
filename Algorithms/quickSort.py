"""
### The Quicksort algorithm ###

Quicksort is a divide-and-conquer algorithm that uses recursion to sort a list
of elements. It works by selecting a pivot element from the list and
partitioning the other elements into two sub-lists according to whether they are
less than or greater than the pivot. The sub-lists are then sorted recursively
The base case for the recursion is when the list has zero or one element, in
which case it is already sorted.

Complexity: O(nlogn) average case, O(n^2) worst case
"""

def quickSort(values):
  # The base case for the recursion is when the list has zero or one
  if len(values) <= 1:
    return values
  less_than_pivot = []
  greater_than_pivot = []
  # We select the first element in the list as the pivot.
  pivot = values[0]
  for value in values[1:]:
    if value <= pivot:
      less_than_pivot.append(value)
    else:
      greater_than_pivot.append(value)
  # We then recursively call quicksort on the two sub-lists and concatenate
  # with the pivot value.
  return quickSort(less_than_pivot) + [pivot] + quickSort(greater_than_pivot)

if __name__ == "__main__":
  # Example: 5 _> 2 3 9 2 2
  n = int(input())
  values = list(map(int, input().split()))
  # Result: 2 2 2 3 9
  print(' '.join(map(str, quickSort(values))))

