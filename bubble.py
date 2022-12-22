
# bubble sort algorithm
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
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
