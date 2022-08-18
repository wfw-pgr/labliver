# -*- coding: utf-8 -*-
import serial

com_num   = "/dev/cu.usbmodem142201"
baud_rate = 19200

def main():

    ser = serial.Serial( com_num, baud_rate, timeout=1)
    while True:

        print( " input control command, ( 'H':on, 'L':off, 'E':quit ) >>>", end="" )
        str_cmd   = input()
        byte_cmd  = bytes( str_cmd, encoding="ascii" )
        
        if ( str_cmd == "E" ): break
        ser.write( byte_cmd )
        
    ser.close()

if __name__ == '__main__':
    main()
