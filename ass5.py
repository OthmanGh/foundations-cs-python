# Assignment 4
# * Excersice 1 : 
# Sorting Strings
# We have wrote the functions “insertion sort” and “selection sort. Change the code in
# one of them so that the function would sort the strings in an alphabetical order 
# (instead of ASCII).
# Example: input [“aA”, ”b”, “BD”, ”Bc”,”D”]
#! Expected Ouput:[“aA”, ”b”, ”Bc”, ”BD”, ”D”]

list1 = ["aA", "b", "BD", "Bc", "D"]
# list3 = ["e", "d", "c", "b", "a"]

def insertion_sort_optimized(list):
    current_index = 1

    while current_index < len(list):
        currentEl = list[current_index]
        prevIndex = current_index - 1
        
        while prevIndex >= 0 and currentEl.lower() < list[prevIndex].lower(): 

            list[prevIndex + 1] = list[prevIndex]
            list[prevIndex] = currentEl
            prevIndex-=1

        current_index +=1


def selection_sort_optimized(list):
    for i in range(0, len(list) - 1):
        minIndex = i
        pos = i + 1

        while pos< len(list):
            if list[pos].lower() < list[minIndex].lower():
                minIndex = pos
            pos+= 1

        temp = list[i]
        list[i] = list[minIndex]
        list[minIndex] = temp

# insertion_sort_optimized(list1)
# insertion_sort_optimized(list2)
#print(list1)
#print(list3)
        
selection_sort_optimized(list1)
print(list1)

# * Excersice 2 : 
# Sorting number in descending order
# We have wrote the function “merge sort”, change the code so that it sorts the 
# numbers in descending order.
# Example: input:[3,5,1,8,-10]
# Output: [8,5,3,1,-10]

mergeList = [3,5,1,8,-10]


def merge(list, s, e):
    i = s 
    m = (s + e) // 2
    j = m + 1

    temp = []

    while i <= m and j <= e:
        if list[i] > list[j]:
            temp.append(list[i])
            i +=1
        else:
            temp.append(list[j])
            j +=1
    
    # apperenlty one of these list will hold some remaining elements so we'll have to handle this case
    # only one of these loops will be executed
    while i <= m:
        temp.append(list[i])
        i+=1

    while j <= e:
        temp.append(list[j])
        j+=1

    k = 0
    for index in range(s, e+1):
        list[index] = temp[k]
        k +=1

    return


def mergeSort(list, s, e):

    # Base Case 
    if s >= e : # reached case where every element is a sorted list of len (1)
        return
    
    mid = (s + e) // 2
    # Recursive Case 
    mergeSort(list, s, mid) # handle left part
    mergeSort(list, mid + 1, e) # handle right part

    return merge(list, s, e)


mergeSort(mergeList, 0, len(mergeList) - 1)
print(mergeList)