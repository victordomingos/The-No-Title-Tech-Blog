Title: Optimize Images v1.3 – Dynamic by default
Date: 2018-10-10 19:00
Lang: en
Tags: python, images, optimization, PIL, Pillow, piexif, cli, Pythonista, multiprocessing, multithreading, argparse
Category: Programming
Slug: optimize-images_v1_3_dynamic_by_default
Author: Victor Domingos
Cover: images/2018/optimize-images_v1.1_screenshots.jpg
Summary: In this new release, Optimize Images will, by default, try to determine dynamically the best quality setting for each JPEG image.

Up until now, by default, Optimize Images would apply a fixed 80 value for the JPEG quality or compression level. Now, it's dynamic by default. It willtest with a few settings between 75 and 80 and try to determine the best one for each image, trying to squeeze a few kilobytes more without adding a lot more visual artifacts. Hopefully, it will allow for smaller files sizes and almost the same image quality. 

In case you still prefer to set a static value for JPEG quality, you still can use the `-q` argument and specify the value you want (the old default was 80). Also, if you just want it to run as fast as possible, now the `-f`/`--fast-mode` argument also disables this dynamic/variable JPEG setting.

The implemented algorithm for image comparison  is based on a the Sum of Absolute Differences. While there may be more advanced perceptual comparison algorithms, like SSIM, they usually either are more CPU intensive, or require packages that can't be used on Pythonista. So, to keep compatibility with iOS, I am opting for this method. If you are curious about it, and want to know more about how it's done and where these ideas came from, I have included a few reference URL's in the source code.

To install it, if you have Python 3.6+ and Pillow, just type `pip3 install optimize-images` on the command-line. More detailed info, including on the required Pillow versions and some iOS specific procedures, is available on the documentation.

So, go ahead and see the updated documentation, which also includes some usage examples, to get you started right away: 
 
 * [English](https://github.com/victordomingos/optimize-images/blob/master/docs/docs_EN.md){target=:_blank}
 * [Portuguese](https://github.com/victordomingos/optimize-images/blob/master/docs/docs_PT.md){target=:_blank}

