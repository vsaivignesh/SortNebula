def shellSort(arr,interval):
    for i in range(len(arr)-interval):
        if arr[i]>arr[i+interval]:
            tmep=arr[i+interval]
            arr[i+interval]=arr[i]
            arr[i]=tmep
    if(int(interval/2)>1):
        shellSort(arr,int(interval/2))
    else:
        j=0
        while(j<len(arr)-1):
            if arr[j]>arr[j+1]:
                tmep=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=tmep
                if(j!=0): j=j-2
            j=j+1
    return arr
                
            
    
thisdict={}
n=int(input(print("Enter number of keys")))
for i in range(n):
    print("Enter key")
    a=int(input())
    print("Enter value")
    thisdict[a]=int(input())
keys=list(thisdict.keys())
h=int(len(keys)/2)
sortedList=shellSort(keys,h)
for i in range(len(keys)):
    print(str(sortedList[i])+": "+str(thisdict.get(sortedList[i])))


