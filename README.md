# SortNebula
Heap sort:
the funnction heapify converts the given list to a max heap. Argument is a list
definig n as the last index of the list
the left child of a membeer of the list at position i will be at position 2i+1
The right child will be at positon 2i+2.
Using this we check if the chhildren aree bigger than the paret. if yes, we swap the values and run heapify again till no more swaps are nescessary,
the funnction returns the max heap
the function heapsort is used to reate a descending order of the aray elements.
the first elemtn of the heap will be the largest element. so, this element is removed from the heap and added in the begining of another aray. the heap is heapified
this process is repeated till all elements are removed from the heap.
