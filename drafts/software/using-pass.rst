pass is my preferred password manager.

For ages I wasn't sure how to handle managing multiple distinct password
stores, so as to keep work and personal secrets separate.

It turns out there's a trivially simple answer:

Whatever's the "main" repo goes in the usual ~/.password-store path.

Then, for each other password store you want to add:

* Check out the pass repo somewhere on disk.

* Import the required private key for decrypting passwords from that collection

* Make sure there's a .gpg-id file in that collection's base directory

* cd ~/.password-store; ln -s $HOME/personal/.password-store personal

* echo 'personal' >> .git/info/exclude

and presto, they're all available to you.

You can even work with passwords in the standard way with insert/edit/rm/mv.
You just have to manage push/pull yourself in the child checkouts.

Loosely inspired by this use of Git submodules, which introduces more
complexity than I need in my case:
https://lists.zx2c4.com/pipermail/password-store/2014-October/001188.html
