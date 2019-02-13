Title: Why and how I have just redesigned my (other) website
Date: 2019-02-12 23:15
Lang: en
Tags: new year, life, work, pelican, static website, static website generator, images, optimization, HTML, web development, Python, iPhone, iPad, iOS, Pythonista, blogging, pelican, static website, static website generator, optimization, HTML, CSS
Category: Programming
Slug: new_website
Author: Victor Domingos
Cover: images/2019/new_website_haiku.jpg
Summary: Going through a moment of change in my life, I have decided to redesign [my other website](https://victordomingos.com/){:target=blank}, using Pelican and other open source tools. The older version was starting to look a bit aged, especially on mobile devices, so it seemed like a good idea to start a complete makeover. As they use to say, *new year... new website*.


### Why I decided to redesign the website and why I wanted to choose other tools

It goes back to 2011, when I built the first version of my personal website. At the time, I already had an unused [RapidWeaver](https://www.realmacsoftware.com/rapidweaver/){:target=blank} license, and after experimenting a little with it, it seemed to me like an easy way to build a nice looking website by using one of the built-in themes. 

But soon I would start noticing some of its shortcomings. The first one was that at that time most themes weren't responsive and didn't fit very well on small screens, like an iPhone. So, in 2014, I started using the [Solstice RapidWeaver Theme](https://themeflood.com/solstice/){:target=blank}, by a developer named Will Woodgate, who, by the way, has always provided timely updates and very helpful technical support. That new theme was responsive, it had some interesting new features and a fresher look. At that time I was complementing RapidWeaver's built-in features with that theme, and a few third-party plugins, like [Stacks](https://yourhead.com/stacks/){:target=blank}, [Animagic](https://elixirgraphics.com/plugins/animagic){:target=blank}, [Slot Machine](https://docs.joeworkman.net/rapidweaver/stacks/slot-machine){:target=blank}, [SiteMap](http://www.yourhead.com/sitemap){:target=blank}, [FaqMaker](http://yourhead.com/faqmaker){:target=blank}, [PlusKit](http://yourhead.com/pluskit){:target=blank} and a few more.

![RapidWeaver 7]({static}/images/2019/rapidweaver7.jpg)

But then, the years go by and technology always changes rapidly. RapidWeaver and its quite large third-party ecosystem is still on active development, with new versions being released every couple years. If you want to be on the cutting edge, you need to get the new version, and make sure you have licenses for the latest version of all the plugins and stacks. And, eventually, you may find out you also need to buy a new computer to be able to run a newer version of RapidWeaver. What was once a simple solution can sooner or later become an undesired expense, amounting to more than you may be willing to pay.

This is not to say that RapidWeaver isn't cool anymore. It is still a very nice software, especially if you prefer a [WYSIWYG](https://en.wikipedia.org/wiki/WYSIWYG) interface and you manage to get a lower price in a software bundle, and it has an ecosystem that includes some very ingenious and talented third-party developers. It really makes it easy to build some very good-looking websites, but it also gets you stuck on that platform: you can only use a Mac computer, you can only use a computer that has RapidWeaver and all the needed themes and plugins, you can't easily update your website on the go, whenever you're away from your Mac, you can't easily customize the themes and templates, and eventually you will need to buy new software licenses and new themes.


### My new toolset

If you have been following this blog, you already know I am both a Python fan and a [Pelican](https://docs.getpelican.com/){:target=blank} user. I have been using Pelican since the creation of [The No-Title Tech Blog](https://no-title.victordomingos.com), about a year ago. It works fine, with what appears to be the right doses of *keep-it-simple* and *fiddle-a-bit-until-it-works-as-you-want-it*. And, most importantly, it results in a highly portable web development platform, with very low system requirements, both on the local development environment and on the remote server. I can write and update the website from anywhere, provided I have access to GitHub and Python. I can work both online and offline if I need so. I even managed to [get the whole thing working from Pythonista on iOS]({filename}/articles/2018/2018-07-01_how_i_use_python_to_blog_from_iphone.md). 

So, naturally, since my needs for the other website were basically the same, I decided to rebuild it using Pelican. I chose the open source [Pelican-Hyde](https://github.com/jvanz/pelican-hyde){:target=blank} theme, by [José Guilherme Vanz](https://jvanz.com){:target=blank} and did some CSS and template customization, making sure the website was easily browseable on different screen sizes. I adapted some of the stuff I already had (like the Pelican settings files, and the Python and shell scripts used for the build and deployment processes), and I set up a new GitHub repository. This allows for easy source code backup and version control, but it is also useful to sync the source files between devices.

Then came the hardest part: migrating blog articles and pages — this was a pain, because I had no easy way to automate it (that's why I now prefer to use a platform that is based on simple and open file formats), and I wanted all the articles and pages to be properly configured to use the features provided by Pelican. Of course, I also had to redesign all the static pages to fit the new theme and to compensate for the lack of some RapidWeaver plugins and stacks. For instance the new HTML/CSS book download buttons, or the related articles/books you can find at the bottom of some pages. The new related articles box, that automatically updates itself based in the articles' tags, is far superior to the old Slot Machine + PlusKit combo, which required a manual include for each article and only allowed to select randomly from a list of a few manually inserted entries.

![Pelican being used alongside Koder in Haiku]({static}/images/2019/pelican_koder_haiku.png)

I also decided to adapt the existing PHP-based [contact form](https://victordomingos.com/info/contactos.php){:target=blank}, just by restyling it and making sure it worked again inside the new website. 

Finaly, I took the opportunity to extend the [biography](https://victordomingos.com/info/biografia.html){:target=blank} page and eliminated some less important content pages.

During the process, I dedicated some care on optimization, trying to keep the site as fast and lightweight as possible, without compromising the way it appears on high-resolution screens. There are a few additional steps that could be done to further reduce page load times. Some of them, however, are made a bit complicated by the way Pelican and some plugins handle certain HTML tags (e.g., the <tt>picture</tt> element). I was able to reduce by half the overall bandwidth required by the main page and to reduce by 30% the number of requests, which has clearly resulted in faster load times.

![GTMetrix]({static}/images/2019/gtmetrix_optimization_history.png)


Beyond the better overall price (I am now using free, open source software), now I have a toolset for this website that is device independent. Just like I had experimented with The No-Title Tech Blog, I can now use any operating system, including macOS, Windows, Linux, Haiku or even iOS, to build and deploy that website. I can even use an iPhone or iPad to update it or to fix something on it at any time. I can now be sure that if, at any time, I decide to replace my current computer, it will be fairly easy and very quick to start using it to update my website. With no additional software costs, which is a nice plus.

The contents are also more isolated from the technical stuff, in Markdown text files, so whenever I decide it's time to move away from this Pelican setup, it will certainly be a much easier task.

Oh, and in the process, I also got the opportunity to learn something new on CSS, and you already know how I like to learn stuff...
