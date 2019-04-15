# Real-tracker-cs-462




Real-time traffic tracker


Texas A&M University 
CSCE 462-501 Project
Professor: Dr. Jyh Liu
TA: Zelun Wang


Team Doorman:
Huy Pham
Jadie Marshall 







Last Updated: 3/17/2019




Summary:

This device can be used for security and statistical reasons. For example, it can track the people get in and out a shop to see the when it’s busy and how popular the shop is. Or it can count the people get in to airplane, an event or movie theater to prevent intruder. It could be used for a lot of organizations and/or venues to track total attendance, max number of people that were in the room, average attendance for weekly events such as church. This device can act as a foundations of many useful Data Science projects.

The motivation was initially for Dr. Krishna Narayanan from Electrical Engineering department on his data science research on Graph signal processing for vehicle traffic prediction. His team was collecting data from Dallas region and found that collecting most recent data is one of the biggest challenges. With the motivation, our team would come up with a IoT system that can collect weather and traffic data.

Goal:

Design and build reliable system for business use and scalable up to outdoor vehicles and pedestrians
Real-time Machine/Deep Learning model deployed into the system
Deploy cloud service tools for data analytic purpose
Webapp UI for stakeholders 


Design:


Image 1: Sketch of Prototype design

A camera module with a Raspberry Pi “Counter system” is placed on the ceiling of the inner side of the door (or hallway). The Counter system is trained with Machine/Deep learning technique that combines both object detection and object tracking.Object Recognition model detects human and object tracking model identifies whether a person is walking in or out. 
There will be a register of the time of each entry or exit, the total number of people who entered, the maximum number of people (as well as the corresponding time) who were in the building/room at once, the average number of people over the course of the time, etc. The current count and other statistics will be displayed on the LCD screen at the entrance.
A Internet of Things system will allow the devices to communicate using AWS for data analysis, monitoring, and controlling other subsystems over internet connection.
	A second Raspberry Pi that handles UI displaying, will also need to handle the optional subsystems such as barrier arm motion or metal detection. 



Image 2: Counter system

A laser “range finder” is placed on each side of the door, at approximately mid-body height. A change in the distance detected (meaning, a person moves across the emitted laser) would signal an interrupt. If the other subsequently detects a change within a given time (in case of accidentally walking too close to a doorway), the counter will then add or subtract from the current “head count”. 

Image 3: Metal detector subsystem

Team Agreement
Communication
Agree to communicate through text, email, Discord, and in-person as needed and in a timely fashion
Agree to communicate any complications, conflicts, etc. as soon as possible
	Time Willing to Commit
Agree to work together on project weekly, Tuesday or Thursday afternoons, as schedules permit
Agree to work separately as needed to divide work equally 


Signed:
Jadie Marshall UIN: 624005016, Date 02/14/2019
Huy Pham UIN: 826001901, Date 02/14/2019

Bill of Materials
Raspberry Pi (from CSCE 462 lab kit)
3D print components  
Device name
Website
Specs
kuman 7 Inch Capacitive Touch Screen TFT LCD Display HDMI Module 800x480 for Raspberry Pi 3 2 Model B and RPi 1 B+ A BB Black PC Various Systems SC7B (Touch Screen) (7 Inch Capacitive Touch Screen
[$53.99]
https://amzn.to/2TPHVJQ 
-Capacitive touch control and has vertical and horizontal image flip function. Image 4:3 / 16:9 display format conversion.

-Operating voltage: 5V 1A power supply current requirements within the above 2A, On board 400mA DC-DC Boost regulator to provide power supply to LCD backlight.

-Support 864 x 480 x 24bit graphics content through SSD1963 controller. .It also equips parallel MCU interfaces in different bus width to receive graphics data and command from MCU. Its display interface supports common RAM-less LCD driver of color depth up to 24 bit-per-pixel. Warning: All data port voltage can not exceed 3.6V.

-Supports BB Black, comes with related images like:Angstrom. and also Supports Banana Pi/Banana Pro,comes with related images like:Lubuntu, Raspbian.
Kuman 7 inch Raspberry Pi Touch Screen Case Holder

[$11.99]
https://amzn.to/2Fua00o 
Application: This Acrylic Protective Case Bracket Suitable for raspberry pi 7 inch TFT touch screen, the screen size can be 164.9(w)X100.0(H)x5.7(D)mm.

Saves space: Raspberry pi board can be installed on the back.
TFmini Lidar Range Finder Sensor Module
[$39.90] (x2)
https://amzn.to/2Ctl2kv 
LIDAR Sensor module
How to use with raspberry pi: https://github.com/TFmini 
Operating Range : 0.3-12m
Maximum operating range at 10% reflectivity : 5m
Applicable voltage range : 4.5-6V
Average power consumption : 0.12W
Command Large Picture Frame Hangers, 14 Pairs
[$9.19]
https://amzn.to/2JwKk7i 
Command Strips for attaching sensors - Will be using the “Large” size that hold up to 16 lbs, to ensure secure hold.
Gikfun MDS-60 Metal Detector Module for Arduino (Pack of 2 pcs) EK1906
[$15.98]
https://amzn.to/2TZsU8r
【Metal Detector】Working Voltage: DC3-5V, Detecting Distance: <60mm.
【Buzzer&Light】Buzzer start to ring and the red light indicator is on when the metal is close to the metal detector.
【Mini Size】PCB Board Size: 86X61mm/3.39X2.40inch


3/4 in. Nickel Plated Fixed Pulley
[$2.36] X2
 
https://thd.co/2TFXtuK 
Pulley to implement “full-body scan” metal detection


 





Total: $175.60





