Title: Get started with Git!
Date: 2019-10-30 22:00
Lang: en
Tags: git, console, terminal, tutorial, shell, version control 
Category: Tutorials
Slug: get_started_with_git  
Author: Victor Domingos
Cover: images/2019/git.png
Summary: When doing software or web development, you should have your code (and even other kinds of files) managed by a version control system, so that you are able to backup meaningful changes, checkout a file from a previous version, or collaborate with your team more efficiently. Over the years there have been some tools that serve for this purpose, but these days Git seems to be the most popular version tracking system.

Basically, Git provides a way to manage multiple versions of the files in your project. With remote repositories, you'll have the additional benefits of a permanent off-site backup and powerful collaboration tools.

Please keep in mind that, while there are a few famous online services that allow you to create remote git repositories (for instance, [GitHub](https://github.com), [GitLab](htts://gitlab.com), [Sourceforge](https://sourceforge.net), among others), they are not the same thing as Git, which is one of the many technologies they use. Git can also be used independently, but you may arrive to the conclusion that having a private or public remote repository can become very handy in a number of situations. And, in fact, those websites offer some additional features that are useful, like publicly accessible issue trackers for open source projects, easy to use web interfaces for code review and, perhaps even more important, great open source developer communities that help each other in a lot of cool projects.

### Before you begin: install `git`
`git` is a command-line application which can be installed in most operating systems and which allows us to interact with git repositories. There are Integrated Development Environments (IDE) and other specialized applications that offer graphical user interfaces (GUI), but at this time it is enough to use the command-line shell, which by the way is often a more practical tool. 

You can download the installers for the `git` command from the website [git-scm.com](https://git-scm.com/), where you can also find useful documentation on how to use it. If you work with Visual Studio on Windows, you can also install Git from the Visual Studio Installer application.



### Creating a local copy (clone) of a repository 

When we need to create a local copy of an existing remote repository, in order to be able to explore its code and documentation in our own computer, to compile and use an application, or to start collaborating with that project, we use the command `git clone`:

```console
$ git clone https://github.com/victordomingos/EFAProg2019
Cloning into 'EFAProg2019'...
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 12 (delta 2), reused 3 (delta 1), pack-reused 0
Unpacking objects: 100% (12/12), done.
```

This command will create a new folder inside the current working directory, and inside it there will be a copy of all the files from that repository. This copy is what we call a clone. So, it may be a good idea to start by using the `cd` command first, to change the working directory to the folder where we want to keep our `git` repositories.


### Creating a new local repository

If what you want is to create a new (empty) repository in your computer, even if you intend to make it available later on GitHub or any other server, first you need to create the project's folder (in case it does not exist yet). Then, use the command `cd` to get into that folder. Finally, the following command will initialize a new local repository on that project's folder:

```console
$ mkdir Brinquedo6
$ cd Brinquedo6/
$ git init
Initialized empty Git repository in C:/Users/victor/dev/Brinquedo6/.git/
```


### Creating a new local repository from an existing folder

If you already have in your computer a folder that you want to transform into a repository, that's also possible. First, you need to initialize the repository with `git init` and then add all of its content `git add .` (this command adds all the content of the current folder into the staging area). The `git commit` command, which we will show in a section below, will save that initial repository state.



### Setting up a list of files and folders to ignore

During software development it is very common to have files and folders that don't need to be added to the version control system. For instance, temporary files that are created when you compile an application, some generated binary executable files, and many others. The easiest way to automatically exclude all those files is to add a file named `.gitignore` to the project's root directory.

The website [www.gitignore.io](https://www.gitignore.io) makes it very easy to generate that file based on your operating system, programming language and/or the IDE you are using. In [this GitHub repository](https://github.com/github/gitignore), there are also dozens of ready to use `.gitignore` files, including one for [Visual Studio](https://github.com/github/gitignore/blob/master/VisualStudio.gitignore).


### Getting the most recent changes from the remote repository

In order to make sure you're working with the most recent version of the project, I mean, to be sure that the files in your local repository is synchronized with the remote repository, start by going into the repository folder and then use the `git fetch` command.

```console
$ cd EFAProg2019/
$ git fetch
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/victordomingos/EFAProg2019
   ed77901..121f33d  master     -> origin/master
```

The command `git status` allows you to check if there are any pending changes:

```console
$ git status
On branch master
Your branch is behind 'origin/master' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean

```

In case there are more recent changes in the remote repository, the command `git pull` allows us to get our local repository up to date with those changes. 

```console
$ git pull
Updating ed77901..121f33d
Fast-forward
 README.md | 14 ++++++++++++--
 1 file changed, 12 insertions(+), 2 deletions(-)

$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```



### Sending local changes to the remote repository

After making changes to our local repository, like for instance file creation, deletion or renaming, or file content changes, we can save the current state performing an operation called `commit`. But first we need to prepare that `commit`, adding the folders and files that we want to include:

```console
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

$ git add README.md
```

Once again, the `git status` command allows us to check for any pending operations, or as in this case, any changes being staged to commit:

```console
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   README.md
```

By entering `git commit` we then save the current repository state (with regard to the files and folders we previously added with `git add`):

```console
$ git commit -m "Conteúdo adicional no ficheiro README.md"
[master ef23443] Conteúdo adicional no ficheiro README.md
 1 file changed, 131 insertions(+), 94 deletions(-)
 rewrite README.md (67%)
```

At this moment, a quick check to the output of `git status` clarifies that even though there aren't any files or folders to register into a new `commit`, our repository is ahead of the remote repository:

```console
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
``` 

In order to send these changes to the remote repository (which, in this example, is hosted on GitHub), we just need to use the `git push` command:

```console
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 382 bytes | 95.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/victordomingos/EFAProg2019
   c638269..cb2faf6  master -> master
```

### Final thoughts

So, there you have it, a short guide to get started with Git, which is both powerful and pretty complex tool. There are many aspects of Git that couldn't fit in an introductory guide like this, and many other features that I confess I am still learning each day. However, by using these simple commands you can already make a basic use of Git in your own projects, and I hope it will help you by serving as a base to start using and learning it.
