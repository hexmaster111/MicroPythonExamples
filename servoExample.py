from machine import Pin, PWM, ADC
import utime

def rescale(val, in_min, in_max, out_min, out_max): #This will rescal a val
    return out_min + (val - in_min) * ((out_max - out_min) / in_max - in_min)

def nsToDeg(val): #Just to make servo stuff easer
    return rescale(val, 0, 180, 400000, 2600000)




pwm = PWM(Pin(15))
pwm.freq(50)
pwm.duty_ns(1500000)

analog_value = ADC(28) #what adc pin we are on

while True:
    reading = analog_value.read_u16() #read the analog value
    scail = rescale(int(reading),0,65535,0,180) #scail the value to 0-180 for the nstodeg
    pwm.duty_ns(int(nsToDeg(scail))) #set the servo to the scailed number for the deg 
