import threading
import tkinter as tk

from gui.app import KeyLoggerApp
from logger.key_listener import KeyLogger
from logger.logger import KeyLoggerService

logger = KeyLoggerService()

def run_gui():
    root = tk.Tk()
    app = KeyLoggerApp(root)
    
    def on_key(key_str):
        app.show_key(key_str)
        logger.log(key_str)
    keylogger = KeyLogger(on_key_callback=on_key)
    keylogger.start()
    
    root.mainloop()


if __name__ == "__main__":
    gui_thread = threading.Thread(target=run_gui)
    gui_thread.start()
        