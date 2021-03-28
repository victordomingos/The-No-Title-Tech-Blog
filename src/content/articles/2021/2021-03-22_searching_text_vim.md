Title: Searching and replacing text on long files with Vim
Date: 2021-03-28 16:00
Lang: en
Tags: vim, console, terminal, linux, haiku, macos, text editor, tutorial, shell, unix
Category: Tutorials
Slug: searching_text_vim  
Author: Victor Domingos
Cover: images/2021/vim_searching.png
Summary: You may wonder how I came up with this topic. I usually code in a graphical IDE like PyCharm or Visual Studio, or even a text editor like VS Code or BBEdit. But sometimes you need some lightweight application that is capable of opening and efficiently edit a file. I often return to VIM for quick edits in small files. Sometimes, just for the convenience of not leaving the shell. Other times, because it's a powerful editor that runs perfectly under a SSH connection. And a few days ago, it was the only application I had installed on Windows which would let me open, navigate and read a several GB heavy text file without complaining. 

You see, even though I tend to prefer other editing environments, these situations occur quite often to me. So I don't mind learning small bits of VIM every now and then. It is an investment that pays itself, sooner than later. A testament to that are the facts that it has been around for about 30 years, it is [still in active development](https://github.com/vim/vim) (including several alternative forks like [NeoVim](https://neovim.io), [SpaceVim](https://spacevim.org) and [PyVim](https://github.com/prompt-toolkit/pyvim)), it is based on [vi](https://en.wikipedia.org/wiki/Vi) (a much older Unix editor), it is included by default in some well known operating systems.

In a previous article, I wrote [a brief introduction to Vim]({filename}/articles/2019/2019-08-09_get_started_with_vim.md) on which I presented the basics of this editor. Please feel free to take a minute or so to read it now, in case you're not yet familiar with VIM. Today I would like to expand a little on this topic, and show how easily you can use it to search for some text. 

## How search for a given text pattern?
Suppose you are looking for the word 'worker'. First make sure you are in Normal mode (just press `ESC` if you're unsure), then press `/` to start searching. After the `/` character you may write a text pattern to search like this:

	/worker

Then press `ENTER` and all the occurrences of that text bit will be highlighted. You can navigate through them using these keys:

 - `n` (lowercase N) - jump to next occurrence (search forwards)
 - `N` (uppercase N) - jump to previous occurrence (search backwards)
 
You can make the search case-insensitive by appending `\c` to the command. The following command would match any occurrences of the text "broken", regardless of the capital B, for instance:

	/broken\c

## More on text patterns

You can use simple words or even regular expressions as search patterns, which largely expands the kind of search you are able to do. Even if you don't feel very comfortable using cryptic regular expressions, these simple symbols may be quite helpful without complicating too much:

- `^` - line start (more specifically, the first *non-blank* character of the line)
- `$` - line end

- `\<` - beginning of a word (separated by space or punctuation)
- `\>` - end of a word (separated by space or punctuation)

- `.*` - any number of any characters (wildcard)

For instance, the `\<import\>` pattern will match `import` as an individual word, and `^import`  will match `import` at the beginning of the line. 

In case you want the search or replace operations to match either one of two text patterns, there is an "or" operator:

- `\|` - the "or" operator 

Merging some of the above together, imagine you want to search all the occurrences of either `if` or `else` as individual words, but not as part of other words (like `exif`):

```
/\<if\>\|\<elif\>
```


By the way, it can be very useful to know a nice shortcut which is using `*` in Normal Mode to quickly jump to the next occurrence of the current word. You don't even need to type a command, just enter Normal mode using `ESC` and place the cursor in the word you want to use. 

The slash character `/` used in these commands can be replaced with another non-alphanumerical character, which can be handy when you need to search/replace text that contains the slash character. In the following example, the slash character `/` will mean the slash character itself in the text pattern and the pipe character `|` will serve as the command parameter separator:

```
:s|pattern/to/search
```

In case you need to delete the searched string in the text, you may provide an empty replacement string using two slashes without any characters between them (`//`):

- `:s/pattern-to-search//g)` - deletes all matching occurrences in the current line (`g`).

Which takes us to the next section in this article, on how to substitute text.

## How to search and replace text?

Now that you know how to search for some text, you may want to replace it. There's a command for that. Enter Command-Line Mode (`ESC :`) (remember, when in Command-Line mode, in the examples below, the initial colon `:` is part of the command) and type `:s/` followed by the text pattern to search, then another slash and the text to be used as replacement. Remember: the `s` here does not stand for `search`, in this context `:s` means `:substitute`. This would replace the string `pattern-to-search` with `replacement-string`:

```
    :s/pattern-to-search/replacement-string
```

Well replacing text without confirmation can be dangerous, so you can add `/c` and Vim will ask for confirmation before each substitution. The message presented looks like this:

```
replace with ProcessPool (y/n/a/q/l/^E/^Y)?
```

There are several reply options indicated between the parenthesis, just press the character corresponding to your need. For the sake of conciseness, I will just explain a few:

- `y` - substitute this match
- `n` - skip this match
- `a` - substitute *all* remaining matches, including this one.
- `q` - quit the command
- `l` (lowercase L) - substitute only this match and quit the command, treating it as the *last* match to replace.


## Specifying where to perform the search/replace operation

Sometimes you have a long text file but you only need to search/replace within a known internal of lines. You can specify the range like in the following examples:

- `:10,90s/pattern-to-search/replacement-string/gc` - search and replace any occurrences between lines 10 and 90 (`gc` indicates all occurrences in that line, asking for confirmation).

- `:%s/pattern-to-search/replacement-string/g` - search and replace any occurrences in the *whole* file (`%` indicates all lines), without confirmation (notice the `g` option, instead of `gc`).

- `:.,10s/pattern-to-search/replacement-string/g` - search and replace any occurrences between the current line (indicated by the `.`) and line number 10.

- `:.,$s/pattern-to-search/replacement-string/g` - search and replace any occurrences between the current line (indicated by the `.`) and last line (indicated by the `$`).

You may also start in current line and specify how many lines to process counting from that line, using `+` followed by the number of lines:

- `:.,8s/pattern-to-search/replacement-string/g` - search and replace any occurrences between the current line (indicated by the `.`) and next 8 lines (indicated by `+8`).

- `:%s/pattern-to-search//g)` - deletes all matching occurrences in the whole file (`%`).


## Final thoughts
Vim is a very complex application which packs a large number of features, and learning all of then can be challenging, to say the least. But learning the basics is not that hard, and paves the way to use it in a lot of simple everyday tasks, sometimes making your work a lot easier. 

I hope this article, together with the previous one, can help you quickly get started with Vim and let you add it as one more useful tool in your toolbox. And remember, you don't need to memorize all these commands and keyboard shortcuts at once. You can always bookmark this page and get back to it when you need it. ;-)
