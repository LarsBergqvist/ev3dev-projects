#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

ts = TouchSensor()
leds = Leds()
m = MediumMotor(OUTPUT_A)

Sound.speak("Hello, I am a robot! Awaiting your command...")

while True:
    if ts.is_pressed:
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")
        m.on(speed=45)
    else:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")
        m.off()
