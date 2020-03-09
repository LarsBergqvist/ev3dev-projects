#!/usr/bin/env python3
from ev3dev.ev3 import *

ir = InfraredSensor() 
ts = TouchSensor()
m1 = LargeMotor(OUTPUT_C)
m2 = LargeMotor(OUTPUT_D)

ir.mode = 'IR-PROX'

while not ts.value():
    distance = ir.value()

    if distance < 80:
        m1.run_forever(speed_sp=100)
        m2.run_forever(speed_sp=100)
    else:
        m1.stop(stop_action="hold")
        m2.stop(stop_action="hold")

Sound.beep()       
