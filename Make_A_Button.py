import tkinter as tk
#Code is in the description
#this is the first way to create buttons
"""
def onclick1():
    print("Button Clicked")

def onclick2():
    print("2nd Button Clicked")

root = tk.Tk()
root.title("The button")
btn1 = tk.Button(root, text="Button 1", command=onclick1)
btn2 = tk.Button(root, text="Button 2", command=onclick2)

btn1.pack()
btn2.pack()

root.mainloop()

"""

#Now we run the code
# as you can see, the first way is just for the basics. Now I will show you the second way, which is a little more advanced
#First we have to make all the code above text, this is how you do that
#Keep the import because we need it for both ways

def onclick(args):
    if args == 1:
        print("Button 1 clicked")
    if args == 2:
        print("Button 2 clicked")

root = tk.Tk()
root.title("Gui Button")
root.configure(bg = "Blue")
btn1 = tk.Button(root, text="Button 1", command=lambda:onclick(1))
btn1.config(fg = "Black")
btn2 = tk.Button(root, text="Button 2", command=lambda:onclick(2))
btn2.config(fg = "Black")

btn1.pack()
btn2.pack()
root.mainloop()

#all right now time to test


