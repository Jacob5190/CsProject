import tkinter as tk


def build():
    window = tk.Tk()
    window.title("login system")
    # TODO: Complete Name process
    LabelName = tk.Label(window, text="Name", width=15, height=4)
    LabelName.grid(row=4, column=3)

    EName = tk.Entry(window)
    EName.grid(row=4, column=4)

    # TODO: Complete Gender process
    LabelGender = tk.Label(window, text="Gender", width=5, height=4)
    LabelGender.grid(row=5, column=3)

    BoxGender1 = tk.Radiobutton(window, text="male", value=0)
    BoxGender1.grid(row=5, column=4)

    BoxGender2 = tk.Radiobutton(window, text="female", value=1)
    BoxGender2.grid(row=5, column=5)
    # EGender = tk.Entry(window)
    # EGender.grid(row = 5,column =4)

    # TODO: Complete IDnumber
    LabelID = tk.Label(window, text="ID", width=15, height=4)
    LabelID.grid(row=6, column=3)

    EID = tk.Entry(window)
    EID.grid(row=6, column=4)

    # TODO: Complete Button task
    ButtonInsert = tk.Button(window, text="Insert", width=15, height=4)
    ButtonInsert.grid(row=7, column=4)

    # TODO:Search Button
    SearchFrame = tk.Frame(window)
    SearchFrame.grid(row=6, column=10)

    ESearch = tk.Entry(window)
    ESearch.grid(row=6, column=10)

    ButtonSearch = tk.Button(window, text="Search", width=5, height=3)
    ButtonSearch.grid(row=7, column=9)

    ButtonQuit = tk.Button(window, text="Leave", width=5, height=3)
    ButtonQuit.grid(row=7, column=10)

    LabelSearch = tk.Label(window, text="Search ID", width=15, height=4)
    LabelSearch.grid(row=6, column=9)

    window.geometry("740x380")
    window.mainloop()


build()