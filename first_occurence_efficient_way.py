def first_occurence(list1,x):                                   # Passing the SORTED list and element x as  the parameters list1=[1,2,2,3,4,5,6,7,8] and element x=2
    low=0                                                       # low=0 means that we are accessing the first index element of the list1              ---->low ^               ^<----high
    high=len(list1)-1                                           # high=len(list1)-1 means that we are accessing the last element of the list1           list1=[1,2,2,3,4,5,6,7,8]                                                                  
    while low<=high:                                            # if low and high crossed each other then the loop will break and retunrs -1
        mid=(low+high)//2                                       # Computing the mid value by using low=0 and high=len(list1)-1 
        if list1[mid]>x:                                        # If list1[mid]>x: if the list1's mid is element is greater than the given x element then we take high from the right and assign high=mid-1 because the searching element is smaller than the mid element which is greater so the searching element is present on the left side of the list 
            high=mid-1
        elif list1[mid]<x:                                      # If list1[mid]<x: if the list1's mid is element is smaller than the given x element than the search element is present on the right side of the list1 so we take low from the left side and assign low=mid+1
            low=mid+1
        else:                                                           
            if mid==0 or list1[mid]!=list1[mid-1]:              # If mid==0 this condition says that if the searching element is at index 0 
                return mid                                      # list1[mid]!=list1[mid-1] this comdition checks that if the current mid element is not equal to the previous element ; if the previous element is not equal to mid it will return mid otherwise it will fall down to else condition
            else:
                high=mid-1                                      # high=mid-1 we are checking the first occurrence right , the array is sorted right , so we take high from the right and assign right=mid-1 FIRST OCCURRENCE even if the element is present on the right pivot or left pivot
    return -1



list1=[1,2,3,3,4,5,6,7,9,0]
x=3
print(first_occurence(list1,x))