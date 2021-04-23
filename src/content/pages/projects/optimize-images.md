Title: Optimize Images
Slug: optimize-images
Lang: en
Status: hidden
Cover: images/projects/optimize-images.png

![Optimize Images]({static}/images/projects/optimize-images.svg)

A command-line interface (CLI) utility written in (almost) pure Python to help you reduce the file size of images.

You must explicitly pass it a path to the source image file or to the directory containing the image files to be processed. By default, it will go through all of its subdirectories and try to optimize the images found. You may however choose to process the specified directory only, without recursion.

This application is intended to be pure Python, with no special dependencies besides Pillow, therefore ensuring compatibility with a wide range of systems, including iPhones and iPads running Pythonista 3. If you don't have the need for such a strict dependency management, you will certainly be better served by any several other image optimization utilities that are based on some well known external binaries.

While it certainly can't compare with other well-established image compression utilities, it can still  be prety handy as a quick one-liner to perform some of those optimizations. This is particularly true when doing web development or web content publishing on iOS, since there are very few tools available for web image optimization, and none that really compares to what you get on desktop. Whether you're using your iPhone or iPad to build and update a static website, or to write and publish posts to a Wordpress blog, image optimization is something you won't want to overlook.

Despite the limitations imposed by the scope of this project (keeping compatibility with iOS), there are some nice aspects to it, like for instance the ability to automatically adjust its operation to the device being used. Some extra care has been put into the text output formating, so everytime you run it it will adapt to the current screen width, even on iOS (try to turn your device horizontally and run it again). On iOS, you will benefit from multithreading, which provides a good performance, but on a regular computer it will compress several images in parallel making use of all available cores or processors to finish the whole set of images faster.

*Bonus Tip: If, like me, you're using Pythonista to build and update a website (based on Pelican, Nikola, or any other tool), you can use the Workflow app (and maybe soon, Siri Shortcuts in iOS 12) to create a home screen shortcut that launches this script and optimizes all the images in your `output` folder in one single step.*


Want to know more about this project? Check out its [full story of its begining]({filename}/articles/2018/2018-06-15_new_python_project_optimize-images.md)  in the blog.

If you were just looking for the graphical user interface (GUI) version of this application, it's a separate project:  [Optimize Images X]({filename}/pages/projects/optimize-images-x.md) .

___

**Current Status: <span style="color:green">stable</span>**  
**Main toolset: ** [Python 3.7+](https://www.python.org){target=:_blank}, [Pillow](http://python-pillow.org/){target=:_blank}, [Watchdog](https://github.com/gorakhargosh/watchdog){target=:_blank}, [Pythonista 3](http://omz-software.com/pythonista/){target=:_blank}    
**Source code: ** [**Fork it on GitHub**](https://github.com/victordomingos/optimize-images){target=:_blank}

