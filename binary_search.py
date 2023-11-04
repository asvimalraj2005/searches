def binary_search(list,x):                                          #Passing the SORTED array as 'list1' and search element as x
    low=0                                                           #considering the low as index 0 of the list elements  --->list1=[1,2,3,4,5,6,7]  low=0  --> list1[0]
    high=len(list1)-1                                               #considering the high as the last index element in the list elements --->list1[1,2,3,4,5,6,7] high=len(list1)-1 --> list1[6]
    while low<=high:                                                # if low crosses (crossed each other i.e low becomes greater than high) the high then the loop breaks and the code will return -1
        mid=(low+high)//2                                           # mid=(low+high)//2 'this line of code finds the index of the middle element of the list'                    
        if list1[mid]==x:                                           # list1[mid]==x:  'this line of code return the element if the element is found in the middle of the given list
            return mid                                              # << low--->[1,2,3,4,5,6,7]----<high  mid=(low+high)//2 which is 0+7//2 which gives 3.5 so we assume its 3
        elif list1[mid]>x:                                          # list1[mid]>x:   'this line of code tells us that the given element x is smaller than the mid element of the list , then we are assigning the high=mid-1 , high is in the right RIGHT? array is sorted right? then we are taking the high and the mid is in the middle of the list , so we are decreasing the index value of mid by using -1 (mid-1)
            high=mid-1
        elif list1[mid]<x:
            low=mid+1                                               # list[mid]<x: 'this line of code tells that us we are assigning the low=mid+1 because we traversing to the right side of the list because the mid element of the list is smaller than the given element x i.e x>mid so we are the taking the 'low' from the left side and assigning the low=mid+1 ; mid+1 says that we are increasing the index value to the right
    return -1                                                       # retunr -1 if the element is not present inside the given list

list1=[1,2,3,4,5,6,7,8,9]
x=3
print(binary_search(list1,x))