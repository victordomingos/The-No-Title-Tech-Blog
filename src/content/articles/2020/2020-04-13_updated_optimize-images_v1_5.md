Title: Just updated - Optimize Images v1.3.5
Date: 2020-04-13 22:37
Lang: en
Tags: python, images, optimization, PIL, Pillow, piexif, cli, Pythonista, JPEG
Category: News
Slug: updated_optimize-images_v1_5
Author: Victor Domingos
Cover: images/2020/optimize-images_1_5_macos.jpg
Summary: If you are using [Optimize Images]({filename}/pages/projects/optimize-images.md), please notice that it has just been updated to version 1.5, which fixes a bug and adds some support to a JPEG sub-format known as [MPO](https://en.wikipedia.org/wiki/JPEG#JPEG_Multi-Picture_Format){target=:_blank}.

Here is the corresponding change log entry:


<blockquote>
 <strong>v.1.3.5 - 07-04-2020</strong>
 <ul>
   <li> Fixed a small bug in unsupported image format treatment.</li>  
   <li> Added experimental support for MPO images, which are now treated as JPEG  
    image files (if multiple pictures are present in one MPO file, only the first  
    one will be processed).</li>
  </ul>  
</blockquote>


Also, earlier this year, we've released another update that was small enough not to deserve its own mention in a news article:

<blockquote>
 <strong>v.1.3.4 - 19-02-2020</strong>
 <ul>
   <li> Ignore unsupported image formats (contributed by Petro (liashchynskyi@GitHub).</li>
   <li> Added brief instructions (and a script for macOS) for Pillow-SIMD 
    installation, as a faster alternative to Pillow.</li>
  </ul>  
</blockquote>


Regarding this last bit, please notice that the above mentioned script, intended to replace Pillow with [Pillow-SIMD](https://python-pillow.org/pillow-perf/){target=:_blank} on macOS, is currently only available in our GitHub repository. The ability to replace Pillow on you system will depend on its hardware and software. If you are indeed able to swap Pillow with the faster version Pillow-SIMD, you should be able to get a considerably faster speed. Please notice, however, that it usually requires a compilation step and it was not throughly tested by us, so your mileage may vary.

Finally, for those users who have been contributing to this project with feature suggestions, bug reports, or pull requests, thank you very much! It's nice to know that you find this application interesting and useful.


## Get it now!

To install Optimize Images, if you have Python 3.6+ and Pillow, just type `pip3 install optimize-images` on the command-line. More detailed info, including on the required Pillow versions and some iOS specific procedures, is available on the documentation.

So, go ahead and see the updated documentation, which also includes some usage examples, to get you started right away: 
 
 * [English](https://github.com/victordomingos/optimize-images/blob/master/docs/docs_EN.md){target=:_blank}
 * [Portuguese](https://github.com/victordomingos/optimize-images/blob/master/docs/docs_PT.md){target=:_blank}

