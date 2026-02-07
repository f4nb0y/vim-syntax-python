# vim-syntax-python

Alternate syntax highlighting for Python in Vim

### Why?

The [Python syntax highlighting] in Vim was maintained by @nascheme and rewritten by @zvezdan. It contains many special cases, and some impressively dense regular expressions. It is also incomplete, and difficult to update.

This alternate syntax highlighting aims to:

- Support all current Python syntax, including archaic features such as `%` string formatting
- Support all default Vim [syntax groups], including constants, operators and types
- Test all highlighting with every change
- Enable all highlighting by default

### How?

This is the interesting part. Is it possible to mechanically translate Python parser definitions into a working syntax file?

[Python syntax highlighting]: https://github.com/vim/vim/blob/master/runtime/syntax/python.vim
[syntax groups]: https://vimhelp.org/syntax.txt.html#group-name
