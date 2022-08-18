# -*- coding: utf-8 -*-
import serial

com_num   = "/dev/cu.usbmodem142201"
baud_rate = 19200

def main():

    ser = serial.Serial( com_num, baud_rate, timeout=1)
    while True:

        print( " input PWM control value ( 0 < val < 255, or type quit ) >>> ", end="" )
        int_cmd   = input()
        byte_cmd  = bytes( int_cmd, encoding="ascii" )
        
        if ( int_cmd == "quit" ): break
        ser.write( byte_cmd )
        
    ser.close()

if __name__ == '__main__':
    main()
