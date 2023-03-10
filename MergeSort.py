import time

def mergeSort(data , drawData, timeTick):
    mergeSort_Algo(data, 0, len(data)-1, drawData, timeTick)

def mergeSort_Algo(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left+right)//2
        mergeSort_Algo(data, left, middle, drawData, timeTick)
        mergeSort_Algo(data, middle+1, right, drawData, timeTick)
        merge(data, left ,middle, right, drawData, timeTick)

def merge(data, left ,middle, right, drawData, timeTick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftpart = data[left:middle+1]
    rightpart = data[middle+1:right+1]

    leftIndex=rightIndex = 0

    for dataIndex in range(left, right+1):
        if leftIndex < len(leftpart) and rightIndex < len(rightpart):
            if leftpart[leftIndex] <= rightpart[rightIndex]:
                data[dataIndex] = leftpart[leftIndex]
                leftIndex+=1
            else:
                data[dataIndex] = rightpart[rightIndex]
                rightIndex += 1
        elif leftIndex<len(leftpart):
            data[dataIndex] = leftpart[leftIndex]
            leftIndex += 1
        else:
            data[dataIndex] = rightpart[rightIndex]
            rightIndex+=1
    drawData(data, ['green' if x>=left and x<=right else 'white' for x in range(len(data))])
    time.sleep(timeTick)

def getColorArray(length, left, middle, right):
    colorArray = []
    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append('yellow')
            else:
                colorArray.append('pink')
        else:
            colorArray.append('white')
    return colorArray

