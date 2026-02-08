#!/usr/bin/env python3
"""Map keywords to syntax groups"""

import inspect
import keyword
import os.path
import sys

kwGroups = {
    # https://vimhelp.org/syntax.txt.html#group-name
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


def die(msg: str):
    caller = inspect.stack()[1]
    sys.exit(f'{os.path.basename(caller.filename)}: {caller.lineno}: {msg}')


if __name__ == '__main__':
    for kw in kwGroups:
        if kw not in keyword.kwlist:
            die(f'Unknown keyword: {kw}')
    for kw in keyword.kwlist:
        if kw not in kwGroups:
            die(f'Ungrouped keyword: {kw}')

    for kw, group in sorted(kwGroups.items()):
        print(f'syntax keyword {kw:15} python{kwGroups[kw]}')
    print()
    for group in sorted(set(kwGroups.values())):
        print(f'highlight default link python{group:15} {group}')
