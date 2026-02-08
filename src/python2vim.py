#!/usr/bin/env python3
"""Map Python grammar to Vim syntax"""

import inspect
import keyword
import os.path
import sys

header = '''" Copyright (c) 2026 Robert Berry
"
" Vim syntax file
"
" Language: Python
" License:  MIT License
" Origin:   https://github.com/f4nb0y/vim-syntax-python

if exists("b:current_syntax")
  finish
endif

let s:_cpo = &cpo
set cpo&vim
'''

footer = '''
let b:current_syntax = "python"

let &cpo = s:_cpo
unlet s:_cpo

" vim: shiftwidth=2 softtabstop=2 expandtab'''


def die(msg: str):
    caller = inspect.stack()[1]
    sys.exit(f'{os.path.basename(caller.filename)}: {caller.lineno}: {msg}')


def groupKeywords() -> str:
    groups = {
        'None': 'Constant',
        'False': 'Boolean',
        'True': 'Boolean',
        #
        'break': 'Statement',
        'class': 'Statement',
        'continue': 'Statement',
        'def': 'Statement',
        'del': 'Statement',
        'global': 'Statement',
        'nonlocal': 'Statement',
        'pass': 'Statement',
        'return': 'Statement',
        'with': 'Statement',
        'yield': 'Statement',
        'elif': 'Conditional',
        'else': 'Conditional',
        'if': 'Conditional',
        'for': 'Repeat',
        'while': 'Repeat',
        'and': 'Operator',
        'is': 'Operator',
        'not': 'Operator',
        'or': 'Operator',
        'as': 'Keyword',
        'async': 'Keyword',
        'await': 'Keyword',
        'from': 'Keyword',
        'in': 'Keyword',
        'lambda': 'Keyword',
        'except': 'Exception',
        'finally': 'Exception',
        'raise': 'Exception',
        'try': 'Exception',
        #
        'import': 'Include',
        'assert': 'Debug',
    }

    for kw in groups:
        if kw not in keyword.kwlist:
            die(f'Unknown keyword: {kw}')
    for kw in keyword.kwlist:
        if kw not in groups:
            die(f'Ungrouped keyword: {kw}')

    return '\n'.join(
        ['" https://docs.python.org/3/reference/lexical_analysis.html#keywords']
        + [f'syntax keyword {k:15} python{v}' for k, v in sorted(groups.items())]
        + ['']
        + [f'highlight default link python{v:15} {v}' for v in sorted(set(groups.values()))]
    )


if __name__ == '__main__':
    print(header)
    print(groupKeywords())
    print(footer)
