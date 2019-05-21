thisdict={}
n=int(input(print("Enter number of keys")))
for i in range(n):
    print("Enter key")
    a=int(input())
    print("Enter value")
    thisdict[a]=int(input())
arr=list(thisdict.keys())
j=0
while(j<len(arr)-1):
    if arr[j]>arr[j+1]:
        tmep=arr[j+1]
        arr[j+1]=arr[j]
        arr[j]=tmep
        if(j!=0):
            j=j-2
    j=j+1
for i in range(len(arr)):
    print(str(arr[i])+": "+str(thisdict.get(arr[i])))
