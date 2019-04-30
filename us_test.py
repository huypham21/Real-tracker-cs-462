import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG=23
ECHO = 24
TRIG2 = 5
ECHO2 = 6

print("Distance measurement in progess")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)

def distance():
    #set Trigger to HIGH
    GPIO.output(TRIG, True)

    #set Trigger to LOW
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = time.time()

    #save StartTime
    while GPIO.input(ECHO)==0:
        start_time = time.time()

    #save time of arrival
    while GPIO.input(ECHO)==1:
        stop_time = time.time()

    #time difference between start and time of arrival
    time_elapsed = start_time - stop_time
    #multiply with the sonic speed (34300 cm/s)
    #and divide it by 2, because there and back
    distance = (time_elapsed * 34300)/2

    return distance

def distance2():
    #set Trigger to HIGH
    GPIO.output(TRIG2, True)

    #set Trigger to LOW
    time.sleep(0.0001)
    GPIO.output(TRIG2, False)

    start_time = time.time()
    stop_time = time.time()

    #save StartTime
    while GPIO.input(ECHO2)==0:
        start_time = time.time()

    #save time of arrival
    while GPIO.input(ECHO2)==1:
        end_time = time.time()

    #time difference between start and time of arrival
    time_elapsed = start_time - end_time
    #multiply with the sonic speed (34300 cm/s)
    #and divide it by 2, because there and back
    distance = (time_elapsed * 34300)/2

    return distance


if __name__ == '__main__':
    try:
        start = time.time()
        current = time.time()
        end = start +5
        totalIn = distance()
        averageIn = totalIn
        count = 1
        totalOut = distance2()
        averageOut = totalOut
        print("Please wait...calibrating sensors")
        
        while time.time() < end:
            dist1 = distance()
            dist2 = distance2()
            count = count +1
            totalIn = totalIn + dist1
            totalOut = totalOut + dist2
            averageIn = totalIn / count
            averageOut = totalOut / count
            time.sleep(0.1)
        print("AverageIn == %.1f" % averageIn)
        print("AverageOut == %.1f" % averageOut)
        print("Over %d points " % count)
        print("In trigger = %.1f" % (averageIn / 2))
        print("Out trigger = %.1f" % (averageOut / 2))
        timeIn = time.time()
        InSense = False
        timeOut = time.time()
        OutSense = False
        roomCount = 0
        totalCount = 0
        timeElapsed = 0
        maxPeople = 0
        averagePeople = 0
        inTrigger = abs(averageIn / 2)
        outTrigger = abs(averageOut / 2)
        while True:
            distIn = abs(distance())
            distOut = abs(distance2())
            
            if distIn < inTrigger:
                InSense = True
                print("In sensor triggered: %.1f" % distIn)
                timeIn = time.time()
            elif distOut < outTrigger:
                OutSense = True
                print("Out sensor triggered: %.1f" % distOut)
                timeOut = time.time()
            
            if InSense == True:
                #print("In")
                if OutSense == True:
                    #print("Out")
                    if timeIn < timeOut:
                        roomCount += 1
                        totalCount += 1
                        print("Person entered")
                        InSense = False
                        OutSense = False
                        time.sleep(0.5)
                    elif timeIn > timeOut:
                        roomCount -= 1
                        if roomCount < 0:
                            roomCount = 0
                        print("Person exited")
                        time.sleep(0.5)
                        InSense = False
                        OutSense = False
                    else:
                        print("Same time")
                elif time.time() > (timeIn + 0.25):
                    InSense = False
                    print("Too long before Out triggered")
            
            elif OutSense == True:
                #print("Out (2nd)")
                if time.time() > (timeOut + 0.25):
                    OutSense = False
                    print("Too long before In triggered")
                elif InSense == True:
                    if timeIn < timeOut:
                        roomCount += 1
                        totalCount += 1
                        print("Person entered")
                        InSense = False
                        OutSense = False
                        time.sleep(0.5)
                    elif timeIn > timeOut:
                        roomCount -= 1
                        print("Person exited")
                        time.sleep(0.5)
                        InSense = False
                        OutSense = False
            timeElapsed = time.time() - start
            print("time Elapsed == %.1f" % timeElapsed)
            averagePeople = totalCount / timeElapsed
            if roomCount > maxPeople:
                maxPeople = roomCount
            time.sleep(0.1)
        #reset by pressing CTRL + C
    except:
            print("Measurement stopped by User")
            print("Total people: %d" % totalCount)
            print("People inside at end: %d" % roomCount)
            print("Average number of people: %d" % averagePeople)
            print("Max attendance: %d" % maxPeople)
            print("Total time running %.1f" % timeElapsed)
            GPIO.cleanup()
