def last_occurence(list1,x):                                # Naive solution for finding the last occurences of the given element in the given list
    for i in reversed(range(len(list1))):                   # By using the for loop and reversed keyword for reversing the list 
        if(list1[i]==x):                                    # By using if condition to check whether the given element is present inseide the given list or not list1[i] --->list1<----[contains the objecrs] ---->i<----[contains the index values]
            return i                                        # If the element is present inside the list it will return i
    return -1                                               # If the element is not present inside the list it will return -1
    

list1=[1,2,3,4,5,5,6,7]
x=5
print(last_occurence(list1,x))