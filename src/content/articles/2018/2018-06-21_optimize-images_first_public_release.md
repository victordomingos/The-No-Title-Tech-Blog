Title: Optimize Images – check out the first public release!
Date: 2018-06-21 01:22
Lang: en
Tags: python, pelican, static website, static website generator, images, optimization, cli, PIL, Pillow, Pythonista, web development, multiprocessing, multithreading, argparse
Category: Programming
Slug: optimize-images_first_public_release
Author: Victor Domingos
Cover: images/projects/optimize-images.png
Summary: Last week, I told you how I had decided to start building my own (almost pure Python) utility to optimize images for the web. Today I am announcing the first public release of this CLI application. Check it out!

*If you didn't read my previous article about this project, please feel free to take a quick look at the [full story of its begining]({filename}/articles/2018/2018-06-15_new_python_project_optimize-images.md).*

One thing that I really enjoy in Python development is how fast you can go from a first prototype to a working application. Another good thing about it is the fact that you can use it to develop cross-platform applications that may run your Windows PC, in your Mac laptop, in a remote Linux server or even on your iPhone or iPad using Pythonista.

So, a week later, we have a working application (no GUI, just text mode, but it's *by design*, ok?). Comparing this release with one of the first development versions, it's now about 3 to 4 times faster, or even more, mostly thanks to the use of multiprocessing (on desktop operating systems) and multithreading (on mobile). It has more customizable options, like reducing the number of colors for PNG files or choosing the quality percentage for JPEG files. Finally, some extra care has been put into the text output formating, so everytime you run it it will adapt to the current screen width, even on iOS (try turning your device horizontally and run it again).

While it certainly can't compare with other well-established image compression utilities, it can still  be prety handy as a quick one-liner to perform some of those optimizations. This is particularly true when doing web development or web content publishing on iOS, since there are very few tools available for web image optimization, and none that really compares to what you get on desktop. Whether you're using your iPhone or iPad to build and update a static website, or to write and publish posts to a Wordpress blog, image optimization is something you won't want to overlook.

*Bonus Tip: If, like me, you're using Pythonista to build and update a website (based on Pelican, Nikola, or any other tool), you can use the Workflow app (and maybe soon, Siri Shortcuts in iOS 12) to create a home screen shortcut that launches this script and optimizes all the images in your `output` folder in one single step:*

![iPhone Workflow - Optimize Images]({static}/images/2018/iPhone-workflow-optimize-images.jpeg)


You can check out the development repository on GitHub:

* **GitHub Repository:**  [optimize-images](https://github.com/victordomingos/optimize-images){:target=“_blank”}

If you have some cool idea about how to improve this application and want to contribute, I will certainly appreciate very much! :)

