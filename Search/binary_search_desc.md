# Binary Search

 Here we are implementing a binary search that returns the index of the target

 Binary search takes a list and target value. It will check if the middle
 value equals the target; if not the half in which the target cannot lie is
 removed and we continue this process on the remaining list. If the search
 ends with the remaining half being empty, the target is not in the array.

 This algorithm runs in O(log[n]) as for each iteration we are removing half
 the list.