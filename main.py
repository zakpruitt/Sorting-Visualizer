from sort_class import Sorter
from tkinter import *
from tkinter import ttk
import random

sort = Sorter()

root = Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(1040, 600)
root.config(bg='white')

#variables
selected_alg = StringVar()

def drawData(data):
    canvas.delete("all")
    c_height = 600
    c_width = 700
    x_width = c_width / (len(data) - .5)#20
    offset = 100 - len(data) #20
    spacing = 2
    normalizedData = [ i / max(data) for i in data]
    
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + 5.5 + offset + spacing
        y0 = c_height - height * 500
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill="#317773")
        canvas.create_text(x0+1, y0, anchor=SW, text=str(data[i]))
    
    root.update_idletasks()

def generate_data():
    print('Algorithm Selected: ' + algorithmList.get(algorithmList.curselection()))
    
    minValue = int(minimumScale.get())
    maxValue = int(maximumScale.get())
    populationSize = int(populationScale.get())
    
    sort.PopulateArray(minValue, maxValue, populationSize)
    
    drawData(sort.array)

#frame / base layout
UI_frame = Frame(root, width=200, height = 600, bg='#317773')
UI_frame.grid(row=0, column= 1)

canvas = Canvas(root, width=850, height=600, bg='white smoke', highlightthickness=0)
canvas.grid(row=0, column=0)

# algorithm list
algorithmList = Listbox(UI_frame, fg='#317773', bg='white smoke', font=("Dosis", 11), height=6, justify=CENTER,
                        selectbackground="#317773", highlightcolor="white smoke")

algorithmList.insert(0, "Bubble Sort")
algorithmList.insert(1, "Insertion Sort")
algorithmList.insert(2, "Quick Sort")
algorithmList.insert(3, "Selection Sort")
algorithmList.insert(4, "Merge Sort")
algorithmList.insert(5, "Counting Sort")

algorithmList.grid(row=0, column=0, pady=15, ipadx=10)

# array size entry
populationScale = Scale(UI_frame, from_=10, to=40, length =155, resolution=1, orient=HORIZONTAL, label="           Population Size",
                       fg='#317773', bg='white smoke', troughcolor='white smoke', activebackground='black',
                       font=("Dosis", 11))
populationScale.grid(row=1, column=0, ipadx=10, ipady=5, padx=5, pady=5)

# minimum value entry
minimumScale = Scale(UI_frame, from_=1, to=50, length=155, digits=2, resolution=0.2, orient=HORIZONTAL,
                   fg='#317773', bg='white smoke', troughcolor='white smoke', activebackground='black', 
                   label="Minimum Value", font=("Dosis", 11))
minimumScale.grid(row=2, column=0, ipadx=10, ipady=5, padx=5, pady=5)

# maximum value scale
maximumScale = Scale(UI_frame, from_=100, to=150, length=155, digits=2, resolution=0.2, orient=HORIZONTAL,
                   fg='#317773', bg='white smoke', troughcolor='white smoke', activebackground='black', 
                   label="           Maximum Value", font=("Dosis", 11))
maximumScale.grid(row=3, column=0, ipadx=10, ipady=5, padx=5, pady=5)

# speed scale entry
speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=155, digits=2, resolution=0.2, orient=HORIZONTAL,
                   fg='#317773', bg='white smoke', troughcolor='white smoke', activebackground='black', 
                   label="                  Delay", font=("Dosis", 11))
speedScale.grid(row=4, column=0, padx=5, pady=5, ipadx=5, ipady=5)

# generate button
Button(UI_frame, text="Generate Array", command=generate_data, fg='#317773', bg='white smoke', font=("Dosis", 10)).grid(row=5, column=0, padx=5, pady=5)

# sort
Button(UI_frame, text="  Sort Array  ", command=generate_data, fg='#317773', bg='white smoke', font=("Dosis", 10)).grid(row=6, column=0, padx=50, pady=5)


root.mainloop()

# if __name__ == '__main__':
#     sort = Sorter()
#     sort.populateArray()
#     sort.bubbleSort()
#     print(sort.array)


