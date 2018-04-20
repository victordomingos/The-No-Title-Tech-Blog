Title: Serving responsive and optimized images in a Pelican static website 
Date: 2018-04-20 20:00
Lang: en
Tags: pelican, static website, images, optimization, responsive
Category: Programming
Slug: responsive_images_in_pelican
Author: Victor Domingos
Cover: 
Status: draft
Summary: Making this website load fast while looking good is one of my goals. And making sure that high resolution images don't weight more that necessary is not that easy, when you're writing your content in Markdown...


### The problem
Well, in fact there are two separate problems here: 

1. automating the image resizing and optimization process;
2. serving the correct image size for each device.

Let's talk about each one separately...

### Automatic image resizing and optimization in Pelican

Using the [pelican-advthumbnailer plugin](https://github.com/AlexJF/pelican-advthumbnailer){:target="_blank"}, by Alexandre Fonseca, it's pretty easy to generate thumbnails inside Jinja2 templates that are part of the theme being used. This is the line that generates the thumbnails for the blog index page:
````
<img class="article_list_img" src="{{ SITEURL}}/{{ article.cover | thumbnail("400x_") }}" width="100%"/>
````



### Serving the correct image size for each device in Pelican



### Have a better idea?
So, if you are also using Pelican and have come up with better solution for these problems, please [let me know](https://victordomingos.com/contactos/). 