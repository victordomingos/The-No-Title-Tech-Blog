Title: Just updated - Optimize Images v1.4.0
Date: 2020-11-01 23:41
Lang: en
Tags: python, images, optimization, PIL, Pillow, piexif, cli, Pythonista, JPEG, PNG, watchdog
Category: News
Slug: updated_optimize-images_v1_4_0
Author: Victor Domingos
Cover: images/2020/optimize-images_1_4_0_macos_watch_directory.jpg
Summary: [Optimize Images]({filename}/pages/projects/optimize-images.md) has a new version just released on [PyPI](https://pypi.org/project/optimize-images/){target=:_blank}! Besides the usual clean and polish, this release includes two new features that may be of interest for you, especially if you are using this utility on servers. 

The first one is a new `--watch-directory` (or the more abbreviated form `-wd`), which puts the application in a *listening mode*, waiting for newly created files in a given folder - any new files are immediately processed, continuously, until you press CTRL-C to exit the application. For now, it runs a single process at a time, so please be aware that in most cases it will take longer to process an equal number of images. It also adds a third-party dependency ([Watchdog](https://github.com/gorakhargosh/watchdog){target=:_blank}), which is considered optional, since it is only required for this new feature.

The other feature is a smaller one, but still important for some use cases. If are running Optimize Images in a shared system, where you would prefer not to let it use all the available processor cores, spanning a large number of processes, you can now specify the maximum number of simultaneous tasks or processes with the command-line argument `-jobs`. This way you can reserve some CPU power for other applications or for other users.

We are also bumping the minimum requirements to Python 3.7+ and the Pillow version, in order to make it a little easier to perform some pre-release cross-testing. If you are still on Python 3.6 or using an older version of Pillow, and you can't upgrade those yet,  please submit a pull request and let us know. While we haven't tested Optimize Images on Python 3.6, it will most likely run just fine, but there could be some unexpected (and untested) glitches.

Thank you for using Optimize Images and/or contributing with feature suggestions, bug reports, or pull requests! 


Here is the corresponding change log entry:


<blockquote>
 <strong>v.1.4.0 - 2020-11-01</strong>
 <ul>
   <li> New feature: watch a directory for changes and optimize any new image file as soon as it is created (no multiprocessing for now, sorry). This feature is not compatible with Pythonista for iOS, since it requires a third-party package called Watchdog, which is currently not available on Pythonista).
   <li>Long running tasks, like optimizing recursively a folder containing a large number of image files, or watching for new files a a directory, can now be interrupted by the user with CTRL+C. Instead of an ugly traceback, the final report is presented with the usual statistics for the images that were processed.
   <li> Added the ability to specify the number of tasks to run simultaneously, so that you can optionally limit the number of processor cores being used by this application and keep in reserve some CPU power for any other tasks.  
  </ul>  
</blockquote>




## Get it now!

To install Optimize Images, if you have Python 3.7+ and Pillow or Pillow-SIMD, just type `python3.9 -m pip install optimize-images` on the command-line. More detailed info, including on the required Pillow versions and some iOS specific procedures, is available on the documentation ([English](https://github.com/victordomingos/optimize-images/blob/master/docs/docs_EN.md){target=:_blank}, [Portuguese](https://github.com/victordomingos/optimize-images/blob/master/docs/docs_PT.md){target=:_blank}).

