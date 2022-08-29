#!/usr/bin/python3
import can
import time
import logging

logging.basicConfig(level=logging.INFO)

def periodic_send(msg, bus):
    task = bus.send_periodic(msg, 0.20)
    assert isinstance(task, can.CyclicSendTaskABC)

    return task

if __name__ == "__main__":
    bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
    can_ids = [
        0x181080F5, 0x181081F5, 0x181082F5, 0x181083F5,
        0x181084F5, 0x181085F5, 0x181086F5, 0x181087F5,
        0x181088F5, 0x181089F5
    ]
    tasks = []

    for can_id in can_ids:
        msg_volt = can.Message(arbitration_id=can_id,
                               data=[1, 0, 0, 0, 0, 0, 0, 0],
                               extended_id=True)
        tasks.append(periodic_send(msg_volt,bus))
        msg_temp = can.Message(arbitration_id=can_id,
                               data=[2, 0, 0, 0, 0, 0, 0, 0],
                               extended_id=True)
        tasks.append(periodic_send(msg_temp,bus))

    time.sleep(200)
