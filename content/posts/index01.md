+++
authors = ["Vi Pau"]
title = "Pebble Index 01 is not open source"
date = "2026-08-31"
description = "A product advertised and sold as fully open is breaking its promises."
tags = []
+++

I am a big fan of the rePebble/Pebble Index 01, a wearable ring with a microphone and a button that sends recordings to your phone.
I believe the idea is quite genius, but unfortunately, the device is being sold on a false promise right now: open source.

## The promise

On the Index 01 official website, we can see multiple claims of the software being open:


![](/images/index-0.png)  
![](/images/index-1.png)  
![](/images/index-2.png)

While this doesn't claim that the firmware is open source, although a customer would gladly expect that given the promises, it does claim that the Pebble app for smartphones is open source.

## The lie

If the app was truly, fully open source, anyone could build their own app that interacts with the Index 01. That is not the case.
A developer trying to build a MacOS app that could interact with the ring got the creator of the ring, Eric Migicovsky, to admit that the app is not actually open source, and both the client-side code needed to interact with the ring as well as the firmware are "provided by a friend" and not open.

[GitHub issue](https://github.com/coredevices/mobileapp/issues/333)

![](/images/index-3.png)

This limitation makes it impossible to make an app that communicates with the ring, forcing users to use the official Pebble app. This is the opposite of open source, it's vendor lock-in at its finest.
