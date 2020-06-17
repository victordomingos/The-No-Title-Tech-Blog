Title: Haiku R1/beta2 has been released
Date: 2020-06-16 20:00
Lang: en
Tags: haiku, beos, operating systems, python, open source, beta, review
Category: News
Slug: haiku_r1_beta2_has_been_released
Author: Victor Domingos
Cover: images/2020/haikur1beta2/haiku_r1_beta2.jpg
Summary: After about 20 months of hard work, the Haiku team has finally released, a few days ago, the second beta version of Haiku, the BeOS-inspired open-source operating system that aims to offer a fast, simple to use, and powerful alternative for personal computing. This time, I am particularly happy, even a bit proud myself, because I have also been contributing with Portuguese translations for the user interface, and this is the first beta which includes those translations. So, let's celebrate!

I first wrote about Haiku back in 2018, right after the first Haiku beta was released. As an old time BeOS user, I had been waiting for that moment. You can read [my review of Haiku R1/beta1]({filename}/articles/2018/2018-10-17_haiku_r1_beta1_revisiting_beos.md) in case you're curious. So, today, I will write a few paragraphs about some things that have changed and share with you some of my impressions on what there's to love on this new operating system. And, just because it can be done and it's more fun, I will be writing, editing, and publishing this article just using [Haiku R1/beta2](https://www.haiku-os.org/get-haiku/r1beta2/release-notes/). I will include a brief note explaining what software I used and if there were any difficulties.

As a recap, [Haiku](https://www.haiku-os.org/) is an open-source operating system inspired on BeOS. It keeps the classic features and user interface design. Also, in the 32-bit version it aims at binary compatibility with BeOS applications, which means that if you have some old BeOS game or application, like Gobe Productive, you will probably be able to run it on Haiku. But, even if the original plan for Haiku R1 was to achieve feature parity and compatibility with BeOS R5, the development team has meanwhile decided to add some useful features, and that has contributed to make Haiku overall a much more modern operating system.

## What's new in beta 2

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

Currently, Haiku is generally quite usable with HiDPI (or *Retina*) displays. The icons are presented in a vectorial format (an improvement over BeOS's bitmap-based icons) and, by adjusting the font size in Settings, the whole interface scales accordingly. There are still some small details that can be improved, like the relative size of some widgets, but there has been a noticeable progress since beta 1.

The Deskbar now supports a new single line mini-mode that makes it fit in the display corner, in the small space left by the yellow tabs (the window title bars). 

![HaikuDepot]({static}/images/2020/haikur1beta2/deskbar.png)

You get the system tray and two clickable buttons: the one with the blue leaf icon displays the main Deskbar menu, and the one with a little man standing at a green screen presents the list of current running applications.

WebPositive, the builtin web browser, keeps getting more stable and more compatible. It is based on Webkit (not the most up to date version, though), the same engine that powers Apple's Safari, and it is able to process most websites. Sure, you will find some oddities here and there, especially on some heavy pages with special fonts, video, animations and so on, but most of the time it's just OK. And I can say that I have found some pages that now work better in WebPositive that they used to (like for instance the [Haiku Community](https://discuss.haiku-os.org/) forum). WebPositive seems to be mostly stable now, even though I have seen it crash once during this review.

As you may have noticed, I also consider the user interface translation as an important new feature in this beta. While I am pretty comfortable with English, in most cases I prefer to use software in my native language (Portuguese), and I know that many other users feel the same about it. I have personally contributed as a volunteer on this translation effort, and it's good to see that the Haiku user interface and many of its builtin and third-party applications are now available in multiple languages, and Portuguese is one of those.

If you haven't heard about Haiku for a long time and have missed both the first beta in 2018 and all the nightly builds since then, then there are certainly many other features that will be new to you, like the package management system, HaikuDepot, WebPositive or the Network settings.

## Available software

![HaikuDepot]({static}/images/2020/haikur1beta2/haikudepot.jpg)

Haiku is currently available on both 32 and 64-bit versions, the first one being more directed towards legacy support and the second one being the best option for more recent hardware and better performance. If you are on 32-bit, then you may also use old BeOS applications that you may have kept from the late 90's. But if you were not a BeOS user back then, or if you just want to use current software in a more modern computer, you will be happy to know that there are many applications available on HaikuDepot, and the list grows every few days. For me, in 2018, LibreOffice and Krita were a clear sign that the Haiku platform was maturing and becoming increasingly useful for many everyday tasks. 

Keep in mind that we are still talking about an operating system that is in a beta stage of development, but the fact is the software list on HaikuDepot keeps growing and growing. So, depending on your specific needs, maybe you will find there all the software you need to get your job done.


## Hardware support

As with any other non-profit, volunteer-based, open-source operating system, adding proper hardware support is not easy, mainly because manufacturers do not release drivers (which is understandable in the context of a pre-release operating system like Haiku) and, most importantly, they don't make available the documentation that would allow other developers to build new drivers. So, although it has been improving over time, having good hardware support (booting, sound, Ethernet, Wi-Fi) on your current computer can still be a matter of luck. 

But even if you don't have a spare computer to try a beta operating system like this, or if its hardware does not have very good support on Haiku, you may still try it in a virtual machine. Haiku is pretty much a lightweight operating system, and runs just fine inside VirtualBox, Parallels Desktop, or VMWare, even with much less than 1 GB of RAM. You may still be amazed on how fast many Haiku applications can launch. There is no 3D graphics acceleration available yet, which is sad, but the truth is that for many tasks it is not a very big problem.

The good news is that Haiku has much better hardware support than BeOS for hardware released in the last two decades. You can now use 64-bit processors, Wi-Fi, XHCI (USB3), NVMe SSDs and so on. And this is precisely an area that has improved since Beta 1. For instance, I have a 13 years old MacBook Pro that is now able to play sound through external earphones or speakers. And many computers are now able to boot from USB3. So, if you have tried Beta 1 without success, go ahead and give it another shot. If it goes well, enjoy! If it doesn't, please consider reporting any bugs you find. Any way, you definitely should join the conversation with the developers and other users at the [Haiku Community forum](https://discuss.haiku-os.org/), sharing your experience and learning from the others' tips.

## Final thoughts - what I miss on Haiku

Coming from macOS, I certainly miss some of the MultiTouch trackpad gestures, Mission Control (a macOS feature that makes easy to view all open windows and switch between them, or even move content from one window to another) and the nice hardware and software integration. I miss the display brightness auto-adjustment, or at least the ability to manually set the brightness using the keyboard. I don't have that problem in the newer Mac, since I use Haiku on a virtual machine there, but on the old MacBook Pro, the one with a native Haiku installation, the screen can sometimes be too bright. 

I also miss system-wide multilingual grammar and spellchecking across different applications. On macOS, we take that for granted these days, but here even LibreOffice still seems not to be willing to help we writing with minimal correctness... Luckily enough, I discovered that CuteMarkEd had spellchecking working for both English and Portuguese (provided we install the necessary hunspell/myspell packages). Calligra Writer seems to be working too, but I really need LibreOffice fully operational, which means I should consider filing a bug report on HaikuPorts. This is not directly related to Haiku itself, since the software porting is not done by the Haiku team, but for the end user this is certainly an important part of the overall experience.

I miss cloud services integration (Dropbox synchronization mainly), but currently most of my file syncing needs are done through Git, which works just fine on Terminal and even with graphical clients like Trackgit and Guitar.

I miss a robust mail client with easy Gmail configuration. There are a few mail clients available, and I must confess I did not try them all yet, but until now the experience has not been as good as I wished. I am able to use the browser as an alternative, but the performance on some web applications like Gmail is still not very exciting.

With regards to development tools, there has been a persistent effort to port many programming languages and development utilities to Haiku, so you can build your own software using C++ and a variety of other languages like Rust, Python, Java, Elixir, Erlang, Nodejs, R, Ruby, OCaml, Nim, Go, Lua, Perl, Swift, Tcl or Yab. In HaikuDepot you will find all these and also a few well known IDEs like PyCharm CE, IDEA IntelliJ CE or NetBeans. 

From my experience with Python and Python-related tools, I feel that there has been great progress, but there is still a long way to go. For instance, making easier to run different Python versions and to create and manage virtual environments. HaikuDepot includes some well known packages, but in the case of binary distributions you will have to stick with the versions offered in the catalog, which may not be viable for some Python projects.

Other languages, like Swift, are only available in older versions and are in need for someone to volunteer to update their respective HaikuPorts recipes. 

If you are willing to create your own GUI applications for Haiku, C++ is still your best bet,  using either the Haiku API or Qt5. I have not explored NetBeans to see if Swing GUI apps are possible, because it has been constantly crashing on launch. In fact, it was one of the very few applications that I have seen crashing during the preparation of this review. But if you were expecting to be able to use tkinter/ttk or wxWidgets in Python, no way. You could learn [Yab](http://yab.orgfree.com/) instead, which is a BASIC based language with additional Haiku commands. You could also do web front-end stuff in JavaScript, provided you have installed Otter-Browser in order to have access to the Developer Tools. Just keep in mind that there are no app generation toolkits like Electron available for Haiku yet.

## How this article was written and published using Haiku

![Haiku R1/beta2 - CuteMarkEd Markdown editor and Terminal, displaying generation of a static site using Pelican]({static}/images/2020/haikur1beta2/haiku_cutemarked_terminal.jpg)

This review was entirely written on CuteMarkEd, which is a nice Markdown editor that supports both spellchecking and real-time HTML preview.

I used Haiku's builtin Screenshot application to make some screenshots and I tend to save them using OptiPNGTranslator. Then I use ShowImage to view the result and Krita for some editing (resizing, cropping...). Finally, most of the images end up being processed in Terminal using Optimize Images to find out if I can squeeze them a bit.

The website is compiled or generated using my usual Python/Pelican setup in Terminal, where I also manage version control with Git. Except for the fact that it still does not display Emoji characters, I just love Haiku's Terminal. In order to make my Pelican project compile under Haiku, I had to create two separate dependency installation steps. Python 3 and some packages (like Pillow) must be installed first using `pkgman` or HaikuDepot. Then, most pure-python packages can be installed using `pip` as usual. This was not very difficult to me because I had already been very selective on dependencies to make sure this project would also work on iOS/Pythonista.

For web browsing and to check the results of Pelican output, I used both WebPositive and Otter-Browser.

When I configure a new Haiku system, I always make sure I install QuickLaunch and then I go to **Preferences** > **Shortcuts** to define a keyboard shortcut. This alows me to have a quick application launching method similar to Spotlight on macOS. But I also like to set a few additional keyboard shortcuts for launching the most commonly used apps, like Terminal, WebPositive, HaikuDepot, or SoftwareUpdater, which is for me the simplest and quickest way to get into some task.
