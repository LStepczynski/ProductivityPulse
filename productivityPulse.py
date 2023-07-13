import pygetwindow as gw
import win32gui, win32process, psutil
from time import sleep
import keyboard
from grapths import Plot
from KandL import extract


class ProductivityPulse:
    """Measures how much time is spent on all focused windows"""
    def __init__(self) -> None:
        """Checks what window is focused and starts counting"""
        self.window_list = list()
        while True:
            sleep(1)

            if keyboard.is_pressed("ctrl+shift+r"):
                Plot(extract(self.window_list, 0), extract(self.window_list, -1))

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

            print(self.window_list)

    def active_window_process_name(self):
        try:
            pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
            return(psutil.Process(pid[-1]).name())
        except:
            return None
    
    def active_window_title(self):
        try:
            window_handle = win32gui.GetForegroundWindow()
            window_title = win32gui.GetWindowText(window_handle)
            return window_title
        except: 
            return None

