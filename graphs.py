import matplotlib.pyplot as plt
import tkinter as tk
import datetime

class Plot:
    def __init__(self, names: list, values: list, mode: str) -> None:
        self.names = [name[:-4] for name in names] # Strips the window names of the ".exe"
        self.values = [value/60 for value in values] # Converts the seconds to minutes
        self.mode = mode

        if self.mode == "Graph":
            self.graph()
        else: self.table([self.names, values])
    
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
        """Displays a table with the time info"""
        self.names = data[0]
        self.values = data[1]
        self.items_in_row = 4 # How much items will be in a row

        self.root = tk.Tk()
        self.root.geometry(f"550x{(len(self.values) // self.items_in_row)*65 + 110}")
        self.root.title("Data Display")

        self.window_label = tk.Label(self.root, text="Time Spent", font=('', 20))
        self.window_label.pack()

        # Contains all the DataBox() instances
        self.data_container = tk.Frame(self.root)
        self.data_container.pack()

        # Creates a DataBox() for each of the tracked windows and displays them in a grid
        for index in range(len(self.names)): 
            DataBox(self.data_container, 
                    self.names[index], 
                    self.convert_seconds(self.values[index]), 
                    index // self.items_in_row, 
                    index % self.items_in_row)

    def convert_seconds(self, seconds: int) -> str:
        """Converts seconds to HH:MM:SS format"""
        time_delta = datetime.timedelta(seconds=seconds)
        time_string = str(time_delta)
        hours, minutes, seconds = time_string.split(':')
        return f"{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}"

class DataBox():
    def __init__(self, window, label, value, row, col) -> None:
        """Creates an object that the data will be displayed in and renders it"""
        self.window = window
        self.label = label
        self.value = value
        self.row = row
        self.col = col

        self.databox = tk.Frame(self.window)
        self.data_label = tk.Label(self.databox, text=self.label, font=('', 15))
        self.data_value = tk.Label(self.databox, text=self.value)
        self.databox.grid(row=self.row, column=self.col, padx=10, pady=10)
        self.data_label.pack()
        self.data_value.pack()