import ctypes
from ctypes import wintypes
import time
import pyautogui

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
VK_TAB  = 0x09
VK_MENU = 0x12
VK_SPACE = 0x20
VK_WKEY = 0x57
VK_LBUTTON = 0x01
VK_2KEY = 0x32
VK_F1 = 0x71
VK_GKEY = 0x47

VK_F2 = 0x71
VK_F6 = 0x75
VK_F7 = 0x76
VK_F8 = 0x77
VK_F11 = 0x7A
VK_ESCAPE = 0x1B

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

#TO-DO: IMPLEMENT VIRTUAL KEY PRESSES FOR F2, F6, F7, F8, F11

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def F2Key():
    print("F2 Key Pressed!")
    PressKey(VK_F2)
    time.sleep(0.5) #This might need to be adjusted.
    ReleaseKey(VK_F2)
    time.sleep(0.5)
    print("F2 Key Released!")

def F6Key():
    print("F6 Key Pressed!")
    PressKey(VK_F6)
    time.sleep(0.5)
    ReleaseKey(VK_F6)
    time.sleep(0.5)
    print("F6 Key Released!")

def F7Key():
    print("F7 Key Pressed!")
    PressKey(VK_F7)
    time.sleep(0.5)
    ReleaseKey(VK_F7)
    time.sleep(0.5)
    print("F7 Key Released!")

def F8Key():
    print("F8 Key Pressed!")
    PressKey(VK_F8)
    time.sleep(0.5)
    ReleaseKey(VK_F8)
    time.sleep(0.5)
    print("F8 Key Released!")

def F11Key():
    print("F11 Key Pressed!")
    PressKey(VK_F11)
    time.sleep(0.5)
    ReleaseKey(VK_F11)
    time.sleep(0.5)
    print("F11 Key Released!")

def escKey():
    print("Escape Key Pressed!")
    PressKey(VK_ESCAPE)
    time.sleep(0.5)
    ReleaseKey(VK_ESCAPE)
    time.sleep(0.5)
    print("Escape Key Released!")

def AltTab():
    """Press Alt+Tab and hold Alt key for 2 seconds
    in order to see the overlay.
    """
    PressKey(VK_MENU)   # Alt
    PressKey(VK_TAB)    # Tab
    ReleaseKey(VK_TAB)  # Tab~
    time.sleep(2)
    ReleaseKey(VK_MENU) # Alt~

def SpaceBar():
    PressKey(VK_SPACE)
    print("Spacebar pressed!")
    #time.sleep(0.25)
    #ReleaseKey(VK_SPACE)

def SpaceBarRelease():
    print("Spacebar released!")
    ReleaseKey(VK_SPACE)

def WKey():
    print("W Key pressed!")
    for x in range(0,2):
        PressKey(VK_WKEY)
        time.sleep(0.5)
        ReleaseKey(VK_WKEY)
        time.sleep(0.5)
    print("W Key released!")

def LButton():
    print("Left Mouse Button pressed!")
    for x in range(0,20):
        PressKey(VK_LBUTTON)
        pyautogui.scroll(-1)
        time.sleep(0.5)
        pyautogui.scroll(1)
        #time.sleep(0.5)
        ReleaseKey(VK_LBUTTON)
        #pyautogui.scroll(-1)
        time.sleep(0.5)
    print("Left Mouse Button released!")

def LButton2(): #This one works and is simplier. Use of over LButton()
    print("Left Mouse Button pressed!")
    pyautogui.mouseDown(); pyautogui.mouseUp()
    print("Left Mouse Button released!")

def GKey():
    print("G Key pressed!")
    for x in range(0,2):
        PressKey(VK_GKEY)
        time.sleep(0.5)
        ReleaseKey(VK_GKEY)
        time.sleep(0.5)
    print("G Key released!")
        
    


#if __name__ == "__main__":
#    AltTab()