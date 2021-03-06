---
title: Illuminations
slug: illuminations
template: project.html.tmpl
links:
  - url: https://www.brightideaspress.com/product-category/illuminations/
    text: Main product page
  - url: https://www.youtube.com/watch?v=CE9uwdUNnGM
    text: Demo screencast
screenshots:
  - filename: schedule.png
    caption: The weekly schedule view in the Illuminations app.
summary: Cross-platform lesson planning software
# TODO Should I explain the underpinnings? Update handling? The pain of
# building drag-and-drop?
---

Illuminations is a homeschool curriculum with a large set of pre-planned
subjects to choose from, so academic schedule planning for the year takes
just a few minutes.

The early versions were just sets of PDFs containing the daily lesson plans
for each subject and a grid showing the weekly schedule for all subjects
together.

Customers loved the core product of pre-packaged lesson plans, but wanted
some features PDFs couldn't provide:

* a way to show only their selected subjects on the weekly schedule
* a way to add their own subjects to the weekly schedule
* a way to change subject order on the weekly schedule

The publishers hired me to write an application to replace their weekly
schedule PDFs and meet those needs.

The result was a wxPython program that runs on Mac OS X (10.6+) and Windows (XP
and up). The Windows installer is built using
[InnoSetup](http://www.jrsoftware.org/isinfo.php).

The client eventually decided to discontinue their use of the Python program.
