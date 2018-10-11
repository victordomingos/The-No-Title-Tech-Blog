Title: Optimize Images v1.3 – Dynamic by default
Date: 2018-10-10 23:30
Lang: en
Tags: python, images, optimization, PIL, Pillow, piexif, cli, Pythonista, multiprocessing, multithreading, argparse
Category: Programming
Slug: optimize-images_v1_3_dynamic_by_default
Author: Victor Domingos
Cover: images/2018/optimize-images_v1.1_screenshots.jpg
Summary: In this new release, Optimize Images will, by default, try to determine dynamically the best quality setting for each JPEG image.

Up until now Optimize Images would, by default, apply a fixed 80 value for the JPEG quality or compression level. Now, it's dynamic by default. It will test with a few settings between 75 and 80 and try to determine the best one for each image, trying to squeeze a few kilobytes more without adding a lot more visual artifacts. Hopefully, it will allow for smaller files sizes and almost the same image quality.

In case you still prefer to set a static value for JPEG quality, you still can use the `-q` argument and specify the value you want (the old default was 80). Also, if you just want it to run as fast as possible, now the `-f`/`--fast-mode` argument also disables this dynamic/variable JPEG setting.

## How it works

The implemented algorithm for image comparison is based, I believe, on the [Sum of Absolute Differences](https://en.wikipedia.org/wiki/Sum_of_absolute_differences){target=:_blank}. While there may be more advanced perceptual comparison algorithms, like [SSIM](https://en.wikipedia.org/wiki/Structural_similarity){target=:_blank}, they usually either are more CPU intensive, or require packages that can't be used on Pythonista. So, to keep compatibility with iOS, I am opting for this method.

Basically, I started from an idea [first exposed by Stephen Arthur](https://engineeringblog.yelp.com/2017/06/making-photos-smaller.html){:target=_blank}, a software engineer at Yelp. I tried to adapt and replicate his approach, but I soon discovered the available implementations of SSIM couldn't run on Pythonista for iOS, because they relied on binary packages like SciPy. I have been researching for alternative image comparison algorithms that would require only Python and packages available for iOS/Pythonista, like Pillow and NumPy. After trying a few options, I have decided to use a Pillow-based implementation that is relatively fast and seems to do the job. I adapted a small piece of code from Nicolas Hahn's [diffimg](https://github.com/nicolashahn/diffimg/blob/master/diffimg/__init__.py){target=:_blank} and combined it with Stephen Arthur's variable quality approach. The image comparison snippet, which kind of replaces [PySSIM](https://github.com/jterrace/pyssim){target=:_blank} is quite simple:

```python3

def compare_images(img1, img2):
    # Don't compare if images are of different modes or different sizes.
    if (img1.mode != img2.mode) \
            or (img1.size != img2.size) \
            or (img1.getbands() != img2.getbands()):
        return None

    # Generate diff image in memory.
    diff_img = ImageChops.difference(img1, img2)

    # Calculate difference as a ratio.
    stat = ImageStat.Stat(diff_img)
    diff_ratio = sum(stat.mean) / (len(stat.mean) * 255)
    return diff_ratio * 100
```

It takes two `PIL.Image` objects and returns a difference ratio as a percentage. This function is used to quickly compare the original image saved at a standard 95 quality setting (i.e., the highest JPEG quality level) with the same image saved at 75-80 quality. Since this comparison yields different ratios than SSIM, I adjusted the ratio goal to get some variation.

To speed up things, Stephen Arthur has found that using smaller resolution images allowed a faster processing without much impact in the overall reliability. So, I decided to keep his original approach of comparing 400x400px thumbnails. Yet, I have chosen to use a distinct range of quality levels, instead of the proposed 80-85. I had chosen before 80 as the default quality setting. So, in this version it also starts, by default, at 80 (the old default), and then it tries to further reduce the value and checks, at each step, if there was a big impact on image quality. If the diff ratio overlaps the goal, the last quality setting is applied in the full image.

When using this dynamic algorithm, JPEG quality varies between 80 and 75, which in most cases results in reasonable quality images. Since the increase in processing time ended up being smaller than I had expected, I decided to make it dynamic by default. You may still, however, opt for a static quality value. You just need to use `-q 80` as an argument, you will have the old static behaviour with the previous default quality setting.


## Get it now!

To install Optimize Images, if you have Python 3.6+ and Pillow, just type `pip3 install optimize-images` on the command-line. More detailed info, including on the required Pillow versions and some iOS specific procedures, is available on the documentation.

So, go ahead and see the updated documentation, which also includes some usage examples, to get you started right away: 
 
 * [English](https://github.com/victordomingos/optimize-images/blob/master/docs/docs_EN.md){target=:_blank}
 * [Portuguese](https://github.com/victordomingos/optimize-images/blob/master/docs/docs_PT.md){target=:_blank}

