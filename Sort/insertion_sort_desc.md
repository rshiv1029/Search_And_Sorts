# Insertion Sort

Here we implemented insertion sort.

If the we find an element that is not sorted properly, we compare it to its
predecessor. If this element is smaller than its predecessor, we compare it
to the elements before. Move the greater elements one position up to make space
for the swapped element.

The time complexity for this is O(n^2) due to the nested loops. The worst
case occurs when the list is in reverse order.
