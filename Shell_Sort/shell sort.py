def shellSort(arr,interval):
    for i in range(len(arr)-interval):
        if arr[i][0]>arr[i+interval][0]:
            tmep=arr[i+interval]
            arr[i+interval]=arr[i]
            arr[i]=tmep
    if(int(interval/2)>1):
        shellSort(arr,int(interval/2))
    else:
        j=0
        while(j<len(arr)-1):
            if arr[j][0]>arr[j+1][0]:
                tmep=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=tmep
                if(j!=0): j=j-2
            j=j+1
    return arr
                
            
    
thisdict=[]
n=int(input(print("Enter number of keys")))
for i in range(n):
    print("Enter key")
    a=int(input())
    print("Enter value")
    b=int(input())
    thisdict.append([a,b])
h=int(len(thisdict)/2)
sortedList=shellSort(thisdict,h)
for n in range(h*2):
    print(str(sortedList[n][0])+": "+str(sortedList[n][1]))


