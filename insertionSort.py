def insertionSort(arr):
    length = len(arr)
    count = 0
    
    # go through the whole array
    for i in range(1, length):
        item = arr[i]
        j = i-1
        # move elements that are greater than item one ahead
        while j >= 0 and item < arr[j]:
            count = count + 1
            arr[j+1] = arr[j]
            j -= 1
            print(f"comparisons: {count}, array: {arr}")
        arr[j+1] = item

arr = [ 9, 20, 14, 17, 85, 3, 21, 6, 4, 10 ]

insertionSort(arr)