# vim-syntax-python

Alternate syntax highlighting for Python in Vim.

### Why?

There are many options to highlight Python syntax in Vim:

- https://github.com/vim/vim/blob/master/runtime/syntax/python.vim was originally maintained by
  @nascheme, then rewritten by @zvezdan in 2010. It contains many special cases, and some
  impressively dense regular expressions. It is also incomplete, and difficult to update.

- Many folks recommend https://github.com/sheerun/vim-polyglot which loads
  https://github.com/vim-python/python-syntax, which was last updated in 2020 for the `:=` operator.

- There is also https://github.com/kh3phr3n/python-syntax (2021),
  https://github.com/hdima/python-syntax (2015), https://github.com/pfdevilliers/Pretty-Vim-Python
  (2013) and https://www.vim.org/scripts/script.php?script_id=790 (2013).

Syntax highlighting is a fun project with immediate results, but edge cases multiply as more 
features are added. None of these projects support all of Python's syntax.

### What?

This project aims to:

- Highlight all valid Python syntax, including archaic features such as `%` string formatting
- Support as many Vim syntax groups as possible, including constants, operators and types
- Enable all highlighting by default, and make non-syntax conventions optional
- Test all highlighting and rebuild regularly to detect changes
- Be easy for others to update or fork

### How?

This is the interesting part. Is it possible to mechanically translate Python [grammar] into Vim
[syntax]?

[grammar]: https://docs.python.org/3/reference/grammar.html
[syntax]: https://vimhelp.org/syntax.txt.html
