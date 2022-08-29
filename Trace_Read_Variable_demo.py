import platform
import ctypes
import sys
import xlrd
import xlwt
import xlsxwriter
from openpyxl import load_workbook

ostype = ctypes.sizeof(ctypes.c_voidp) * 8
if (platform.system()=='Windows') or (platform.system()[0:6]=='CYGWIN') :
    # WINDOWS
    t32api = ctypes.CDLL("D:/Programme/Trace32/TriCore/ICD/19_09_01\demo/api/capi/dll/t32api64.dll" if ostype==64 else "D:/Programme/Trace32/TriCore/ICD/19_09_01\demo/api/capi/dll/t32api.dll")
    print("Pass")
elif platform.system()=='Darwin' :
    # Mac OS X
    t32api = ctypes.CDLL("./t32api.dylib")
else :
    # Linux
    t32api = ctypes.CDLL("./t32api64.so" if ostype==64 else  "./t32api.so")


# Declare UDP/IP socket of the TRACE32 instance to access
t32api.T32_Config(b"NODE=",b"localhost")
t32api.T32_Config(b"PORT=",b"20000")

# Connect to TRACE32
error = t32api.T32_Init()
if error != 0 :
   sys.exit("Can't connect to TRACE32!")

# Select to debugger component of TRACE32 (B:: prompt)
t32api.T32_Attach(1)
print("pass2")

# Get details for symbol flags[3]
#vname = b"DL_Valve_SignalObjectCA[0].SignalState"
#vaddr = ctypes.c_int32(0)
#vsize = ctypes.c_int32(0)
#vaccess = ctypes.c_int32(0)
#rc = t32api.T32_GetSymbol(vname,ctypes.byref(vaddr),ctypes.byref(vsize),
#ctypes.byref(vaccess))
#print(vaddr)
#print(vname)
#print(vsize)
#print(vaccess)

# Set a write breakpoint to flags[3]
#t32api.T32_WriteBreakpoint(vaddr.value,0,16,vsize.value)

# Start program
t32api.T32_Go()
print("pass2")

# Wait for breakpoint hit
#pstate = ctypes.c_uint16(-1)
#while rc == 0 and not pstate.value == 2:
#      rc = t32api.T32_GetState(ctypes.byref(pstate))

# Read variable
vname = b"HL_AnalogIn_SignalValue[27]"
print(type(vname))
vvalue = ctypes.c_int32(0)
vvalueh = ctypes.c_int32(0)
rc = t32api.T32_ReadVariableValue(vname,ctypes.byref(vvalue),ctypes.byref(vvalueh))
print (rc)
b=str(vvalue.value)
print(b)
print(type(b))
#print("flags[3] = " + str(vvalue.value))
print("completed")



