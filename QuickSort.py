import time

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:

            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border+=1
        
        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)
    
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]
    return border

    


def quickSort(data, head, tail, drawData, timeTick):
    if head<tail:
        partitionIndex = partition(data, head, tail, drawData, timeTick)

        #Left Partition
        quickSort(data, head, partitionIndex-1, drawData, timeTick)
        #Right Partition
        quickSort(data, partitionIndex+1, tail, drawData, timeTick)

def getColorArray(dataLength, head, tail, border, currentIndex, isSwaping=False):
    colorArray=[]
    for i in range(dataLength):
        if i >=head  and i <=tail:
            colorArray.append('grey')
        else:
            colorArray.append('white')
        if i==tail:
            colorArray[i]= 'blue'
        elif i==border:
            colorArray[i]= 'red'
        elif i==currentIndex:
            colorArray[i]= 'yellow'

        if isSwaping:
            if i==border or i==currentIndex:
                colorArray[i] = 'green'
    return colorArray
