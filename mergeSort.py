counter = 0

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temporary arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # copy data into arrays
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        global counter 
        counter = counter + 1
        print(f"comparisons: {counter}, array: {arr}")

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

arr = [ 9, 20, 14, 17, 85, 3, 21, 6, 4, 10 ]

mergeSort(arr, 0, len(arr)-1)
print(f"comparisons: {counter}, array: {arr}")