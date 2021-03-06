Title: Haiku R1/beta1 review - revisiting BeOS, 18 years after its latest official release
Date: 2018-10-17 20:30
Lang: en
Tags: haiku, beos, operating systems, python, open source, beta, review
Category: Software Reviews
Slug: haiku_r1_beta1_review_revisiting_beos
Author: Victor Domingos
Cover: images/2018/haikur1beta1/haiku_macbook.jpg
Summary: Having experimented and used BeOS R5 Pro back in the early 2000’s, when the company that created it was just going down, I have been following with some interest the development of Haiku during all these years. While one can argue that both the old BeOS and Haiku miss some important features to be considered modern OSes these days, the fact is that a lightweight operating system can always be, for instance, an excellent way to bring new life into old, or new but less powerfull, hardware. 


## A long history of love, sorrow and hope

Back in 2000, the [BeOS](https://en.wikipedia.org/wiki/BeOS){:target=_blank} operating system was known  for its multiprocessing, multithreading capabilities, the way it handled multimedia, and its clean design. I still remember the surprisingly short time it would take to boot in my old computer, with an AMD K6-2 processor at 400MHz, or how most applications would launch almost instantaneously, without the lag I was used to see in Windows 98 or in the most common Linux distributions. I kind of fell in love with it, and have used it as much as I could for some time. There was a notorious lack of compatible software, in many areas, but [Gobe Productive](https://en.wikipedia.org/wiki/Gobe_Software){:target=_blank} and a few other apps were in fact powerfull enough to get a lot of work done.

![BeOS R5 Pro]({static}/images/2018/haikur1beta1/beos_screenshot.jpg)

Then, in 2001, we started reading the news that  Be, Inc. was being sold to Palm, Inc. and soon it was shutting down all its operations. BeOS was dead!... 

A lot of its users didn't want to believe it was the end of the line. And the idea of buying the source code back from Palm or even building a completely new BeOS started to gain traction in the community. There were [a few attempts to replicate the BeOS experience](https://en.wikipedia.org/wiki/History_of_Haiku_(operating_system)){:target=_blank}, including one that intended to recreate the BeOS interface on top of a Linux kernel. But the only project that has survived all these years was OpenBeOS, later renamed as [Haiku](https://www.haiku-os.org/){:target=_blank}. The main idea was to create an open-source and backward-compatible replacement for BeOS. It seemed like an impossible mission, but in 2009, about 8 years after the last official BeOS update, the Haiku team released the Haiku R1/Alpha 1, its first public snapshot, that gave former BeOS users a little bit of hope. There were four alpha versions, from 2009 to 2012. And then... an even longer wait period. There was no stable release, no beta version, not even a new alpha. 

This year, however, we had some good news. The Haiku team was finally releasing the first beta of the new BeOS-inspired operating system! [Haiku R1/beta 1](https://www.haiku-os.org/get-haiku/release-notes){:target=_blank} came out in 28 September 2018 and, while the initial idea for Haiku R1 was to reproduce as much as possible BeOS R5, it comes with some notable new features that increase it's usefulness and make it a little more likely to please both old and new users.


## Running Haiku R1/beta1 on two decade-old Mac&nbsp;laptops 

I happen to have at home two 10 to 11 years old Mac computers that are still in use, and both would benefit from the speed improvement that a lightweight OS could offer. From time to time, I load the latest Haiku alpha or nightly build in VirtualBox just to see how it’s going, but it’s never quite the same as having a native operating system. So, recently, when I heard that the Haiku team was releasing it's first beta, I decided to give it another try. Here is my brief report of how it went.

My first attempt at doing a native installation was on my [MacBook Pro 15” 2.2 GHz (Mid 2007)](https://everymac.com/systems/apple/macbook_pro/specs/macbook-pro-core-2-duo-2.2-15-santa-rosa-specs.html){:target=_blank}. It was frustrating to see that it didn't boot from USB (the very same issue I have often found when trying to run Linux on that computer), and the DVD drive had been replaced by a second hard disk drive, long time ago. I did several tries using two different USB sticks, an external USB hard disk drive, [Etcher](https://etcher.io/){:target=_blank} and [rEFInd](http://www.rodsbooks.com/refind/){:target=_blank}, a FireWire cable, the other Mac, the install DVD, and I did every procedure that came to my mind using those tools, without success. I was still stuck with VirtualBox. It allowed me to run Haiku in the full screen resolution and with access to the internet, which was positive. However, there was no sound at all and it was very slow, which is perfectly normal when doing virtualization in a 11 years old laptop, but certainly does not give the same nice feel we used to appreciate on BeOS.

Then I decided to try my luck with a [MacBook 13” 2.4GHz (Early 2008)](https://everymac.com/systems/apple/macbook/index-macbook.html){:target=_blank} that is currently used by a member of my family. It didn't boot from USB, but when I tried to boot Haiku from a DVD, I was finally able to boot the Live CD. I just needed to disable APIC and ACPI during the boot sequence. So, for that MacBook, this is what I was able to get:

- Only one processor core, but sill pretty snappy, when compared with MacOS X 10.7 Lion.
- Full screen resolution (but no way to control screen brightness).
- Does not turn off automatically after shutdown.
- Seems to be able to record audio using the built-in microphone, but apparently there is no audio output.
- No WiFi.
- No iSight camera.
- Trackpad works, but without secondary button and no scrolling.
- Keyboard layout (portuguese) does not fully match the physical keyboard.

![Haiku R1/beta1 - Boot time error on MacBook Pro 15" Mid 2007]({static}/images/2018/haikur1beta1/haiku_error.jpg)

At that time, my only hope was that maybe I could get Haiku to work on the MacBook Pro by extracting the SSD and doing the install process externally, using the MacBook. I had previously promised myself I wouldn’t tear down that laptop ever again, but I was ready to change my mind, for a good reason.

So, after completing a full install in a 20GB partition in the MacBook, I created a similar partition on the Macbook Pro and started taking out the 23 screws (the hard part, in this case, was keeping track of all the screws). I took the disk out and connected it to the MacBook using a USB enclosure. The install process, done from Haiku, was a breeze and reminded how I used to love the amazingly quick and easy way BeOS could be installed or migrated to a different drive or partition. After a few minutes, I placed the SSD and the screws back into their respective places. The rEFInd boot manager detected the new Haiku partition and it booted at the first attempt, without having to set up any of those boot time restrictions. Not bad, for a beta:

- Detects and uses both processor cores, so it's even faster than on the other MacBook.
- Full screen resolution (but no way to control screen brightness).
- WiFi (detects networks nearby and easily connects to my iPhone’s personal hotspot).
- No iSight camera.
- Partial trackpad support (no right button and no scroll, mouse pointer seems a bit too much nervous in this Mac).
- Keyboard layout (portuguese) does not fully match the physical keyboard.
- The computer switches completely off when shutting down. 
- Sound recorder displays a graph, similarly to the MacBook, so it seems to be able to use the built-in microphone, but there is no audio output.

I am very happy to see this old computer launching apps much faster than I had ever seen it before. 

![Haiku R1/beta1 running natively on two Mac laptops]({static}/images/2018/haikur1beta1/haiku_native_two_macs.jpg)

As a side note, Haiku R1/beta 1 is available in both 32 and 64 bit versions, but at this time there is no compatibility layer to allow the execution of 32 bit applications on the 64 bit operating system. So, I have chosen the 32 bit version because, at this time, it will probably have more apps available and I read somewhere that is was a bit more stable. I have already seen a few app crashes, and sometimes it hangs in the beginning of the boot process requiring a forced reboot, but I would say it’s normal in a beta version. Everything, including drivers and many of the third-party applications, is still under development. 

But hey, it works! In fact, this article is being written on Haiku, just to celebrate the fact that we are able to do so.

![Haiku R1/beta1 - WepPositive browser and StyleEdit text editor]({static}/images/2018/haikur1beta1/haiku_webpositive_stylededit.png)

## What's new

First of all, now Haiku has a built-in package management system, that makes very easy to update the operating system, and to discover and install new applications. The installed packages can also be deactivated if needed at boot time. 

![Haiku R1/beta1 - Software updates]({static}/images/2018/haikur1beta1/haiku_software_updates.png)

The users are now offered a new application called HaikuDepot, that acts like an app store with lots of free software. The list of available titles include some old favourites like [BePDF](https://depot.haiku-os.org/#!/pkg/bepdf/haikuports/2/1/0/-/3/x86_gcc2?bcguid=bc382-OFNA){:target=_blank}, [ArtPaint](https://depot.haiku-os.org/#!/pkg/artpaint/haikuports/2/1/2/-/2/x86_gcc2?bcguid=bc422-UYTH){:target=_blank} or [Sum-It](https://depot.haiku-os.org/#!/pkg/sum_it/haikuports/0/2beta/-/-/6/x86_gcc2?bcguid=bc461-JABP){:target=_blank}, but also some new power tools that have been ported or developed from scratch more recently, like for instance the office suites [Calligra](https://depot.haiku-os.org/#!/pkg/calligra_x86/haikuports/3/1/0/-/3/x86_gcc2?bcguid=bc200-HFAB){:target=_blank} and [LibreOffice](https://depot.haiku-os.org/#!/pkg/libreoffice_x86/haikuports/6/2/0.0/git/19/x86_gcc2?bcguid=bc349-JSUS){:target=_blank}, the image editor [Krita](https://depot.haiku-os.org/#!/pkg/krita_x86/haikuports/4/1/0/-/2/x86_gcc2?bcguid=bc235-EEIE){:target=_blank}, or the [Paladin IDE](https://depot.haiku-os.org/#!/pkg/paladin/haikuports/1/4/-/git/4/x86_gcc2?bcguid=bc271-SYVI){:target=_blank}, among many others. 

![Haiku R1/beta1 - the new HaikuDepot package manager]({static}/images/2018/haikur1beta1/haikudepot.png)

And, of course, if you feel specially nostalgic, you can still stare longly at the good old spinning teapot demo.

![Haiku R1/beta1 - the classic GLTeapot demo application]({static}/images/2018/haikur1beta1/haiku_glteapot_demo.png)

Another big improvement is [WebPositive](https://www.haiku-os.org/docs/userguide/en/applications/webpositive.html){:target=_blank}, the new WebKit based web browser that replaces the old NetPositive. Compared to what we used to have in BeOS R5, this is a massive upgrade, with support for many of the modern technologies that enable current websites. It means that you are now able, for instance, to watch YouTube videos, check Facebook updates or help translating the Haiku user interface in the [Pootle Translation Server](https://i18n.haiku-os.org/pootle/){:target=_blank}. Even with the majority of the improvements being under the hood, anyone who has used BeOS to access the web in the old times will certainly understand how significant this will be for any user.

The Network preferences panel is completely new and very easy to use. In addition to the selection and configuration of wired and/or wireless network connections, it supports VPNs and allows to manage services like DNS, FTP SSH and Telnet servers.

![Haiku R1/beta1 - The new Network preflet]({static}/images/2018/haikur1beta1/haiku_network.png)

There are other improvements that are less noticeable at first glance, but that add up to a better experience overall. You can find more detailed information in the [release notes](https://www.haiku-os.org/get-haiku/release-notes/){:target=_blank}.

At this time, there are still some stability issues in some applications (especially third-party ones), or in certain hardware related features (like Wi-Fi, keyboard layouts, trackpad features, webcams, audio I/O, Bluetooth). There are some features missing (for instance, hardware 3D acceleration, the ability to put the computer to sleep, or to adjust the brightness of the screen), and other features still need improvements. 

Also, the localization to other languages is, naturally, a work in progress. I will try to help on this regard during the next few weeks, contributing as much as I can to expand and improve the Portuguese translation of the Haiku user interface.

I must say, however, that the operating system itself seems to be very stable and usable. The LibreOffice port is very recent and has indeed crashed a few times in my system, but other applications, like Krita or [StyledEdit](https://www.haiku-os.org/docs/userguide/pt_PT/applications/stylededit.html){:target=_blank}, seem to be very solid. There were a few temporary visual glitches in WebPositive or occasional hiccups in certain apps, but the operating system was always responsive. I could easily `kill` any stuck process from the Terminal, and the computer would otherwise keep working happily without needing to reboot. 


# A great opportunity for developers

With regard to development tools, if you want to contribute directly to the Haiku code base or to port or build drivers or applications for it, you will probably need to use C++, especially if you want to work with the native API. You can find a few IDE's in HaikuDepot, like  [Paladin IDE](https://depot.haiku-os.org/#!/pkg/paladin/haikuports/1/4/-/git/4/x86_gcc2?bcguid=bc271-SYVI){target=_blank}, [MonkeyStudio](https://depot.haiku-os.org/#!/pkg/monkeystudio_x86/haikuports/1/9/0.4/-/10/x86_gcc2?bcguid=bc66-JIYB){:target=_blank} and [Qt Creator](https://depot.haiku-os.org/#!/pkg/qt_creator_x86/haikuports/4/7/1/-/1/x86_gcc2?bcguid=bc101-BWRH){:target=_blank} (yes, you can also use [Qt](https://www.qt.io/){:target=_blank} in Haiku), and some powerful text editors, like [Pe](https://depot.haiku-os.org/#!/pkg/pe/haikuports/2/4/5/-/8/x86_gcc2?bcguid=bc184-OLGL){:target=_blank}, [QEmacs](https://depot.haiku-os.org/#!/pkg/qemacs/haikuports/0/4/1/pre20170225/4/x86_gcc2?bcguid=bc384-DETR){:target=_blank}, [Vim](https://depot.haiku-os.org/#!/pkg/vim/haikuports/8/0/1230/-/1/x86_gcc2?bcguid=bc501-YKWR){:target=_blank} or [Koder](https://depot.haiku-os.org/#!/pkg/koder_x86/haikuports/0/4/0/-/1/x86_gcc2?bcguid=bc577-RITP){:target=_blank}. There is also [Yab-IDE](http://yab.orgfree.com/){:target=_blank}, wich allows to develop GUI applications in yab (a BASIC-like programming language) using the [BeAPI](https://www.haiku-os.org/docs/api/){:target=_blank}.

![Haiku R1/beta1 - The Paladin IDE]({static}/images/2018/haikur1beta1/haiku_paladin_ide.png)

The software repository has already a port of Python 3.6, wich is great, but there are still a lot of missing python packages tat require compilation, like Pillow, Pelican, Flask, Numpy or Pandas. You are able to install Requests and SQLalchemy, though. There is no `tkinter`/`ttk` at this time, but I believe that WxPython and PyQT are already available. And it will certainly get better in the future. 

![Haiku R1/beta1 - Python]({static}/images/2018/haikur1beta1/haiku_terminal_python.png)

`pip` seems to work but the process seems to hang after completion, not returning control to the shell. `git` works just fine, as expected, wich is great. If you speak Lua or Perl, you will be happy to know that they are also available in the HaikuPorts repository. 

An operating system under development like Haiku is particularly interesting for software developers, as they get a great opportunity to learn, to achieve and to help building something that other people will find very useful. If you're interested or if you have some experience in C++, you may consider [contributing to the Haiku project](https://www.haiku-os.org/development/){:target=_blank} with your work and expertise. I don't speak C++, but I have heard that the API for this BeOS/Haiku is actually very nice to use.

Even non-programmers who want to join this open source project as voluntary workers may contribute to the Haiku community in many other less technical tasks, like translating the user interface or the [Haiku User Guide](https://www.haiku-os.org/docs/userguide/en/contents.html){:target=_blank} to other languages. 

Haiku may never become a mass-market operating system like Windows, macOS, iOS or Android, but will certainly touch the hearts of many users, just as BeOS did i its time. It has touched mine for sure. Haiku is still in its first beta, and I have already decided it deserves its own SSD partition in my Mac. 

