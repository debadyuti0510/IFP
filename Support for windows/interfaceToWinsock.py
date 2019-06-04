from ctypes import *
mydll = cdll.LoadLibrary("C:\\pythondll_1.dll")
mydll.sendtoserver()

