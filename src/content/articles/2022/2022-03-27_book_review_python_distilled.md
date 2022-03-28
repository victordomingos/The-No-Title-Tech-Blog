Title: Book review — Python Distilled, by David M. Beazley
Date: 2022-03-27 22:00
Lang: en
Tags: python, books, Beazley, distilled, learning, standard library, modules
Category: Book Reviews
Slug: book_review_python_distilled
Author: Victor Domingos
Cover: images/2022/python_distilled_book_cover.jpg
Summary: This is a pragmatic book that presents some of the most important topics about the Python programming language in a concise form, designed to make it easier to find out the most relevant information bits in a context where resources abound and frequently are just too overwhelming.


### Book structure and contents

The book is organised in 10 chapters and starts with the basics, like variables, data types, operators, expressions, control flow, looping, and so on. Compared to other books I have read recently, it uses a smaller font size, which is quite readable to me but may be less comfortable for some readers. On the other hand, it contributes to make it a lighter and less thick book, compared with other programming manuals. It uses no syntax highlighting, but code samples are short enough that actually this does not become a problem at all.

![Python Distilled]({static}/images/2022/python_distilled_ch01.jpg)

The text is always short, simple and as direct as possible, without long explanations or examples. It does not present step-by-step tutorials - this is not that kind of book. Think of it more like a reference guide that contains a summary for the most important language features. Need a quick refresh on how to use a mapping? You got it. There is a section for that and a small table that lists the most common operations, methods and functions. And the same goes for other similar features. Its like someone was attending the Python classes and then compiled a nice set of notes for you, with the stuff you need to know, but without the extra fluff.

If you're just starting, you may find this approach a bit too dry, so you may feel more inclined to read another book first. But don't discard this one just yet - you may want to get back to it in a couple of weeks, as it works as a summary that helps to highlight a set of topics that are important. 

![Python Distilled]({static}/images/2022/python_distilled_ch03.jpg)

If you have programmed a bit in Python, or have experience in other programming languages, this book may be specially useful, as its concise style provides a shortcut for the transition. You will probably be able to start writing some Python code quickly after the first three or four chapters, and then you can start digging more advanced topics in the remaining ones. You will read about classes and objects, generator expressions, context managers, and you will probably be able to understand how those features relate to the concepts you already have learned in C# or Java, for instance.

The author provides an interesting summary on protocols (you would probably call them *interfaces* in other programming languages), and how you may use them to make your code more pythonic. Everyone talks about writing "pythonic code", but this is something that frequently is overlooked. Chapter 4 describes number, comparison, conversion, container, iteration, attribute, function and context manager protocols. Knowing about them and implementing when appropriate can make a huge difference in the quality of a module of package.

Chapter 5 covers functions, including variadic arguments, keyword arguments, positional-only arguments, recursion, lambda expressions, higher order functions, callback functions. It also covers several other features, including asynchronous functions and `await`. Taking a hint from that, chapter 6 talks about several aspects related to generators.

On chapter 7, you get an overview on Python's object oriented programming model and ways to avoid inheritance via composition or functions. The reader is shown how python deals with class variables, static methods, properties and mixins, abstract classes, and more. This is a denser chapter, which speaks to the relevance of the topic. Object oriented programming can be very powerful, but it also may be used in some confusing ways that are error prone and have poor maintainability. So, it is a chapter that can make you think more deeply and make you reconsider some earlier notions about OOP.

![Python Distilled]({static}/images/2022/python_distilled_ch07.jpg)

After such a dense chapter, the reader is presented with a much shorter one that describes modules and packages, how they help to organize a project's code and how the `import` statement works.

No programming language is complete without input and output methods, so chapter 9 covers these topics, including data encoding, command-line options, environment variables, file I/O and data serialization. Together with chapter 10, they also present some useful modules and functions from the Standard Library. It is not an extensive description, since the detailed documentation can easily be found online, nowadays. It's more like a roadmap where you can find a brief description of some useful tools, that you can then go investigate more if you need them.

![Python Distilled]({static}/images/2022/python_distilled_ch09.jpg)

Throughout the book, the book tends to present small examples and short code samples, as it tries to explain the python programming language itself. So, it does not cover the techniques and design or architectural patterns that are usually required in larger scale projects. But, once again, there are other (some of them much longer) books for that purpose.





### Conclusions 

Writing a concise reference book can be very challenging, especially when it covers a programming language that has matured throughout more that two decades, includes an extensive standard library and an enormous ecosystem of third-party packages, and quite a lot of established *opinionated traditions* on how code should be written. It requires a lot of choices and some compromises. 

*Python Distilled* offers a good selection of information that will be useful for python programmers that are in different stages of the learning path. I would recommend it particularly for those what have been using other programming languages and need a quick reference on Python, but also for those who have basic to medium knowledge of the language, since the book also explores some advanced features of Python that may not be very obvious.



_______

### Get the book:

- [www.dabeaz.com/python-distilled](http://www.dabeaz.com/python-distilled/){:target=_blank}  
 
- [www.informit.com/store/python-distilled-9780134173276](https://www.informit.com/store/python-distilled-9780134173276){:target=_blank}

<hr ><small>
<strong>Disclosure Notice:  </strong>
For this review, I received a free copy of the book from the publisher (I had to pay the customs expenses, though). I do not personally know the authors or the publishers, and did not receive any other compensation. The link to the publisher is provided as a reference only, I am not endorsing the company or making any profit from it. 
</small>
