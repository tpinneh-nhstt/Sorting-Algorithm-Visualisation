import time

def heapify(arr, n, i, drawData, timeTick): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
    drawData(arr, getColourArray(len(arr), i, l, r))
    time.sleep(timeTick)
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
        drawData(arr, getColourArray(len(arr), i, l, r))
        time.sleep(timeTick)
        # Heapify the root. 
        heapify(arr, n, largest, drawData, timeTick) 

def heapSort(arr, drawData, timeTick): 
    n = len(arr) 
    # Build a maxheap. 
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i, drawData, timeTick) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0, drawData, timeTick)

def getColourArray(size, i, left, right): 
    colourArray = [] 

    for j in range(size): 
        if j == i: 
            colourArray.append("#03fc77") # green elements are selected
        else:
            colourArray.append("#3ea9f0") # blue
    return colourArray