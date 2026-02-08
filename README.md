# vim-syntax-python

Alternate syntax highlighting for Python in Vim

### Why?

The [Python syntax highlighting] in Vim was originally maintained by @nascheme and rewritten by
@zvezdan in 2010. It contains many special cases, and some impressively dense regular expressions.
It is also incomplete, and difficult to update.

This alternate syntax highlighting aims to:

- Support all valid Python syntax, including archaic features such as `%` string formatting
- Support all default Vim [syntax groups], including constants, operators and types
- Test all highlighting with every change
- Enable all highlighting by default

### How?

This is the interesting part. Is it possible to mechanically translate Python [grammar] into Vim
[syntax]?

[grammar]: https://docs.python.org/3/reference/grammar.html
[python syntax highlighting]: https://github.com/vim/vim/blob/master/runtime/syntax/python.vim
[syntax]: https://vimhelp.org/syntax.txt.html
[syntax groups]: https://vimhelp.org/syntax.txt.html#group-name
