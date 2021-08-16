# Jump Search

Here we are implementing a jump search that returns the index of the target

Jump search takes a list, target value, and block size ('m') to jump. It will jump
indices by the block size until it reaches an element that is greater than
the target. If it does come across such a value, it will then do linear
search in the last block. If it cannot find an element larger it will be
forced to linear search in the last block.

This algorithm runs in O((n/m)+(m-1)). This worst case occurs when the
target is not in the list. The algorithm is forced to do m-1 iterations for
each block and then iterate n/m times in the last block.