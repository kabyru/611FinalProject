import win32.win32gui

windowID = win32.win32gui.FindWindow(None,"windowFocus")

print(windowID)

win32.win32gui.SetForegroundWindow(windowID)