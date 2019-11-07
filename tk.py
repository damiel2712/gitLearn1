__auther_ = "Daniel David"
import tkinter as tk


def main():
    root = tk.Tk()
    d = tk.PhotoImage(file=r'C:\Users\d2712\Desktop\j.jpg')
    m = tk.PhotoImage(file=r'C:\Users\d2712\Desktop\cash.jpg')
    b = tk.PhotoImage(file=r'C:\Users\d2712\Desktop\w.jpg')
    lb = tk.Label(root, image=d)
    lb.pack()
    root.mainloop()

if __name__ == '__main__':
    main()