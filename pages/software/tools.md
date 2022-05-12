---
title: "Software Development Tools"
meta_content: "Tools Nate Eagleson uses to write software."
template: "essay.html.tmpl"
# TODO Merge my useful-programs repository into this page.
# I don't believe I use it for anything other than dev software at present...
# TODO Break this page into multiple sub-pages.
# It would be nice to have a breakdown of tools I use for specific tasks and
# environments.
---

I use [Emacs](https://www.gnu.org/software/emacs/), [heavily
customized](https://github.com/NateEag/.emacs.d), as my text editor.

When I'm not in Emacs, I'm usually in a
[bash](https://www.gnu.org/software/bash/) prompt. I have flirted with using
Emacs' built-in terminal emulators, and was on the verge of making the jump to
using libvterm when
[cool-retro-term](https://github.com/Swordfish90/cool-retro-term) seduced me
with its wonderful aesthetics. I use [tmux](https://github.com/tmux/tmux) as a
mechanism to have something like overpowered scriptable tabbed terminal
sessions with the same configuration and shortcuts no matter what platform or
terminal emulator I'm using.

My preferred desktop is Mac OS X, with
[HammerSpoon](http://www.hammerspoon.org/) for keyboard-driven window
management and
[Karabiner-Elements](https://github.com/tekezo/Karabiner-Elements) to remap a
handful of keys on MacBooks. In an ideal world I might prefer to run a Linux
desktop, but since Macs can run Windows and Linux, and no other hardware
reliably runs MacOS or simulates iOS, OS X it is. I don't want to ever have to
tell a client "I can't update your app because an OS update broke my
Hackintosh," so even if it were legal to build one, I still wouldn't.

I use [Nix](https://nixos.org/) to manage my collection of day-to-day
development tools, though, and am very tempted to try NixOS for my desktop, the
above pragmatism notwithstanding.

Version control is a fundamental part of my programming workflow, whether solo
or on a team. I think about it a lot, and while I believe [a better VCS is
possible](https://github.com/NateEag/next-vcs), my default choice at present is
[Git](https://git-scm.com/). I almost went with
[Mercurial](https://www.mercurial-scm.org/) when I first made the jump to DVCS,
but decided that Git's popularity was more valuable than Mercurial's simpler
interface.

I have learned enough programming languages to know that [all languages are
equal](https://stackoverflow.com/questions/7284/what-is-turing-complete), but
some are [more equal than others](http://www.paulgraham.com/avg.html). In
descending order of preference (not necessarily experience or expertise), I
have spent quality time with:

* JavaScript
* Emacs Lisp
* Python
* bash
* Scheme
* C
* PHP
* Java
* Pascal
* Objective-C
* C++

When it makes sense (which it often does), I use relational databases for data
modeling. I've used a few different SQL DBs. Again, in descending order of
preference:

* PostGreSQL
* SQLServer
* SQLite
* MySQL

They all have different strengths and weaknesses, but on the whole I prefer
PostGres. MySQL gets a special shout-out for [causing much
suffering](http://grimoire.ca/mysql/choose-something-else), and I recommend
avoiding it where reasonable.

[Chrome](https://www.google.com/chrome/browser/desktop/) is my preferred
browser, both for regular use and development. It's primarily open-source,
includes an excellent suite of development tools, and is easy to extend.
