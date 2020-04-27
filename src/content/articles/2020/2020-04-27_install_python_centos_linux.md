Title: How to install the current Python version on CentOS Linux 7
Date: 2020-04-27 00:40
Lang: en
Tags: python, linux, CentOS, shell, terminal, tutorial, installation, git, Tkinter, sqlite, tutorial, console
Category: Tutorials
Slug: install_python_centos_linux
Author: Victor Domingos
Cover: images/2020/centos_linux_7_python3_8.jpg
Summary: One of these days, while setting up a couple of Linux virtual machines to test my Python applications, I was faced with a series of obstacles on CentOS 7 that I needed to overcome. Since this is the kind of issues that many other Python developers may encounter when setting up a Linux machine, I will share what I learned with this experience. 

## Some context

I usually use macOS as my main personal development environment. Although I have come to enjoy PyCharm as a very valuable IDE, I still like to do a lot of things in the Terminal. Apples's macOS includes a wonderful shell and many well known Unix utilities, and many other are available through the [Homebrew](https://brew.sh) package manager. I tend  to create and activate virtual environments with [Pipenv](https://pipenv.pypa.io/en/latest/), usually using the most current Python version, and sometimes in some of the previous ones. For instance, I may want to check how one of my Python applications is behaving under Python 3.6, 3.7 and 3.8, or even the latest Python 3.9 alpha. Or I may want to check if updating a specific third-party dependency will break something. 

From time to time, I also want to check for platform specific issues and make sure my code is working as expected on Windows, Linux or Haiku. For that kind of work, in the past I have used both VMware Fusion and VirtualBox, but currently I am using Parallels Desktop.

So, this week, I decided to test one of my applications on CentOS 7, a version that has been released a few years ago, but has excellent support in Parallels Desktop and is still officially maintained.

## Installing Python 3

![Python2.7 on CentOS Linux 7]({static}/images/2020/centos7_python27.jpg)

The first disappointment with CentOS 7 was that it didn't include Python 3. Even after updating the system software, all I got was Python 2.7.5 (which was released 7 years ago!), and in the default `yum` repositories all I could find was an older Python 3.6.8 version. I wanted to use the current stable version (Python 3.8.2), so I had to find out how to get it and install it. 

At the official Python website, when searching for Linux downloads, we are directed to the [Python Source Releases](https://www.python.org/downloads/source/) page, which lists many source code downloads for both stable releases and pre-releases. So, jump right to **"Python 3.8.2 - Feb. 24, 2020"** and copy the link from **"Download Gzipped source tarball"**. You can use that URL to download the Python source code right from the Terminal using `wget`. In my case, I already had `wget` installed, so I could move on.

### 1. Download Python source code (gzipped tarball):
```console
$ wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
```

### 2. Extract source code:
```
$ tar xvf Python-3.8.2.tgz
```

### 3. Go inside the extracted `Python 3.8.2` folder, build and install Python:
```
$ cd Python-3.8.2/
$ ./configure --enable-optimizations
$ sudo make altinstall
```

Whenever you need to run a command with administrative privileges in Unix-like systems, you may use the `sudo` prefix. It will ask you the password in order to proceed.

The `configure` and `make` commands in step 3 will take some time and generate a lot of console output, but if there are no errors it should be ok.

Unfortunately, I got one error, with the following traceback:

```pytb
Traceback (most recent call last):
  File "<frozen zipimport>", line 520, in _get_decompress_func
ModuleNotFoundError: No module named 'zlib'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<frozen zipimport>", line 568, in _get_data
  File "<frozen zipimport>", line 523, in _get_decompress_func
zipimport.ZipImportError: can't decompress data; zlib not available

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/parallels/Python-3.8.2/Lib/runpy.py", line 193, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/parallels/Python-3.8.2/Lib/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/home/parallels/Python-3.8.2/Lib/ensurepip/__main__.py", line 5, in <module>
    sys.exit(ensurepip._main())
  File "/home/parallels/Python-3.8.2/Lib/ensurepip/__init__.py", line 200, in _main
    return _bootstrap(
  File "/home/parallels/Python-3.8.2/Lib/ensurepip/__init__.py", line 119, in _bootstrap
    return _run_pip(args + [p[0] for p in _PROJECTS], additional_paths)
  File "/home/parallels/Python-3.8.2/Lib/ensurepip/__init__.py", line 27, in _run_pip
    import pip._internal
  File "<frozen zipimport>", line 241, in load_module
  File "<frozen zipimport>", line 709, in _get_module_code
  File "<frozen zipimport>", line 570, in _get_data
zipimport.ZipImportError: can't decompress data; zlib not available
make: *** [altinstall] Error 1
```

The solution was to install `zlib-devel` and then rebuild Python using the same commands:

```console
$ sudo yum install zlib-devel
$ ./configure --enable-optimizations
$ sudo make altinstall
```

This time I had no errors. But…

## Configuring additional builtin packages

…I would soon discover that my freshly installed Python 3.8.2 was missing some modules I have used in my projects, like `tkinter` and `sqlite3`. 

![Installing Python 3.8 on CentOS Linux 7 - missing modules: Tkinter and sqlite3]({static}/images/2020/centos7_python3_tk_sqlite_error.jpg)

Once again, I needed to install a few support packages using `yum` and then rebuild Python using `configure` and `make`:

```console
$ sudo yum install sqlite-devel tkinter tcl-devel tk-devel
$ ./configure --enable-optimizations
$ sudo make altinstall
```

So, you can see a pattern here. 

1. Python misses something.
2. You find out which development package provides that dependency.
3. You install it using a package manager (for CentOS 7, it's `yum`, but for other versions or other Linux distributions it could be `dnf`, `apt-get` or even other package managers).
4. Then you re-run the configuration and `make` steps to recompile and reinstall Python. 

In fact, I also needed to install other dependencies later, when I tried to use `pip` and got an SSLError. 

![Installing Python 3.8 on CentOS Linux 7 - SSLError]({static}/images/2020/centos7_python3_sslerror.jpg)

Once again, after identifying the missing packages, the process was the same:

```console
$ sudo yum -y install openssl-devel bzip2-devel libffi-devel
$ ./configure --enable-optimizations
$ sudo make altinstall
```

![Python 3.8 on CentOS Linux 7]({static}/images/2020/centos7_python38_success.jpg)

Then, to upgrade `pip` for the current user:
```console
python3.8 -m pip install --upgrade --user pip
```

This time, it worked just fine.


## Managing virtual environments and third party packages

In order to be able to set up different Python environments for each application, which allow us to use more than one Python version on the same computer and different sets of third-party packages, there are multiple ways. You could stick with the builtin `venv` [as described in the Python documentation](https://docs.python.org/3/tutorial/venv.html), or you could use [Virtualenv](https://virtualenv.pypa.io/en/latest/#), or [Poetry](https://python-poetry.org). Since I am used to [Pipenv](https://pipenv.pypa.io/en/latest/) and it has served me well for a few years, that's what I use when I am able to do so. After that last step in the previous section, I was able to install Pipenv by running the following command:

```console
$ python3.8 -m pip install --user pipenv
```

Then I was finally able to run the usual commands `pipenv --python 3.8`, `pipenv shell`, `pip instal -r requirements.txt` and so on.

As a side note, to be able to easily clone my git repositories, I just needed to install `git`:

```console
$ sudo yum install git
```

## Conclusions

Setting up a Python version that does not come preinstalled can be an headache and it surely can discourage people from using Python on Linux. But once you figure out how to do it, it gets easier. 

I hope this article can help those of you that encounter a similar difficulty to find their way, but please remember that there are many Linux distributions and versions. Many of them may require a different set of steps to achieve the same result, and some even include Python versions that are much more recent than the one in CentOS 7. On the other hand, having available a Python version that is separate from the one used internally by the operating system may be a good idea, as it helps to keep the system sane and working properly. 

Finally, just a brief word to remember that dependency hell can be a really ugly place. So, if you are starting to learn Python, please take some time to understand virtual environments and to find out the virtual environment management tool that works best for you. It will save you from a lot of trouble and make your Python developer life much more enjoyable.
