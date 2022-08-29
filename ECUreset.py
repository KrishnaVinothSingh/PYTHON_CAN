import logging
import time
import can


def send_one():
    print("start")
#bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
#bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
    bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=[1], bitrate=500000)
    print(bus)
    msg1 = can.Message(arbitration_id=0x57A,data=[0x50, 0x00, 0xE8, 0x01, 0x8F ,0xE1, 0x00, 0x00],dlc=8,extended_id=False)
    msg2 = can.Message(arbitration_id=0x57B,data=[0x50, 0x00, 0xE8, 0x01, 0x8F ,0xE1, 0x00, 0x00],dlc=8,extended_id=False)
    msg3 = can.Message(arbitration_id=0x57C,data=[0x50, 0x00, 0xE8, 0x01, 0x8F ,0xE1, 0x00, 0x00],dlc=8,extended_id=False)
    msg4 = can.Message(arbitration_id=0x57D,data=[0x50, 0x00, 0xE8, 0x01, 0x8F ,0xE1, 0x00, 0x00],dlc=8,extended_id=False)
    msg5 = can.Message(arbitration_id=0x57E,data=[0x50, 0x00, 0xE8, 0x01, 0x8F ,0xE1, 0x00, 0x00],dlc=8,extended_id=False)
    msg6 = can.Message(arbitration_id=0x57F,data=[0x50, 0x00, 0xE8, 0x01, 0x8F ,0xE1, 0x00, 0x00],dlc=8,extended_id=False)
     
    try:
        bus.send(msg1)
        bus.send(msg2)
        bus.send(msg3)
        bus.send(msg4)
        bus.send(msg5)
        bus.send(msg6)
        print("Message sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message NOT sent")

if __name__ == "__main__":
    send_one()
def simple_periodic_send(bus):
    """
Sends a message every 20ms with no explicit timeout
Sleeps for 2 seconds then stops the task.
"""
    print("Starting to send a message every 200ms for 2s")
    msg = can.Message(arbitration_id=0x18DA0BFE, data=[0x2, 0x11, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0], extended_id=True)
    task = bus.send_periodic(msg, 0.20)
    assert isinstance(task, can.CyclicSendTaskABC)
    time.sleep(2)
    task.stop()
    print("stopped cyclic send")

print("bye")


