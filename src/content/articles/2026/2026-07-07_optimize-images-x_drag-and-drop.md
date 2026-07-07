Title: Optimize Images X now supports WEBP and drag and drop
Date: 2026-07-07 20:00
Lang: en
Tags: python, images, optimization, gui, tkinter, desktop, webp, exif, metadata, drag and drop, pyinstaller, Windows, macOS, Linux
Category: News
Slug: optimize-images-x_drag-and-drop
Author: Victor Domingos
Cover: images/2026/optimize-images-x-v2-1-0.png
Summary: Optimize Images X, the multi-platform desktop application that helps you reduce the file size of your images on macOS, Windows and Linux, has just been updated to version 2.1.0. This new version adds drag-and-drop, conversion to more output formats, including WebP and AVIF, a new image info window with a readable EXIF report, and a PyInstaller spec file for building standalone executables.

You can now drag image files or folders from your file manager straight onto the application window (this requires the optional TkinterDnD2 package; without it, everything keeps working as before). 

A new "Conversion" tab allows converting images to any output format available in your Pillow build — typically JPEG, PNG, WebP, AVIF and JPEG 2000 — and, as usual, the converted file is only kept when it turns out smaller than the original. This feature already existed but has been expanded in this version to support formats other than PNG to JPEG.

![Settings window - conversion]({static}/images/2026/optimize-images-x_settings-conversion.png)

By popular request, `WebP` files are now fully supported, with a dedicated settings tab.

![Settings window - WebP]({static}/images/2026/optimize-images-x_settings-webp.png)

There is also a new image info window: select an image and press Cmd-I (Ctrl-I on other systems) to see its properties, the optimization results and its EXIF metadata. 

![The new Image Info window]({static}/images/2026/optimize-images-x_image-info.png)

And for those who prefer a self-contained application over a Python environment, this release includes a spec file for building a standalone executable for macOS with PyInstaller. In future versions this could be implemented for other operating systems.

Here is the complete changelog for this version:

<blockquote>
 <p><strong>v.2.1.0 - 2026-07-05</strong></p>
 <ul>
   <li>
   		Drag-and-drop support for images and folders (requires TkinterDnD2).
   </li>
   <li>
   		Added a spec file for PyInstaller. Now you can build a standalone
   executable that packages all the dependencies and the application itself,
   using PyInstaller (yay!). Tested on macOS.
   </li>
   <li>
   		Added support for WEBP (using a more recent optimize-images version).
   </li>
   <li>
   		Generalized format conversion: a new "Conversion" tab converts images
   to any output format available in the Pillow build in use (typically JPEG,
   PNG, WebP, AVIF and JPEG2000), with the target chosen from a dropdown
   populated dynamically from the engine. The converted file is kept only when
   it is actually smaller, unless the size comparison is disabled.
   </li>
   <li>
   		Supported input and output formats are now discovered from the
   engine's public API, reflecting the codecs actually present in the Pillow
   build.
   </li>
   <li>
   		Added a dedicated WebP tab (quality, lossless and compression method)
   and moved "Keep EXIF" to the General tab, as it applies to more than one
   format.
   </li>
   <li>
   		Added tooltips to the settings controls and fixed inconsistent
   control fonts.
   </li>
   <li>
   		New image info window: select an image and press Cmd-I (Ctrl-I on
   other systems), or use the File menu, to open a non-modal window with the
   image's properties, the optimization results (size before and after, and
   space saved) and its EXIF metadata, grouped into Image, Camera and GPS
   sections with values shown in a readable form (e.g. f/8, 1/250 s, 50 mm).
   It also reports the colour profile description and the file's creation and
   modification dates. One window per image.
   </li>
   <li>
   		Opening an image now hands the real file to the system's default
   viewer instead of a temporary copy, so the original file is shown. Added
   File menu entries to open the image, to Quick Look it (macOS) and to show
   image info, plus a Finder-style Cmd-Down shortcut on macOS as an alias of
   Enter.
   </li>
   <li>
   		Requires optimize-images >= 2.1.0 (and < 2.2.0).
   </li>
   <li>
   		Minor fixes and improvements.
   </li>
 </ul>
</blockquote>


### Get it now!

Just `pip install optimize-images-x` (or `pip install optimize-images-x[dnd]`, to include the optional drag-and-drop support), following the instructions in the docs ([Optimize Images X](https://github.com/victordomingos/optimize-images-x/blob/master/README.md)).