def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)


def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        i_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i_min]:
                i_min = j
        if i != i_min:
            arr[i], arr[i_min] = arr[i_min], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        hole = i
        while hole > 0 and arr[hole - 1] > key:
            arr[hole] = a[hole - 1]
            hole = hole - 1
        arr[hole] = key


def quick_sort(arr, first, last):
    if first < last:
        q = partition(arr, first, last)
        quick_sort(arr, first, q - 1)
        quick_sort(arr, q + 1, last)


def partition(arr, first, last):
    lastS1 = first
    firstUnkown = first + 1
    while firstUnkown <= last:
        if arr[firstUnkown] < arr[first]:
            lastS1 += 1
            arr[firstUnkown], arr[lastS1] = arr[lastS1], arr[firstUnkown]
        firstUnkown += 1
    arr[first], arr[lastS1] = arr[lastS1], arr[first]
    return lastS1


def findKth(arr, start, end, k):
    j = partition(arr, start, end)
    if k == j:
        return a[j]
    if k < j:
        return findKth(arr, start, j - 1, k)
    if k > j:
        return findKth(arr, j + 1, end, k - j)


def hybrid_sort(arr, thresh):
    if len(arr) > thresh:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        hybrid_sort(left, thresh)
        hybrid_sort(right, thresh)
        merge(arr, left, right)
    else:
        selection_sort(arr)


if __name__ == '__main__':
    a = [6, 1, 7, 2, 3]
    index = findKth(a, 0, 4, 2)
    print(a[index])
    hybrid_sort(a, 2)
    for el in a:
        print(el)
