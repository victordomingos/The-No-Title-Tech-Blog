Title: Optimize Images v1.2 – new features and finally available on PyPI!
Date: 2018-08-27 23:25
Lang: en
Tags: python, images, optimization, PIL, Pillow, piexif, cli, Pythonista, multiprocessing, multithreading, argparse, pypi
Category: News
Slug: optimize-images_v1_2_available_on_pypi
Author: Victor Domingos
Cover: images/2018/optimize-images_v1.1_screenshots.jpg
Summary: The new release of my image optimization command-line utility is out. It has a couple of cool new features and, for the first time, it is now available on PyPI, which means you can just `pip install` it as any other Python package.    

Here are some highlights:

 * A new big feature: "convert big PNG files to JPG format", with an option to convert **all ** PNG files.
 * Added a new option to set background color while doing any PNG operations
that remove transparency (convert big and reduce colors). The background color can be set using both numeric RGB values or in hexadecimal mode (like in HTML).
 * Added an option to convert images to grayscale.
 * Added an option to ignore file size comparison between original and
processed files, allowing to always save anyway the processed version.
 * Added a new palette rebuild step for indexed color images (creates images that
may then be compressed more efficiently using other tools).
 * Refactored module into a full package and created the setup.py file.
 * Added Portuguese version of the documentation.
 * It's now available on PyPI.org: just `pip install` it! 😉


To install it, if you have Python 3.6+ and Pillow, just type `pip3 install optimize-images` on the command-line. More detailed info, including on the required Pillow versions and some iOS specific procedures, is available on the documentation.

So, go ahead and see the updated documentation, which also includes some usage examples, to get you started right away: 
 
 * [English](https://github.com/victordomingos/optimize-images/blob/master/docs/docs_EN.md){target=:_blank}
 * [Portuguese](https://github.com/victordomingos/optimize-images/blob/master/docs/docs_PT.md){target=:_blank}



*If you didn't read my previous article about this project, please feel free to take a quick look at the [full story of its begining]({filename}/articles/2018/2018-06-15_new_python_project_optimize-images.md). If may also want to check the recent [announcement for the first public release]({filename}/articles/2018/2018-06-21_optimize-images_first_public_release.md).*
