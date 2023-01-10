counter = 0

def heapify(arr, n, i):
    # want the largest to be the root
    largest = i
    # set the left and right children
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    
    

    if r < n and arr[largest] < arr[r]:
        largest = r
    

    # change the root if needed
    if largest != i:
        global counter 
        counter = counter + 1
        print(f"comparisons: {counter}, array: {arr}")
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    length = len(arr)

    # make the maxheap
    for i in range(length // 2 - 1, -1, -1):
        heapify(arr, length, i)
    
    for i in range(length-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [ 9, 20, 14, 17, 85, 3, 21, 6, 4, 10 ]

heapSort(arr)
print(f"comparisons: {counter}, array: {arr}")