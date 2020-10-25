Title: Quick tip – How to quickly read just the last lines of a huge text file
Date: 2020-10-19 22:30
Lang: en
Tags: shell, command-line, log files, text, Windows, linux, macOS, Haiku, unix, terminal, tutorial, console, tail
Category: Tutorials
Slug: how-to-read-last-lines-of-huge-text-file
Author: Victor Domingos
Cover: images/2020/tail-command-haiku.jpg
Summary: If you’re a developer or a systems administrator, sooner or later you will meet that HUUUGE, GIANT, ENORMOUS file. A file that weights several gigabytes of more or less cryptic system or application logging messages, with no rotation scheme in place. Since log files are usually built by appending the most recent information to the end, probably you just need to check out the last 100 or 1000 lines, in order to find out why an application has crashed or failed to operate properly some seconds or a minute ago. Turns out that reading such huge files may not be as simple as editing them in Notepad. Probably, an application like that won’t even be able to the file. So, what else can you do?

When a text file is *slightly* big but yet smaller than the available memory, you may be able to open it with a good text editor, [like Vim]({filename}/articles/2019/2019-08-09_get_started_with_vim.md), UltraEdit or BBedit. But again, even if it opens the file but you only need to see the last part, there may be an easier way. My favourite one in those situations (and I had one of those today) is to use a shell command to extract or display the last *N* lines, which is widely known as `tail` in the unix world.

For instance, let’s say you just need the last 100 lines of text:

### Linux, macOS, Haiku, and pretty much almost any Unix flavour

```console
$ tail -n 100 ~/victor/hugelogfile.txt
```

### Windows (PowerShell)

```console
PS C:\> Get-Content hugelogfile.txt -Tail 100
```

The number of lines you specify (counting backwards from the end of file) will be displayed on the screen, with no need to load the whole thing into memory.

Now, if you are responsible for writing or maintaining the code that has been generating those gigantic multi-gigabyte or multi-terabyte log files, it may be a good time to consider implementing a [log rotation scheme](https://en.wikipedia.org/wiki/Log_rotation){:target=_blank}. In fact, there are even ready-to-use implementations available for most programming languages, so it should not be a daunting task.

Your future self, and maybe other people that also need to interact with your system, will deeply appreciate! 😉

