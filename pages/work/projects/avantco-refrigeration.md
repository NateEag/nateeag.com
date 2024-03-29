---
title: Avantco Refrigeration
# TODO Generate slug at load time based on title.
slug: avantco-refrigeration
template: project.html.tmpl
links:
  - url: http://www.avantcorefrigeration.com
    text: Avantco Refrigeration
summary: Avantco Refrigeration website
---

One of my projects at [Clark Associates](http://www.clarkassociatesinc.biz/)
was implementing the Avantco Refrigeration website, a digital product catalog
and warranty registration system for Clark's Avantco Refrigeration product
line.

I took HTML/CSS mockups from a web designer and converted them into clean,
modular, database-driven PHP, using [Composer](https://getcomposer.org/) to
manage dependencies, [Twig](http://twig.sensiolabs.org/) for templating, and
some internal tools Clark's PHP team had developed for use across our sites.

I generalized and reworked the CSS to handle variable amounts of content,
something the designer's CSS did not handle.

I used JavaScript where reasonable, to enhance form validations and implement
the few dynamic client-side features that required it (like the scrolling ad
banner on the front page). I tried to make the site worked well without it,
though, in the tradition of progressive enhancement.

Much of the site's content was pulled from a pre-existing master database, so
using a CMS to manage it would have been clumsy. Thus, I implemented a
lightweight management system that parsed a CSV of the products to list on the
site and populated the database tables accordingly. Most of the complexity was
in the category system, which I designed and implemented.

The site has accumulated some breakage since my time there, and I suspect it
may have been rewritten since, as several UI components have changed
significantly.
