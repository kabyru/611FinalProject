#This program is a rewrite of MWTextMove256, since win32API does not apply to Linux
# and cannot be used.

import pyautogui
import time

#Now, begin automated control of the QuadRay Demo

#First, run the demo with
# ------------------  TARGET CONFIG  ---------------------
# SIMD size/type =  256x2v2, tile_W = 2xW, FSAA = 1 (off)
# Framebuffer X-row =   800, ptr = 0000000046A50080
# Framebuffer X-res =   800, Y-res =  480, l 0, h 0
# Window-rect X-res =   800, Y-res =  480, u 0, o 0
# Threads/affinity =   16/1, reserved = 0, d 3, c 1
# ---------------------  FPS LOG  ------ ptr/fp = 64_64 --

n_simd = [256]
k_size = [2, 1]
s_type = [2, 1]
anti_aliasing = [1, 2, 4]
scenes = [1, 2, 3]

for scene in scenes:

    #If we're on the second scene, we will need to reset back to 256x2v2 before proceeeding since its default is 128x
    #if (scene == 2):
    for AA in anti_aliasing:

        print("Now entering trial:")
        print("Scene: " + str(scene))
        print("n_simd: " + str(nsimd))
        print("k_size: " + str(ksize))
        print("s_type: " + str(stype))
        print("Anti-Aliasing: " + str(AA))

        #First, check if s_type = 4, because if so, it should only be used when n_simd = 128
        #Otherwise, if n_simd = 128, then s_type can ONLY be 4
        if (stype == 4 and nsimd != 128):
            print("Invalid case, nsimd must be 128 for stype to be 4. Skipping...")
            print("Changing AA...")
            #Increase AA prematurely... Press the F2 key
            print("F2 Key has been pressed!")
            pyautogui.keyDown('f2')
            time.sleep(0.5)
            pyautogui.keyUp('f2')
            time.sleep(0.5)
            print("F2 Key has been released!")

            continue

        if (nsimd == 128 and stype != 4):
            print("Invalid case, stype must be 4 for nsimd to be 128. Skipping...")
            print("Changing AA...")
            #Increase AA prematurely... Press the F2 key
            print("F2 Key has been pressed!")
            pyautogui.keyDown('f2')
            time.sleep(0.5)
            pyautogui.keyUp('f2')
            time.sleep(0.5)
            print("F2 Key has been released!")

            continue

        print("Waiting for 10 seconds for the trial to finish...")
        # Wait for 10 seconds to let the trial to run...
        time.sleep(10)

        #Increase AA... Press the F2 key
        print("Changing AA...")
        print("F2 Key has been pressed!")
        pyautogui.keyDown('f2')
        time.sleep(0.5)
        pyautogui.keyUp('f2')
        time.sleep(0.5)
        print("F2 Key has been released!")

    #Change the scene... Press the F11 key
    print("Changing scene...")
    print("F11 Key has been pressed!")
    pyautogui.keyDown('f11')
    time.sleep(0.5)
    pyautogui.keyUp('f11')
    time.sleep(0.5)
    print("F11 Key has been released!")
