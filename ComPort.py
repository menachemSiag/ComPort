import sys
import serial
import glob

# this function recognize COM connection and print the right port.
def serial_ports():
    if sys.platform.startswith('win'): #check if you using windows
        ports= ['COM%s' % (i + 1) for i in range(256)] #search all avilable com ports between 0-256
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'): # check  if your system is linux
        ports = glob.glob('/dev/tty[A-Za-z]*') #search for useable com ports
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform') #not supported platform
    result = []
    for port in ports:
        try:
            s = serial.Serial(port) #port useable
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result