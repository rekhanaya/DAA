#PPT SLIDE 34 QUICK-SORT

# Function to find the partition position
def partition(array, low, high):
    #choose the rightmost element as pivot
    pivot = array[high]

    #pointer for greater element
    i = low -1

    #traverse through all elements
    #compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            #if element smaller that pivot is found
            #swap it with the greater elemnt pointed by i
            i = i + 1

            #swapping aelement at i with element at j
            (array[i + 1], array[j], array[i])

    #swap the pivot elemnt with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    #return the position from where partition is done
    return i + 1
    # function to perform quicksort
def quickSort (array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort (array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort (array, pi + 1, high)

data = [4,12,23,9,21,1,35,2,24]
print("Unsorted Array")
print(data)

size= len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)