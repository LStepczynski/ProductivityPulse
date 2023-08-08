import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

class Plot:
    def __init__(self, names: list, values: list, mode: str) -> None:
        self.names = names
        self.values = [value/60 for value in values]
        self.mode = mode

        if self.mode == "Graph":
            self.graph()
        else: self.table([names, values])
    
    def graph(self) -> None:
        # Create the bar graph
        plt.bar(self.names, self.values)

        # Add labels and title
        plt.xlabel('Windows')
        plt.ylabel('Time')
        plt.title('Time Spent in Minutes')

        # Display the plot
        plt.show()
    
    def table(self, data: list) -> None:
        self.names = data[0]
        self.values = data[1]

        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Data Display")

        self.data_container = tk.Frame(self.root)
        self.data_container.pack()

        for index in range(len(self.names)):
            DataBox(self.data_container, self.names[index], self.values[index], 0, index)

class DataBox():
    def __init__(self, window, label, value, row, col) -> None:
        print('p')
        self.window = window
        self.label = label
        self.value = value
        self.row = row
        self.col = col

        self.databox = tk.Frame(self.window)
        self.data_label = tk.Label(self.databox, text=self.label)
        self.data_value = tk.Label(self.databox, text=self.value)
        self.databox.grid(row=self.row, column=self.col)
        self.data_label.pack()
        self.data_value.pack()



        































        # style = ttk.Style(self.root)
        # style.configure("Treeview", rowheight=25, font=('Arial', 12), borderwidth=1)
        # style.configure("Treeview.Heading", font=('Arial', 14))

        # tree = ttk.Treeview(self.root, columns=data[0], show="headings", style="Treeview")  # Set fixed width here

        # for col in data[0]:
        #     tree.heading(col, text=col, anchor=tk.CENTER)  # Center-align column headings
        #     tree.column(col, width=150, anchor=tk.CENTER, stretch=True)  # Center-align column data

        # vsb = ttk.Scrollbar(self.root, orient="horizontal", command=tree.xview)  # Change to xview
        # tree.configure(xscrollcommand=vsb.set)  # Change to xscrollcommand
        # vsb.pack(side="bottom", fill="x")  # Change to bottom
        # tree.pack(fill="both", expand=True)

        # for row in data[1:]:
        #     tree.insert("", "end", values=row)

