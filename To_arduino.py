import serial, time

serialPort = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

serialString = ""

def write_read(x):
    serialPort.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = serialPort.readline()
    return data        
        
while(1):
   if(serialPort.in_waiting > 0):
        
        num = input("Enter a number: ") # Taking input from user
        value = write_read(num)
        print(value) # printing the value
        
        serialPort.write(b"Thank you for sending data \r\n")   
        
        
        