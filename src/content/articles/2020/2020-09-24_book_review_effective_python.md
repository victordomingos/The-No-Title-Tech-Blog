Title: Book review – Effective Python, by Brett Slatkin (and a free chapter for download)
Date: 2020-09-24 00:04
Lang: en
Tags: python, books, Slatkin, effective, learning, code quality, pythonic, best practices, performance
Category: Programming
Slug: book_review_effective_python
Author: Victor Domingos
Cover: images/2020/effective_python_book_cover.jpg
Summary: Those among you who have already learned some Python or may even have used it in some projects will certainly have heard the expression "Pythonic Code", which conveys a general and somewhat wide meaning of "clean code and good software development practices in the context of Python". With *Effective Python*, the author presents you with nothing less than 90 practical examples on how to adopt a pythonic developer mindset and how to write better Python code.

This is the second edition of a great book that Brett Slatkin had published in 2015, and which many of you may still recall. But this new edition has lots of new contents (it has grown from 59 to 90 subjects or sections, and from around 250 to more than 400 pages). It has also been updated to cover some important new features that are included in recent Python versions, up to Python 3.8, which is currently the most up-to-date stable version and will be [supported for some years](https://devguide.python.org/#status-of-python-branches){:target=_blank} after 3.9 comes out. 

So, even if you have read the first edition, it may be worth checking it out because, besides having been revised and updated to reflect the constantly evolving best practices, it covers some more recent topics like [assignment expressions](https://www.python.org/dev/peps/pep-0572/){:target=_blank} (a.k.a. the *walrus operator*).

### Book structure and contents

First of all, I must say that I really enjoyed the graphical layout of the book, the font size and spacing, and especially its subtle use of color for section titles and for syntax highlighting. Those small details, in my opinion, significantly contribute to a pleasant reading experience.

![Effective Python]({static}/images/2020/effective_python_ch10.jpg)

Effective Python is composed of 10 chapters, starting with themes like "Pythonic Thinking" and "Lists and Dictionaries", and spreading to more advanced topics like "Concurrency and Parallelism" or "Robustness and Performance". Each chapter aggregates 7 to 13 items, which are smaller sections (usually less than 10 pages). 

Each of those sections is focused around a specific and practical recommendation, like "Item 6: Prefer Multiple Assignment Unpacking Over Indexing", or "Item 63: Avoid Blocking the *asyncio* Event Loop to Maximize Responsiveness". 

You can check the full list of items at the official website of [effectivepython.com](https://effectivepython.com){:target=_blank}. 


![Effective Python]({static}/images/2020/effective_python_ch07.jpg)


Since this is an intermediate to advanced level book, you may find things you already are familiar with, especially in the first chapters. However, my experience with it is that even there you may find some precious and useful information. That's the case, for instance, of the explanation in chapter 1 about assignment expressions, a feature that was introduced with Python 3.8, but one that many Python developers are still not very comfortable with.

![Effective Python]({static}/images/2020/effective_python_ch01.jpg)

Every programmer needs to be able to use an arsenal of data structures, starting of course with lists and dictionaries, which are both covered in chapter 2. Once again, the books starts with a somewhat fundamental topic (sequence slicing) and goes on to other less known intricacies, like "Item 17: Prefer `defaultdict` Over `setdefault` to Handle Missing Items in Internal State".

![Effective Python]({static}/images/2020/effective_python_ch02.jpg)

Each section (or item, as they're called in the book) includes a brief and clear explanation and some code examples that illustrate its topic. As I mentioned before, the code samples are nicely formatted with syntax highlighting and tend to be pretty short and simple, so that you can quickly understand the idea being presented.

![Effective Python]({static}/images/2020/effective_python_ch09.jpg)

Finally, each item ends up with a short list titled "Things to Remember", which summarises its main ideas. I just love technical and scientific books that include nice summaries like these, because it makes a lot easier for the readers to check if they have correctly understood what they have read. But it is also very useful when we just need to select a few sections, both while skimming throw the book to find out the most interesting topics, or when we are getting back to it after some time in order to search for an answer that we know is *somewhere* inside the book.

![Effective Python]({static}/images/2020/effective_python_ch07a.jpg)


### Conclusions 

This is a book that I definitely recommend to anyone who already has some basic or intermediate knowledge of Python. You can read it cover to cover, or just pick the specific topics that you're interested in at a given time, and get back to it later when you need it. Even more experienced Python users may still benefit from some of the explanations in this book, like those on chapter 6 ("Metaclasses and Attributes") or on chapter 7 ("Concurrency and Parallelism"). 

In a world where the web is full of videos and tutorials on programming (which is great, but not always the most efficient way to learn), it is good to know that there are excellent quality books like this one being published, both on print and on digital formats, which can guide us throughout our journey towards a deeper knowledge of Python and its best programming practices.


_______


### Free sample chapter

The publisher has kindly provided us a sample chapter in PDF, which you may download for free, so that you can get a more concrete feel of the looks, tone and contents of this book:

* [Effective Python – Free Sample Chapter (click to download!)]({static}/pdf/Ch05_Effective-Python.pdf){:target=_blank}

_______

### Get the book:

- [effectivepython.com](https://effectivepython.com){:target=_blank}  
 
- [www.pearson.com/store/p/effective-python-90-specific-ways-to-write-better-python/P100001064508](https://www.pearson.com/store/p/effective-python-90-specific-ways-to-write-better-python/P100001064508){:target=_blank}

<hr ><small>
<strong>Disclosure Notice:  </strong>
For this review, I received a free copy of the book from the publisher. I do not personally know the authors or the publishers, and did not receive any other compensation. The link to the publisher is provided as a reference only, I am not endorsing the company or making any profit from it. 
</small>