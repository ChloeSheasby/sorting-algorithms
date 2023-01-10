counter = 0

def partition(arr, l, r):
    # last element is pivot
    pivot = arr[r]
    # first element is index/pointer
    index = l

    for i in range(l, r):
        if arr[i] <= pivot:
            # move values smaller than pivot to the front
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
        global counter 
        counter = counter + 1
        print(f"comparisons: {counter}, array: {arr}")

    # swap last element with index/pointer
    arr[index], arr[r] = arr[r], arr[index]
    return index


def quickSort(arr, l, r):
    if len(arr) == 1:
        return arr
    if l < r:
        pi = partition(arr, l, r)
        quickSort(arr, l, pi-1)
        quickSort(arr, pi+1, r)

arr = [ 9, 20, 14, 17, 85, 3, 21, 6, 4, 10 ]

quickSort(arr, 0, len(arr)-1)
print(f"comparisons: {counter}, array: {arr}")