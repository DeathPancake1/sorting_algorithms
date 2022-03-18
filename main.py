import copy
import random
import time


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
            arr[hole] = arr[hole - 1]
            hole = hole - 1
        arr[hole] = key


def quick_sort(arr, first, last):
    if first < last:
        q = partitionrand(arr, first, last)
        quick_sort(arr, first, q - 1)
        quick_sort(arr, q + 1, last)


# gets random element, exchanges it with the last element then calls partition
def partitionrand(arr, first, last):
    randpivot = random.randrange(first, last)
    arr[last], arr[randpivot] = arr[randpivot], arr[last]
    return partition(arr, first, last)


# gets the last element in the list and partitions the list
# to elements smaller than it on the left and higher on the right
def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


# The function uses partitioning to find the kth smallest element
def findKth(arr, l, r, k):
    pos = partition(arr, l, r)
    if pos - l == k - 1:
        return arr[pos]
    if pos - l > k - 1:
        return findKth(arr, l, pos - 1, k)
    return findKth(arr, pos + 1, r, k - pos + l - 1)


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


def testQuickSort(arr300, arr1k, arr25k, arr50k, arr100k):
    temp300 = copy.deepcopy(arr300)
    startTime = time.time()
    quick_sort(temp300, 0, 299)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Quick Sort is {elapsedTime * 100} ms at 300 elements')
    temp100k = copy.deepcopy(arr100k)
    startTime = time.time()
    quick_sort(temp100k, 0, 99999)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Quick Sort is {elapsedTime * 100} ms at 100k elements')
    temp1k = copy.deepcopy(arr1k)
    startTime = time.time()
    quick_sort(temp1k, 0, 999)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Quick Sort is {elapsedTime * 100} ms at 1k elements')
    temp25k = copy.deepcopy(arr25k)
    startTime = time.time()
    quick_sort(temp25k, 0, 24999)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Quick Sort is {elapsedTime * 100} ms at 25k elements')
    temp50k = copy.deepcopy(arr50k)
    startTime = time.time()
    quick_sort(temp50k, 0, 49999)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Quick Sort is {elapsedTime * 100} ms at 50k elements')


def testMergeSort(arr300, arr1k, arr25k, arr50k, arr100k):
    temp300 = copy.deepcopy(arr300)
    startTime = time.time()
    merge_sort(temp300)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Merge Sort is {elapsedTime * 100} ms at 300 elements')
    temp100k = copy.deepcopy(arr100k)
    startTime = time.time()
    merge_sort(temp100k)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Merge Sort is {elapsedTime * 100} ms at 100k elements')
    temp1k = copy.deepcopy(arr1k)
    startTime = time.time()
    merge_sort(temp1k)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Merge Sort is {elapsedTime * 100} ms at 1k elements')
    temp25k = copy.deepcopy(arr25k)
    startTime = time.time()
    merge_sort(temp25k)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Merge Sort is {elapsedTime * 100} ms at 25k elements')
    temp50k = copy.deepcopy(arr50k)
    startTime = time.time()
    merge_sort(temp50k)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Merge Sort is {elapsedTime * 100} ms at 50k elements')


def testInsertionSort(arr300, arr1k, arr25k, arr50k, arr100k):
    temp300 = copy.deepcopy(arr300)
    startTime = time.time()
    insertion_sort(temp300)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Insertion Sort is {elapsedTime * 100} ms at 300 elements')
    temp100k = copy.deepcopy(arr100k)
    startTime = time.time()
    insertion_sort(temp100k)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Insertion Sort is {elapsedTime * 100} ms at 100k elements')
    temp1k = copy.deepcopy(arr1k)
    startTime = time.time()
    insertion_sort(temp1k)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Insertion Sort is {elapsedTime * 100} ms at 1k elements')
    temp25k = copy.deepcopy(arr25k)
    startTime = time.time()
    insertion_sort(temp25k)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Insertion Sort is {elapsedTime * 100} ms at 25k elements')
    temp50k = copy.deepcopy(arr50k)
    startTime = time.time()
    insertion_sort(temp50k)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Insertion Sort is {elapsedTime * 100} ms at 50k elements')


def testSelectionSort(arr300, arr1k, arr25k, arr50k, arr100k):
    temp300 = copy.deepcopy(arr300)
    startTime = time.time()
    selection_sort(temp300)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Selection Sort is {elapsedTime * 100} ms at 300 elements')
    temp100k = copy.deepcopy(arr100k)
    startTime = time.time()
    selection_sort(temp100k)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Selection Sort is {elapsedTime * 100} ms at 100k elements')
    temp1k = copy.deepcopy(arr1k)
    startTime = time.time()
    selection_sort(temp1k)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Selection Sort is {elapsedTime * 100} ms at 1k elements')
    temp25k = copy.deepcopy(arr25k)
    startTime = time.time()
    selection_sort(temp25k)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Selection Sort is {elapsedTime * 100} ms at 25k elements')
    temp50k = copy.deepcopy(arr50k)
    startTime = time.time()
    selection_sort(temp50k)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print(f'Running time for Selection Sort is {elapsedTime * 100} ms at 50k elements')


# Main function for testing all algorithms
if __name__ == '__main__':
    # We make the arrays before testing to ensure all elements test on the same arrays
    arr300 = [random.randint(1, 100000) for _ in range(300)]
    arr1k = [random.randint(1, 100000) for _ in range(1000)]
    arr25k = [random.randint(1, 100000) for _ in range(25000)]
    arr50k = [random.randint(1, 100000) for _ in range(50000)]
    arr100k = [random.randint(1, 100000) for _ in range(100000)]
    # We call the testing function for our sorting algorithms
    testMergeSort(arr300, arr1k, arr25k, arr50k, arr100k)
    print('------------------------------------------------------')
    testQuickSort(arr300, arr1k, arr25k, arr50k, arr100k)
    print('------------------------------------------------------')
    testSelectionSort(arr300, arr1k, arr25k, arr50k, arr100k)
    print('------------------------------------------------------')
    testInsertionSort(arr300, arr1k, arr25k, arr50k, arr100k)
    print('------------------------------------------------------')
    arr50 = [random.randint(1, 1000) for _ in range(50)]
    temp50 = copy.deepcopy(arr50)
    # Testing the hybrid sort method with threshold of 6
    hybrid_sort(temp50, 6)
    print('The sorted array of 50 elements to test hybrid sort and kth element')
    for el in temp50:
        print(el, end=" ")
    # Testing kth element function to find 8th smallest element in array of 50 elements
    # We call this function on the unsorted array
    print("\n" + "Kth element in array is " + str(findKth(arr50, 0, 49, 8)))
