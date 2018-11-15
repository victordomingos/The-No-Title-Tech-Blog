Title: Translating Haiku operating system to Portuguese, and other stories
Date: 2018-10-31 23:30
Lang: en
Tags: haiku, beos, operating systems, UI, user interface, localization, translation, portuguese, open source
Category: Reviews
Slug: translating_haiku_operating_system_to_portuguese
Author: Victor Domingos
Cover: images/2018/translating-haiku/pootle_translation_server_haiku.png
Summary: Since two weeks ago, I have been back to the Haiku world, exploring the present status of the operating system and currently available tools, and I decided to start using Haiku to translate the Haiku operating system to Portuguese.

Being able to install Haiku natively in my trusty, 11 years old, Macbook Pro, was the click I needed to get using it and to start contributing to the project. I must say that I had been following Haiku from a distance for many years, like a hidden love, since its beginnings, but never risked to install it natively. The recent launch of the first beta encouraged me to try it and I managed to get it up and running. 

In order to be able to use old BeOS software, I knew I needed to have the 32 bit version of the operating system. But I also wanted to be able to test the 64 bit version, and I noticed that some applications (*particularly* Python 3) were running faster on 64 bit. So I couldn't rest until I had both versions installed in my Mac, side to side with macOS. I have been using mainly the 64 bit version since then. The fact is that some old software seems to require some weird installation process and will not always run smoothly. Besides, many of the old titles were already compiled to 64 bit and there are many new applications available that reduce the need for that kind of compatibility. I would like to be able to use [Gobe Productive](https://en.wikipedia.org/wiki/Gobe_Software){:target=_blank} and SoundPlay, right, but after almost 20 years, I am pretty sure I can live without them if needed.

As you know, Haiku is still in development, in a slow but consistent pass. There are some hiccups every now and then, but the operating system itself is getting very stable. And, provided you can find the needed applications for the kind of work you do, maybe you can already use it to do real life work. Well, for me it means having some kind of text editor or word processor, an image editing software and a web browser. And Python, of course. And, in fact, Haiku has almost everything I needed. There are a couple of text editors and word processors. I am still exploring, but today I am writing this in Markdown using [CuteMarkEd](https://cloose.github.io/CuteMarkEd/){:target=_blank}. For image editing, I am sticking with [Krita](https://krita.org/){:target=_blank}. For web navigation I have been using the built-in [WebPositive](https://www.haiku-os.org/docs/userguide/pt_PT/applications/webpositive.html){:target=_blank} browser, alternating with [QupZilla](https://www.qupzilla.com/){:target=_blank} and others. Web pages and web applications are very complex beasts nowadays, but most of them work just fine with these browsers. 

Regarding Python, well, it's a work in progress. We have Python 3.6 (no Python 3.7 for now), without `tkinter`/`ttk` (no TK port available for now). We have some important binary packages ported to Haiku, like Requests, Pillow, Numpy, BeautifulSoup or Flask, but not all versions are available and virtual environments still seem to need some developer care. Some of the packages can be installed through `pip`, but others may require using the HaikuDepot package manager). Having said that, I am able to run my Count Files and Optimize Images applications in Haiku. But no Pelican, at least not yet.


## Translating Haiku using Haiku itself

I decided to contribute with my own work and... ahem... expertise to the Haiku project. I am not a fluent C++ speaker, so doing development for this platform was out of the equation, but I am pretty comfortable with text editing, and with both English and Portuguese languages. Being a native Portuguese speaker/writer and a long time computer geek, I thought I could be the right person to make the Portuguese localization move forward.

![Haiku operating system translation]({static}/images/2018/translating-haiku/haiku_translation.png)

At the time, Haiku had about 20% of its user interface translated to Portuguese, but was having no progress since a long time ago. I enlisted myself and started working on it. I reviewed all the pending translation suggestions (many of them had been pending for 4 years) and added many more. Right now, after 2 weeks, it's already 50% done, and many important sections are already fully completed: WebPositive, StyledEdit, PackageInstaller, HaikuDepot, Expander, DriveSetup, Installer... It's a matter of time until these translations get merged to the main Haiku distribution.

![Translating Haiku using Haiku itself, Pootle Translation Server in WebPositive window]({static}/images/2018/translating-haiku/haiku_translation_the_operating_system_on_haiku_itself.png)

I have also been working on the translation of some third-party applications, like BePDF, BePodder, QuickLaunch, and others.

![Translating third-party applications using Polyglot]({static}/images/2018/translating-haiku/polyglot_haiku_apps_translation.png)

Meanwhile, it's worth noting that almost all of this work has been done using Haiku itself, which proves that it is possible to use it right now, even if it is still not quite ready for a production release. By using Haiku, I am able to get a better grasp at the current status of the ecosystem and to contribute in another way: detecting existing problems, doing some testing and submitting error reports.

I hope I can get at least 70% of the operating system translated to Portuguese in the following weeks, and that this work I am doing now can serve all Portuguese-speaking users right after the release of Haiku R1/beta2.
