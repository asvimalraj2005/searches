def last_occurence(list1,x):
    low=0
    high=len(list1)-1
    while low<=high:
        mid=(low+high)//2
        if list1[mid]>x:
            high=mid-1
        elif list1[mid]<x:
            low=mid+1
        else:
            if mid==len(list1)-1 or list1[mid]!=list1[mid+1]:
                return mid
            else:
                low=mid+1
    return -1

list1=[1,2,2,2,2,2,3,4,5,6,7,8]
x=2
print(last_occurence(list1,x))