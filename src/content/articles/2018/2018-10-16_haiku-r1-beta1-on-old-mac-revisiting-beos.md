
Running Haiku R1/beta1 on a decade-old Mac laptop (revisiting BeOS 18 years after its latest release) 

Having experimented and used [BeOS R5 Pro](https://en.wikipedia.org/wiki/BeOS){:target=_blank} back in the early 2000’s, when its company was just going down, I have been following with some interest the development of [Haiku](https://www.haiku-os.org/){:target=_blank} during all these years. While one can argue that the old BeOS and Haiku both miss some important features to be considered modern OSes these days, a lightweight operating system can be, for instance, a good way to bring new life into old, or new but less powerful, hardware. 


## A history of love and hope

Back in 2000, the BeOS operating system was known  for its multiprocessing capabilities and its clean design. I still remember the surprisingly short time it would take to boot in my old computer, with an AMD K6-2 processor at 400MHz, or how most applications would launch almost instantaneously, without the lag I was used to see in Windows 98 or in the most common Linux distributions. I kind of fell in love with it, and have used it as much as I could for some time. There was a notorious lack of compatible software, in many areas, but [Gobe Productive](https://en.wikipedia.org/wiki/Gobe_Software){:target=_blank} and a few other apps were in fact powerfull enough to get a lot of work done.

Then, in 2001, came the news that  Be, Inc. was being sold to Pal, Inc. and soon it was shutting down its operations. BeOS was dead. A lot of its users didn't want to believe it was the end of the line. And the idea of buying the source code back from Palm or even building a completely new BeOS started to gain traction in the community. There were [a few attempts to replicate the BeOS experience](https://en.wikipedia.org/wiki/History_of_Haiku_(operating_system)){:target=_blank}, including one that intended to recreate the BeOS interface on top of a Linux kernel. But the only project that has survived all these years was OpenBeOS, alter renamed as Haiku. The main idea was to create an open-source and backward-compatible replacement for BeOS. It seemed like an impossible mission, but in 2009, about 8 years after the last official BeOS update, the Haiku team released the Haiku R1/Alpha 1, its first public snapshot, that gave former BeOS users a little bit of hope. There were four alpha versions, from 2009 to 2012. And then... an even longer wait period. There was no stable release, no Beta version, not even a new alpha. 

This year, we had some good news. The Haiku team was finaly releasing the first beta of the new BeOS inspired operating system! [Haiku R1/beta 1](https://www.haiku-os.org/news/2018_09_28_haiku_r1_beta1/){:target=_blank} came out in 28 September 2018 and, while the initial idea for Haiku R1 was to replicate as much as possible BeOS R5, it comes with some notable new features that increase it's usefulness and make it a little more likely to please both old and new users.


## Running Haiku R1/beta1 on two decade-old Mac laptops

In fact, I happen to have at home two 10 to 11 years old Mac computers that are still in use, but would benefit from the speed improvement that a lightwight OS could offer. From time to time, I load the latest Haiku alpha or nightly build in VirtualBox just to see how it’s going, but it’s never quite the same as having a native operating system. So, recently, when I heard that the Haiku team was releasing it's first beta, I decided to give it another try. Here is my brief report of how it went.

My first attempt at doing a native intallation was on my MacBook Pro 15” 2.2 GHz (Mid 2007). It was frustrationg to see that it didn't not boot from USB (the same issue I have frequently found when trying to run Linux), and the DVD drive has been replaced by an hard disk drive long time ago. I did several tries using two different USB sticks, an external USB hard disk drive, Etcher and Refind, a FireWire cable, the other MacBook, the install DVD, and I did every procedure that came to my mind using those tools, without success. I was still stuck with VirtualBox. It allowed me to run Haiku in the full screen resolution and with access to the internet, which was positive. However, there was no sound at all and it was very slow, which is perfectly normal when doing virtualization in a 11 years old laptop, but certainly does not give the same nice feel we used to appreciate on BeOS.

Then I decided to pick a MacBook 13” 2.4GHz (Early 2008) that is currently used by a member of my family. it didn't boot from USB, but when I tried to boot from a DVD, I was able to boot the Live CD at full resolution (1280x800x32). I just needed to disable APIC and ACPI during the boot sequence. So, for that MacBook, this is what I was able to get:

- Only one processor core, but sill pretty snappy, when compared with MacOS X 10.7 Lion.
- Does not turn off automatically.
- Seems to be able to record audio using the internal microphone, but apparently there is no audio output.
- No Wi-Fi.
- No iSight câmera.
- Trackpad works, but without secondary button and no scrolling.

At that time, my only hope was that maybe I could get Haiku to work on my MacBook Pro by extracting the SSD and doing the install process externally, using the other MacBook. I had previously promised myself I wouldn’t tear down that laptop ever again, but I was ready to change my mind, for a good reason.

So, after completing a full install in a 20GB partition in the MacBook, I created a similar partition on the Macbook Pro and then started taking out the 23 screws (the hard part, in this case, was keeping track of all the screws). I took the disk out and connected it to the MacBook using a USB enclosure. The install process, done from Haiku, was a breeze and reminded how I used to love the amazingly quick and easy way that BeOS could be installed or migrated to a new different drive or partition. After a few minutes, I placed the SSD and the screws back into their respective places. The ReFind boot manager detected the new Haiku partition and it booted at the first attempt, without having to setup any of those boot time restrictions. Not bad, for a beta:

- Full screen resolution.
- Parcial trackpad support (no right button and no scroll, mouse pointer seems a bit more nervous in this Mac).
- Wifi (detects networks nearby and easily connects to my iPhone’s personal hotspot)
- Detects both processor cores, so its even faster than on the other MacBook.
- It is able to switch completely off when shutting down. 
- Sound recorder displays a graph, similarly to the MacBook, so it seems to be able to use the microphone, but there is no audio output.

I am very happy to see this old computer launching apps much faster than I had ever seen it before. 

As a side note, Haiku R1/beta 1 is available in both 32 and 64 bit versions, and at this time there is no compatibility layer to allow running 32 bit applications under the 64 bit operating system. So, I have chosen the 32 bit version because, at this time, it will probably have more apps available and I read somewhere that is was a bit more stable. I have already seen a few app crashes, but I would say it’s normal in a beta version. Everything, including drivers and many of the the third-party applications are still under development. But hey, it works! In fact, this article is being written on Haiku, just to celebrate the fact that we are able to do so.

## What's new (and what's missing)
