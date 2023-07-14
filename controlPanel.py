import tkinter as tk
from productivityPulse import ProductivityPulse
from grapths import Plot
from KandL import extract
import threading
import datetime

class ControlPanel:
    def __init__(self) -> None:
        self.window_list = list()
        self.stop_event = threading.Event()

        t1 = threading.Thread(target=lambda: ProductivityPulse(self.stop_event, self.window_list))
        t1.start()


        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.title("Productivity Pulse Control Panel")
        self.root.configure(bg="gray")

        self.count = 0

        self.time_elapsed = tk.Label(self.root, text=f"Time Elapsed: {self.convert_seconds(self.count)}", font=('', 25))
        self.time_elapsed.pack(pady=20)

        self.history_button = tk.Button(self.root, 
                                        text="Show History", font=("", 15), 
                                        command=lambda: Plot(extract(self.window_list, 0), extract(self.window_list, -1)))
        self.history_button.pack(pady=20)

        self.countup()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

        self.stop_event.set()
        t1.join()
        
    
    def countup(self):
        self.count += 1
        self.time_elapsed.config(text=f"Time Elapsed: {self.convert_seconds(self.count)}")
        self.time_elapsed.after(1000, self.countup)
    
    def convert_seconds(self, seconds):
        time_delta = datetime.timedelta(seconds=seconds)
        time_string = str(time_delta)
        hours, minutes, seconds = time_string.split(':')
        return f"{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}"
    
    def on_close(self):
        self.stop_event.set()
        self.root.destroy()
