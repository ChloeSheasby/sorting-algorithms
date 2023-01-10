def bubbleSort(arr):
    length = len(arr)
    count = 0

    swapped = False
    
    # go through the whole array
    for i in range(length-1):
        # the last i elements are already in place
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        count = count + 1
        print(f"comparisons: {count}, array: {arr}")
        # we can leave the loop if we haven't made a swap
        if not swapped:
            return

arr = [ 9, 20, 14, 17, 85, 3, 21, 6, 4, 10 ]

bubbleSort(arr)