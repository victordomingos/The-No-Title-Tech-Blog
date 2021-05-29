Title: Just updated - both Optimize Images and Optimize Images X
Date: 2021-05-29 19:10
Lang: en
Tags: python, images, optimization, cli, GUI, graphical interfaces, web development, tkinter, watchdog, pillow, pil, ui, Windows, macOS, Linux, desktop
Category: News
Slug: updated_optimize-images-and-optimize-images-x
Author: Victor Domingos
Cover: images/2021/optimize-images-updates-may-2021.png
Summary: This time, we are releasing both Optimize Images and Optimize Images X at the same time. The original CLI version now uses temporary files with in-memory buffers, which prevents unnecessary I/O, and also displays more detailed and more useful version information. Optimize Images X, the GUI version, is now compatible with Python3.7+ and has the ability to open or preview a selected image.
 
 
<blockquote>
 <strong>Optimize Images v.1.5.0 - 2021-04-29</strong>
 <ul>
   <li> Replaced temporary files with in-memory buffers which, at the expense of a
   bit higher RAM usage, prevents unnecessary I/O and may result in faster
   performance when working with slower disks.</li>  
   <li> Added information about the running environment to the -v/--version CLI
   argument, so that you can check which python version is being used, as well
   as some information about required and optional third-party packages.</li>  
   <li> Added a minimum space saving threshold (1% per file). Files are only replaced
   if the space saved is at least 1% of the original file size. Contributed by
   varnav@GitHub.</li>
   <li> Added a check for the presence of the required package Piexif.</li>
   <li> Added new methods intended to allow optimize-images to be imported and used
   as a package. The initial refactoring was kindly contributed by Tharindu N.
   (truethari@GitHub)</li>
   <li> Added custom exceptions to better support the public API.</li>
  </ul>  
</blockquote>


<blockquote>
 <strong>Optimize Images X v.0.9.2 Beta - 2021-04-29</strong>
 <ul>
   <li> Added the ability to open the currently selected image in the system's
   default image viewing application by pressing <Enter> or double-clicking.</li>  
   <li> On macOS, you may also display a QuickLook window by pressing the spacebar.</li>  
   <li> Removed the usage of walrus operator to make it compatible with Python3.7+.</li>   
  </ul>  
</blockquote>



### Get them now!

Just `pip install` both apps, following the instructions in the docs ([Optimize Images](https://github.com/victordomingos/optimize-images/blob/master/README.md), [Optimize Images X](https://github.com/victordomingos/optimize-images-x/blob/main/README.md)).

