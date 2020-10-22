"I have the most ill-regulated memory. It does those things which it ought not
to do and leaves undone the things it ought to have done." -- Lord Peter Wimsey


I am starting to use spaced repetition flashcards to help me store useful
information in my long-term memory.


## Topics

What things do I wish I remembered better?

- Unix command-line trickery (don't memorize too much, as automation >
  memorization, but some things I forget regularly are worth remembering)

- Programs I use or think may be useful in future (I already write these down
  but reviewing them as needed to keep them in my head would be helpful)

- Passwords (my personal password safe is on my laptop so when I don't have it
  I'm hamstrung; maybe some tool exists that can use arbitrary programs for
  spaced repetition tests?). Any approach I come up with here could apply to
  other secrets, too (family member SSNs, for instance, or credit card
  numbers).

- Useful formulas and data for Fermi approximations

- Mental math techniques (particularly for aphantasiacs, as I cannot do mental
  math nearly as effectively as people who can visualize)

- Standard mathematical techniques (algebra, linear algebra, calculus,
  statistics... all things I used to know but have forgotten)

- A mapping of algorithm names to their purposes and runtime properties (space
  / time complexity). Not going to worry about implementations, just enough so
  I can find them in the appropriate reference. Should be mildly helpful as a
  programmer day-to-day, but very useful in job interviews / programming
  tests - if you know which algorithm you need, you can just look it up and/or
  pull in an existing implementation. Reasonable people will accept "I've
  memorized which algorithms apply, but not the algorithms themselves because
  why memorize what you can easily look up?"

- A mapping of data structure names to their purposes and runtime properties
  (space complexity, perhaps algorithms that rely on them?). Again, the idea
  here is to memorize just enough to recognize when to apply them - you can
  look up the details, and usually find a library that already does the heavy
  lifting.

- People's names and basic info

- Family facts and anecdotes


## Tools

### Basic Flashcards From Reference Sheets

I would like to store my flashcards as plain text. That way I have reference
sheets of information I can hyperlink to and can refer to when I do forget
things.

Also reference sheets that aren't hugely important can just live as reference
sheets and not get imported into the spaced repetition deck.

Looks like Ankidown might be an option:

https://github.com/glfharris/ankidown

I'm slightly inclined to try Mnemosyne instead of Anki, just because it has a
mobile sync component that's totally open (Anki's mobile sync is not).

Ideally I'd like to keep the actual review data as plain text, too, or at least
be confident I can move it from one system to another.

A quick test of Ankidown shows that, yes, it should be usable for keeping basic
reference sheets in Markdown. See other changes in the commit that adds this
essay for the rough draft.

I'd have to ditch any prefatory matter before importing a deck, but as long as
that's documented, it shouldn't be hard to automate. Can just put that in a
standard header block and add a custom template for rendering these things.

Reminds me that I should really add TOCs and subsection anchors to this site. I
don't put a lot of long-form stuff on it because that's not my style, but these
reference documents that can be converted into Anki decks would really benefit
from that, I think.

Anyway, Ankidown does not seem to have great support for adding new cards by
re-importing existing note sets.

It highlights duplicates for you, but IMO it would be better to override the
existing cards when importing duplicates.

I imagine logic something like:

* Any note with contents or title exactly matching an existing note is treated
  as an override by default, but can be added as a new note

* Any note with contents or title close to an existing one suggests it could be
  a conflict and lets you either skip, add as new, or add as override.

* Any note that looks new is added as new by default

I should ask if a PR implementing something like this would be accepted.


### Testing Skills Interactively

You could in principle use spaced repetition to check all kinds of things.

Flashcards are what most systems seem to use, but what else could you do?

If I had a generic spaced repetition scheduler that just kept a record of
different commands that ask for input and matching commands that grade the
input, I could use that to check lots of things beyond just flashcards. Ability
to solve math problems (use a CAS to check the results), for instance. Ability
to remember secrets (use `pass` as the source of secrets and also the way to
check whether my input matches what's stored). I guess I'd need a way to define
'generators', not just hardcoded commands.

My impression is that the research has mostly focused on strictly memory tasks.
Might it work for other things, like keeping physical skills fresh?

For instance, a possible piano technique refresher practice regime could look
something like this:

- Export MIDI version of
  [Hanon](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=2037) or
  whatever else you want to drill

- Have a spaced repetition scheduler tell you when a given exercise should be
  run

- Fire up the test runner and perform the song on your MIDI-connected keyboard

- Test runner compares your performance to the pure MIDI file, grades it
  accordingly, and reschedules you based on divergence from true (with some
  tolerance, obviously - no human gets close to exact replication of MIDI
  files)

This proposal makes the massive assumption that spaced repetition works on
physical skills, which I have no evidence for and suspect is unlikely.

However, you could adapt it to check memory of musical pieces, which could fit
spaced repetition quite well, I think. As long as you break things down by
phrases / sections.

Comparing sequences of notes / chords for match up in relative order is far
easier than saying "How close are you to correct rhythm?", so when considering
just memorization, that might be all we need to do.

Someone has built a less-nerdy, simpler version of something like this here:
http://pianopracticeassistant.com/spaced-repetition/

It's quite possible the gain of automatic checking and grading of your memory /
performance is not worth the increased complexity of my proposed solution.
Certainly what I suggest wouldn't help for pieces you don't have access to a
MIDI file for, because you can't use it at all.


## Links

This is more about general learning, but it seems relevant to what this file is
trying to be - how do I learn? How do I keep what I've learned in my head?
https://vasilishynkarenka.com/learning/
