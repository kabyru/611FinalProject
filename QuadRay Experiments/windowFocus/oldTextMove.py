import win32.win32gui
import win32com.client
import keystrokeHandler
import pyautogui
import time

commandWindowID = win32.win32gui.GetForegroundWindow()
print("The HWND for the command window is " + str(commandWindowID))
gameWindowID = win32.win32gui.FindWindow(None,"QuadRay engine demo, (C) 2013-2020 VectorChief")
print("The HWND for the window is " + str(gameWindowID))

while True:
    command = input("Enter a command: ")

    if (command.lower() == "move forward"):
        print("Moving forward...")
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32.win32gui.SetForegroundWindow(gameWindowID)
        keystrokeHandler.WKey()
        time.sleep(0.5)
        win32.win32gui.SetForegroundWindow(commandWindowID)
    
    elif(command.lower() == "shoot"):
        print("Shooting gun...")
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32.win32gui.SetForegroundWindow(gameWindowID)
        keystrokeHandler.LButton2()
        time.sleep(0.5)
        win32.win32gui.SetForegroundWindow(commandWindowID)

    elif(command.lower() == "grenade"):
        print("Throwing Grenade...")
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32.win32gui.SetForegroundWindow(gameWindowID)
        keystrokeHandler.GKey()
        time.sleep(0.5)
        win32.win32gui.SetForegroundWindow(commandWindowID)
