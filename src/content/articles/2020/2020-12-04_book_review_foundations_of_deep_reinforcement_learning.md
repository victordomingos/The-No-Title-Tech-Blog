Title: Book review - Foundations of Deep Reinforcement Learning, by Laura Graesser and Wah Loon Keng
Date: 2020-12-04 01:00
Lang: en
Tags: python, books, Laura Graesser, Wah Loon Keng, machine learning, deep learning, reinforcement learning, learning, SLM Lab, data science, PyTorch	
Category: Book Reviews
Slug: book_review_foundations_of_deep_reinforcement_learning
Author: Victor Domingos
Cover: images/2020/deep_reinforcement_learning_cover.jpg
Summary: Deep Reinforcement Learning is a somewhat new field within Machine Learning or Artificial Intelligence (you may pick your favorite term between these two, even if they're not strictly the same), which combines Deep Learning and Reinforcement Learning and is based on the general idea that an agent can learn by observing its actions and their consequences. No, it is not a return to John B. Watson and B. F. Skinner's behavioral psychology. We are talking, instead, about a set of pretty advanced machine learning algorithms that, when properly mastered, allow computers to achieve remarkable results in some complex tasks. That's what this book is about, so let's dive in…

### Book structure and contents

*Foundations of Deep Reinforcement Learning - Theory and Practice in Python*  begins with a brief preliminary chapter, which serves to introduce a few concepts and terms that will be used throughout all the other chapters: agent, state, action, objective, reward, reinforcement, policy, value function, model, trajectory, transition. 

![Foundations of Deep Reinforcement Learning - Theory and Practice in Python - Chapter7]({static}/images/2020/deep_reinforcement_learning_ch1_intro.jpg)

If you are already familiar with some of these, great - you will probably enjoy reading the whole book. If you're not, you should at least take your time to let these terms become a little familiar before going on. This is not, in my opinion, a book intended for fast reading, and it's ok to go back and read again some of the previous pages to let this new terminology slowly take shape in your mind.

![Foundations of Deep Reinforcement Learning - Theory and Practice in Python - Chapter7]({static}/images/2020/deep_reinforcement_learning_ch3_sarsa.jpg)

After this introduction chapter, the book is organized in four parts. The first two parts ("Policy-Based and Value-Based Algorithms" and "Combined Methods") present several deep reinforcement learning algorithms, such as REINFORCE, SARSA, Deep Q-Networks (DQN), Advantage Actor-Critic (A2C), and Proximal Policy Optimization (PPO). The code examples are brief and are mostly based on [Numpy](https://numpy.org) and [PyTorch](https://pytorch.org), on top of [SLM Lab](https://slm-lab.gitbook.io/slm-lab/) (a companion library by the book authors). That allows to create a reproducible environment to play around with implementations of some of the algorithms described. Some of those environments, provided by [Open AI Gym](https://gym.openai.com) and made available in SLM Lab (a software utilized throughout the book), are based in well-known vintage Atari games like Pong or Breakout. That brings us a familiar task from a more ludic context, with simple requirements, that makes it easier to understand how the algorithm fits. 

The first algorithm, REINFORCE, is fully implemented in code using Numpy and PyTorch, but then the others are implemented using the SLM Lab framework. The usage of SLM Lab allows to minimize the amount of boilerplate code, which helps highlight the most important bits of the algorithms themselves. However, it has a potential drawback, which is the fact that some of the code samples are not quite self-contained. Aside from a learning context, you wouldn't probably use SLM Lab in production, you would want to use PyTorch directly, for instance.

![Foundations of Deep Reinforcement Learning - Theory and Practice in Python - Chapter7]({static}/images/2020/deep_reinforcement_learning_ch5_dqn.jpg)

The authors also mention briefly in the introduction the existence of model-based algorithms, but in this book, they opted to focus on policy and model-based ones. The information is presented with some equations that, depending on your background, you may consider either quite complex or quite simple, but usually the authors explain the general idea in the text and sometimes with an algorithm nicely represented in pseudo-code. 

![Foundations of Deep Reinforcement Learning - Theory and Practice in Python - Chapter7]({static}/images/2020/deep_reinforcement_learning_ch7_ppo.jpg)

If you survived those first two hundred pages, you will be ready to take a pause, in a certain sense. The third part of the book ("Practical Details") discusses other important topics that are needed to make these algorithms work in practice, like software engineering practices (unit tests, code quality, git workflow), debugging, algorithm performance comparison, SLM Lab, types of neural networks (MLPs, CNNs, RNNs), and hardware considerations. 

![Foundations of Deep Reinforcement Learning - Theory and Practice in Python - Chapter7]({static}/images/2020/deep_reinforcement_learning_ch12_network.jpg)

The four chapters in last part of the book ("Environment Design") return to some of the concepts that were presented earlier (states, actions, rewards and transition function) and give some practical examples. That return to a concrete approach helps to make a bit clearer how the data is prepared and manipulated throughout the process of training and testing. It also discusses some practical issues and technical challenges that arise when attempting to apply this kind of algorithms and techniques to solve real world problems.


### Conclusions

I must confess that I often felt that there was a lot of field specific terminology in this book, making it a bit challenging to follow through. But to be honest, I really think that it had more to do with me as reader than it has with the book itself. In first place, because there were a few mathematical concepts and notation symbols that I am simply not familiar with. You see, my academic background is in Psychology, and all the Math I needed to study back then was some social sciences related topics, like statistics, probability, distributions, and the like. And while in the last few years I have been more into computer programming, this is still a very specific field that happens to make use of a programming language, one where I am sure a more advanced knowledge in Math and Machine Learning can really help.

*Foundations of Deep Reinforcement Learning* can be seen as kind of an advanced introduction for well-prepared ML students. Which I am not, by the way. And why do I mention this? Well, because it seems to me that it is very important to select the right learning resources for each learning stage, the ones that give you the bits you need to progress. So, for instance, if you are just getting into Python programming or even trying out some basic machine learning tutorials for the first time, this is not the right book for you. However, if you already have a broad understanding of how machine learning works, with some math or engineering background, and if you have been studying some topics on deep learning and reinforcement learning, this will most likely be the best book for the next step in your learning path.


**Get the book:**  
[informit.com/store/foundations-of-deep-reinforcement-learning-theory-and-9780135172384](https://www.informit.com/store/foundations-of-deep-reinforcement-learning-theory-and-9780135172384){:target=_blank}

<hr ><small>
<strong>Disclosure Notice:  </strong>
For this review, I received a free copy of the book from the publisher. I do not personally know the authors or the publishers, and did not receive any other compensation. The link to the publisher is provided as a reference only, I am not endorsing the company or making any profit from it. 
</small>
