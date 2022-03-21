I am thinking more about computer and display hardware lately.

Keeping some quick notes in here.


## How To Not Buy Smart TVs

I recently saw someone suggest that buying commercial displays is a viable
strategy for avoiding 'smart' TVs. Huge monitors fill a similar role. They're
more expensive, but that might be worth avoiding the insanity of having
computers in my displays (and the attendant spying).


## New Laptop

I'll need to replace my personal laptop soon - it's dying. Nine years is a
decent run.

I'm increasingly confident I don't want to use OS X long-term, not as a daily
driver. They're so developer-hostile, and I worry that one day they'll finish
closing the loopholes that let you run whatever code you want. :( ...those
Apple Silicon chips sure do perform, though. Maybe someday Linux will be stable
and usable on them.

The Librem 15 from Purism has good Linux support, hardware killswitches for
wireless connections and cameras, has been used for NixOS, and has an aluminum
body: https://puri.sm/products/librem-15/

The hardware killswitches are appealing, as is supporting a company that's
trying to make freedom-supporting hardware.

It has a USB-C port and an HDMI port, but the USB-C port is data-only, so
getting two monitors to work can be pretty involved:
https://forums.puri.sm/t/please-recommend-a-port-replicator-docking-station/1115/16

Their 14-inch model, on the other hand, has a fully-functional USB-C port and
HDMI port, so it can just drive dual monitors without fussing. Maybe they'll
update the 15 to work similarly next.

Apparently you can get Windows 10 working on it without too much headache, too,
so I have a fallback option if I try Linux for a year or so and wind up wanting
to bail out.

The Penguin M3 might be another decent option. Appears to support Windows,
looks roughly like a MacBook (though I'll never have a use for that freaking
numeric keypad they all waste space on).
https://www.thinkpenguin.com/gnu-linux/penguin-m3-gnulinux-laptop

The Framework laptop is genuinely modular hardware, with an eye to letting you
upgrade and expand your laptop and swap out the hardware you need for a given
job. It's anyone's guess if the company will survive, but if it does it would
almost certainly be the most sustainable laptop I've seen.
https://frame.work/blog/category/hardware

Over in hardcore OSS land is the MNT Reform, which is fully open hardware,
built with a blazing focus on repairability. You can pull out individual
battery cells. ARM chips, only 4 GB of RAM - it's definitely an idealist's toy.
That said, I think it might be an excellent first laptop for an inquisitive,
electronics-minded kid. https://mntre.com/ Paired with a Lightphone, an older
kid or younger teenager might have an effective set of tools that aren't
optimized for sacrificing them to The Algorithms.


## Family Media Machine

Our old phones are not really a viable answer for streaming media.

We mostly stream Netflix and Amazon Video - I have not found an off-the-shelf
device that manages to do both.

I'm therefore considering an IntelNUC machine with NixOS.

Bonus - could put emulators on it for our old consoles, like the N64, GameCube,
and even the Wii (Dolphin). Obviously a media library with rips of our DVDs
would be feasible too, as would some sort of photo browsing UI (Plex or similar
could cover both of those). Could use it for playing stuff from the music
library, too, maybe even dig up a mobile app for controlling that so we don't
have to have the TV on (use Bluetooth to broadcast to wireless speakers).

First step here would be to hack up a NixOS VM on which I can stream Netflix,
Amazon Prime, and Disney Plus. If I can get that working, I'd say buying a
machine to host that setup is a no-brainer (though I'd need to also build out a
simple UI and get a remote control of some kind working for it).

...actually the first step would be to buy the hardware with Windows
preinstalled. I may hate it but it'll Just Work, as they say. Replacing it with
a Linux substrate may be possible but may not be a good use of time.

Next step would be to show some sane method for controlling the thing. Would
Steph be okay with a wireless keyboard / trackball combo?

...we wound up buying a cheap Android tablet with a Mini HDMI port. It
technically does the job, but is prone to stutter with all the streaming
services we use.

I have not given up on the idea of replacing it with something more general.


## Office Chair And Desk

This is kind of a chicken-and-egg problem.

I have a lovely pair of 27" monitors and high-end arms to put them on.

I need a desk that supports:

1) holding the monitor arms in place so that the monitors can be positioned at
eye level while both standing and sitting.

2) mounting my personal keyboard tray underneath it so that I use it both
sitting and standing

I'm not sure what will enable me to achieve that in practice, because I need a
chair and desk that work together well.

I could go with standard desk height while sitting and a normal chair, as long
as the keyboard tray and monitor arms give enough height for me to work
standing (which I haven't tried measuring).

The other strategy is to have a really tall desk and a tall chair to go with it
(plus a footrest of some kind).

Matt Guest tried this gaming chair and recommended it:
https://www.staples.com/staples-gaming-chair-black-and-white-55172/product_24381063


## Physical Teletype Terminal Project

I would really love for the boys' early years of computing to include some
hands-on time with a physical teletype-style terminal, if at all possible.

Seeing this glorious video (https://youtu.be/2XLZ4Z8LpEE) helped me understand
a whole lot of the ancient history of computing better than I had, and also to
understand intuitively how you could have ever used `ed` for programming. In
the context of an endless stream of physical paper, it's a really reasonable
design.

So, thinking about ways we could do this.

Apparently one is to buy an IBM Wheelwriter 1000 and build the board described
here https://github.com/IBM-1620/Cadetwriter to have your very own mechanical
typewriter terminal.

There is always, of course, the ridiculous option of just paying through the
nose for an ASR 33.

And there's Drew DeVault's line printer pseudo-terminal hack:
https://drewdevault.com/2019/10/30/Line-printer-shell-hack.html

There is also the social angle - maybe we can get in touch with someone who has
a restored teletype and arrange to try it out in person at some point.


## Physical Glass Terminal

I would sort of love to own a glass terminal and use it for hacking in Emacs
with all the horsepower of LSP and friends.

(https://github.com/Swordfish90/cool-retro-term is the closest you'll get in
any sane way, and I kind of love it far more than makes sense [especially since
it doesn't support using Option as the Meta key {though I got Meta-x to work by
tapping escape promptly followed by x}])

The VT100 is the classic, but I thought it was worth noting that there actually
were multicolor terminals, such as the Wyse WY350 and WY370 terminals. If I
could get one of those I really could code like it's 1985 with the best tech
2022 has to offer (Emacs, evil-mode, lsp-mode, etc). Note that the terminfo
database on most *nix systems should make it possible to find most hardware
terminals that ever supported color.
