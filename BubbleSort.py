import time
def bubbleSort(data, drawData, sleepInterval):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if val == j or val ==j+1 else 'red' for val in range(len(data))])
                time.sleep(sleepInterval)
    drawData(data, ['green' for val in range(len(data))])