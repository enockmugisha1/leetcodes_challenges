def binarysearch(array,target):
    first = 0
    last = len(array) -1
    while first < last : 

        mid_index = first + (last-first)//2 # for getting index of value btn in this array

        mid_value = array[mid_index] # variable which will store mid_value 

        if mid_value == target: # if it fits with this conditions automatically 

            #it will return mid_index of target value .
            return mid_index
        elif  mid_value < target:
            first = mid_index + 1 # it means first index will be move to the next index of mid_index.
        else:
            last = mid_index -1
    return None

array = [1,5,6,7,8,10,4]
number = 7
print(binarysearch(array,number))
