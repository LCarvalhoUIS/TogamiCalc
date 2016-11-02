# **TogamiCalc 1.1**
## By Lucas (/u/ItsProfOak AKA Collector Togami) <br/>


Credits:<br/>
Rising_Fog from the Dolphin dev team, for developing the custom RTC feature that made this possible <br/>
Kaphotics and Omegadonut, for figuring out XDRNG <br/>
Zari, for researching seeding and code optimization<br/>
Admiral_Fish, for helping with testing and making a video tutorial on how to use the program<br/>
Chimera, for additional testing

Note: this is **not** working for Colosseum at this time. There is not a constant increase/decrease, and manipulating the clock frequency is not precise enough.

[Admiral_Fish's video guide](https://www.youtube.com/watch?v=bcARBesyEEI)

## Usage instructions: <br/>
1. Open the program with Python **2.7** (not 2.6).<br/>

2. Using dolphin dev mode _5.0-266_ or above, go to Config, Advanced, and check the “Enable Custom RTC” box. Set the date/time to January 1, 2000, at midnight. Depending on your system, this may be 12:00:00 AM, 00:00:00, or another format. Make sure the correct date and time are selected.<br/>

3. Open Gale of Darkness and pause the game at the warning screen. Check the PRNG state at 004e8610. If this does not display a valid location, then 804e8610 works for your version of Dolphin. The original location is different for non USA versions.<br/>
This is your calibrated seed, factoring the nanosecond clock timing. (See Nanosecond Issue explanation for more information) Enter this in the program.<br/>

4. Enter the seed at which your desired target is generated. If you do not know, use RNG Reporter’s 4th gen tools -> calculate PiD from IVs to find out. Note that this program does **NOT** factor nature locks, N-Count, and otherwise unhittable seeds. __You are responsible for any extraneous variables that prevent your desired outcome.__

5. Enter the minimum number of frames you are willing to be away from your target. The program will run XDRNG backwards that many times, then use that value as the adjusted target. The program will reject a value that is too low, as the title screen eats frames.<br/>
Furthermore, you will want to give yourself room to handle nature locks, N-Count, noise, and other factors that consume pseudorandom frames before you reach your target.

6. Enter the maximum distance you want to be from your adjusted target. For example, if your adjusted target is 10,000 frames from your target seed, and you do not want to be more than 50,000 frames away from it, from your starting seed. In that case, enter 40,000. Due to the limited amount of possible initial seeds, values that are too small will prompt the user to input a higher value.<br/>

 You may change the conditional in the code itself, but too low a value may cause the program to run indefinitely and never find a target. _Change the thresholds at your own risk._

7. Wait for the program to find the date/time for your target. This may take anywhere from a few minutes to over an hour, depending on your computer’s specs and the chosen parameters. The program will let you know every time one minute’s worth of RTC seeds are checked.

8. When a target is found, enter the date/time specified on Dolphin's custom RTC settings.

9. Double-check the result by entering the seed you get from Dolphin at the given date/time on RNG Reporter. From there, RNG your target as usual.

## Nanosecond Issue Explanation </br>
Gamecube and Wii games that use date/time for seeding will do so at a nanosecond level. For example, Gale of Darkness increments the initial seed at a constant 40.5 million added to it for every additional second on the RTC. This value will not go over 32 bits. If a game has such a constant, then one may predict what the next seed will be. <br/> I have left comments on the code about what parts to change, if one wishes to adapt the code for another game. This is useful for TAS, speedrunning, debugging, and other activities that require RNG manipulation. <br/> Expanding the scope of this program is my way of saying thanks to the Dolphin devs and the TAS community, for their help on making this possible. <br/>

Depending on how 3DS, Wii U, and Switch emulation turn out in the future, it may be possible to use this program to manipulate initial seeds there. I assume the constant will have to be changed, among other things. I plan to revisit this as applicable. <br/>

While you are able to replicate the same result over and over, it is highly unlikely that two computers will obtain the same result. The following is an incomplete list of what may affect your seeding. If you know something else that may affect it, please let me know by submitting an issue or just emailing me. <br/>
1. Incorrect custom RTC value entered (or custom RTC being disabled).

2. Using the GC BIOS.

3. Different computers (due to CPU).

4. Any setting on your computer itself that affects clock timing, such as overclocking.

5. CPU emulation engine setting.

6. Audio emulation setting (anything in the Audio section of the config, except volume level).

7. CPU clock override in Dolphin.

8. SRAM.raw file.

9. Different versions of Dolphin.
