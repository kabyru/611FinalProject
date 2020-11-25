import win32.win32gui
import win32com.client
import keystrokeHandler
import pyautogui
import time
import array as arr

commandWindowID = win32.win32gui.GetForegroundWindow()
print("The HWND for the command window is " + str(commandWindowID))
gameWindowID = win32.win32gui.FindWindow(None,"QuadRay engine demo, (C) 2013-2020 VectorChief")
print("The HWND for the window is " + str(gameWindowID))

#Now, begin automated control of the QuadRay Demo

#First, run the demo with
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
#Increase n_simd
print("Changing n_simd...")
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys('%')
win32.win32gui.SetForegroundWindow(gameWindowID)
keystrokeHandler.F8Key()
time.sleep(0.5)
win32.win32gui.SetForegroundWindow(commandWindowID)

for scene in scenes:

    #If we're on the second scene, we will need to reset back to 256x2v2 before proceeeding since its default is 128x
    #if (scene == 2):


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

                    #First, check if s_type = 4, because if so, it should only be used when n_simd = 128
                    #Otherwise, if n_simd = 128, then s_type can ONLY be 4
                    if (stype == 4 and nsimd != 128):
                        print("Invalid case, nsimd must be 128 for stype to be 4. Skipping...")
                        print("Changing AA...")
                        #Increase AA prematurely...
                        shell = win32com.client.Dispatch("WScript.Shell")
                        shell.SendKeys('%')
                        win32.win32gui.SetForegroundWindow(gameWindowID)
                        keystrokeHandler.F2Key()
                        time.sleep(0.5)
                        win32.win32gui.SetForegroundWindow(commandWindowID)
                        
                        continue
                    if (nsimd == 128 and stype != 4):
                        print("Invalid case, stype must be 4 for nsimd to be 128. Skipping...")
                        print("Changing AA...")
                        #Increase AA prematurely...
                        shell = win32com.client.Dispatch("WScript.Shell")
                        shell.SendKeys('%')
                        win32.win32gui.SetForegroundWindow(gameWindowID)
                        keystrokeHandler.F2Key()
                        time.sleep(0.5)
                        win32.win32gui.SetForegroundWindow(commandWindowID)

                        continue
                    
                    print("Waiting for 10 seconds for the trial to finish...")
                    time.sleep(10) #Wait for 10 seconds to let the trial to run...

                    #Increase AA...
                    print("Changing AA...")
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shell.SendKeys('%')
                    win32.win32gui.SetForegroundWindow(gameWindowID)
                    keystrokeHandler.F2Key()
                    time.sleep(0.5)
                    win32.win32gui.SetForegroundWindow(commandWindowID)
                
                #Increase s_type...
                # print("Changing s_type...")
                # shell = win32com.client.Dispatch("WScript.Shell")
                # shell.SendKeys('%')
                # win32.win32gui.SetForegroundWindow(gameWindowID)
                # keystrokeHandler.F7Key()
                # time.sleep(0.5)
                # win32.win32gui.SetForegroundWindow(commandWindowID)

            #Increase k_size
            print("Changing k_size...")
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32.win32gui.SetForegroundWindow(gameWindowID)
            keystrokeHandler.F6Key()
            time.sleep(0.5)
            win32.win32gui.SetForegroundWindow(commandWindowID)

        # #Increase n_simd
        # print("Changing n_simd...")
        # shell = win32com.client.Dispatch("WScript.Shell")
        # shell.SendKeys('%')
        # win32.win32gui.SetForegroundWindow(gameWindowID)
        # keystrokeHandler.F8Key()
        # time.sleep(0.5)
        # win32.win32gui.SetForegroundWindow(commandWindowID)

    #Change the scene...
    print("Changing scene...")
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32.win32gui.SetForegroundWindow(gameWindowID)
    keystrokeHandler.F11Key()
    time.sleep(0.5)
    win32.win32gui.SetForegroundWindow(commandWindowID)






#This is the default configuration of the file.
print("Running the RooT Demo for n_simd = 256, k_size = x2, s_type = v2...")
time.sleep(10) #Let the Demo run this default config for 10 seconds...
#Now, swap this 
