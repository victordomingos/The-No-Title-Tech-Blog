Title: How I use Python to blog from my iPhone 
Date: 2018-07-01 01:00
Lang: en
Tags: python, iPhone, iPad, iOS, Pythonista, blogging, workflow, Siri, automation, Siri shortcuts, iOS 12, pelican, static website, static website generator, images, optimization, html, web development
Category: Programming
Slug: how_i_use_python_to_blog_from_iphone
Author: Victor Domingos
Cover: images/2018/python_blog_iphone.jpg
Summary: Over the last 12 years, I have been blogging almost uninterruptedly about different subjects (mostly on tech stuff), on different platforms and using a variety of devices and applications. First on desktop and laptop computers, and more recently from iPhone and iPad. This year I went on to try something new and decided to create this blog based on Pelican, a static site generator made with Python. And I got the whole process working even from my iPhone, which has become, arguably, my main personal computer. So, how do I publish new content to this blog from my iPhone?


## 1. I write each article in Markdown
Markdown is a simple syntax that can be easily translated to HTML (and a bunch of other formats), but only requires a simple text editor and allows us to focus on the content. On my Mac, I tend to use either Ulisses, or BBEdit, or VIM, whatever comes to hand. On iPhone, currently, I use Ulysses, Drafts or Working Copy. I may start with Drafts or Ulysses, then copy to Working Copy and go on from there... 

Pelican only requires that the header contains some standard metadata. Some of it is optional, but I try to always include the same set of fields. Here’s an example of the header I am using for this article:

```
Title: How I use Python to blog from my iPhone 
Date: 2018-07-01 01:00
Lang: en
Tags: python, iPhone, iPad, iOS, Pythonista, blogging, workflow, Siri, automation, Siri shortcuts, iOS 12, pelican, static website, static website generator, images, optimization, html, web development
Category: Programming
Slug: how_i_use_python_to_blog_from_iphone
Author: Victor Domingos
Cover: images/2018/iphone_automation.jpg
Summary: Over the last 12 years, I have been blogging almost uninterruptedly about different subjects (mostly on tech stuff), on different platforms and using a variety of devices and applications. First on desktop and laptop computers, and more recently from iPhone and iPad. This year I went on to try something new and decided to create this blog based on Pelican, a static site generator made with Python. And I got the whole process working even from my iPhone, which has become, arguably, my main personal computer. So, how do I publish new content to this blog from my iPhone?
```

Then I just leave a white line and write the rest of the article below.


## 2. Sync with the cloud, I mean, commit to GitHub 
The source code for this website is hosted as an open source repository on GitHub. It’s a good way to share the experience with other, while keeping track of any changes and having them synced between devices on demand.

I may start on iPhone and commit the changes to GitHub using Working Copy. Then, if I want, I may clone the repo or fetch the changes from iPad or Mac, do some further editing and commit again to GitHub.


## 3. Build the website with Pelican

Usually you will use the shell to type a command like `pelican content/ -s publishconf.py` or `make html`. While on a desktop operating system it is an easy task, on mobile it is less than ideal. So, I created my own building script that I can use in Pythonista to generate all the HTML and image thumbnail files. Actually, I compiled a few scripts that do the whole process – as I want it to be done – just by tapping a few buttons. 

If I need to grab the most current version from GitHub, I run the following code in StaSh:

```
cd ~/Documents/pelican-stuff/
echo “Removing old local repository, if it exists.”
rm -rf ~/Documents/pelican-stuff/The-No-Title-Tech-Blo
echo “Cloning git repository from GitHub...”
git clone https://github.com/victordomingos/The-No-Title-Tech-Blog.git
cd The-No-Title-Tech-Blo
clear
cd src
echo “ “
pwd
echo
ls -l
echo “ “
echo “Done!”
```

Note that I don't need to manually open Pythonista app, then open StaSh in Python 2.7 mode (required here for this `git` command to work properly), then type the path to this script... No. I created a simple workflow that automates all those steps and added an icon to the home screen. I just tap the icon and it downloads all the source files. Then I do the same with another button that calls my `make_html.py` script. One tap and it starts building the site in Pythonista with Pelican:

``` python
#!/usr/bin/env python2
import os

from pelican import Pelican
from pelican.settings import read_settings

print ‘\nReading the publish settings file.\n’
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(os.path.expanduser(‘~/Documents/pelican-stuff/The-No-Title-Tech-Blo/src’))

settings_filepath = os.path.expanduser(dname+’/The-No-Title-Tech-Blo/src/publishconf.py’)
settings = read_settings(settings_filepath)

print ‘Building the website with Pelican...\n’
pelican = Pelican(settings)
pelican.run()
```

##  4. Optimize images
OK, if you follow this blog, you already know I have been exploring ways to automate my image optimization workflow. On my Mac, I like to export my images to PNG or JPEG (the image format will depend on the type of content), in the best suitable size. When possible, I try to offer images in 2x resolution for *Retina* displays. Then I use ImageOptim and JPEGmini to shrink the files.

On iOS, I often use the Workflow app, when I have a picture on my photo library, to resize it and save it as a smaller JPEG. Or to combine 2, 3 or 4 Iphone screenshots into a single image, using just a few taps.

But if I already have all the source images in their folders, after I build the site I do a final optimization step. It's still kind of experimental, but I have another home screen button that runs my  [Optimize Images]({filename}/pages/projects/optimize-images.md) Python application on the Pelican output folder. That way I can squeeze out a few more bytes from the thumbnails generated during the build process.

## 5. Upload using FTP
Yeah, our old and beloved friend, FTP, an old solution that is still simple and efficient enough to keep deserving some usage in the present. The way I do it is by running a Python script that opens an FTP connection to my web server and uploads everything from the output folder:

```
#!/usr/bin/env python3.6
from ftpsync.targets import FsTarget
from ftpsync.ftp_target import FtpTarget
from ftpsync.synchronizers import UploadSynchronizer

from ftpsetupfile import *

print(‘\n\nOpening an FTP connection for the upload...\n’)

local = FsTarget(LOCAL_DIR)
remote = FtpTarget(REMOTE_DIR, REMOTE_HOST, username=FTP_USERNAME, password=FTP_PASSWD)
opts = {“force”: True, “delete_unmatched”: True, “verbose”: 3}

s = UploadSynchronizer(local, remote, opts)
s.run()

print(‘\n\nUpload complete!’)
```

On iOS, of course, it requires a single tap on an home screen icon. It takes a while to upload, depending on the connection speed, so it may be a good idea to do something else while it is working. When it finishes, I usually open Safari and do a final check to see if there way no typo, or a broken link.

## 6. On iOS 12 (currently in public beta) you can do it "hands free" with Siri
On the upcoming iOS 12 operating system, Apple is adding a new feature called Siri Shortcuts, that seem to be an evolution from URL schemes and the Workflow app (in fact, Apple has acquired the company that created Workflow). On the current beta we still don't have the new Shortcuts app, but we do have access to some Siri suggestions of available shortcuts we can set. The trick is to use the Workflow app to create a new workflow for each task (like running a specific Python script in Pythonista), then you run it, and then you should be able to find that workflow action in Siri's suggestions, in Settings. You set a voice command and that's it.

I created four Siri shortcuts for those same four actions for which I had created home screen icons (I could probably reduce this to just one or two steps, but I prefer to go through each stage at a time, in order to see any eventual warnings or error messages):

1. Get latest version from GitHub 
2. Build website
3. Optimize images
4. Upload website

![Setting up a custom Siri Shortcut in iOS 12 beta](ios12_beta_siri_shortcuts.jpg)

So, after I finish writing and preparing images, all it takes is 4 taps on the screen, or 4 voice commands to Siri. The iPhone does the rest of the magic, automatically.

Here is a small video of the whole build and deployment process being done directly from an iPhone 7:

[![iOS  automation - building and deploying a website from an iPhone using Python](http://img.youtube.com/vi/lPGnXdi7jXw/0.jpg)](http://www.youtube.com/watch?v=lPGnXdi7jXw "iOS  automation - building and deploying a website from an iPhone using Python")


## What do you think?
So, if you are also using Pelican and have come up with a better solution for these problems, please [let me know](https://victordomingos.com/contactos/). 
