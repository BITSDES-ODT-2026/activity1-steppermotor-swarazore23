from machine import Pin
import time

IN1 = Pin(27,Pin.OUT)
IN2 = Pin(12, Pin.OUT)
IN3 = Pin(4,Pin.OUT)
IN4 = Pin(5,Pin.OUT)
pb1 = Pin(33, Pin.IN, Pin.PULL_UP)
pb2 = Pin(19, Pin.IN, Pin.PULL_UP)
my_t = 5


pos = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    val1 = pb1.value()
    val2 = pb2.value()
    
    if val1 == 0:
        print (val1)  
        for i in pos:
            IN1.value(i[0])
                
            IN2.value(i[1])
                
            IN3.value(i[2])
                
            IN4.value(i[3])
                
            time.sleep_ms(my_t)
    if val2 == 0:        
        print (val2)    
        for i in reversed(pos):
            
            IN1.value(i[0])
                
            IN2.value(i[1])
                
            IN3.value(i[2])
                
            IN4.value(i[3])
                
            time.sleep_ms(my_t)
        
