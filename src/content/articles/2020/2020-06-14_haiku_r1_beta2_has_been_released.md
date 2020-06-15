Title: Haiku R1/beta2 has been released
Date: 2020-06-11 20:00
Lang: en
Tags: haiku, beos, operating systems, python, open source, beta, review
Category: News
Slug: haiku_r1_beta2_has_been_released
Author: Victor Domingos
Cover: images/2020/haikur1beta2/haiku.jpg
Summary: About 20 months of hard work, the Haiku team has released this week the second beta version of Haiku, the BeOS-inspired open-source operating system that aims to offer a fast, simple to use, and powerful alternative for personal computing. This time, I am particularly happy, and even a bit proud myself, because all these months I have been contributing with Portuguese translations for the user interface and this is the first beta which includes those translations.

I first wrote about Haiku back in 2018, right after the first Haiku beta was released. As an old time BeOS user, I had been waiting for that moment. You can read my review of Haiku R1/beta1 in case you're curious. So, today, I will write a few paragraphs about some things that have changed and about some of what there's to love on this new operating system. And, just because it can be done and it's more fun, I will be writing, editing, and publishing this article just using Haiku R1/beta2. I will include a final note explaining what software I used and if there were any difficulties.

As a recap, Haiku is an open-source operating system inspired on BeOS. It keeps the classic features and user interface design, and in the 32-bit version it aims at binary compatibility with BeOS applications, which means that if you have some old BeOS game or application, like Gobe Productive, you will probably be able to run it on Haiku, either on a virtual machine or natively using supported hardware. But even if the original plan for Haiku R1 is to achieve feature parity and compatibility with BeOS R5, the development team has since then decided to add some useful features, that help make Haiku a much more modern operating system.

## What's new

The [release notes for Haiku R1/beta2](https://www.haiku-os.org/get-haiku/r1beta2/release-notes/) highlight some of the best new features you will find in this version:

- Improved HiDPI support
- Deskbar improvements
- New Input preferences
- WebPositive improvements
- More ported software
- Installation improvements
- NVMe support
- Enhanced and stabilized XHCI (USB3) support

...and more.

Currently, Haiku is mostly usable with HiDPI (or *Retina*) displays. By adjusting the font size in Settings, the interface adjusts accordingly. There are still many details that can be improved, like the size of some widgets, or the window borders thickness, but there is a noticeable progress.

The Deskbar now supports a new mini-mode that make it fit in the corner, in the space left free by the yellow tabs (the window title bars). You get the system tray and two clickable buttons: the one with the blue leaf icon displays the main Deskbar menu, and one with a little man standing at a green screen displays the current running applications.

WebPositive, the builtin web browser, keeps getting more stable and more compatible. It is based on Webkit (not the most up to date version, though), the same engine that powers Safari, which allows it to be able to process most websites. Sure, you will find some oddities here and there, especially on some heavy pages with special fonts, video, animations and so on, but most of the time it's just OK.

I also see the user interface translation as an important new feature in this beta. While I am comfortable with English, in most cases I prefer to use a computer in my native language (Portuguese), and I know that many other users feel the same. I have personally contributed as a volunteer on this translation effort, and it's good to see that the Haiku user interface and many of its applications are now available in more than 20 languages, and Portuguese is one of them.

If you didn't heard about Haiku in a long time and missed both the first beta in 2018 and all the nightly builds since then, there are probably other features that will be new to you, like the package management system, HaikuDepot, WebPositive or the Network settings.


## Available software
If you are on 32-bit, you may use old BeOS applications. But if you were not a BeOS user, and/or if you want to use current software, you will be happy to know that there are many applications available on HaikuDepot, and the list grows every few days. For me, in 2018, LibreOffice and Krita were a clear sign that the platform was maturing and becoming increasingly useful for many everyday tasks. 

The software list keeps growing, so depending on your specific needs maybe you will find there all the software you need to get your job done. 


## Hardware support

As with any other non-profit, volunteer-based, open-source operating system, adding proper hardware support is not easy, mainly because manufacturers do not release drivers (which is understandable in the context of a pre-release operating system like Haiku) and, most importantly, they don't make available the documentation that would allow other developers to build new drivers. So, although it has been improving over time, having good hardware support (booting, sound, Ethernet, Wi-Fi) on your current computer can still be a matter of luck. 

But even if you don't have a spare computer you can use to try a beta operating system, or if it does not have very good hardware support on Haiku, you may still try it in a virtual machine. Haiku is pretty much a lightweight operating system, and runs just fine inside VirtualBox, Parallel, or VMWare, even with much less than 1 GB of RAM. You may still be amazed on how fast many Haiku applications launch. There is no 3D graphics acceleration available yet, which is sad, but the truth is that for many tasks it is not a very big problem.

The good news is that Haiku has much better hardware support than BeOS for hardware released in the last two decades. You can now use 64-bit processors, Wi-Fi, XHCI (USB3), NVMe SSDs and so on. And this is precisely an area that has improved since Beta 1. For instance, I have a 13 years old MacBook Pro that now is able to play sound through external earphones or speakers. And many computers are now able to boot from USB3. So, if you have tried Beta 1 without success, go ahead and give it another shot. If it goes well, enjoy! If it doesn't, consider reporting any bugs you find. Any way, you definitely should join the conversation with the developers and other users at the [Haiku Community forum](https://discuss.haiku-os.org/), sharing your experience and learning from the others' tips.



![Haiku R1/beta1 - WepPositive browser and StyleEdit text editor]({static}/images/2018/haikur1beta1/haiku_webpositive_stylededit.png)



## Final thoughts - what I miss on Haiku

Coming from macOS, I certainly miss the MultiTouch gestures, Mission Control (a macOS feature that makes easy to view all open windows and switch between them, or even easily move content from one window to another) and the nice hardware/software integration. I miss the display brightness auto-adjustment, or at least the ability to manually set the brightness using the keyboard. I don't have that problem in the newer mac, since I use Haiku on virtual machine there, but on the old MacBook Pro, the one with a native Haiku installation, the screen can be too bright sometimes. 

I also miss global grammar and spellchecking across different applications. On macOS, we take that for granted, but here even LibreOffice and Calligra still seem not to be willing to help we writing with minimal correctness... Luckily enough I discovered that CuteMarkEd had spellchecking working for both English and Portuguese (provided we install the necessary hunspell/myspell packages).

I miss cloud services integration (Dropbox synchronization mainly), but these days most of my file syncing needs are done through Git, which works just fine on Terminal and even with graphical clients like Trackgit and Guitar.

I miss a robust mail client with easy Gmail configuration. There are a few mail clients available, and I must confess I did not try them all yet, but until now the experience has not been the best. I am able to use the browser as an alternative, but the performance on web applications like Gmail is still not very good.

Speaking to dev tools, there has been persistent effort to port many programming languages and development utilities to Haiku, so you can develop your own software using C++ and a variety of other languages like Rust, Python, Java, Elixir, Erlang, Nodejs, R, Ruby, OCaml, Nim, Go, Lua, Perl, Swift, Tcl or Yab. In HaikuDepot you will find these and also a few well known IDEs like PyCharm CE, IDEA IntelliJ CE or NetBeans. 

From my experience with Python and Python-related tools, I feel that there has been a great progress, but there is still a long way to go. For instance, in making easier to run different Python versions and to create and manage virtual environments. Other languages, like Swift, are only available in older versions. If you are willing to create GUI applications, C++ is still your best bet on Haiku, either using Haiku API or Qt. I did not explore NetBeans to see if Swing GUI apps were possible, because it was crashing on launch. In fact, it was one of the very few applications that I have seen crashing during the preparation of this review. But if you were expecting to use tkinter/ttk or wxWidgets in Python, for instance, no way. You could learn [Yab](http://yab.orgfree.com/) instead, which is a BASIC based language with additional Haiku commands. You could also do stuff in JavaScript, provided you had installed Otter-Browser in order to have access to the Developer Tools.

## How this article was written and published using Haiku

CuteMarkEd - Markdown editor - nice because it supports both spellchecking and real-time HTML preview.

Terminal, git, optimize-images, and my usual Python/Pelican setup. 
Except for the fact that it does not display emoji characters, I just love Haiku's Terminal. In order to make my Pelican project compile under Haiku, I had to create two separate dependency installation steps: Python 3 and some packages (like Pillow) must be installed using `pkgman` or HaikuDepot. Most pure-python packages can be installed using `pip` as usual. This was not very difficult because I had already been very selective on dependencies to make it work on iOS/Pythonista.

Screenshot / OptiPNGTranslator

ShowImage / Krita

WebPositive - browsing through the Haiku Project website, Wikipedia and other sources to check some facts.

When I configure a new Haiku machine, I always make sure I install install QuickLaunch and then go to Preferences > Shortcuts to define a keyboard shortcut. This alows me to have a quick application launching method similar to Spotlight on macOS. But I also like to set a few keyboard shortcuts for the most commonly used apps, like Terminal, WebPositive, HaikuDepot, or SoftwareUpdater, which is for me the simplest and quickest way to get into some task.


