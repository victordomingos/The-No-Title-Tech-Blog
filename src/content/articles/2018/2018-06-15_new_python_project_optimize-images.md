Title: New project: yet another [almost pure Python] image optimizer
Date: 2018-06-15 9:40
Lang: en
Tags: python, pelican, static website, static website generator, images, optimization, cli, Pythonista, web development
Category: Programming
Slug: new_python_project_optimize-images
Author: Victor Domingos
Cover: images/2018/optimize-images.png
Summary: When you want or need a custom tool and you can’t find it, you have two options: you either buy one (or ask someone to build it for you), or you make your own and do the best you can to make it work for you. This week, I decided to start building my own (almost pure Python) utility to optimize images for the web.



## The problem

As you know, I have been trying to build and publish one of my websites from either my Mac or my iPhone. For that specific website, I write my content in Markdown, and then I use Pelican and a couple of Python and shell scripts to build the static HTML with the correct file and folder structure and, finally, to upload the website through FTP. By using this workflow, I can have my custom-made website, compatible with any server, with fast response times, and still be able make changes at anytime and publish them either from my computer or from my phone. As discussed before, this approach has some important benefits, but it also has its limitations (or, should I say, challenges). One difficulty is that on iOS we are missing a good image optimization app, something like [ImageOptim](https://imageoptim.com/mac){:target="_blank"} (that in turn makes use of several more specific tools) ou [JPEGmini](https://www.jpegmini.com){:target="_blank"}, that apply lossless or lossy image compression to reduce file size without considerably affecting the overall image quality.

A few years ago, there was a nice iOS application called [Reduce](https://www.cultofmac.com/209942/reduce-is-an-awesome-photo-resizer-for-ios/){:target="_blank"} that had a nice interface and could be a good help. Unfortunately it has been discontinued by its author. Besides, none of the currently existing alternatives seems to be good fit my intended workflow.

When I started to set up this Pelican based website, I tried to include some basic performance optimizations, but soon I stumbled with this problem. On Mac, ImageOptim and JPEGmini do nice job, but on iOS there is a very different story. After some thought, I decided to make a [small adjustment]({filename}/articles/2018/2018-04-20_responsive_images_in_pelican.md) in the `pelican-advthumbnailer` plugin, to make it use `Pillow`’s optimization routines while saving image files. It automatically saves a few kilobytes when generating thumbnails, but it is still not a perfect solution. If I create some content directly on iOS and it includes some images that won’t need to be resized by Pelican, they will end up being uploaded without any optimizations.

## optimize-images - my new [almost pure Python] image optimizer

Having done some research, I also couldn’t find a Python-based tool that I liked enough. Some of the existing ones rely heavily on web APIs or on binaries like `pngcrush` or `MozJPEG`, or some non pure Python packages that simply can’t be installed on Pythonista for iOS.

So I started with that little Pillow image optimization bit and I will use it to make a desktop and mobile compatible command-line tool that I can use separately from Pelican to optimize either a single image file or every image files contained in a specified folder. I know that image optimization algorithms are a pretty technical subject, and I certainly won’t be able to come out with a Python implementation of any of the mentioned binary utilities. However I will still try to find out if there is any other kind of optimization that can be done using the Python tools available or installable in Pythonista.

In last resource, if no other qualifying tools can be used, we can add support to one of the web APIs that offer free image compression services. But first, let’s see what can be done locally and offline. 

You can check out the development repository on GitHub:

* **GitHub Repository:**  [optimize-images](https://github.com/victordomingos/optimize-images){:target=“_blank”}

If you have some nice tip and want to contribute, I will certainly appreciate very much! :)



