from tkinter import *
from tkinter import ttk
import numpy as np
import random
from BubbleSort import bubbleSort
from QuickSort import quickSort
from MergeSort import mergeSort
from HeapSort import heapSort

#Set UI information with root informations
root = Tk()
root.title('Sorting Algorithm Visualisation')
root.maxsize(1000,800)
#Setting background color for UI
root.config(bg='black')


#Variables
chosen_algorithm = StringVar()
data = []

#Functions
def StartAlgo():
    global data
    if not data: return

    if algorithm_menu.get() == 'Bubble Sort':
        bubbleSort(data, drawData, speed_scale.get())

    elif algorithm_menu.get() == 'Quick Sort':
        quickSort(data, 0, len(data)-1, drawData, speed_scale.get())
        
    elif algorithm_menu.get() == 'Merge Sort':
        mergeSort(data, drawData, speed_scale.get())
    
    elif algorithm_menu.get() == 'Heap Sort':
        heapSort(data, drawData, speed_scale.get())

    drawData(data, ['green' for x in range(len(data))])
    

def drawData(data, colorArray):
    canvas.delete('all')
    c_height = 380
    c_width= 600
    x_width = c_width / (len(data) + 1)
    offset = 15
    spacing = 5
    normalize_data = np.linalg.norm(data)
    new_data = data / normalize_data
    for i , height in enumerate(new_data):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 375
        x1 = (i+1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update()

def generate():
    global data
    min_val = int(minEntry.get())
    max_val = int(maxEntry.get())
    size = int(sizeEntry.get())
    data = [random.randrange(min_val, max_val+1) for i in range(size)]
    drawData(data, ['red' for i in range(len(data))])

#Frame / Base layout
UI_Frame = Frame(root, width=800, height=220, bg='grey')
UI_Frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=420, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)


#User Interface Area
#Row[0]
Label(UI_Frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algorithm_menu = ttk.Combobox(UI_Frame, textvariable=chosen_algorithm, values=['Bubble Sort','Merge Sort','Quick Sort', 'Heap Sort'])
algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
algorithm_menu.current(0)

speed_scale = Scale(UI_Frame, from_=0.0, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed (s)")
speed_scale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_Frame, text="Start", command=StartAlgo, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_Frame, from_=3, to=25, resolution=10, orient=HORIZONTAL, label="Dataset Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_Frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_Frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5) 

Button(UI_Frame, text="Generate", command=generate, bg='white').grid(row=1, column=3, padx=5, pady=5)


root.mainloop()
