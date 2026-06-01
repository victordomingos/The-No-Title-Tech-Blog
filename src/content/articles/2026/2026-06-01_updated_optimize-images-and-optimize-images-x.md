Title: Just updated - both Optimize Images and Optimize Images X
Date: 2026-06-01 22:40
Lang: en
Tags: python, images, optimization, cli, GUI, graphical interfaces, web development, tkinter, watchdog, pillow, pil, ui, Windows, macOS, Linux, desktop
Category: News
Slug: updated_optimize-images-and-optimize-images-x-v2
Author: Victor Domingos
Cover: images/2026/optimize-images-updates-june-2026.png
Summary: This release represents a significant milestone for both Optimize Images and Optimize Images X, marking a coordinated step forward in modernization, dependency cleanup, and internal architecture improvements across the ecosystem.

Both packages now support all currently maintained Python versions from Python 3.10 onwards, and are also tested against 3.15 pre-releases, ensuring forward compatibility with upcoming releases.

After several years of incremental releases, both projects are now aligned on a shared 2.0.0 major version. This reflects the introduction of a more clearly defined and documented `optimize-images` public API for programmatic usage, as well as the goal of keeping both tools in sync going forward.

The command-line interface version, Optimize Images v2.0.0, removes outdated dependencies, improves packaging flexibility, and introduces early experimental support for free-threaded Python. Support for Pythonista on iOS has also been discontinued. While it was an excellent environment in its time, it is no longer maintained, and dropping it allows the project to focus on actively supported platforms and modern Python ecosystems.

Meanwhile, the GUI version, Optimize Images X v2.0.0, updates compatibility with the latest Python versions and the new optimize-images package, and improves macOS UI behavior under modern theme configurations. On macOS, when using the Aqua theme, the application now automatically adapts to both light and dark modes.
 
 
<blockquote>
 <strong>Optimize Images v.2.0.0 - 2026-05-26</strong>
<ul> 
   <li> 
     	Removed dependency on piexif, since Pillow supports EXIF metadata 
     	(thanks to varnav@GitHub for the alert on this).
   </li>  
   <li>
   		Refactored some code to make it easier to import optimize-images as a
   package in your python projects, without having to execute the CLI app.
   </li>  
   <li> 
   		Changes in requirements to allow newer versions of Python and dependencies.
   </li>  
   <li> 
   		Removed support for older python versions, keeping only active support
   versions.
   </li>  
   <li> 
   		Initial, experimental support for free threaded python, which seems
   significantly faster (tests and feedback are always very welcome).
   </li>  
   <li> 
   		Removed support for Pythonista/iOS, since it is no longer maintained.
   </li>  
   <li> Added some basic tests.</li>  
</ul> 
</blockquote>


<blockquote>
 <strong>Optimize Images X v.2.0.0 - 2026-06-01</strong>
 <ul> 
   <li> 
     	Bumped dependencies to more recent Python versions (we're trying to support
   officially supperted versions) and the recently revised optimize-images
   v.2.0.0 api.
   </li>  
   <li>
   Better theme management on macOS (buttons were not being correctly displayed
   on macOS using the aqua theme in the latest python versions), including
   toolbar icons, alternate background in the grid rows, and support for dark
   mode using the aqua theme on macOS.
   </li>  
</ul> 
</blockquote>



### Get them now!

Just `pip install` both apps, following the instructions in the docs ([Optimize Images](https://github.com/victordomingos/optimize-images/blob/master/README.md), [Optimize Images X](https://github.com/victordomingos/optimize-images-x/blob/main/README.md)).

