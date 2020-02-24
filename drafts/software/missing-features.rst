This is intended to be a bucket list of features I wish software packages had.

Ideally all entries eventually become feature requests, bug reports, or
configuration updates to my software setups. Sometimes, though, I expect an
idea won't matter enough for me to follow up on, or I'll realize it was a bad
idea to begin with.


Android should offer a way to slow-poll for viable WiFi connections while WiFi
is off. The goal is to minimize use of cellular data while preserving battery
life. When active, every N minutes it flips on WiFi and scans for open or known
networks. If none is found it turns WiFi back off until the next sleep period.
If one is found, it connects, confirms that the network's internet connection
is functioning, and keeps WiFi on until the network connection is lost, at
which point WiFi is turned off again. Android 9 has almost this feature as
"Turn on WiFi Automatically", but my reading suggests it does not turn the WiFi
off again after disconnecting from the network. :/
