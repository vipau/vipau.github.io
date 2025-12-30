+++
authors = ["Vi Pau"]
title = "veeship - custom starship theme"
date = "2025-10-22"
description = "Fast shell prompt based on Starship with advanced features"
tags = ["linux", "shell"]
+++

**Download this config file: [starship.toml](https://raw.githubusercontent.com/vipau/zsimple/refs/heads/main/starship.toml)**  

**Try it in Docker (with [zsimple](https://github.com/vipau/zsimple).):** `docker run --rm -it ghcr.io/vipau/zsimple:latest`

Here is my custom shell prompt, designed over the course of a weekend.  
It uses [Starship](https://starship.rs/) which is very fast as well as cross-shell, allowing me to have the same prompt in bash, zsh, nushell and others. I explicitly disable most of the Starship plugins in my config to make it even faster and cleaner.

My config file is designed around the Solarized Dark colorscheme, using the colors from the official website from Ethan Schoonover. This can be changed very easily and Starship even lets you define multiple palettes in the same config.
**NOTE: This prompt won't change the background color, that depends on the settings of your terminal emulator.**

It uses Powerline font symbols, but it won't look too broken if you use it on a system without Powerline fonts. I tried to limit the use of them in the shell, and might consider removing the need entirely in the future.

---

![](/images/prompt-1.png)

Right away, you can notice:
* indicators for the shell and OS in use. This is very useful when you have the same looking prompt everywhere.  
* The home directory is conveniently shortened to `~`   
* We can see how long the last command took, if execution lasted for more than 1 second (configurable)  
* `[0]` is the exit code of the last command.

---

The directory indicator detects how much space it has to show the current working dir, but it will always truncate at 3 levels maximum to not clutter the screen. I use `pwd` if needed. This is what works best for me, but everything is easily configurable to the user's liking.  

![](/images/prompt-2.png)

---

The hostname is hidden when on a local machine, but it will be visible when connected via SSH, along with a red SSH warning. 

![](/images/prompt-3.png)

---

When logged in as root, the username will be red on black, and flashing if your terminal supports it.

![](/images/prompt-7.png)

---

When a process exits with a non-0 code, the status indicator will be red and show the common meaning of the exit code, and if not found, the actual code. The config includes a comment on how to change it to show the integer code only. I wanted to show both but limitations of Starship make it hard to make it pretty (I plan on submitting a PR)

![](/images/prompt-4.png)

---

It will also show if the last process was killed by a signal, and the common meaning of the signal if found.

![](/images/prompt-5.png)

---

If the last command was a pipe, the exit status for the processes in the pipe will be shown.

![](/images/prompt-6.png)

---

Finally, on the bottom line (where the actual command is typed) a blue indicator will appear if there are jobs running in the background, and a battery indicator of varying colors will appear if the battery is below 30%. I cannot provide a screenshot of the battery widget at this time.

There is also a configuration option that allows you to get a desktop notification when a command finishes and it took more than a configurable amount of time.
