Title: Just updated - Optimize Images X v0.9.1 (Beta 2)
Date: 2021-04-25 22:50
Lang: en
Tags: python, images, optimization, GUI, graphical interfaces, web development, tkinter, watchdog, pillow, pil, ui, Windows, macOS, Linux, desktop
Category: News
Slug: updated_optimize-images-x_beta2
Author: Victor Domingos
Cover: images/2021/optimize-images-x_settings_macOS_themes_classic.png
Summary: So, just 3 days after the first public beta, here we got the second beta for [Optimize Images X]({filename}/pages/projects/optimize-images-x.md). It includes an important hot fix for Windows and Linux, and two new usability features.

Here is the corresponding change log entry:


<blockquote>
 <strong>v.0.9.1 beta - 2021-04-25</strong>
 <ul>
   <li> Added the ability to choose a different GUI (ttk) theme.</li>  
   <li> Added a new button to restore all the default settings.</li>  
   <li> Fixed an error that prevented the application to launch on Windows/Linux.</li>
  </ul>  
</blockquote>

When you change the user interface theme, the whole app instantly responds and changes its visual aspect, in real time. Here are some screenshots that show what the new settings tab looks like when using different combinations of operating systems and ttk themes:

### Linux

![Optimize Images X on Linux Ubuntu 20.04 - default theme]({static}/images/2021/optimize-images-x_settings_linux_themes_default.png)


### macOS

![Optimize Images X on Linux Ubuntu 20.04 - aqua theme]({static}/images/2021/optimize-images-x_settings_macOS_themes_aqua.png)

![Optimize Images X on Linux Ubuntu 20.04 - classic theme]({static}/images/2021/optimize-images-x_settings_macOS_themes_classic.png)


### Windows

![Optimize Images X on Linux Ubuntu 20.04 - clam theme]({static}/images/2021/optimize-images-x_settings_windows_themes_clam.png)

![Optimize Images X on Linux Ubuntu 20.04 - vista theme]({static}/images/2021/optimize-images-x_settings_windows_themes_vista.png)

You get the idea. If you are fond of retro styles, tkinter/ttk can surely contribute to set a fun and nostalgic mood.

There are still some rough edges, but the application is already pretty much usable. It still needs to get properly packaged as an easy to install application. Right now, you can run it, basically, if you're a Python developer and know how to use `pip`. I am not sure yet if [PyInstaller](https://www.pyinstaller.org){:target=“_blank”} can do the trick for this one, considering its use of tkinter/ttk, Pillow and watchdog, but I will be looking into that in a few weeks, unless someone who knows how to do it decides shows up with a pull request.


## Get it now!

To install Optimize Images X, if you have Python 3.9+, just type `python3.9 -m pip install optimize-images-x` on the command-line. The documentation is still incomplete with regards to the install process, and should be updated soon with further information.

