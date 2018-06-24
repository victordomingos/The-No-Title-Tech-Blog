Title: Optimize Images v1.1 – new features
Date: 2018-06-24 18:55
Lang: en
Tags: python, images, optimization, PIL, Pillow, piexif, cli, Pythonista, multiprocessing, multithreading, argparse
Category: Programming
Slug: optimize-images_v1_1_new_features
Author: Victor Domingos
Cover: images/projects/optimize-images.png
Summary: Check out the new release of my image optimization command-line utility, which packed some new features.

Here are some highlights:

 * Added new options to allow downsizing of images to a maximum width and/or height before applying any other optimization (guess what? It really makes a huge difference in file sizes…)
 * Added a new option to keep EXIF data in JPEG images (by default, it will be discarded).
 * Added a new CLI argument to display current version.
 * Added a new CLI argument to display a list of the currently supported image formats.

*If you didn't read my previous article about this project, please feel free to take a quick look at the [full story of its begining]({filename}/articles/2018/2018-06-15_new_python_project_optimize-images.md). If may also want to check the recent [announcement for the first public release]({filename}/articles/2018/2018-06-21_optimize-images_first_public_release.md).*
