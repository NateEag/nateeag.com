Notes on various pieces of physical equipment I own or wish to own.


## How To Not Buy Smart TVs

I recently saw someone suggest that buying commercial displays is a viable
strategy for avoiding 'smart' TVs. Huge monitors fill a similar role. They're
more expensive, but that might be worth avoiding the insanity of having
computers in my displays (and the attendant spying).

I have investigated this option, but discussion with my wife leaves me
concerned that she might not be able to tolerate the brighter screens on
commercial displays.

As a result, we've gone the less-ideal route of buying a smart TV and
resolutely treating it as a dumb TV, giving no quarter when it begs for the
ability to send its spy reports back to Amazon.


## Hot Water Heater

Ours is failing. We need to replace it promptly.

Options (no natural gas in our neighborhood, just external propane tanks):

- electric tank

- electric tankless

- geothermal (ground water heat pump, do both hot water and house temperature
  with one [expensive] install)

Geothermal is probably worth considering. Takes a lot of capital, but I do have
some stock I should be able to sell off for a decent amount of exactly that.

My wife's been told by plumbers that tankless would use way too much
electricity.

I'm skeptical, because they gave no clear breakdown of why - just asserted it
would use tons. That I don't doubt, but I do doubt the constant energy
consumption of a tank model would be better.

So how do I figure out which one would be more cost-effective?

Do the (basic) thermo.

Cold water is coming in ~61 degrees Fahrenheit.

Hot water comes out ~117 degrees Fahrenheit.

The Eemax HA036240 (36 kW) is officially rated for 8 gallons/minute. [According
to the
manual](https://files.myrheem.com/webpartners/ProductDocuments/CF96AE9D-9A44-4F7D-A134-74CB0455B50A.pdf),
it can produce 5.5 gallons/minute of 105-degree water when inbound water is 60
degrees. From the temperature -> GPM table, I speculate that we could count on
~4.5 GPM at 115 degrees.

That's not _quite_ enough for two showers simultaneously. Each one would get
warm water, but not hot water.

What would it cost to operate monthly?

Let's SWAG that we use ~75 gallons daily at present, since we regularly empty
the tank by showering back-to-back.

That will likely increase to >100 gallons daily once all the kids are showering
every day.

Our shower does 3 GPM (I just measured it). No wonder we burn through water
fast. I think the kids' shower is the same.

That means our max usage, assuming ten-minute showers, would be 3 * 10 * 5 =
150 gallons. Realistically, we're probably doing fifteen-minute showers, so 3 *
15 * 5 = 225 gallons. Oof.

If we downgraded to the efficient 1.5 GPM showerheads, that becomes 112.5
gallons.

At 4.5 GPM, heating 300 gallons means running for 66 minutes daily.

36 kW * (66 minutes / 60 minutes) hours = 13.2 kWh daily. We pay $0.11 / kWh,
so ~$1.45 / day.

But that's not enough to meet our needs, as noted previously.

The Rheems RTEX-18 (18 kWh) can achieve a 25-degree temperature rise at 5 GPM,
with a max. throughput of 7 GPM.



Now, what's heating similar usage with a tank gonna take?

Worst case, everyone showers in the morning before some event.

For that, I think we'd need a first-hour delivery rating of ~100 gallons. Such
tanks seem to be rare.

Rheems does have a 105-gallon Marathon heater that does 104 gallons first-hour
(which I guess tells me how many kWh it takes / gallon, implicitly).

So what kind of electricity usage are we looking at for those?

Finding actual numbers on these heaters' usage (or raw stats to compute numbers
for it) is kinda hard. According to [this
post](https://community.sense.com/t/rheem-marathon-100-gallon-water-heater-usage/9766/15),
the EnergyGuide label thinks it'd be 4825 kWh / year, or 13.2 kWh / day. That'd
be about $1.45 / day. Obviously that's a very rough estimate.

Any day we all shower (which will be most of them in five years), with our 3
GPM

...it's also $5000 to purchase.


## Computer Keyboard

I have had wrist problems throughout my career as a programmer.

As a result I've used many different keyboards:

2005 - 2006: Microsoft Erogonomic 4000
2006 - 2012: Happy Hacker Lite 2
2011: brief flirtation with Kinesis Advantage
2012 - 2015: Truly Ergonomic Computer Keyboard
2015 - 2024: ErgoDox EZ

My ErgoDox EZ is still much-beloved and my daily driver, but I have kept my
eyes on evolution in the space, and there are some interesting boards out
there:

- MoErgo Glove80: https://www.moergo.com/
- ReDox Wireless: https://falbatech.click/products/ReDOX_FT-Wireless-Fully-Assembled-Custom-Mechanical-Keyboard-p648828330
- Ergodox Wireless Pro: https://www.slicemk.com/products/ergodox-wireless-pro

Wireless vs. wired is a difficult tradeoff. Wireless consumes batteries, but
over a long-enough timespan, wired devices break due to unplugging and
replugging. Which is more sustainable?


## Laptop

In fall 2022 I acquired a Framework 13" laptop, with the 12th gen Intel CPU.
I'm currently using NixOS as my daily driver. I have a long way to go before
I'm genuinely happy with the OS (my macOS setup has been carefully tweaked over
a decade), but the hardware's serving pretty well, and I have been enjoying the
upgrade-safety the OS promises and seems to deliver on so far.

I've been surprised to discover that thanks to Steam, a whole lot of Windows
games can actually work on this thing. In case I ever start playing something
that requires a real graphics card, here's a forum discussion of how to get an
eGPU working with Linux on the 13" Framework:
https://community.frame.work/t/guide-egpu-performance-tests-using-amd-rx-580-on-linux/26384

The Framework laptop is genuinely modular hardware, with an eye to letting you
upgrade and expand your laptop and swap out the hardware you need for a given
job. It's anyone's guess if the company will survive, but if it does it would
almost certainly be the most sustainable laptop I've seen.
https://frame.work/blog/category/hardware

I'm inordinately intrigued by the MNT Reform laptop, which is fully open
hardware, built with a blazing focus on repairability. You can pull out
individual battery cells. ARM chips, only 4 GB of RAM - it's definitely an
idealist's toy. That said, I think it might be an excellent first laptop for an
inquisitive, electronics-minded kid. https://mntre.com/ Paired with a
Lightphone, an older kid or younger teenager might have an effective set of
tools that aren't optimized for sacrificing them to The Algorithms.


## Family Media Machine

Currently a cheap desktop with an HDMI out. I just bought one, installed
Chrome, and paired it with a Logitech K600 TV keyboard, which has been working
just fine.

At first I tried a much cheaper Macally Bluetooth keyboard and it worked pretty
poorly - insufficient range and flaky reliability.

Windows 10 was getting slow and flaky, so I installed NixOS.

That hasn't been much faster, and I'm suspicious the issues are actually due to
our internet connection (which is most of what we use it for).


## Router

Shiva (coworker at $DAYJOB) says the AmpliFi Alien is a home router built by an
enterprise-grade router company. He uses it and has found it to be extremely
reliable.

I'm currently skating by on the router provided by my ISP, mainly because it
came with a preconfigured backhaul extender.


## Replacement Audio Processing Headphones

I used to do a lot of heavy sound design and musical work, especially audio
synthesis.

I still care about audio more than is reasonable.

My beloved Beyerdynamic DT 770 Pros have a flaky cable that gets worse with
each passing year.

Thus, I've replaced them with the [DT 770 Prox
X](https://north-america.beyerdynamic.com/p/dt-770-pro-x), which features a
detachable cable, with nearly-identical hardware to my beloved old headphones in
almost every other respect.


## Ploopy Thumb Trackball

I like open-source things, for repairability and sustainability.

I also like my thumb trackballs, as they distress my wrists far less than any
other pointing tool I have tried.

The Ploopy Thumb ticks both those boxes, so I'm inclined to get one next time I
need to replace a trackball: https://ploopy.co/shop/thumb-trackball-full-kit/


## PQ Y28 Earbuds

Wireless earbuds are a dreadful source of e-waste, because in most cases the
battery cannot be replaced, which means consigning perfectly functional
electronics to destruction.

However, the PQ Y28s are designed to avoid that problem, by making their
batteries easily replaced and recycled.

They don't seem to be considered all-around great - people have complaints.

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

I've been using the BC26R for several years now, and it's served me admirably
well.


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

To that end, I have recently purchased a [used SuperMicro
6028U-TR4T+](https://www.supermicro.com/en/products/system/2u/6028/sys-6028u-tr4t_.cfm).
Its twelve hot-swap drive bays should be more than I'll ever need for a home
NAS / media server.

I purchased mine [from
TheServerStore.com](https://www.theserverstore.com/supermicro-superserver-6028u-tr4t-2u-w-x10dru-i).

I manage the setup in [this project](https://gitlab.com/home-server).


## Sanni Cartridge Reader

This would let me rip my beloved old N64 cartridges, thus letting me legally
play the games in future. More to the point, we could share them with the kids
(without worrying about paying for Nintendo Switch Online in perpetuity).
They're old and low-res, but James is curious and I think might enjoy them.

https://github.com/sanni/cartreader

I've purchased one from [this Etsy
seller](https://www.etsy.com/listing/1313908826/open-source-cartridge-reader-oscr-hw5)
and have been quite happy with it.


## N64 (and others) Emulator

The Sanni cart reader enables legal emulation of N64 games.

Now then, how can I actually emulate these games in a satisfactory manner?

I tried Mario 64 on our Windows media PC, and it was kind of laggy.
Playable-ish, but not an ideal experience.

I've just learned that [Moonlight](https://moonlight-stream.org/) and
[Sunshine](https://github.com/LizardByte/Sunshine) exist.

Between the two of them, I should be able to run emulators on a beefier machine
(say, my laptop, Steph's gaming rig, or the hypothetical NAS device), along
with a Sunshine server, then run Moonlight on the media PC.


## Standing / Sitting Desk Setup

Thanks to Jared Worthen's recommendation when I started at ServiceTitan, I've
been using the wonderful [Husky 52"x24" adjustable height
workbench](https://www.homedepot.com/p/Husky-52-in-W-x-24-in-D-Steel-2-Drawer-Adjustable-Height-Solid-Wood-Top-Workbench-Table-in-White-HOLT5202BJ2/311742117)
as a sit/stand desk. Paired with 27" external monitors and two of ErgoTron's
[tall pole monitor
arms](https://www.ergotron.com/en-us/products/product-details/45-295#?color=polished%20aluminum),
it's sit/stand desk bliss.

I _would_ like to get another inch or three of height out of them. Swapping out
the tall poles for [these 28"
poles](https://www.ergotron.com/en-us/products/product-details/20-137#?color=black)
would would more than do the job. Would need to verify they'll actually work
with the other parts I have, though.

I've bought a used [Humanscale
Freedom](https://www.humanscale.com/products/seating/freedom-headrest-executive-chair).
I accidentally got one that does not have the real headrest, which I'm
disappointed about (though return proved impractical), but it should work well
enough for now.

In case I do ever want to buy a full headrest and add it, here are the assembly
instructions and part list:
https://www.humanscale.com/userfiles/file/HeadrestSupportAssemblyInstructions.pdf

I need a keyboard tray that will attach usefully to my desk before I can use
the Humanscale as my chair.

A trackless keyboard tray is one option:

https://www.ergoexperts.com/products/vanish-trackless-keyboard-tray?variant=44594745278676

but another option would be to get some risers for a tracked tray.

## Physical Teletype Terminal Project

I'm using a TI Silent 703 to teach my kids basic computing like it's 1973.

Seeing [this glorious video](https://youtu.be/2XLZ4Z8LpEE) helped me understand
a whole lot of the ancient history of computing better than I had, and also to
understand intuitively how you could have ever used `ed` for programming. In
the context of an endless stream of physical paper, it's a really reasonable
design.

After I showed James a video of teletypes, he became slightly enamored of them,
too.

After some research, the elegant solution appeared: TI's Silent 700 line of
terminals.

They use thermal paper and a heating element, with acoustic couplers and serial
ports for communicating to computers.

The 703 is capable of case-sensitivity, making it suitable for use on a
traditional Unixy filesystem, and has a 25-pin female RS-232 serial port,
making it easy to connect physically to any computer with a serial port.

The design made them much more mechanically simple and robust than a standard
teletype (and also quieter), so it's not that hard to find working ones in
2026.

For a detailed overview of the setup, see [my home server
config](https://gitlab.com/NateEag/home-server/-/blob/main/readme.md)

## Build-Your-Own Teletype

As I've been teaching my children to compute using a teletype, I've been
realizing that there's a lot to recommend it as a learning environment.

So, I'm pondering how people could use the approach more widely.

The biggest issue is the low supply of actual teletypes.

It occurred to me that adapting electronic typewriters into teletypes might be
feasible.

Lo, an admirable gentleman has [done this with a Brother
SX-4000](https://github.com/numist/project-typewriter).

He hand-soldered some lines to the keyboard's scan circuitry, connected it to
an Arduino, then wrote the code to handle interfacing between the two.

Soldering is outside my wheelhouse, but that basic approach seems adaptable to
almost any daisywheel electronic typewriter - they probably all use
roughly-similar mechanisms.

It would be _really_ fun if there were an adaptable typewriter that supported
more than one color, so basic syntax coloration and the like would be possible.


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


## e-ink Monitor

I would really love to try an e-ink external monitor.

Behold:

https://www.indiegogo.com/projects/paperlike-color-world-first-color-e-ink-monitor#/

Also there's this impressive piece of engineering, though it's smaller and
black and white:

https://www.modos.tech/blog/modos-paper-monitor
