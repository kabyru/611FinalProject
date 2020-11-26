import win32.win32gui
import win32com.client
import keystrokeHandler
import pyautogui
import time
import array as arr

commandWindowID = win32.win32gui.GetForegroundWindow()
print("The HWND for the command window is " + str(commandWindowID))
gameWindowID = win32.win32gui.FindWindow(
    None, "QuadRay engine demo, (C) 2013-2020 VectorChief")
print("The HWND for the window is " + str(gameWindowID))

# Now, begin automated control of the QuadRay Demo

# First, run the demo with
# ------------------  TARGET CONFIG  ---------------------
# SIMD size/type =  256x2v2, tile_W = 2xW, FSAA = 1 (off)
# Framebuffer X-row =   800, ptr = 0000000046A50080
# Framebuffer X-res =   800, Y-res =  480, l 0, h 0
# Window-rect X-res =   800, Y-res =  480, u 0, o 0
# Threads/affinity =   16/1, reserved = 0, d 3, c 1
# ---------------------  FPS LOG  ------ ptr/fp = 64_64 --

n_simd = [128]
k_size = [2, 1]
s_type = [4]
anti_aliasing = [1, 2, 4]
scenes = [1, 2, 3]

#First, set n_simd to 128
#Increase n_simd... Press the F8 Key
print("Changing n_simd...")
print("F8 Key has been pressed!")
pyautogui.keyDown('f8')
time.sleep(0.5)
pyautogui.keyUp('f8')
time.sleep(0.5)
print("F8 Key has been released!")

for scene in scenes:

    # If we're on the second scene, we will need to reset back to 256x2v2 before proceeeding since its default is 128x
    # if (scene == 2):

    for nsimd in n_simd:
        for ksize in k_size:
            for stype in s_type:
                for AA in anti_aliasing:

                    print("Now entering trial:")
                    print("Scene: " + str(scene))
                    print("n_simd: " + str(nsimd))
                    print("k_size: " + str(ksize))
                    print("s_type: " + str(stype))
                    print("Anti-Aliasing: " + str(AA))

                    print("Waiting for 10 seconds for the trial to finish...")
                    # Wait for 10 seconds to let the trial to run...
                    time.sleep(10)

                    # Increase AA...
                    print("Changing AA...")
                    print("F2 Key has been pressed!")
                    pyautogui.keyDown('f2')
                    time.sleep(0.5)
                    pyautogui.keyUp('f2')
                    time.sleep(0.5)
                    print("F2 Key has been released!")

                # Increase s_type... Press the F7 Key
                print("Changing s_type...")
                print("F7 Key has been pressed!")
                pyautogui.keyDown('f7')
                time.sleep(0.5)
                pyautogui.keyUp('f7')
                time.sleep(0.5)
                print("F7 Key has been released!")

            # Increase k_size... Press the F6 key
            print("Changing k_size...")
            print("F6 Key has been pressed!")
            pyautogui.keyDown('f6')
            time.sleep(0.5)
            pyautogui.keyUp('f6')
            time.sleep(0.5)
            print("F7 Key has been released!")

        # #Increase n_simd
        # print("Changing n_simd...")
        # shell = win32com.client.Dispatch("WScript.Shell")
        # shell.SendKeys('%')
        # win32.win32gui.SetForegroundWindow(gameWindowID)
        # keystrokeHandler.F8Key()
        # time.sleep(0.5)
        # win32.win32gui.SetForegroundWindow(commandWindowID)

    # Change the scene... Press the F11 key
    print("Changing scene...")
    print("F11 Key has been pressed!")
    pyautogui.keyDown('f11')
    time.sleep(0.5)
    pyautogui.keyUp('f11')
    time.sleep(0.5)
    print("F11 Key has been released!")

# Finally, kill the program... press the ESC key
print("Ending RooT Demo and saving data...")
print("ESC Key has been pressed!")
pyautogui.keyDown('esc')
time.sleep(0.5)
pyautogui.keyUp('esc')
time.sleep(0.5)
print("ESC Key has been released!")
