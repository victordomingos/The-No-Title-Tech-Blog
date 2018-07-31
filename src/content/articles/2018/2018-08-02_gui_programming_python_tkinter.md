Title: Graphical User Interfaces on Python with tkinter
Date: 2018-07-21 00:01
Lang: en
Tags: python, talks, tkinter, ttk, macOS, GUI, graphical interfaces
Category: Programming
Slug: gui_programming_python_tkinter
Author: Victor Domingos
Cover: images/2018/summer_talks.jpg
Summary: This Wednesday, 1 August, I did a brief presentation on *GUI programming on Python with Tkinter*, at [Blip.PT](https://blip.pt){:target=_blank}, during a Summer Talks event promoted together by [DevOps Porto](https://www.meetup.com/devopsporto/){:target=_blank} and [Python Porto](https://www.meetup.com/pyporto){:target=_blank}. This article puts together the main topics from my presentation, and adds a few details that I couldn't fit in the short time of that session.

### Summary
One of the most overlooked packages from the Python Standard Library is `tkinter` and its child `ttk`. This package allows us to build graphical user interfaces without adding any external dependencies, and with a bit of care, it allows for a good user experience. While learning Python programming, I have been exploring tkinter/ttk as a tool for building user-friendly graphical interfaces. I would like to share that experience and some of the insights that have arisen during that process. Tkinter may not be able to replace a native GUI toolkit, but can certainly be an important addition to any developer's toolbox, both for personal use, or for bridging our code to less technical users.

### How I got into Python and tkinter
First of all, I should start by clarifying that I am not a professional programmer, at least most of the time. I studied Psychology and had basically no formal education on computer science or programming. But I am a tech user and I like to play around to find out new ways to do tasks more easily or more quickly. And I enjoy the fact that programming makes us think.

So, about 2 years and a half ago, I decided to learn Python. I had in the past touched a tiny bit of C, some HTML and CSS, but Python was in fact my first programming language, the one I really invested in learning. And there's so much to learn! It's a great language for beginners, but it lets us grow within its ecosystem.

Well, I like to learn things in a practical way. So, right from the beginning I tried to apply what I was learning to everyday tasks. I work at a company that runs an online store, but still has a couple of manual processes, and currently no one available to build and implement new features that we would like to see in the platform we use. One of those tasks is taking care of the tracking status of our shipments. Every day the carrier leaves, for each shipment, a tracking code that we can use to check on their website if it has been delivered or not. If in the next day the order was not delivered, we need to know and take action. So, as a personal learning project, I started building my own parcel tracker in Python, at first as an interactive console application. In a month or so, I had my first text-based prototype working.

But when your team is not composed of programmers, a text-mode app won't probably be well regarded by them. Especially if they're all Mac users, accustomed to beautiful graphical interfaces, based mostly on visual interaction using mouse and trackpad. After I had that early prototype (and feedback from some of the target users), I started exploring on the possibility of creating a GUI. I read about the existing options and discovered that Python comes bundled with `tkinter`, which is frequently described as Python's *de facto* standard GUI (Graphical User Interface) package. So, I thought it would be a good starting point, as it should have some stability and community support. About a month later, I already had a new version of that application, now with a working GUI.

### Here is my first tkinter app

Tkinter has some limitations, but I believe that many developers ignore its potential. It has a reputation of looking antiquated and limited, and many developers put it aside and skip it entirely without even giving it a try, just because the default unthemed widgets look like something from the 70's.

However, when you use `ttk`, which is a themed widget set, it blends with the native OS theme, so it looks very similar to a native app. And, in fact, it's not that bad, in my opinion. Let me show you my first Python/tkinter app, [PT Tracking]({filename}/pages/projects/pt-tracking.md):

[!embed?max_width=740](https://www.youtube.com/watch?v=t-iBO8xAjO8&t=58s)

It definitely needs some extra care in packaging and some other details, but hey, it has been working well for me and my team for the last two years.

It uses a simple SQLite database (not very fancy, but does the job), queries CTT Expresso website with [Requests](http://docs.python-requests.org){:target=_blank} and scraps the info we need using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/){:target=_blank}. If I have 20 orders to track, I just open the app and it tracks them all in one click.

The general structure of most windows (three horizontal sections, for toolbar, table and status bar) is put into place by the `pack()` geometry manager. Then, each of those sections is organized using the `grid()` manager.

Now, notice what I did. I spent some time reading through Apple's Human Interface Guidelines and seeing how other developers placed stuff in the window. You can see a toolbar that is not very different from what you can find in a native application like Safari or Finder. It has icons with labels below, a search field that gives instant results as you type, a menu with all the features and keyboard shortcuts hints, autocomplete in the entry form... You can see some basic animation in the panels. A context menu when you right click in the main table view.  The text fonts, sizes and colors were slightly adjusted, in order to match some of the conventions of the platftorm. All those details make for an experience that is more welcoming for the end user. And it's made with `tkinter` and the `ttk` widget set.

In case you are worried that it can't scale up from a simple single window application into something more elaborated, don't be. Please, take a look this other tkinter project I have been working on:

[!embed?max_width=740](https://www.youtube.com/watch?v=ai51wUk5MrU)

Once again, it's also a desktop database application, this time backed by [SQLAlchemy](https://sqlalchemy.org){:target=_blank}. It starts with a login box and then spreads into several windows that have different designs, according to their respective purpose. Despite the fact that this project is still under development, still with some rough edges, you will certainly notice some intentional interface familiarity, in terms of what a Mac user would expect. Did you notice, for instance, that short animation in the login box, when the user enters some invalid login credentials? Tkinter does not provide any animation primitives, but it's relatively easy to use the `place()` geometry mechanism to generate simple animations like these.

Also, you can combine the provided widgets to build your own custom widgets, like a calendar date picker (like the one I used in the new repair form, in RepService), or a `LabelEntry` that mixes an `Entry` widget and a label. Also, there is a `Canvas` widget that lets you draw custom made 2D graphics.


### How does it work in practice?

A typical tkinter application starts like this:

```python
import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "Hello World\n(click me)"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side="top")

		self.quit = tk.Button(self, text="QUIT", fg="red",
							  command=root.destroy)
		self.quit.pack(side="bottom")

	def say_hi(self):
		print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
```


`Tk()` is usually the the parent of the root window class, and if you need more Windows you will then use one or more `Toplevel()` instances.

You can use these built in widgets (in this list I am including widgets from both `tkinter` and `tkinter.ttk`):

- Label
- Entry
- Button
- Checkbutton
- Menubutton
- Radiobutton
- Combobox
- Text
- Scale
- Scrollbar
- Spinbox
- Progressbar
- Treeview
- Separator
- Toplevel (+windows)
- Frame
- LabelFrame
- PanedWindow
- Notebook
- Sizegrip
- Canvas


...and some more from these modules:

- tkinter.colorchooser
- tkinter.filedialog
- tkinter.messagebox
- tkinter.scrolledtext
- turtle



It you research a little on the web, you may find some other pre-made useful stuff, like a calendar date picker, an autocomplete text entry field, a tool tip balloon widget, and more...

You should learn not only about the widget set, but also about the 3 layout managers: pack, grid and place. In my PT Tracking app, I used `pack()` to define the main areas (toolbar, central area and status bar), I used `place()` to slide in the panels from the bottom and to create the animation for the in-app notification panel. And I used `grid()` everywhere to organize the widgets inside each section.

Start by using them separately, but keep in mind that sometimes it is useful to combine them. However, if you don't do things right and mix them in the wrong way, your app may freeze. So take your time exploring how it works.

Then you should also learn about Tkinter's event loop, the existing events and the event bindings.

### Tkinter's limitations, and how to cope with them

There are some rough edges. For instance, if you use a bitmap image for the buttons, they will have a different shape (for that reason, I used emojis instead in the toolbar buttons). And on Mac, using this aqua theme that looks native, you can't choose the background color for frames and other widgets, which is particularly annoying in the `Notebook` widget.

If you try to run a Python app with GUI directly from the Finder or the Dock (on a Mac), you will get a console window. You can avoid it by creating a launcher with AppleScript:

```applescript
do shell script "export LC_ALL=en_US.UTF-8; export LANG=en_US.UTF-8; /usr/local/bin/python3 '/Users/USER/FOLDER/SCRIPT.py' &> /dev/null &"
```

It launches the Python application without Terminal windows. The AppleScript application can then be personalised with a custom icon as usual, and can be placed in the Dock. When clicked, it will launch the Python intepreter, that still shows up in Dock, but with no visible windows.

There are some usual widgets that are missing like a calendar picker or split buttons. Some of that functionality, however, can be replaced by using other widgets or by combining them into new reusable widgets. Maybe the biggest limitation is the fact that it misses a web view. If you need to present some HTML formatted content you will need to use some other package or the web browser itself.

Also, currently images may not make use of full resolution on "retina" screens.

### So, should I use tkinter?

First of all, if you write Python code and are interested in Graphical interfaces, I think you should take some time learning tkinter, even if you decide later to go back to text mode stuff or to learn or use some other GUI toolkit. Think about it as another tool in your backpack. You may choose to use it when the right time comes.

Now, because not everything is perfect, let's do a quick summary of some of tkinter's strengths and weaknesses:

**PROS:**

- It's simple to learn and use
- Comes bundled with Python
- Highly portable
- Can look [kind of] native
- It's fast enough for most uses
- It is a mature and stable toolkit
- It's free for commercial use.


**CONS:**

- Limited widget set (e.g., no date picker, no webview)
- No UI designer.
- It doesn't look *totally* native
- It's not as fast as a native Swift or C\+\+  GUI
- The development of tkinter is not very active, so don't expect a lot of new features.


### Some final advice

Think about who are your target users, what kind of interfaces they're used to, what features they will value. Observe and study the UI conventions of your target platform. My apps were intentionally designed to fit macOS as much as tkinter would allow, but on other platforms some of my customizations would need to be different. For instance, the toolbar layout, the keyboard shortcuts or the theme. This advice will also apply to any other GUI kit you may choose to use in the future.

If your app will have more than just a few buttons, you will need to build it in an object-oriented way and maybe splitting it in several modules. Python can be a very compact language, but when building a GUI, you'll probably end up with 3 times more code.


### Resources:

There are some interesting books about tkinter that won't ruin your wallet and may be a good introduction:

- [Tkinter GUI Application Development Blueprints - Second Edition](https://www.packtpub.com/application-development/tkinter-gui-application-development-blueprints-second-edition){:target=_blank}, by Bhaskar Chaudhary (Packt Publishing, 2018)
- [Python GUI Programming Cookbook - Second Edition](https://www.packtpub.com/application-development/python-gui-programming-cookbook-second-edition){:target=_blank}, by Burkhard Meier (Packt Publishing, 2017)

These websites also contain lots of useful information:

 - [Graphical User Interfaces with Tk](https://docs.python.org/3/library/tk.html){:target=_blank} (official Python docs)
 - [TkDocs](https://tkdocs.com){:target=_blank} - some basic Tk examples explained in 4 programming languages, including Python.

 - [An Introduction To Tkinter](http://effbot.org/tkinterbook/tkinter-index.htm){:target=_blank} - Lots of information, not exhaustive, but will certainly appear on Google when your searching for something related to tkinter, and probably the answer you need is there.

- [Tkinter 8.5 reference: a GUI for Python](http://infohost.nmt.edu/tcc/help/pubs/tkinter/tkinter.pdf){:target=_blank} - some code may be outdated, but still a useful resource to learn the basics and find some answers.


...and if you know Tcl/Tk and can translate from Tcl to Python, you will probably feel at home using tkinter, and the [Tcl/Tk docs](https://www.tcl.tk/man/tcl8.6/){:target=_blank} may be a helpful resource (for more information, check out [this section of Python docs](https://docs.python.org/3/library/tkinter.html#a-very-quick-look-at-tcl-tk){:target=_blank}).


If you get stuck, [StackOverflow](https://stackoverflow.com/questions/tagged/tkinter){:target=_blank} probably can help. Sooner or later, you will probably get an insightful  answer from a guy named Brian Oakley, on some topic related to tkinter. You should trust his advice. :)

