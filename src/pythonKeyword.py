#!/usr/bin/env python3
'''Map Python keywords to Vim syntax items'''

from collections import defaultdict
import inspect
import keyword
import os.path
import sys

keywordGroups = {
    'False': 'Boolean',
    'None': 'Boolean',
    #
    'True': 'Constant',
    #
    'and': 'Operator',
    'is': 'Operator',
    'not': 'Operator',
    'or': 'Operator',
    #
    'elif': 'Conditional',
    'else': 'Conditional',
    'if': 'Conditional',
    #
    'for': 'Repeat',
    'while': 'Repeat',
    #
    'except': 'Exception',
    'finally': 'Exception',
    'raise': 'Exception',
    'try': 'Exception',
    #
    'as': 'Include',
    'import': 'Include',
    'from': 'Include',
    #
    'assert': 'Keyword',
    'async': 'Keyword',
    'await': 'Keyword',
    'break': 'Keyword',
    'class': 'Keyword',
    'continue': 'Keyword',
    'def': 'Keyword',
    'del': 'Keyword',
    'global': 'Keyword',
    'in': 'Keyword',
    'lambda': 'Keyword',
    'nonlocal': 'Keyword',
    'pass': 'Keyword',
    'return': 'Keyword',
    'with': 'Keyword',
    'yield': 'Keyword',
}


def die(msg: str):
    caller = inspect.stack()[1]
    sys.exit(f'{os.path.basename(caller.filename)}: {caller.lineno}: {msg}')


if __name__ == '__main__':
    for kw in keyword.kwlist:
        if kw not in keywordGroups:
            die(f'Ungrouped keyword: {kw}')

    for kw, group in sorted(keywordGroups.items()):
        print(f'syntax keyword {kw:15} python{keywordGroups[kw]}')
    print()

    for group in sorted(set(keywordGroups.values())):
        print(f'highlight default link python{group:15} {group}')
