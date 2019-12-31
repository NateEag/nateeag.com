---
title: "Software Ideas"
meta_content: "Programs Nate Eagleson wishes existed."
template: "essay.html.tmpl"
---

When I find myself wishing for a program and unable to find it, I put it in
this list.

When I discover one of these already exists, I move it to my [list of useful
programs](https://github.com/NateEag/useful-programs).

When I (help) get one to a usable point, I move it to my [list of
projects](/software/projects.html).


## The Audio Engine

I would love to have an open-source, real-time, auto-scaling audio DSP engine
for general-purpose hardware - something like an open-source
[Kyma](http://kyma.symbolicsound.com/) for arbitrary hardware. Discovering this
already exists would be spectacular, but since I have not yet found it, I [work
towards building it](https://github.com/NateEag/audio-engine).


## A Better (D)VCS

Git is a powerful piece of software with a poor user interface and a few
shortcomings.

I chip away at [designing a better VCS](https://github.com/NateEag/next-vcs).

Note that before I started thinking about designing a new DVCS, I planned an
[improved hook manager](https://github.com/NateEag/githooks.d) and a
[distributed code review system](https://github.com/NateEag/git-revue) for Git.


## track-time

I occasionally use [Watson](https://github.com/TailorDev/Watson) to keep track
of how I spend my time, but I think a significantly better command-line
interface for the job [is possible](https://github.com/NateEag/track-time).


## media-list

I care a lot about art in various media, and have in spare moments here and
there mapped out a data model for tracking works and makers I'm interested in,
and the times I've experienced those works.

Think of it as an [unfinished, over-engineered todo list for experiencing
artwork](https://github.com/NateEag/media-list).

It's more a playground for practicing data modeling and experimenting with
software design than it is a focused product.


## OSS Desktop / Mobile Calendar Client

I would like a clean, consistent, functional, hackable interface to calendar
data that works on multiple platforms (at minimum, Android and OS X, as they're
what I currently use).

Perhaps what I want is already out there. I haven't really looked much.

I basically want my calendar to look, feel, and behave analogously between
desktop and mobile devices.

I would also like a few features I haven't bumped into, such as the ability to
set reminders after events (for when you want to timebox things).


## OSS Calendar Data Manager

I want my computers to share calendar data with each other, regardless of form
factor. If two of my devices are on the Internet, or on the same local network
without a net connection, they should come to agreement quickly about my
current schedule (or force me to resolve conflicts if some exist).

I tend to assume this requires a central server running somewhere, but perhaps
that's not the case. Though I would want a good backup system if the system was
genuinely decentralized so I'd have low risk of losing things.


## Distributed Scheduling Assistant

Scheduling an event with more than about two people is a pain. It means a lot
of back and forth proposing dates then finding out that they don't work for
someone in the group.

Computers could just do this for us, if everyone in the group uses an
digital calendar.

Feed it a list of CalDAV (or similar) URLs and an event length (allow support
for an optional target datetime range, e.g. "next month") and it finds you a
list of slots of that length that are currently open for everyone. Then press
"invite" to send invites to all the URLs.

That outline may be ill-formed in its current incarnation (not sure caldav
supports invites), but the core idea is reasonable. I don't know the
calendaring protocols well enough to know if it fits with them or not.

Note this proposal involves some security concerns. You could abuse naive
designs to mine people's unavailable/available times, which is more than you
likely meant to give someone when you said "sure, a jam session could be fun -
here's my schedule QR code."

Using nonced URLs for accepting invites should prevent that from being feasible
(the nonce loses access rights once the engine has found a solution [though the
engine can re-grant it rights if the initiating user chooses to reschedule]).

CalDAV itself probably doesn't have all the features this would need in order
to work, so you'd have to stand up an API that acts as the intermediary between
the scheduling logic and actual calendar URLs. Each user would have to opt into
that API

Once it's arrived at an acceptable date, it could show a review UI (making note
of the most-crowded schedules), and on confirmation it can send invites to
everyone who got a QR code scanned.

Note that such an API doesn't have to be on a server - a single person's phone
could do the job by scanning QR codes from other devices to get the nonced
URLs, as long as the other phones are on the same WiFi network.

That said, you'd probably want the API available on a server, so that you can
plan events without everyone being in the same physical space (which is what
the distributed QR scanning logic assumes).


## Open Source Calorie/Nutrient Tracker

The FDA has a branded food products database that would be a decent baseline for "scan a UPC and add calories to the day".

Pair that with their regular nutrient database and a source of meal
ingredients and amounts (like an OSS recipe database, perhaps?), and I think
most meals could be pretty quick to enter.

Obviously you'd still want support for adding random calorie entries, as well
as UPCs that aren't yet in the branded food products DB.

Aforementioned DB gets updated every now and again, so you'd want to design
this to be capable of taking advantage of these updates, rather than using a
one-time snapshot.


## Open Source Fitness Tracker

I am a firm believer in the value of data, and I'm intrigued by the idea of
keeping a record of things like my heart rate and physical movement for
analysis and better understanding of my health.

I am not at all interested in generating that data and handing it over to a
company specializing in health analytics, as the day will come when that data
is either sold to a health insurance company to help them determine my rates,
or just be part of a massive data breach (and who knows how it will be abused
then).

To that end, I would like an open-source phone app that can save the constant
stream of data generated by a fitness tracker and sync it to a larger storage
mechanism.

In practice, that likely means buying a fitness tracker that speaks the [ANT+
protocol](https://www.thisisant.com) and finding or building an Android app
that can record the streams of sensor data to my phone. In practice, the two
device profiles that would actually be useful for physical fitness are probably
heart rate and step count, since for focused walking / running / cycling, you
can use GPX tracks to generate speed and distance.

[RunnerUp](https://github.com/jonasoreland/runnerup) is not what I'm looking
for, but should serve as an example of an app that uses ANT+ data. [This blog
post](https://johannesbader.ch/2014/06/track-your-heartrate-on-raspberry-pi-with-ant/)
on using a Raspberry Pi to track your heart rate shows that you can do it
without an Android device (using this [Python implementation of
ANT](https://github.com/mvillalba/python-ant))

It would be nice to be able to get raw accelerometer data, which I believe is
what's usually used for sleep tracking, but I don't see a mechanism that would
make it possible at present.

In tandem with this, I would like some tools that can analyze the data locally
on my system to show me the big-picture trends.


## Open Source GPS Track Analyzer

Runners and walkers often use proprietary programs to record their ambulation
and analyze it for data points like average speed, distance covered, estimated
calories burned, and the like.

Those programs usually store user data on remote servers. That means the users
have little control over the data, which could easily be stolen by or sold to
third parties (like health insurance companies) against the users' will.

I would like to have a program that analyzes GPS track files for similar
purposes. I would like it to work locally on the computer where the data are
stored, so that the user can maintain control of their personal data while
still gaining insight into the details of their walking and running routines.


## Real-Life Marauder's Map

[The Marauder's
Map](https://www.pottermore.com/writing-by-jk-rowling/the-marauders-map) was
one of J. K. Rowling's cleverer ideas.

It should be possible to build something surprisingly close to the original
using GPS, [OpenStreetMap data](https://planet.openstreetmap.org/), a color
e-ink display, and an internet connection.

The most crucial functionality of the map, the ability to see the name and
location of everyone in a defined area, you could not reproduce. People who
carry an internet-equipped GPS device (like a smartwatch or smartphone) and who
will let it report location to the map software could be displayed, however.

Using the stream of location data, the map could display an area of the earth
that displays the locations of all linked devices framing and size, dynamically
resizing it as necessary so that all participants are visible at all times.

With OpenStreetMap's raw data, it should be possible to render the map in a
visual style similar to the one from the film adaptations.

The color e-ink display is not necessary, strictly speaking. It would certainly
enhance the effect, though, if mounted on the wall in a plausible frame. The
lower framerate e-ink displays suffer from might make it less convincing, but
the texture and coloration of paper would make it look much more like the
genuine item.

I doubt I will ever write this program - it would be highly entertaining, but it
seems to have little practical value, and I care about my other ideas more.
