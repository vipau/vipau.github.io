+++
authors = ["Vi Pau"]
title = "zsimple - minimal modern zsh environment"
date = "2025-11-07"
description = "Portable zsh configuration that provides a modern and comfy feel while remaining blazing fast"
tags = ["linux", "shell"]
+++
# [View on GitHub](https://github.com/vipau/zsimple) <font size=2>(for install instructions)</font>

**Try it in Docker (with [veeship](https://vipau.dev/posts/veeship) included):** `docker run --rm -it ghcr.io/vipau/zsimple:latest`  
Or with a minimal configuration: `docker run --rm -it ghcr.io/vipau/zsimple:void-latest`
## Why zsimple
If you are looking for a .zshrc that has no plugin manager, only 3 highly trusted plugins, and extremely minimal but modern config and that works well on Linux and MacOS, you... I hope you found it here, and if something doesn't work on your setup, shoot me an email or [open an issue on GitHub](https://github.com/vipau/zsimple/issues) :)
## Showcase
Full case-insensitive match with tab, including backwards in word + good tab menu with shift-tab to go backwards
<script src="https://asciinema.org/a/yGPPnSoexqoLcsovDHvpoF72K.js" id="asciicast-yGPPnSoexqoLcsovDHvpoF72K" async="true" data-autoplay="1" data-loop="1"></script>

Embedded man pages
<script src="https://asciinema.org/a/iwZLxWe9mxadlniMXbmYB4QKS.js" id="asciicast-iwZLxWe9mxadlniMXbmYB4QKS" async="true" data-autoplay="1" data-loop="1"></script>

`Autocompletions and autosuggestions`
<script src="https://asciinema.org/a/amMp6ufGgiKWSi7XAHUNeum5Y.js" id="asciicast-amMp6ufGgiKWSi7XAHUNeum5Y" async="true" data-autoplay="1" data-loop="1"></script>
## The plugins
These are the only plugins that this zshrc uses, all from the zsh-users GitHub account:
* https://github.com/zsh-users/zsh-syntax-highlightingw
* https://github.com/zsh-users/zsh-autosuggestions
* https://github.com/zsh-users/zsh-completions

These are also packaged in most distributions and homebrew, and installing them that way will make automated upgrades easier to handle.
## How it works
My dotfiles now live in these places:
* `~/.zshrc` - Main config. This is zsimple. Possibly with your tweaks.
* `~/.aliases` - Aliases that work with any shell
* `~/.exports` - Exported variables
* `~/.zsh/plugins` - Plugins (if installed from zsimple)

The .zshrc does the following:
1. Set modern built-in shell options that make zsh much more enjoyable.
2. Load ~/.exports
3. Try to load plugins from your system path (check it if you installed the plugins from packages), homebrew path, or our plugin dir
4. If all fail, git clones the plugins to the plugin dir and loads them
5. Set a lot more built-in options to make zsh comfy.
6. Load ~/.aliases
7. Only if [starship](https://starship.rs/) is installed, launch it (see [veeship](https://vipau.dev/posts/veeship/))
## How to update plugins 
If your plugins were downloaded from your system's package manager or homebrew, update them from there. If they were git cloned by our script, and you find them in `~/.zsh/plugins` and I left a small function in my ~/.aliases to update them.  
If you included my aliases file, you can just run `zsimple-upgrade-plugins`

```bash
alias zsimple-upgrade-plugins='for d in ~/.zsh/plugins/*; do echo "Updating ${d%/.git}" ; git -C "${d%/.git}" pull ; done'
```
## How to install
Read the [GitHub Readme](https://github.com/vipau/zsimple)