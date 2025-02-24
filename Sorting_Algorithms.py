import time;
import random;

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        # Assume the current position holds
        # the minimum element
        min_idx = i
        
        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                # Update min_idx if a smaller element is found
                min_idx = j
        
        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def heapify(arr, n, i):
    
     # Initialize largest as root
    largest = i 
    
    #  left index = 2*i + 1
    l = 2 * i + 1 
    
    # right index = 2*i + 2
    r = 2 * i + 2  

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

# Main function to do heap sort
def heapSort(arr):
    
    n = len(arr) 

    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):
      
        # Move root to end
        arr[0], arr[i] = arr[i], arr[0] 

        # Call max heapify on the reduced heap
        heapify(arr, i, 0)

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Generate arrays of different sizes
small_array = [random.randint(0, 10100) for _ in range(10000)]
medium_array = [random.randint(0, 20100) for _ in range(20000)]
large_array = [random.randint(0, 30100) for _ in range(30000)]

# Driver code to test above
print("Testing small array:")
arr = small_array.copy()
start = time.time()
insertionSort(arr)
end = time.time()
print(end - start)

arr = small_array.copy()
start = time.time()
selection_sort(arr)
end = time.time()
print(end - start)


arr = small_array.copy()
start = time.time()
bubbleSort(arr)
end = time.time()
print(end - start)


arr = small_array.copy()
start = time.time()
merge_sort(arr, 0, len(arr) - 1)
end = time.time()
print(end - start)


arr = small_array.copy()
start = time.time()
heapSort(arr)
end = time.time()
print(end - start)


arr = small_array.copy()
start = time.time()
arr = quickSort(arr)
end = time.time()
print(end - start)


print("Testing medium array:")
arr = medium_array.copy()
start = time.time()
insertionSort(arr)
end = time.time()
print(end - start)


arr = medium_array.copy()
start = time.time()
selection_sort(arr)
end = time.time()
print(end - start)


arr = medium_array.copy()
start = time.time()
bubbleSort(arr)
end = time.time()
print(end - start)


arr = medium_array.copy()
start = time.time()
merge_sort(arr, 0, len(arr) - 1)
end = time.time()
print(end - start)


arr = medium_array.copy()
start = time.time()
heapSort(arr)
end = time.time()
print(end - start)


arr = medium_array.copy()
start = time.time()
arr = quickSort(arr)
end = time.time()
print(end - start)


print("Testing large array:")
arr = large_array.copy()
start = time.time()
insertionSort(arr)
end = time.time()
print(end - start)


arr = large_array.copy()
start = time.time()
selection_sort(arr)
end = time.time()
print(end - start)


arr = large_array.copy()
start = time.time()
bubbleSort(arr)
end = time.time()
print(end - start)


arr = large_array.copy()
start = time.time()
merge_sort(arr, 0, len(arr) - 1)
end = time.time()
print(end - start)


arr = large_array.copy()
start = time.time()
heapSort(arr)
end = time.time()
print(end - start)


arr = large_array.copy()
start = time.time()
arr = quickSort(arr)
end = time.time()
print(end - start)  

