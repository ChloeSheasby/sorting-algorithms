def selectionSort(arr):
    length = len(arr)
    count = 0
    
    # go through the whole array
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        count = count + 1     
        print(f"comparisons: {count}, array: {arr}")   
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [ 9, 20, 14, 17, 85, 3, 21, 6, 4, 10 ]

selectionSort(arr)