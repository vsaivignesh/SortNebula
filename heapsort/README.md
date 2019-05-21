Heap sort:
the funnction heapify converts the given list to a max heap. Argument is a list
definig n as the last index of the list. n is decremented to 0 as the function progresses
the left child of a membeer of the list at position i will be at position 2i+1
The right child will be at positon 2i+2.
Using this we check if the chhildren are bigger than the parent. If yes, we swap the values and run heapify
again till no more swaps are nescessary.
the function returns the max heap
the function heapsort is used to create a descending order of the aray elements.
the first element of the heap will be the largest element. So, this element is removed from the heap and 
added in the begining of another aray. The heap is passed to the heapify function once again to get the
next largest element.
This process is repeated till all elements are removed from the heap.
