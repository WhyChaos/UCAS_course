from gui.index import start
import ctypes

def hide_console():
    hide_window = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(hide_window, 0)

if __name__ == '__main__':
    hide_console()
    start()