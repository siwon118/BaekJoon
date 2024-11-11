import sys

def heap(arr, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, largest, n)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heap(arr, i, n)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, 0, i)


n = int(sys.stdin.readline())

a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))
heapSort(a)
for i in range(n):
    print(a[i])
