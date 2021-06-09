# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:19:44 2021

@author: Nathan Drouillard
"""

import serial
import numpy as np
import time

#%% Open the COM port

ser = serial.Serial('COM4',38400,timeout=10)

#%% Home the stage

def home():
    
    ser.write(b'1HOM\r')
    ser.write(b'1WST\r')
    ser.flush()
    isstopped = ser.readline()
    print(isstopped)
    print("homed")
    ser.write(b'1ZRO\r')
    ser.flush()
    zeroed = ser.readline()
    print("zeroed")

#%% Move the stage (moves one way, but not back and forth)
home()

# def move():
pos_array = np.empty(1)
tic = time.time()
for i in range(0,20):
    # ser.write(b'1PGL0\r') #loop program continuously
    ser.write(b'1MVR0.00001\r') #move to negative limit
    ser.flush()
    #ser.write(b'1WST\r')
    #time.sleep(1)
    #ser.flush()
    ser.write(b'1POS?\r')
    pos = ser.readline()
    pos_str = str(pos)
    pos_splt = pos.strip().split(b",")
    enc_pos_str = pos_splt[1]
    enc_pos_val = float(enc_pos_str)
    # print(enc_pos_val)
    pos_array = np.append(pos_array, enc_pos_val)
    ser.flush()
toc = time.time()
print(toc-tic)
#%% Close COM port (important)
ser.close()
def close():
    
    ser.close()
