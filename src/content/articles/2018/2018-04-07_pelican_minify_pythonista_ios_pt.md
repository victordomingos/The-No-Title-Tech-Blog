Title: Enabling the pelican-minify plugin in Pythonista (iOS)
Date: 2018-04-07 09:20
Lang: pt
Tags: pelican, minify, Python, plugins, debugging, iOS, Pythonista, web development, static site generator
Category: Programming
Slug: pelican_minify_pythonista_iOS
Author: Victor Domingos
Cover: images/2018/pelican_logo.png
Summary: When I started this blog, I had a few technical requirements in mind. First of all, I wanted the whole static website build process to be based on Python and to be reproducible both on desktop and on iOS. So, I was very glad to find out I was able to `pip install pelican` and a few of its dependencies in Pythonista, using StaSh, and get my iPhone to process a bunch of Markdown formatted text files. But then I went on to add features and optimizations that required Pelican plugins. And soon I would get into trouble...


I decided not to use plugins that depended on executable binaries, since I wanted to keep my pipeline compatible with Pythonista. So, I had to read through the documentation and requirements files for each one and eventually decided to skip some that otherwise would be nice to use, like some image optimization automations.

When investigating website performance, I intended to include code 'minification', a process that compresses the HTML (and/or JavaScript + CSS) and shortens the time needed to download the pages. There are Pelican plugins available for that purpose, and I found `pelican-minify`, that didn't use any external binaries. To keep Pythonista compatibility, I needed that pure-pythoness. However, things started to get a bit complicated.

I got some tracebacks like this in Pythonista:

```pytb
Traceback (most recent call last):
  File "/private/var/mobile/Containers/Shared/AppGroup/F3C0E711-6D38-4FDF-81F2-DC3B97E4E9F1/Pythonista3/Documents/pelican-stuff/make_html.py", line 15, in <module>
    pelican.run()
  File "/private/var/mobile/Containers/Shared/AppGroup/F3C0E711-6D38-4FDF-81F2-DC3B97E4E9F1/Pythonista3/Documents/site-packages/pelican/__init__.py", line 181, in run
    signals.finalized.send(self)
  File "/private/var/mobile/Containers/Shared/AppGroup/F3C0E711-6D38-4FDF-81F2-DC3B97E4E9F1/Pythonista3/Documents/site-packages/blinker/base.py", line 267, in send
    for receiver in self.receivers_for(sender)]
  File "/private/var/mobile/Containers/Shared/AppGroup/F3C0E711-6D38-4FDF-81F2-DC3B97E4E9F1/Pythonista3/Documents/site-packages/minify.py", line 32, in minify_html
    Parallel(n_jobs=-1)(delayed(create_minified_file)(filepath, options) for filepath in files_to_minify)
  File "/private/var/mobile/Containers/Shared/AppGroup/F3C0E711-6D38-4FDF-81F2-DC3B97E4E9F1/Pythonista3/Documents/site-packages/joblib/parallel.py", line 772, in __call__
    n_jobs = self._initialize_pool()
  File "/private/var/mobile/Containers/Shared/AppGroup/F3C0E711-6D38-4FDF-81F2-DC3B97E4E9F1/Pythonista3/Documents/site-packages/joblib/parallel.py", line 542, in _initialize_pool
    self._pool = MemmapingPool(n_jobs, **poolargs)
  File "/private/var/mobile/Containers/Shared/AppGroup/F3C0E711-6D38-4FDF-81F2-DC3B97E4E9F1/Pythonista3/Documents/site-packages/joblib/pool.py", line 580, in __init__
    super(MemmapingPool, self).__init__(**poolargs)
  File "/private/var/mobile/Containers/Shared/AppGroup/F3C0E711-6D38-4FDF-81F2-DC3B97E4E9F1/Pythonista3/Documents/site-packages/joblib/pool.py", line 419, in __init__
    super(PicklingPool, self).__init__(**poolargs)
  File "/var/containers/Bundle/Application/46E67BC7-8A23-4C29-9CBA-6E4CC2B2BB96/Pythonista3.app/Frameworks/Py2Kit.framework/pylib/multiprocessing/pool.py", line 160, in __init__
    self._repopulate_pool()
  File "/var/containers/Bundle/Application/46E67BC7-8A23-4C29-9CBA-6E4CC2B2BB96/Pythonista3.app/Frameworks/Py2Kit.framework/pylib/multiprocessing/pool.py", line 224, in _repopulate_pool
    w.start()
  File "/var/containers/Bundle/Application/46E67BC7-8A23-4C29-9CBA-6E4CC2B2BB96/Pythonista3.app/Frameworks/Py2Kit.framework/pylib/multiprocessing/process.py", line 131, in start
    self._popen = Popen(self)
  File "/var/containers/Bundle/Application/46E67BC7-8A23-4C29-9CBA-6E4CC2B2BB96/Pythonista3.app/Frameworks/Py2Kit.framework/pylib/multiprocessing/forking.py", line 122, in __init__
    self.pid = os.fork()
OSError: [Errno 1] Operation not permitted
```

I really wanted minification to work, so I decided to read through the minify module and it's dependencies to find out a solution. That plugin uses `joblib` to parallelize the page minification jobs, which is nice because it allows it to run a lot faster on multi core and multiprocessor computers. But it turns out that multiprocessing on Pythonista is limited, so I should find out a way to turn it off. I soon discovered that changing a single character in `site-packages/minify.py` would solve issue for me.

Line 32 has this code:

```python
    Parallel(n_jobs=-1)(delayed(create_minified_file)(filepath, options) for filepath in files_to_minify)
```

And in `site-packages/joblib/parallel.py` there was this explanation for the `Parallel` class:

```python
class Parallel(Logger):
    ''' Helper class for readable parallel mapping.

        Parameters
        -----------
        n_jobs: int, default: 1
            The maximum number of concurrently running jobs, such as the number
            of Python worker processes when backend="multiprocessing"
            or the size of the thread-pool when backend="threading".
            If -1 all CPUs are used. If 1 is given, no parallel computing code
            is used at all, which is useful for debugging. For n_jobs below -1,
            (n_cpus + 1 + n_jobs) are used. Thus for n_jobs = -2, all
            CPUs but one are used.
```

So I went on and changed the instantiation call by removing the minus (-) sign:

```
    Parallel(n_jobs=1)(delayed(create_minified_file)(filepath, options) for filepath in files_to_minify)
```

And guess what? It worked! Finally I had this plugin working both on desktop and iPhone and iPad.

