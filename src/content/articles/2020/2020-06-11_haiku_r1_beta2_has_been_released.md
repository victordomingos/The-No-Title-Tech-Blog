Title: Haiku R1/beta2 has been released
Date: 2020-06-11 20:00
Lang: en
Tags: haiku, beos, operating systems, python, open source, beta, review
Category: News
Slug: haiku_r1_beta2_has_been_released
Author: Victor Domingos
Cover: images/2020/haikur1beta2/haiku.jpg
Summary: 


## A long history of love, sorrow and hope


![BeOS R5 Pro]({static}/images/2018/haikur1beta1/beos_screenshot.jpg)










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

