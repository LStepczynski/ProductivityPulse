import pygetwindow as gw
import win32gui, win32process, psutil
from time import sleep
from grapths import Plot
from KandL import extract


class ProductivityPulse:
    """Measures how much time is spent on all focused windows"""
    def __init__(self, stop_event, window_list) -> None:
        """Checks what window is focused and starts counting"""
        self.window_list = window_list
        self.stop_event = stop_event
        while not self.stop_event.is_set():
            sleep(1)

            should_add = True # Determines if the focused window should be added to the window list
            self.focused_window = self.active_window_process_name()

            if not self.focused_window:
                continue

            for element in self.window_list:
                if element[0] == self.focused_window:
                    should_add = False
            
            if should_add:
                self.window_list.append([self.focused_window, 0])

            for element in self.window_list:
                if element[0] == self.focused_window:
                    element[-1] += 1


    def active_window_process_name(self) -> str:
        try:
            pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
            return(psutil.Process(pid[-1]).name())
        except:
            return None
    
    def active_window_title(self) -> str:
        try:
            window_handle = win32gui.GetForegroundWindow()
            window_title = win32gui.GetWindowText(window_handle)
            return window_title
        except: 
            return None

