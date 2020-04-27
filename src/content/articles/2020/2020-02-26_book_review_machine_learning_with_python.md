Title: Book review - Machine Learning with Python for Everyone, By Mark E. Fenner
Date: 2020-02-26 02:10
Lang: en
Tags: python, books, Mark E. Fenner, machine learning, learning, Scikit-learn, data science, Numpy, Pandas,
Category: Programming
Slug: book_review_machine_learning_with_python
Author: Victor Domingos
Cover: images/2020/machine_learning_with_python__book_cover.jpg
Summary: Machine learning, one of the hottest tech topics of today, is being used more and more. Sometimes as the best tool for the job, other times perhaps as a buzzword that is mainly used as a way to make a product look cooler. However, without knowing what ML is and how it works behind the scenes, it’s very easy to get lost. But this book does a great job in guiding you all the way up from very simple math concepts to some sophisticated machine learning techniques.

Today, in the Python ecosystem, we have available a plethora of powerful data science and machine learning related packages, like `Numpy`, `Pandas`, `Scikit-learn`, and many others, that help to simplify a lot of its inherent complexity. In case you are wondering, in terms of Python packages, the great hero in this book is Scikit-learn, often abbreviated as `sklearn`. Of course, the data wrangling is much easier and much faster using Numpy and Pandas, so these two packages are always covering sklearn’s back. `Seaborn` and `Matplotlib`, two of the most standard data visualization packages for Python, are also used here. In chapter 10, `patsy` makes a brief appearance, and in chapter 15 `pymc3` is used in the context of probabilistic graphic models.

Having these tools, you need to pick the right model (and before that you need to know what a model is and how it’s meant to be used) and be able to test its results. Then, how can you be sure that you have really picked the model that better fits your data and which gives the most accurate predictions? You need to validate it and compare it with other algorithms, or even with a different set of hyper-parameters. It quickly starts to get complicated…

### Book structure and contents

The book is organized in four parts, each one divided into three or four chapters. With exception for the first two introductory chapters, all the others end up with some suggestions of exercises that you can use to apply your knowledge on a different dataset, or to solve a different problem.

![Machine Learning with Python for Everyone - Chapter 7]({static}/images/2020/machine_learning_with_python__ch7.jpg)

As a side note, some of the graphs in the book are not very easy to understand in grayscale, which is not ideal. In order to make this book a bit more affordable, the publisher opted to provide an URL to download color PDFs of figures. So, if you buy this book in print, make sure you also download those files, because the presence of color really helps to better understand some concepts being explained.

In **Part I** (“First Steps”), you’re introduced to the idea of machine learning, clarifying the meaning of some common concepts like features, target values, predictions, classification, regression, and the importance of evaluating the correctness and the resource consumption of learning systems. 

![Machine Learning with Python for Everyone - Chapter 1]({static}/images/2020/machine_learning_with_python__ch_1.jpg)

Chapter 2 makes sure that you are provided with some useful mathematical vocabulary that will be essential to understand the rest of the book. On chapter 3, you will find  the first classification algorithms, k-Nearest Neighbors (kNN) and Naive Bayes (NB), as well as a simplistic evaluation of those two classifiers. Chapter 4 does the same for regression, applying kNN regression and linear regression to a simple dataset, and then showing how to evaluate the results in terms of their accuracy and resources utilization.

**Part II** (“Evaluation”) is like a stopping point to discuss in more depth how important it is to evaluate and compare learners, and how to do it. That includes going through training, selection and assessment phases while developing a learning system. 

![Machine Learning with Python for Everyone - Chapter 5]({static}/images/2020/machine_learning_with_python__ch_5.jpg)

Once again, you will be introduced to some new concepts, like train-test splits, hold-out tests (HOT), validation, cross-validation, over-fitting, under-fitting, loss, cost, bias, variance. You will see how to graph learning curves to determine the best amount of data to be used in training, how to generate and interpret a confusion matrix, a ROC curve, and more. 


![Machine Learning with Python for Everyone - Chapter 5]({static}/images/2020/machine_learning_with_python__ch_5b.jpg)

In chapter 7 you also get a brief discussion on data standardization and pipelines as sequences of training and testing steps.

After that stopping point, **Part III** goes on to teach you some other methods of classification (Decision Trees, Support Vector Classifiers, Logistic Regression, and several flavors of Discriminant Analysis) and regression (Support Vector Regression, Piecewise Constant Regression, Regression Trees). Chapter 10 talks about feature engineering, which is a fancy name for some techniques used to add, delete, combine and transform the features being considered in the learning system, including scaling, discretization and categorical coding. Chapter 11 closes part III showing a few way you can use to find out the best hyper-parameters (like the `k` in k-Nearest Neighbors) for your models, so that you don’t have to guess them and don’t take the risk of creating a learning system that is unnecessarily inaccurate or too complex. It also shows how to use pipelines to streamline learning tasks that are composed from multiple steps.


The remaining four chapters in the book (**Part IV**) cover more advanced or more complex techniques, like combining learners (Voting Ensembles, Random Forests, and Boosting), feature selection, feature construction with kernels and Principal Component Analysis (PCA). 

![Machine Learning with Python for Everyone - Chapter 12]({static}/images/2020/machine_learning_with_python__ch12.jpg)

Chapter 14 is particularly interesting because it covers some of the ways to perform feature engineering in some specific domains, like when dealing with text or images. Here you will also learn about clustering, with is, like PCA, an unsupervised learning technique (*unsupervised* means that the system learns from data that has not been previously labeled). 

![Machine Learning with Python for Everyone - Chapter 15]({static}/images/2020/machine_learning_with_python__ch_15.jpg)

The last chapter (ch. 15) gives you some hints on some other important, but also advanced, topics that you might be interested, like optimization, SVM, linear and logistic regression from raw materials, neural networks and probabilistic graphical models.


### Conclusions

What I liked more about this book is the way the author presents each topic, starting with the very basics of the underlying math concepts, often with a fun little story, and then growing all the way up to the higher level machine learning concepts or procedures. 

![Machine Learning with Python for Everyone - Decision Trees]({static}/images/2020/machine_learning_with_python__DecisionTrees.jpg)

Even if, like myself, you feel that your math classes have long been forgotten, this book will help you to pick at the point you need. For instance, chapter 2 presents probability, distributions, weighted sums, dot products, as well as a refresh on geometry (2D/3D graphs, polynomials). It will help you to be able to read those equations throughout the book. The author was very careful indeed to include simple mathematical formulas just as needed, and always explaining them step by step, bit by bit. So that you don’t need to have studied graduate level linear algebra in order to be able to understand most of the book. 

![Machine Learning with Python for Everyone - Equations]({static}/images/2020/machine_learning_with_python__equations.jpg)

I must confess that at some point I felt like I was back in school, studying little bits of math, but this time just the bits I needed, when I needed them. Oh, boy! I had some great Math teachers back then, but I wish I could have this kind of contextualized and entertaining explanations. Throughout most of the book, there is a playful tone and a well paced flow, that make for a very pleasant reading. Of course, there are some parts that you may still find harder to grasp but, honestly, there’s not much more that could be done in that regard.

Machine learning allows computers to achieve surprising and extraordinary results in many different contexts. The flip side of the coin, however, is that it can be overwhelming, requiring  either a huge computational power, or a strong background in Maths, or even both. This book is an amazing guide that shows how machine learning works and makes it very approachable, even for people who don’t have an academic background in Maths. All you need is some basic Python knowledge and a bit of curiosity to get you started through the first few pages.


**Get the book:**  
[pearson.com/us/higher-education/program/Fenner-Machine-Learning-with-Python-for-Everyone/PGM1878196.html](https://www.pearson.com/us/higher-education/program/Fenner-Machine-Learning-with-Python-for-Everyone/PGM1878196.html){:target=_blank}

<hr ><small>
<strong>Disclosure Notice:  </strong>
For this review, I received a free copy of the book from the publisher. I do not personally know the authors or the publishers, and did not receive any other compensation. The link to the publisher is provided as a reference only, I am not endorsing the company or making any profit from it. 
</small>
