Title: New project: counting files with Python
Date: 2018-05-01 00:29
Lang: en
Tags: python, cli, files, file management, file count, file extension
Category: Programming
Slug: new_project_count_files
Author: Victor Domingos
Cover: images/2018/count-files.png
Summary: While working on this website, I had the curiosity to find out how many HTML and image files Pelican was generating behind the scenes. I had no utility at hand to count files recursively through folders and subfolders, so I decided to create my own using Python.

The application started with just a few lines of code in Pythonista right on my iPhone. Then I went on to add a few details. And now it's kind of ready to use. Here is how it works:

```shell
$ countfiles.py -h
usage: countfiles.py [-h] [-nr] [-nt] [-alpha] [-a] [path]

Recursively count all files in a directory, grouped by file extension.

positional arguments:
  path        The path to the folder containing the files to be counted.

optional arguments:
  -h, --help  show this help message and exit
  -nr         Don't recurse through subdirectories
  -nt         Don't show the table, only the total number of files
  -alpha      Sort the table alphabetically, by file extension.
  -a          Include hidden files and directories (with filenames starting
              with '.')
```


All the arguments indicated above, including the path, are optional and you may use whatever order you prefer. So the most simple way to use it is just by typing `countfiles.py` and let it use the default options to scan the current working directory:

```shell
$ countfiles.py

Recursively counting all files, ignoring hidden files and directories, in the current directory.

 EXTENSION | FREQ.
-----------+-------
 png       |    82
 html      |    66
 css       |    28
 jpg       |    26
 svg       |    13
 xml       |    10
 ico       |     1
 md        |     1
 txt       |     1
 js        |     1
-----------+-------
 TOTAL:    |   229
-----------+-------
```

Sometimes, you may want to turn off the table and just obtain a count of all files:

```shell
$ countfiles.py / -a -nt

Recursively counting all files, including hidden files and directories, in:
/.

Total number of files in selected directory: 1998700.
```


You can download the source code and read a more complete description of this application on GitHub. [Check it out](https://github.com/victordomingos/Count-files){:target="_blank"}!


## Have a better idea?
If you have come up with a better solution for these problems, please [let me know](https://victordomingos.com/contactos/).
