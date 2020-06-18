from sort_class import Sorter
# from tkinter import *

# root = Tk()

# # Creating a label widget
# myLabel = Label(root, text="Hello World!")
# myLabel2 = Label(root, text="BRUV MOMENT!!!!!!!!!!!!!!")
# myButton = Button(root, text="Click me!")

# # myLabel.grid(row=0, column=0)
# # myLabel2.grid(row=1, column=5)
# myButton.pack()

# root.mainloop()

if __name__ == '__main__':
    sort = Sorter()
    sort.populateArray()
    sort.bubbleSort()
    print(sort.array)


