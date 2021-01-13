import tkinter as tk


def mouse_click(event):
    x, y = event.x, event.y
    print(x, y)



root = tk.Tk()
root.geometry('600x600')

# x = root.winfo_pointerx()
# y = root.winfo_pointery()
x = root.winfo_pointerx() - root.winfo_rootx()
y = root.winfo_pointery() - root.winfo_rooty()
root.bind('<Button-1>', mouse_click)

root.mainloop()
