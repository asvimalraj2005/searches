def first_occurence(list1,n,x):                               # Passing the SORTED array and the search element as the parameters
    for i in range(0,n):                                      # By using the for loop we traversing the array elements 0,n from 0 to n i.e length of the list list1=[1,2,3,4] len(list1)=4
        if list1[i]==x:                                       # By using if condition we are checking if the given element x is present inside the array or not 
            return i                                          # If the element x is present inside the list it will return the index of that element
    return -1                                                 # If the element x is not present inside the list it will return -1

list1=[1,2,3,4,5,6,7,8,9]                                       # Creating the list named as list1 and the elements is sorted 
n=len(list1)                                                    # n=len(list1) So basically the list index always starts as 0 of we use len it will remove 0 and return the orginal element length of the list
x=9                                                             # x=9 `search element`
print(first_occurence(list1,n,x))