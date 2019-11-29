---
title: "Work History"
meta_content: "Nate Eagleson's work history."
template: "essay.html.tmpl"
---

I worked as a software developer at Rite Aid from June 2005 (exact start date
lost to the ages) to April 27th, 2007.

After taking a lengthy drive around the American West, I settled in to [try a
startup](http://www.codeninjaz.net) with [Bob
Stouffer](https://www.bobandkellystouffer.com/) on September 3rd, 2007. I think
the only startup mistake we didn't make was taking external funding (a.k.a.
"debt"), and on January 31st, 2009 I threw in the towel. Bob threw it in a few
months later, and on May 2nd, 2009, codeninjaz.net, inc was formally dissolved.

I did freelance contracts from then until the end of 2010, doing everything
from web development to system administration to [building a desktop app in
wxPython](/work/projects/illuminations).

On January 3rd, 2011, I started a long-term contract as lead developer for
2x30.com, a startup project to build a social network to help people make good
habits and break bad ones. After a long hard slog, we delivered the product as
requested.

Unfortunately, "as requested" was a pretty far cry from "minimum viable
product", despite our product manager's best efforts to persuade the board and
investors otherwise, and several months after I submitted my last invoice for
initial development (on June 29th of 2012), the project shut down.

I took a few months off to get married, honeymoon for several weeks in Ireland,
and settle in to married life, then started interviewing for full-time
positions. On October 1st, 2012, I started work as a web developer at Clark
Associates.

I was recruited away from Clark to do a contract as a front-end JS developer
for MapQuest, which I started on June 24th, 2014. A month after I started,
Brian McMahon showed up unannounced and said, in effect, "Hey guys, we're
closing the Lancaster office next year. If you want to move to Denver, CO, feel
free to re-apply."

After that earthshattering event, my contract wound up getting extended through
the scheduled office closing in March of 2015, but when most of the employees
left early, leaving the office a ghost town, my contract was summarily
truncated at the beginning of January. I owe my manager Kumiko big for going to
bat for me and getting my contract extended a few weeks so I could finish
closing on my first house.

My last day at MapQuest was January 30th, 2015.

On March 9th, 2015, I started work as a contract JavaScript developer at United
Concordia.

I was told during the interview process that I would be trained in AngularJS,
the framework for the planned project, and that there would be two or three more
experienced JavaScript developers joining the project.

When no AngularJS training or real work materialized in the first few days
there, I learned it myself by building a few toy projects.

When business plans changed a few weeks into my contract, I was moved to a
different project, dubbed BPIR, an acronym for Benefits Plan Information
Repository, if memory serves. It was a set of web services and an editing
interface to define the coverage provided by insurance policies in a structured
way for use by other services and programs throughout United Concordia. It was
intended to replace a thirty-year old IMS-based system that was opaque to
everyone, unusable by any other systems, and took years to train people to use.

When my project changed, I was told there would be no additional JS hires.
Instead, I was offered a student intern who had specialized in COBOL
maintenance. I sighed, added a thirty percent penalty to my estimate
spreadsheet, and warned management we were unlikely to hit their aggressive
project deadline.

Fortunately, [Melanie](https://www.linkedin.com/in/melanie-durko-61197282)
turned out to be brilliant. I sank into teaching her front-end web development
and version control with Git (as an unofficial frontend to Harvest SCM, a
disaster of a VCS) while helping the new project collect business requirements
and review the data model plans.

My content-heavy mentoring style and her ability to soak up information like a
sponge paired well, and she performed beautifully. I did the heavy lifting of
building the complex UI components we did not have while she wrote most of the
individual app screens using them for the first phase of the project.

The major UI components I built were an Outlook-style navigation tree, a
drag-and-drop editor with autosave and smart operation queueing, and a forest
editor (a.k.a. 'collection of trees').

Since SPAs, Angular, and JS generally were not common at United Concordia or
Highmark when I started, I also put together a JS build pipeline and basic
architecture for the project. It did not support anything like all the features
I wish it had, as Highmark's newness to the tech stack meant that most of the
software I wanted to include was not yet approved for use there, and getting
software approved for use was a slow, arduous process (completely at odds with
the fast timeline they gave us). So, in several cases, I wound up reinventing
the wheel (such as in compiling Angular templates down to a single pre-loaded
client-side JS object), while in others we did without (like having Babel to
make ES6 features available, or a linter for HTML/SCSS). We did at least have
ESLint available to us, and I took advantage of its plugin architecture to
write project-specific linters as needed (alas, I can no longer remember what
those were - I think I wrote one to enforce the 'controllerAs: vm' naming
convention?).

TODO Write in-depth explanations of the components I built. I've gone digging
through my old notes to self and I don't seem to have any useful records of
precisely what I did. I remember that the treenav was generic, in that it took
in a JS object following a certain schema and rendered it as a set of nested
HTML nodes with links, and that I was the one who argued for and built the
infrastructure to handle generating that object client-side, to keep the web
services stateless. I also remember Angular's directive compiler didn't support
recursion, at least at the time (1.4.x, I think?), so I had to adapt a hack for
supporting it. The first naive version became fairly slow once we got a real
dataload working, so I had to spend a few days optimizing to make it
acceptable. The last piece of work I did with it was retooling it so that any
slow-loading chunks of data would show a spinner at their location in the
navigation tree.

In the second phase, we extended BPIR to support defining the provider networks
and pricing models that could be attached to policies. As part of that
initiative, the frontend team was expanded.

I was given a pair of Java backend developers and another student intern to
train as front-end JS developers. Once again, we were given a relatively tight
timeline, which was at odds with the goal I was given of training more people
on the project's frontend. We also were told we had to transition from
Highmark's waterfall development model to their newly-rolled-out Agile approach
(which turned out not to be).

When the newly-created frontend team was dropped in my lap, I set myself a few
goals I never actually told the rest of the team:

1) To get the new team members to gel into a real team and learn the new tech
   being thrown at them well

2) To get the project done on the six-month timeline one of the backenders said
   was impossible

3) To make sure we had fun doing it.

I once again spent my development time writing high-level components the other
team members could use to construct individual screens, this time mainly a
ListBuilder directive that offered several modes of operation (all data loaded
locally for smaller datasets and snappy response times, while it also offered
support for specifying a search endpoint for filtering through large datasets
that it was not reasonable).

I had much less development time than previously, though, as various team
members had figured out I was good at gathering requirements, fixing workflows,
and generally solving any problem you might throw at me, so I became one of the
go-to guys on the team for keeping forward momentum.

I also spent a lot of time teaching the new team members about JS, Angular,
code review, and Git (we moved to a more-formal system of using Git as a
collaborative frontend to Harvest, as Melanie and I had both suffered what
would have been data loss at Harvest's hands had it not been for git, and there
were rumblings that the organization would be moving to git in the next year
anyway).

As the second phase was winding down roughly on time and the team was being
split apart by unwise corporate higherups, one of the backend devs said to me
of his own accord: ~"We had a good little team going for a while, didn't we. We
had some fun."

It was very satisfying hearing my goals were achieved, and knowing I'd been
part of why that happened.

My last day contracting for United Concordia was September 12th, 2016, as I was
recruited away to work at Nxtbook Media. I stayed on an extra day beyond my
original planned resignation date to help them with a release, since one of the
managers asked that as a favor.

My first day at Nxtbook was September 19th, 2016.
