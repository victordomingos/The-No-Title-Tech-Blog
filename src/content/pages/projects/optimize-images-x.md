Title: Optimize Images X
Slug: optimize-images-x
Lang: en
Status: hidden
Cover: images/projects/optimize-images-x.png

![Optimize Images X]({static}/images/projects/optimize-images-x.png)

A desktop app written in Python, that exposes and unlocks the full power of Optimize Images in a nice graphical user interface, to help you reduce the file size of images. 

Optimize Images X and its CLI companion optimize-images offer some useful features that are not always present in a single package, like batch downsizing of images within a folder (and recursively though its subfolders) based on specified maximum width and/or height. Just like its CLI companion app, it can process a single file, a folder's root or all images in a folder, recursively. 

Multiple image processing tasks are automatically distributed to all available CPU cores, which means it will compress several images in parallel making use of all available cores or processors to finish the whole set of images faster.

Additionally, it includes a "watch folder" feature that continuously monitors a specified folder for new image files and processes them right after they're created or placed in that folder.


## Some highlights:

 * Easy to use GUI, completely based on Python (Tkinter/ttk).
 * Implements all the features and options currently available on Optimize
   Images (the original CLI version) for batch image optimization and file size
   reduction, including:
  	* Optional recursion through subfolders
    * Conversion to grayscale (less color often means smaller file size)
    * Image downscaling based on maximum width and/or height
    * JPEG quality (lossy compression)
    * EXIF data removal
    * PNG transparency removal, with optional background color replacement
    * PNG pallete reduction
    * PNG conversion to JPEG (all, just big images, or none, with optional
      deletion of the original PNG file)
    * ...and more.
        
 * Uses multiprocessing to take advantage of all available CPU cores (except the
   "watch folder" feature, since watchdog's API only seems allow threading).
 * Automatic saving of all app and task settings, including main window size and
   position.
 * Some usage statistics available on the About window.
 * All image and stats are stored and processed locally in your own computers,
   which means no need for file uploads and no worries with telemetry and other 
   privacy issues.
 * Compatible with some of the most popular desktop operating systems, including
   macOS, Windows and Linux.
 * It's free (MIT License), please feel free to buy me a coffee, or to
   contribute with bug fixing or other code improvements if you'd like so.


If you were just looking for the original (and slightly faster) command-line user interface (CLI) version of this application, it's a separate project: 
[Optimize Images]({filename}/pages/projects/optimize-images.md).

___

**Main toolset: ** [Python 3.9+](https://www.python.org){target=:_blank},  [SQLite](https://www.sqlite.org/about.html){target=:_blank}, [tkinter](https://docs.python.org/3.10/library/tkinter.html){target=:_blank}, [ttk](https://docs.python.org/3.10/library/tkinter.ttk.html#module-tkinter.ttk){target=:_blank}, [Pillow](https://python-pillow.org/){target=:_blank}, [Watchdog](https://github.com/gorakhargosh/watchdog){target=:_blank}, [Optimize Images]({filename}/pages/projects/optimize-images.md)    
**Source code: ** [**Fork it on GitHub**](https://github.com/victordomingos/optimize-images-x){target=:_blank}

