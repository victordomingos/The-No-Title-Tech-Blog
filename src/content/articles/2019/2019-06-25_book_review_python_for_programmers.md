Title: Book review – Python for Programmers, by Paul Deitel and Harvey Deitel
Date: 2019-06-25 20:21
Lang: en
Tags: python, books, Deitel, learning, AI, Natural Language Processing (NLP), Data Mining, Machine Learning, Deep Learning, Big Data, IBM Watson, scikit-learn, Keras, Hadoop, Spark, NoSQL, Data Science, Numpy, Pandas, SciPy, NLTK, TextBlob, MatPlotLi, Seaborn, Folium
Category: Programming
Slug: book_review_python_for_programmers
Author: Victor Domingos
Cover: images/2019/python_for_programmers_book_cover.jpg
Summary: This is a book written while having in mind those who already have some object-oriented programming background but are willing to get into Python and (especially) Artificial Intelligence and Data Science. 

### Like two books in one: <br>Part 1) An introduction to Python, with a data science flavor

In the first half, it provides a quick introduction to the Python language that will be easy to
follow by experienced programmers, while also introducing some basic data science topics. It
covers the basics of the Python language, as well as data analysis essentials like dynamic data
visualization with [MatPlotlib](https://matplotlib.org/) and
[Seaborn](https://seaborn.pydata.org/), high performance array operations using
[NumPy](https://www.numpy.org/),
[Pandas](https://pandas.pydata.org/)' dataframes and data munging or data wrangling (things like deciding what to do about missing or bad values, outliers or duplicates). In chapters 1 to 10, each chapter presents a selection of Python features, like data types, control statements, and exception handling. At the same time, each of those chapters includes a brief mention on data science. For instance, in chapter 2 the authors invite you to learn or recall some basic descriptive statistics (minimum, maximum, range), showing how easy it is to calculate them in Python. Then, in chapter 3, they take you a little further and let you add mean, median, and mode to your toolset. In chapter 9, you will be invited to calculate statistics and generate a simple histogram of passenger ages, using Pandas and the Titanic Disaster Dataset.

It's worth mentioning that, while this approach of mixing the teaching of a programming language with Data Science concepts may seem a bit confusing at first, it rapidly starts to make sense, as the internal chapter structure becomes apparent: an introduction, then some Python that coherently builds on the topics from the previous chapters, then something on data wrangling or statistics, then a wrap-up section that helps you recap what you have just read. Once you grasp that structure, it becomes much easier to navigate through this part of the book.

Chapter 10 follows the same structure but is kind of a turning point. It finally presents
Python’s object-orientedness and a slightly more advanced data science concept, simple linear
regression. Up to this point, the reader (assuming he/she has been reading every chapter in a
sequential way) has been exposed to the basics of Python syntax and data structures, some useful
third-party modules and tools like [IPython](https://ipython.org/), [Jupyter
Notebooks](https://jupyter.org/), MatPlotLib, Seaborn, Numpy, Pandas, as well as CSV and JSON manipulation.

### Like two books in one: <br>Part 2) An introduction to Data Science and Artificial Intelligence, with a Python flavor

Starting in chapter 11, you’ll find out that the authors are focusing more on data science and
less on Python concepts. The reader is now expected to be familiar with the language syntax and
some commonly used data structures, so the second half of the book serves to present some more
specialized topics related to A.I. and Big Data. Chapter 11 presents Natural language Processing
(NLP) and includes exercises on web scraping. Then you have a chapter on Data Mining, where
you'll be invited to use the Twitter API with [Tweepy](https://www.tweepy.org/) to obtain JSON
tweet data and then use it to perform sentiment analysis, geocoding (with
[GeoPy](https://geopy.readthedocs.io/en/stable/)) and mapping (using
[Folium](https://python-visualization.github.io/folium/)).

![Python for Programmers interior chapter 12]({static}/images/2019/python_for_programmers_interior_ch12.jpg)

On chapter 13, you will get a first experience with [IBM Watson](https://www.ibm.com/watson) and
cognitive computing. IBM Watson became [kind of a
celebrity](https://www.youtube.com/watch?v=WFR3lOm_xhE) in 2011, when it was presented in a TV
contest, running against its two all-time best players (oh, and winning, of course). Nowadays,
it's one of the most powerful cognitive computing services platforms available. It sounds hard,
but in fact it is all presented in a gradual progression, leaving much of the inherent complexity
to a later (and deeper) dive into IBM’s documentation. IBM offers many different cloud computing
services, that could never fit in a single chapter, or even a single book, so the authors have
decided to show a few examples, recommending the reader to create a user account on IBM’s Bluemix
(which meanwhile has been rebranded as [IBM Cloud](https://www.ibm.com/cloud)) and to explore their API documentation and tutorials. If you go through the case studies, you will use IBM Watson cognitive computing services to build an application that does natural language translation, including speech-to-text and text-to-speech conversion.

On chapter 14, we get introduced to the basics of machine learning, including the concepts of
classification with K-Nearest Neighbors (as a case study, you will be using the Digits Dataset
bundled with [Scikit-learn](https://scikit-learn.org/) to recognize handwritten digits, like those written in mail envelopes), simple linear regression, multiple linear regression (including an interesting case study where Scikit-learn is used to make sophisticated house pricing predictions from 8 numerical features), and K-Means Clustering (another interesting case study, using the Iris Dataset, where flowers are grouped into their species according to a prediction based on some of their features, like petal and sepal lengths and widths). 
![Python for Programmers - interior (chapter 14)]({static}/images/2019/python_for_programmers_interior_ch14.jpg)

Chapter 15 goes even deeper, focusing on Deep Learning, convolutional and recurrent neural
networks, with a computer vision case study. This time, the reader is invited to use the MNIST
database of handwritten digits, applying convolutional neural networks (using
[Keras](https://keras.io/)/[Tensorflow](https://www.tensorflow.org/)) to achieve a higher digit prediction accuracy. But first you'll get a brief explanation on neural networks and tensors. Then you will be able to get your hands in a recurrent neural network task, to implement a better sentiment analysis on IMDb movie reviews. 

Finally, on chapter 16, you get to know Apache Hadoop, Apache Spark, SQL (SQLite), NoSQL
(MongoDB), and a brief introduction to the IoT (Internet of things). As with the rest of the book, you'll also learn how to create interesting data visualizations.
![Python for Programmers interior chapter 16]({static}/images/2019/python_for_programmers_interior_ch16.jpg)


### Conclusions

It's a complex field, but this book makes the possible to keep it approachable for intermediate level programmers, while at the same time it provides an overview of some of the most usual topics. The authors managed to create a learning curve of growing complexity, so you should feel very confident through, at least, the first 10 chapters, if you have some experience with object-oriented programming. On the other hand, in case you are already a Python programmer, going through those initial chapters won't hurt and may very well serve you to recall the basics of Python, data analysis and data visualization. You will probably learn one or two useful bits. But you may also choose to take a shortcut, by reading each chapter's list of objectives and its "Wrap-Up" section, to check how comfortable you feel about the topics covered there.

The most interesting stuff, however, is presented in the second half of the book. After you read it and experiment with some of the examples provided, maybe you won't become a *certified data scientist* or an *A.I. Engineer*, but you will certainly have a much clearer idea of what A.I., machine learning and deep learning are all about. And you will be better prepared for further exploration in these fields. You'll notice that the authors include URLs for additional learning resources, that you may use to take your A.I. study into a deeper level.

Big Data and Artificial Intelligence are very interesting areas, that have now grown from an academic research niche to a wide range of applied techniques that spread across different scenarios and use cases, from manufacturing to e-commerce; from image, audio and video manipulation to gaming; from weather, election or earthquake prediction to generative art; and many more.

The book will give you a bird's eye over some of the applications and give you some hints on many others. In my opinion, it's designed, precisely, to help you get the first meaningful contact with these topics and then let you decide if you're willing to invest more time on that area. And, if you get through the whole book until the end, I bet you will.



**Get the book:**  
[www.amazon.com/dp/0135224330](https://www.amazon.com/dp/0135224330){:target=_blank}

<hr >
DISCLOSURE NOTICE: For this review, I received a free copy of the book from the publisher. I do not personally know the authors or the publishers, and did not receive any other compensation. The link to Amazon is provided as a reference only, I am not endorsing the company or making any profit from it. 