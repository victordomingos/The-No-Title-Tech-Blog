# pelican-minify

An HTML minification plugin for
[Pelican](http://pelican.readthedocs.org/en/latest/), the static site generator.

This one works with Python3 and the latest Pelican version (4.1.2, as of writing this).

![Pelican Logo](https://github.com/PhasecoreX/pelican-minify/raw/master/pelican.png)

## Install

Clone this repo into a plugin folder (`other-plugins` folder, in this case):

``` bash
cd folder-that-pelicanconf.py-is-in
mkdir -p other-plugins
cd other-plugins
git clone https://github.com/PhasecoreX/pelican-minify.git
```

Then point your `pelicanconf.py` at that folder :

``` python
# pelicanconf.py

# ...

PLUGIN_PATHS = [
    # ...
    "other-plugins"
    # ...
]

# ...
```


## Usage

To use `pelican-minify`, add it to your `PLUGINS` global near or at the end of the list.
If you are using `gzip_cache`, make sure that is after `pelican-minify`:

``` python
# pelicanconf.py

# ...

PLUGINS = [
    # ...
    'pelican-minify',
    'gzip_cache'
]

# ...
```

The next time you build your Pelican site, `pelican-minify` will automatically
minify your Pelican pages after they've been generated.

`pelican-minify` can also be configured by setting `MINIFY` to a hash containing
[parameters to htmlmin](https://htmlmin.readthedocs.org/en/latest/reference.html#htmlmin.minify), eg:

``` python
# pelicanconf.py

# ...

MINIFY = {
    "remove_comments": True,
    "reduce_boolean_attributes": True
}

# ...
```

This reduces file size and obscures the public source code, but keep in
mind--minifying your static site will increase your Pelican build times, as it
adds extra file processing for each page generated.

**NOTE**: You should probably include the `minify` plugin at the very end of
your `PLUGINS` array, but still in front of `gzip_cache` if you are using it.
This will ensure it is the last thing to run, just before the results are gzipped.


## Changelog

v0.1: 12-04-2012

    - First release!

v0.2: 02-12-2013

    - Fixing issue with unicode characters.
    - Upgrading django-htmlmin dependency.

v0.3: 02-12-2013

    - Fixing tests.

v0.4: 02-15-2013

    - Upgrading django-htmlmin.

v0.5: 08-28-2014

    - Python 3 compatibility (thanks @AlexJF!).

v0.6: 09-09-2014

    - Fixing unicode bug (thanks @kura!).

v0.7: 11-04-2014

    - Making minification work on .htm files (thanks @Undeterminant!).

v0.8: 5-12-2015

    - No longer removing optional quotes from HTML elements. This provides
      better compatibility across browsers / etc.

v0.9: 11-25-2015

    - Making minify library configurable.
    - Removing aggressive whitespace removal (*avoids issues*).

v1.0: 10-01-2019

    - Make it work with Python3 and Pelican4
