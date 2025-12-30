+++
authors = ["Vi Pau"]
title = "Proper 1chip SNES PAL to NTSC permament conversion"
date = "2025-12-30"
description = "How to convert a PAL SNES to NTSC"
tags = ["snes", "mod"]
series = ["snes", "mod"]
+++

# How to convert a PAL 1CHIP SNES to NTSC properly (semi-permanent mod)

## Why this page?
When doing this mod myself, I realized that the complete information needed
was scattered throughout the internet, and required me a lot of digging and testing to implement.
I want to save others work by documenting exactly what I did.
Also, most people I found doing this mod left their SNES only capable of using RGB but not RCA video while mine keeps both.

## Why this mod?
The SNES suffers from a similar issue as the NES which is that lots of game studios did not port their games to PAL properly
and as such they don't run as designed (for US/JP hardware) on original (European) hardware.  
There are few reasons to leave a SNES as PAL, or do a switchboard mod, such as the game Terranigma.
I just chose to convert my SNES entirely, but converting it back is very easy and detailed below.

## The schematics
Schematics for the 1CHIP SNES are available [here](https://drive.google.com/file/d/1xUtRI2XKwDy3kQ9ffdalpFNliafL9Pgy/view)  
I took a lot of pictures during the work I was doing, but I still have to sort them and upload them to this page.
For now, I'll limit it to the guide.

## Hardware needed
1. A 21.47727 MHz (NTSC) crystal oscillator, possibly more than one (see later)
2. Soldering iron, solder, wire, willpower
3. A JP/EU SNES flashcart to play NTSC ROMs on PAL consoles. (the shape of the cartridge is different between USA and EU/JP)
4. (optional) 17.734475 Mhz crystal, if you want to go back to PAL and something happened to the old one

## The procedure
The procedure is actually quite easy, and the mod only consists of 3 steps:
1. Connect pin 111 of the CPU (S-CPUN) to ground (GND). This is what tells the SNES to run in NTSC mode at 60Hz. In the 1chip revision, this pin controls both CPU and PPU.
2. Connect pin 9 of S-RGB to +5V. This tells S-RGB to create a NTSC signal instead of a PAL signal.
3. Replace the X1 crystal oscillator with a 21.47727 MHz one. I had to try different crystals to find one that works, but the one I found was from AliExpress. One from a major electronics supplier did not work for the purpose and I am not entirely sure why (load capacitance?).

If you did everything correctly, both RGB and RCA output should still work, of course you need to use a flashcart with NTSC ROMs. PAL games will now run slow.

## The troubleshooting
If you get no video at all, make sure the solder points are correct as described above. Remember, 111->GND and 9->+5V. Also try different X1 oscillators.
If you get poor or no color over RCA, try another crystal oscillator, or fiddle around with the TC1 trimmer capacitor until you get color, or replace TC1 entirely although this should not be needed in most cases.

There's a very good troubleshooting guide [on Console5](https://wiki.console5.com/wiki/SNES) with hints on what to check in case of issues, or you can shoot me an email.

## The reverse (NTSC->PAL)
1. Connect pin 111 of the S-CPUN to +5V
2. Connect pin 9 of the S-RGB to GND
3. Replace the X1 crystal oscillator with a 17.734475 Mhz (PAL) one.
