import tkinter as tk
import datetime

class Timer:
    """Creates a timer that tells the user when to work and rest"""
    def __init__(self, work, rest) -> None:
        self.work = work * 60 #Convert minutes to seconds
        self.rest = rest * 60 #Convert minutes to seconds

        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.root.title("Timer")

        self.time_to_change = tk.Label(self.root, 
                                       text=f"Time until rest: {self.convert_seconds(self.work)}", 
                                       font=('', 25))
        self.time_to_change.pack()

        self.time = self.work
        self.state = True # True represents work and false rest

        self.time_to_change.after(1000, self.count)

        self.root.mainloop()
    
    def count(self):
        if not self.root.winfo_exists():
            return
        if self.time == 0:  
            if self.state:
                self.time = self.rest
            else: 
                self.time = self.work
            self.state = not self.state
        self.time -= 1
        if self.state:
            self.time_to_change.configure(text=f"Time until rest: {self.convert_seconds(self.time)}")
        else: self.time_to_change.configure(text=f"Time until work: {self.convert_seconds(self.time)}")
        self.time_to_change.after(1000, self.count)
        

    def convert_seconds(self, seconds):
        """Converts seconds to HH:MM:SS format"""
        time_delta = datetime.timedelta(seconds=seconds)
        time_string = str(time_delta)
        hours, minutes, seconds = time_string.split(':')
        return f"{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}"