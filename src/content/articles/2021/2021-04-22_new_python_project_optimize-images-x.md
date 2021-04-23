Title: New project: Optimize Images X
Date: 2021-04-22 22:00
Lang: en
Tags: python, images, optimization, GUI, graphical interfaces, web development, tkinter, watchdog, pillow, pil, ui, Windows, macOS, Linux, desktop
Category: Programming
Slug: new_python_project_optimize-images-x
Author: Victor Domingos
Cover: images/2021/optimize-images-x.png
Summary: Just for fun, this month I set myself to start a new Python project. It's the same as Optimize Images, but with a big `X` and a nice graphical user interface. It wants to help you reduce the file size of images, and hopefully make your websites load faster. 

Optimize Images X and its CLI companion [optimize-images]({filename}/pages/projects/optimize-images.md) both offer some useful features that are not always present in a single package, like batch downsizing of images within a folder (and recursively though its subfolders) based on specified maximum width and/or height. Just like its CLI companion app, it can process a single file, a folder's root or all images in a folder, recursively. 

Multiple image processing tasks are automatically distributed to all available CPU cores, which means it will compress several images in parallel making use of all available cores or processors to finish the whole set of images faster.

Additionally, it includes a "watch folder" feature that continuously monitors a specified folder for new image files and processes them right after they're created or placed in that folder.


## Some highlights:

 * Easy to use GUI, completely based on Python (Tkinter/ttk).
 * Implements all the features and options currently available on Optimize Images (the original CLI version) for batch image optimization and file size reduction, including:
  	* Optional recursion through subfolders
    * Conversion to grayscale (less color often means smaller file size)
    * Image downscaling based on maximum width and/or height
    * JPEG quality (lossy compression)
    * EXIF data removal
    * PNG transparency removal, with optional background color replacement
    * PNG pallete reduction
    * PNG conversion to JPEG (all, just big images, or none, with optional deletion of the original PNG file)
    * ...and more.
        
 * Uses multiprocessing to take advantage of all available CPU cores (except the "watch folder" feature, since watchdog's API only seems allow threading).
 * Automatic saving of all app and task settings, including main window size and position.
 * Some usage statistics available on the About window.
 * All image and stats are stored and processed locally in your own computers, which means no need for file uploads and no worries with telemetry and other privacy issues.
 * Compatible with some of the most popular desktop operating systems, including macOS, Windows and Linux.
 * It's free (MIT License), please feel free to buy me a coffee, or to contribute with bug fixing or other code improvements if you'd like so.


The first beta is out, on GitHub and on PyPI, but there are still some rough edges to polish before we can call it a proper release. There's some work to do on documentation, UI polish, and testing. Right now, it runs on Python 3.9 in macOS and the PyPI version crashes with honor and misery right after launching. But if you clone the last version from the GitHub repo, it should run mostly fine. 

I also intend to make a few necessary edits to make the 1.0 release fully compatible with previous Python versions (like replacing the cute [walrus := operator](https://www.python.org/dev/peps/pep-0572/){:target=“_blank”}).


You can check out the development repository on GitHub:

* **GitHub Repository: **  [Optimize Images X](https://github.com/victordomingos/optimize-images-x){:target=“_blank”}

If you want to contribute, I will certainly appreciate very much! :)



