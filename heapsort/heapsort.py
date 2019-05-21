def heapify(arr):
    n=len(arr)-1
    while(n>0):
        if(n%2==0):
            k=int((n-2)/2)
            if arr[n]>arr[k]:
                temp=arr[k]
                arr[k]=arr[n]
                arr[n]=temp
                heapify(arr)
        else:
            k=int((n-1)/2)
            if arr[n]>arr[k]:
                temp=arr[k]
                arr[k]=arr[n]
                arr[n]=temp
                heapify(arr)
        n=n-1
    return arr
            
        
def heapsort(arr,sortedHeap):
    heapify(arr)
    if len(arr)==2:
        sortedHeap.extend(arr)
        return sortedHeap
    else:
        sortedHeap.append(arr[0])
        arr.pop(0)
        heapsort(arr,sortedHeap)
    

thisdict={}
n=int(input(print("Enter number of keys")))
for i in range(n):
    print("Enter key")
    a=int(input())
    print("Enter value")
    thisdict[a]=int(input())
keys=list(thisdict.keys())
sortedHeap=[]
heapsort(keys,sortedHeap)
while(n>0):
    n=n-1
    print(str(sortedHeap[n])+": "+str(thisdict.get(sortedHeap[n])))

