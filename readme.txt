Pokemon XD RTC Calculator 1.0 Beta
By Lucas (/u/ItsProfOak AKA Collector Togami)


Credits:
Rising_Fog from the Dolphin dev team, for making the custom RTC feature that made this possible
Kaphotics and Omegadonut, for figuring out XDRNG PRNG
Zari, for researching seeding
Admiral_Fish, for helping with testing and making a video of this
Chimera, for additional testing

Note: this is not working for Colosseum at this time. There is not a constant increase/decrease, and manipulating the clock frequency is not precise enough.

Admiral's video guide: https://www.youtube.com/watch?v=bcARBesyEEI

Usage instructions:
1. Open the program with Python 2.7 (not 2.6).

2. Using dolphin devmode 5.0-266 or above, go to Config, Advanced, and check the “Enable Custom RTC” box. Set the date/time to Jan 1, 2000, at midnight.


3. Open Gale of Darkness and pause the game at the warning screen. Check the PRNG state at 004e8610 (this value may be different for non USA versions). This is your calibrated seed, factoring the nanosecond issue. (See Nanosecond Issue explanation for more information) Enter this in the program.

4. Enter the seed at which your desired target is generated. If you do not know, use RNG Reporter’s 4th gen tools -> calculate PiD from IVs to find out. Note that his program does NOT factor nature locks and otherwise unhittable seeds.

5. Enter the minim number of frames you want to be away from your target. The program will run XDRNG backwards that many times, then use that value as the adjusted target. The program will reject a value that is too low, as the title screen eats frames. 

Furthermore, you will want to give yourself room to handle nature locks, noise, and other factors that use frames before you reach your target.

6. Enter the maximum distance you want to be from your adjusted target. Let’s say your adjusted target is 10,000 frames from your target seed, and you do not want to be more than 50,000 frames away from it, from your starting seed. In that case, enter 40,000. Due to the limited amount of possible initial seeds, values that are too small will prompt the user to input a higher value.

 You may change the conditional in the code itself, but too low a value may cause the program to run indefinitely and never find a target.

7. Wait for the program to find the date/time for your target. This may take anywhere from a few minutes to over an hour, depending on your computer’s specs and the chosen parameters. The program will let you know every time one minute’s worth of RTC seeds passes.
8. When a target is found, enter the date/time specified (note: this outputs the calendar in a predetermined format and may have to be adjusted for your computer, such as AM/PM vs 24 hour) in your custom RTC settings.
9. Double- check the result by entering the seed you get from Dolphin at the given date/time. From there, RNG your target as usual.

Nanosecond Issue Explanation (technical information on how/why this works):
	Gamecube and Wii games that use date/time for seeding will do so at a nanosecond level. In the case of Gale of Darkness, the initial seed has a constant 40.5 million added to it for every second incremented on the RTC. If a game has such a constant, then one may predict what the next seed will be. I have left comments on the code about what parts to change, if one wishes to adapt the code for another game. This may be useful for TAS, speedrunning, debugging, and other things that require RNG manipulation. Doing so is my way of saying thanks to the Dolphin devs and the TAS community, for their help on making this possible.
Side note: depending on how 3DS emulation turns out in the future, it may be possible to use this program to manipulate initial seeds there. I plan to revisit this when the time comes.

While you can replicate the same result over and over, it is highly unlikely that two computers will obtain the same result. The following is an incomplete list of what may affect your seeding. If you know something else that may affect it, please let me know by submitting an issue or just emailing me.
1. Incorrect custom RTC value entered (or custom RTC being disabled).
2. Using the GC  BIOS.
3. Different computers (due to CPU).
4. Any setting on your computer itself that affects clock timing, such as overclocking.
5. CPU emulation engine setting.
6. Audio emulation setting (anything in the Audio section of the config, except volume level).
7. CPU clock override in Dolphin.
8. SRAM.raw file.
9. Different versions of Dolphin.
