import webview
import threading

def create():
    webview.create_window("Test", "http://www.google.com")

def fullscreen():
    webview.toggle_fullscreen()

threading.Thread(target=create).start()
threading.Thread(target=fullscreen).start()
