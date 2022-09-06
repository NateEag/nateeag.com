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

The cheap Android tablet with a Mini HDMI port that my wife impulse-bought out
of frustration with my lack of progress broke.

So, we should probably do this.


## Replacement Audio Processing Headphones

I used to do a lot of heavy sound design and musical work, especially audio
synthesis.

My beloved Beyerdynamic DT 770 Pros have a flaky cable that gets worse with
each passing year.

I'd therefore like to replace them with either the DT 1770 Pro or the DT 177x
Go. Both have a detachable cable and therefore are at less risk for the kind of
damage my 770s have experienced.

It's hard to pick between them, as the 1770s are built for engineering (more
even frequency response) but have 250 ohms resistance and therefore require a
headphone amp, while the 177xs are tweaked for pleasant listening but have only
32 ohms resistance, making them workable directly with devices like cell
phones. Also the 177x is about $150 cheaper.

I'd probably lean towards the 177x, as it's more all-around usable, and if I
were ever taking audio engineering so seriously that I needed really precise
results for, I could probably buy a second set (and maybe do more exhaustive
research first).


## Ploopy Thumb Trackball

I like open-source things, for repairability and sustainability.

I also like my thumb trackballs, as they distress my wrists far less than any
other pointing tool I have tried.

The Ploopy Thumb ticks both those boxes, so I'm inclined to get one next time I
need to replace a trackball.


## PQ Y28 Earbuds

Wireless earbuds are a dreadful source of e-waste, because in most cases the
battery cannot be replaced, which means consigning perfectly functional
electronics to destruction.

However, the PQ Y28s are designed to avoid that problem, by making their
batteries easily replaced and recycled.

They don't seem to be considered all-around amazing - people have complaints.

Nonetheless, sustainability matters to me, and these are closer to that than
most earbuds I'm aware of.

https://pqearbuds.com/products/longest-lasting-interchangeable-magnetic-attach-battery-wireless-earbuds


## Fenix BC26R Bike Light

Many modern bike lights have a built-in, non-user-replaceable battery pack,
turning the light into electronic waste after a thousand or so charging cycles.

Fenix's bike lights use a standardized replaceable 18650 battery, so that's not
such an issue.

The LED supposedly has a 50,000 hours runtime, which if you bicycle 2 hours /
day would last you ~70 years.

I'd rather have one with a user-replaceable bulb, too, but still - seems like a
good candidate for now.


## PedalCell

I took up bicycling as a form of exercise and potential transit in summer 2022.

I was inordinately intrigued by the idea of generating electricity via
bicycling, and thus did some research that led me to [the PedalCell USB
charger](https://pedalcell.com/).

It moves fairly easily between bikes, is cheaper than a dyno hub, and is more
efficient.

I'd never reach financial breakeven on charging batteries with it, so to justify
the cost of owning one I'd need to go another route, such as deciding I think
it's worth spending on for the coolness factor, or for having the ability to
charge electronics while on a long ride of the sort I don't currently do
(touring, bikepacking, etc).


## Family NAS Device

I would really like a NAS that can hold a large volume of data to serve as the
centralized, online backup for our various hunks of information (could start
storing optical disks in a different physical location to be fireproof).

https://dataswamp.org/~solene/2020-10-18-nixos-nas.html is a recipe for running
a NAS on NixOS. If I could get a chassis that hosts a good number of drive
bays, I might be somewhere interesting.

I recently discovered that you can find old rackmount servers for _dirt_ cheap
(I found one decent one for ~100 USD). One with four drive bays would make it
quite feasible to have a pretty large volume of storage space.


## Sanni Cartridge Reader

This would let me rip my beloved old N64 cartridges, thus letting me legally
play the games in future. More to the point, we could share them with the kids
(without worrying about paying for Nintendo Switch Online in perpetuity).
They're old and low-res, but James is curious and I think might enjoy them.

https://github.com/sanni/cartreader


## Standing / Sitting Desk Setup

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

After I showed James a video of teletypes, he became slightly enamored of them,
too.

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
Apparently https://mailman.qth.net/mailman/listinfo/greenkeys is the mailing
list to be on if you're hoping to pick up some connections for this kind of
thing.


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
terminals that ever supported color. Apparently the VT-525 had color support
but required a separate external monitor.
