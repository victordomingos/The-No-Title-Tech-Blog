Title: Book review – Supercharged Python, by Brian Overland and John Bennet
Date: 2019-11-19 01:27
Lang: en
Tags: python, books, Brian Overland, John Bennet, learning, Numpy, Regular Expressions
Category: Programming
Slug: book_review_supercharged_python
Author: Victor Domingos
Cover: images/2019/supercharged_python__book_cover.jpg
Summary: If you have been following beginner or even intermediate guides on Python and are starting to feel the need for more advanced learning, this book may be the one you have been looking for. According to the authors, was written for those who already know the basics of Python, but want to deepen their knowledge and skills.


While being targeted to people who already know the fundamentals of Python, this book still includes a quick review in the first chapter. It goes briefly through the usual stuff, like variables, operators, data types, basic I/O, `if`/`else`, `while`, `for`, function definitions and arguments, lists, tuples, dictionaries, sets, and the distinction between global and local variables. This initial chapter is presented as being an optional reading, as its contents are pretty basic, but the authors recommend that the reader takes a minute or so on the last to pages, which cover the `global` statement.


### Some thoughts on the chapters’ internal structure
Before moving forward through the rest of the chapters, it may be worthwhile to describe the general internal structure of the chapters (you can also fin the [full chapters list on the publisher website](https://catalogue.pearsoned.co.uk/educator/product/Supercharged-Python-Take-Your-Code-to-the-Next-Level/9780135160244.page)). But even before that, I would just point out a little detail on the exterior of the physical book itself: each chapter has its number on every right side page, inside a black box. And if you look on the right side of the book, you’ll notice those markings are intentionally visible from the outside, even with the book closed, placed in a stairway pattern, similar to what you can find in dictionaries, encyclopedias and other large volume books meant to be used as reference material. 

![Supercharged Python - Side view]({static}/images/2019/supercharged__side_view.jpg)

That detail, combined with the page headers, is a nice help to simplify the navigation in such a long book (633 pages, if you count the index).

Now, about the chapter structure… Each chapter has its own topic, which is briefly introduced in two or three paragraphs. Then you have all the “juice” subdivided into subtopics, with code samples and some additional notes. At the end of each chapter, you get a short summary (with you can use either to make sure you still remember what you have read, or as a previous step to help you decide which chapter you want to read next).

Then, there are two additional sections that are pretty useful, both for self-learners and for teachers: *Review Questions* (to make sure you have really understood the main topics) and *Suggested Problems* (some exercises you may use to practice what you have just learned). If you are really investing in getting a deeper understanding of the language and want to become better at programming, this last section will be particularly useful, so don’t just skip it.


### Back to the contents…

Regarding the contents of the other 14 chapters, it’s not easy to summarize them, so I will start by letting to the reader the possibility to check the full [table of contents at the publisher’s website](https://catalogue.pearsoned.co.uk/educator/product/Supercharged-Python-Take-Your-Code-to-the-Next-Level/9780135160244.page), before highlighting some of its numerous interesting bits.

Chapter 2 covers some advanced string capabilities, like string operators (`+`, `=`, `*`, `>`, etc.), indexing, slicing, binary/hexadecimal/octal conversion functions, search/replace methods, justification methods, and many others. On chapter 3, the same is made for lists: copying lists versus copying list variables (if you don’t know the difference, it’s a good opportunity to find out, as it can avoid some serious bugs), indexing, slicing, assigning into slices, list operators, functions, and methods, lambda functions, list/dictionary/set comprehensions, and more.

![Supercharged Python - List Comprehensions]({static}/images/2019/supercharged_python__list_comprehensions.jpg)

On chapter 4, you will find a long list of programming shortcuts (22, to be more precise), from `for` loops to tuple assignment, from chained comparisons to one line if/then/else statements. Also, in the same chapter, there are some tips on running Python from the command line, packages, `pip`, functions as first-class objects, variable length argument lists (`*args`/`**kwargs`), decorators and generators. A lot of information, indeed!

The next chapter covers precise text formatting (`%` format specifiers, the `format` method, `repr` versus string conversion,…).

Then, there are two chapters entirely dedicated to Regular Expressions, which is the kind of topic every programmer needs to know about, but also one that can feel very intimidating at first. 

![Supercharged Python - Regular Expressions]({static}/images/2019/supercharged_python__regular_expressions.jpg)

Regular Expressions (or simply Regex, for friends) is kind of a mini-language for text matching and replacing. While its apparent crypticness can look a bit out of place in the context of Python (you know, *that special language* that is very high level, almost English-like and with lots of syntactic sugar), the truth is that one or two regular expressions can make some tasks much easier to accomplish. So, you definitely should invest some time learning about them. You won’t regret, even if it hurts a little…

Chapter 8 covers text and binary file I/O, and chapter 9 presents an in-depth on classes and the so-called “magic methods” or “dunder methods” (like, for instance, `__init__`, `__new__`, `__iter__`).

The next chapter will certainly please a lot of readers, since its very practical and deals with the kind of information we are used to, and which sometimes can require more accuracy. You will get to know the `Decimal` class, as well as a suggestion on how to code a Money class that has no floating-point related rounding errors.

In case that math related chapter got you interested, you will be happy to know that the next ones are also number related: chapter 11 talks about `Random` and `Math` packages, chapters 12 and 13 cover the [Numpy](https://numpy.org/) package, which can make your number-crunching code a lot faster, and show some examples of how to generate graphs with [Matplotlib](https://matplotlib.org/).

![Supercharged Python - Numpy]({static}/images/2019/supercharged_python__numpy.jpg)

On chapter 14 you will get a pause from your number crunching adventures, to focus more on code organization in multiple files. You will be guided through `__main__`, `__name__`, `import`, and private and public module variables, in order to split your code into several files, improving the overall maintainability of your project. A practical example is given: an [RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation) calculator started in chapter 3 is now improved using this technique.

Finally, the 15th chapter shows how to get financial data off the internet and process it, suing [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/). The authors say they have saved the best for last, and in fact it is like if they wanted to use this chapter to inspire you to go on and use Python for some fun, useful, and exciting projects. Which is what Python is all about, by the way.

![Supercharged Python - Graphs]({static}/images/2019/supercharged_python__graphs.jpg)

The last fifty or so pages before the index contain five useful quick reference appendices that list some commonly needed features: a Python operator precedence table, a list of built-in Python functions, which includes a brief description for each one, a list of set methods, a list of dictionary methods, and a statement reference, which describes how the various statements (`assert`, `break`, `class`, `super`, `zip`, `iter`, `continue`, `except`) work. Some of these (most likely, not all of them, though) may be already well known by many readers, but it is still a nice reference that can become handy.

### Conclusions 

From the description above, you may already guess some of my final words. This book is intended to an audience who already knows a bit of Python but starts to grasp *how much Python* Python really has underneath itself, and feels the need for a deeper study. With those readers in mind, *Supercharged Python* exposes many details of the Python language that are sometimes ignored but which often allow us to write faster and cleaner code. 

In my opinion, it may not be the most pleasing programming book I have ever read (I am sure it’s not its main purpose either), but it is certainly one of the most useful ones to help you make the *next step*, after some initial contact with the Python language. So, you can see that the lemma that comes written in the book cover (“Take your code to the next level”), more than just a cool marketing phrase, is a quite precise description of the authors’ intents and the contents of this book.

**Get the book:**  
[catalogue.pearsoned.co.uk/educator/product/Supercharged-Python-Take-Your-Code-to-the-Next-Level/9780135159941.page](https://catalogue.pearsoned.co.uk/educator/product/Supercharged-Python-Take-Your-Code-to-the-Next-Level/9780135159941.page){:target=_blank}

<hr ><small>
<strong>Disclosure Notice:  </strong>
For this review, I received a free copy of the book from the publisher. I do not personally know the authors or the publishers, and did not receive any other compensation. The link to Amazon is provided as a reference only, I am not endorsing the company or making any profit from it. 
</small>
