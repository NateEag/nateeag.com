I am starting to use spaced repetition flashcards to help me store useful
information in my long-term memory.

I would like to store my flashcards as plain text, though.

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
