import re
import sys
import datetime

#Pokemon XD RTC Calculator
#By Lucas (/u/ItsProfOak AKA Collector Togami)
#Credits:
# Rising_Fog from the Dolphin dev team for making the custom RTC feature that made this possible
#Kaphotics and Omegadonut for figuring out XDRNG PRNG
#Zari for researching seeding + cleaning code
#Admiral_Fish for helping with testing and making a video of this
#See the readme before using this program


print "Pokemon XD RTC Calculator 1.0 Beta"
print "By Lucas (/u/ItsProfOak AKA Collector Togami)"
print "Credits:"
print "Rising_Fog from the Dolphin dev team for making the custom RTC feature that made this possible"
print "Kaphotics and Omegadonut for figuring out XDRNG PRNG"
print "Zari for researching seeding"
print "Admiral_Fish for helping with testing and making a video of this"
print "Chimera for additional testing"
print "See the readme before using this program."


#The calculation to move the PRNG state ahead one frame. May be modified for other games.
def XDRNG(PRNG):
    return(PRNG * 0x000343FD + 0x00269EC3) & 0xFFFFFFFF


#The calculation to move the PRNG state back one frame. May be modified for other games.
def XDRNGR(PRNG):
    return (PRNG * 0xB9B33155 + 0xA170F641) & 0xFFFFFFFF

#The subroutine to call the RNG multiple times. May be modified for other games.
def callRNG(PRNG,direction,times):
    state=PRNG
    for counter in range(times):
        if direction == 1:
            state=XDRNG(state)
        else:
            state=XDRNGR(state)


    return state


#Finds the resulting seed that will happen if you add one second to the custom RTC.
#For Gale of Darknesxs, that is a constant 40.5 million. This may be adjusted for other games.
def nextSeed(currSeed):
    nextSeed = currSeed + 40500000
    if nextSeed > 4294967296:
        nextSeed &= 4294967295
    return nextSeed

#Prolly not the best way to validate input, but it'll do

def main():
    while True:
        try:
            calibratedSeed=int(raw_input("Enter the seed you get at the Gale of Darkness warning screen at 1/1/2000, 12:00:00 AM. "),16)
            if(calibratedSeed > 4294967296 or calibratedSeed < 0):
                raise ValueError
            else:
                break
        except ValueError:
            print "Your input is invalid. Try again."



    while True:
        try:
            DesiredTarget=int(raw_input("Enter the seed at which your target Pokemon is generated. If you do not know, use Calculate PID from IVs on RNG Reporter. "),16)
            if(DesiredTarget > 4294967296 or DesiredTarget < 0):
                raise ValueError
            else:
                break
        except ValueError:
            print "Your input is invalid. Try again."



    while True:
        try:
            threshold=int(raw_input("Enter the minimum number of frames you want to be away from your target. This program calculates initial seeds, so try not to go below 2-3000. "), 10)
            if threshold <= 2000:
                    print "That's too few frames away from the target. The animations before the title screen will go over your frame! Try something over 2000."
                    raise ValueError
                #I seriously hope this never happens but I leave it just to be sarcastic
            elif threshold >= 4294967296:
                print "You know the PRNG just cycles back after 2^32 frames, right? Congratulations, you hit your target."
                raise ValueError
            else:
                break
        except ValueError:
            print "Your input is invalid. Try again."



    while True:
        try:
            MaxFrames=int(raw_input("Enter the furthest you are willing to be from your initial seed, not counting the minimum threshold. Values below 10000 may never be hit. "),10)
            if MaxFrames <= 10000:
                    print "That's too close from your initial seed. Too small a number and this program may run indefinitely and never find a result, since not all seeds are possible.  Try something over 10000."
                #I seriously hope this never happens but I leave it just to be sarcastic
            elif MaxFrames >= 4294967296:
                print "You know the PRNG just cycles back after 2^32 frames, right? Congratulations, you hit your target."
            else:
                break
        except ValueError:
            print "Your input is invalid. Try again."


    print "The program will now calculate a seed near your target. This may take 20-30+ minutes depending on your settings."





    #Calls XDRNG(R) for the requested distance from your target.
    AdjustedTarget = callRNG(DesiredTarget, 2, threshold)

    secondsToAdd=0
    secondcount = 0
    targetHit = 0

    minutesPassed = 0

    while(targetHit == 0):
        #Setting the PRNG as the calibrated seed here is what factors the nanosecond timing issue.
        PRNG=calibratedSeed
        framesAway=0

        #This loop ensures you don't get frames too far from your desired target.
        for frames in range(MaxFrames):
            PRNG = XDRNG(PRNG)
            framesAway+=1

            #When a target is finally hit, we're done.
            if PRNG == AdjustedTarget:
                targetHit = 1

                break




        #Factors the 40.5 million addition to the PRNG between each second, while not going over 2^32.
        calibratedSeed = nextSeed(calibratedSeed)
        secondsToAdd+=1
        secondcount += 1

        #Maybe change this at some point
        if secondcount == 60:
            minutesPassed+=1
            secondcount = 0
            print "Minute(s) added to the RTC so far: ", minutesPassed, "No seed found yet. Going for the next minute."


    #Creates a clock object with the date set to the earliest possible seed at Jan 1 2000
    clock = datetime.datetime(2000,1,1)
    #Adds however many seconds necessary for the seed
    adjustedClock= clock + datetime.timedelta(seconds=secondsToAdd-1)


    print "The following date/time will work for your current Dolphin settings: \n"
    print(adjustedClock)
    print "This is year/month/day and a 24 hour clock format, that may have to be adjusted accordingly for your computer.\n"
    print "You will be ", threshold + framesAway+1, " frames away from your target.\n"
    print "Due to the nanosecond issue, this will only work on your computer with the settings you have for Dolphin right now. Please read the readme for more information."

while True:
    main()
    more = (raw_input("Type 1 and press Enter if you want to do another search, or anything else to exit."))

    if more != "1":
        break

