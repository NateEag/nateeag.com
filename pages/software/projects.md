---
title: "Software Projects"
meta_content: "Programs Nate Eagleson wrote or made major contributions to."
template: "essay.html.tmpl"
---

This is a list of programs I either wrote, made major
contributions to, or currently maintain.


## ScriptLighter

[ScriptLighter](https://www.scriptlighter.com) is a website that takes the
tedium out of casting group readings for plays.

My good friend [Bob Stouffer](https://www.bobandkellystouffer.com/) wrote the
lion's share of the code, but I have made significant contributions, and it was
my idea.

It was inspired by setting up a family reading of "Kings In Judea" from [The
Man Born To Be King](https://en.wikipedia.org/wiki/The_Man_Born_to_Be_King) for
a Twelve Days of Christmas event, and thinking "I'm spending so much time just
figuring out which characters talk to each other and trying to avoid assigning
roles that result in a reader talking to themselves. This is totally
automatable."


## lsp-mode Compatibility With php-language-server

When I first discovered the [Language Server
Protocol](https://microsoft.github.io/language-server-protocol/), I was
incredibly excited, because I had wanted PHP intelligence in Emacs for over a
decade.

When I dropped
[php-language-server](https://github.com/felixfbecker/php-language-server) into
my setup and hacked up a [quick PHP
backend](https://github.com/NateEag/.emacs.d/blob/8261d90ca053af74632c57983620df0ed66fe7ce/site-lisp/mode-configs/php-mode-init.el#L96)
for [lsp-mode](https://github.com/emacs-lsp/lsp-mode), I discovered that
completion at point wasn't working.

That led to [this bug
report](https://github.com/emacs-lsp/lsp-mode/issues/119), where I uncovered a
corner of lsp-mode that didn't conform to the LSP specification.

Once I understood that was the root cause, [the
fix](https://github.com/emacs-lsp/lsp-mode/pull/127) wasn't hard to get
working.

I now use the official lsp-php backend, but as far as I know, I was the first
person to get a PHP language server working in Emacs and publish the fact
publically.


## skewer-reload-stylesheets

As an Emacser, I'm a fan of live-editing wherever possible.

I thus made it possible to [live-edit
stylesheets](https://github.com/NateEag/skewer-reload-stylesheets), whether
they're in CSS, SCSS, or a CSS preprocessor I've never personally heard of.

As that suggests, the technique used to implement it is
preprocessor-independent. See the project itself for details.

This work is entirely dependent on Chistopher Wellon's awesome
[skewer-mode](https://github.com/skeeto/skewer-mode).


## diff-check

A git pre-commit hook that filters stylechecker output so only lines that are
modified by the commit are considered erroneous.

It is principally useful for incremental adoption of style guidelines in large
codebases that have not observed one previously. Instead of making a large
risky block of changes to huge files to clean them up, you just ensure new
changes follow the rules.

[https://github.com/NateEag/diff-check](https://github.com/NateEag/diff-check)
