import logging
import ctypes
import time
import platform
import ctypes
import sys
import xlrd
import xlwt
import xlsxwriter
from openpyxl import load_workbook
import can
logging.basicConfig(level=logging.INFO)

#bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=500000)
#bus=can.interfaces.vector.VectorBus(channel=1, can_filters=None, poll_interval=0.01, bitrate=None, rx_queue_size=256, app_name='CANalyzer', **config)


def simple_periodic_send(bus):
    """
Sends a message every 20ms with no explicit timeout
Sleeps for 2 seconds then stops the task.
"""
    print("Starting to send a message every 200ms for 2s")
    msg = can.Message(arbitration_id=0x123, data=[0x2, 0x11, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0], extended_id=True)
    print(type(arbitration_id))
    print(type(data))
    task = bus.send_periodic(msg, 0.20)
    assert isinstance(task, can.CyclicSendTaskABC)
    time.sleep(2)
    task.stop()
    print("stopped cyclic send")

    

ostype = ctypes.sizeof(ctypes.c_voidp) * 8
if (platform.system()=='Windows') or (platform.system()[0:6]=='CYGWIN') :
    # WINDOWS
    t32api = ctypes.CDLL("C:/Programme/Trace32/TriCore/ICD/13_12_10\demo/api/capi/dll/t32api64.dll" if ostype==64 else "C:/Programme/Trace32/TriCore/ICD/13_12_10\demo/api/capi/dll/t32api.dll")
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

# Start program
t32api.T32_Go()

#write the values to excelsheet
wb = load_workbook('D:/Krishna_Local/Trace_32_automation/Trace_32_automation/Trace_demo1.xlsx')  # Work Book
sheet = wb.active
#Read the Variable address from excel sheet 
workbook = xlrd.open_workbook('D:/Krishna_Local/Trace_32_automation/Trace_32_automation/Trace_demo1.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
worksheet = workbook.sheet_by_index(0)
num_rows = worksheet.nrows - 1
num_cols = worksheet.ncols - 1
curr_row = 0
curr_col = 0
arbitration_id=worksheet.col(1)
data=worksheet.col(2)
read_variable=worksheet.col(3)

while curr_row < num_rows:
        curr_row += 1
        #row = worksheet.row(curr_row)
        arbitration_id=worksheet.col(1)
        data=worksheet.col(2)
        read_variable=worksheet.col(3)
        #row=(row[0].value)
        arbitration_id=(arbitration_id[curr_row].value)
        #time.sleep(2)
        print(arbitration_id)
        if ((arbitration_id) != (0)):
            data=(data[curr_row].value)
            print(data)
            #print(type(data[0]))
            if((data) !=(0)):
                read_variable=(read_variable[curr_row].value)
                read_variable=read_variable.encode('utf-8')
                # Read variable
                vname = read_variable
                #print(type(vname))
                vvalue = ctypes.c_int32(0)
                vvalueh = ctypes.c_int32(0)
                rc = t32api.T32_ReadVariableValue(vname,ctypes.byref(vvalue),ctypes.byref(vvalueh))
                print (rc)
                print(read_variable,str(vvalue.value))
                print("completed")
                #print(read_variable)
                
            
           

#data=worksheet.col(2)
#print(arbitration_id)
#print(data)
#arbitration_id=arbitration_id[0]
#arbitration_id=(arbitration_id[index].value)

#second_col=int(second_col,base=16)
#arbitration_id=int(arbitration_id,base=16)
#print (arbitration_id)
#print (type(arbitration_id))
#if ((arbitration_id) != (0)):
    #print(data[0])
    #print(type(data[0]))
    
    
    




