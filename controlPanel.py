import tkinter as tk
from productivityPulse import ProductivityPulse
from productivity_timer import Timer
from grapths import Plot
from KandL import extract
import threading
import datetime

class ControlPanel:
    """Creates a window that manages the entire application"""
    def __init__(self) -> None:
        self.window_list = list()
        self.stop_event = threading.Event()

        t1 = threading.Thread(target=lambda: ProductivityPulse(self.stop_event, self.window_list))
        t1.start()

        # Basic configuration
        self.root = tk.Tk()
        self.root.geometry("500x350")
        self.root.title("Productivity Pulse Control Panel by LStep")

        self.validate_func = self.root.register(self.validate_spinbox_input)

        # Measures time from the start of the application
        self.count = 0

        self.time_elapsed = tk.Label(self.root, text=f"Time Elapsed: {self.convert_seconds(self.count)}", font=('', 25))
        self.time_elapsed.pack(pady=10)

        # Container to store all elements used to display the time info
        self.history_container = tk.Frame()
        self.history_container.pack(pady=20)

        # Button used to display the time info
        self.history_button = tk.Button(self.history_container, 
                                        text="Show History", font=("", 15), 
                                        command=lambda: Plot(extract(self.window_list, 0), extract(self.window_list, -1), self.mode))
        self.history_button.grid(row=0, column=0, padx=20)

        # Allows user to choose if they want to see the information in a table or a graph
        self.mode = 'Graph'
        self.mode_choice_button = tk.Menubutton(self.history_container, 
                                              text="Select Display", 
                                              relief="raised",
                                              font=('', 15))
        self.mode_choice_button.grid(row=0, column=1)

        self.mode_choice_menu = tk.Menu(self.mode_choice_button, tearoff=0)
        self.mode_choice_menu.add_command(label='Display: Graph', command=lambda: self.set_mode('Graph'))
        self.mode_choice_menu.add_command(label='Display: Table', command=lambda: self.set_mode('Table'))

        self.mode_choice_button.config(menu=self.mode_choice_menu)

        # Separates sections
        self.separator = tk.Canvas(self.root, width=500, height=30)
        self.separator.pack()
        self.separator.create_line(0, 5, 500, 5, fill="#000000", width=5)
        self.separator.create_line(0, 25, 500, 25, fill="#000000", width=5)

        # Creates a timer
        self.timer_label = tk.Label(self.root, text="Create a Timer", font=('',30))
        self.timer_label.pack(pady=10)

        self.timer_container = tk.Frame() #A container to organize other elements
        self.timer_container.pack()

        # Used to specify how long user wants to work
        self.work_label = tk.Label(self.timer_container, text="Minutes of Work")
        self.work_label.grid(row=0, column=0)
        self.minute_work_input = tk.Spinbox(self.timer_container, 
                                            from_=1, to=60, 
                                            validate="key", 
                                            validatecommand=(self.validate_func, "%P"))
        self.minute_work_input.grid(row=0, column=1)
        
        # Used to specify how much rest the user wants
        self.rest_label = tk.Label(self.timer_container, text="Minutes of Rest")
        self.rest_label.grid(row=1, column=0)
        self.minute_rest_input = tk.Spinbox(self.timer_container, 
                                            from_=1, to=60, 
                                            validate="key", 
                                            validatecommand=(self.validate_func, "%P"))
        self.minute_rest_input.grid(row=1, column=1)
        
        # Button used to create the timer
        self.create_timer_button = tk.Button(self.root, 
                                             text="Create", 
                                             font=("", 15), 
                                             command=lambda: Timer(int(self.minute_work_input.get()), 
                                                                   int(self.minute_rest_input.get())))
        self.create_timer_button.pack(pady=10)


        self.countup()

        # Before exiting closes all processes
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

        self.stop_event.set()
        t1.join()

    def set_mode(self, mode: str) -> None:
        self.mode = mode
        self.mode_choice_button.config(text=f"Display: {mode}")
        
    def validate_spinbox_input(self, P: str) -> bool:
        # P is the proposed input
        if P.isdigit() or P == "":
            return True
        else:
            return False
    
    def countup(self) -> None:
        """Function that is called every second and increases the timer by one"""
        self.count += 1
        self.time_elapsed.config(text=f"Time Elapsed: {self.convert_seconds(self.count)}")
        self.time_elapsed.after(1000, self.countup)
    
    def convert_seconds(self, seconds: int) -> str:
        """Converts seconds to HH:MM:SS format"""
        time_delta = datetime.timedelta(seconds=seconds)
        time_string = str(time_delta)
        hours, minutes, seconds = time_string.split(':')
        return f"{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}"
    
    def on_close(self) -> None:
        """Closes all the processes of the application"""
        self.stop_event.set()
        self.root.destroy()