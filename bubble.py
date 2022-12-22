
# bubble sort algorithm
def bubbleSort(array):
    # loops for entire list
    for i in range(len(array)):
        # loops through array to compare to finde the position for the greates element in unsorted part
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                # swap the elements
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array

# implementation of bubble sort
my_array = [-1, -3, 0 ,10, 5, 7]

print("Unsorted array:", end=' ')
for i in range(0, len(my_array)):
    print(my_array[i], end= ' ')

sorted = bubbleSort(my_array)
print("\nSorted array:", end= ' ')
for i in sorted:
    print(i, end=' ')
