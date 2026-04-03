# NOTES

### Character Classes

From https://docs.python.org/3/reference/lexical_analysis.html#names-identifiers-and-keywords

> Names are composed of the following characters:
>
> * uppercase and lowercase letters (`A-Z` and `a-z`),
> * the underscore (`_`),
> * digits (`0` through `9`), which cannot appear as the first character, and
> * non-ASCII characters. Valid names may only contain “letter-like” and “digit-like” characters; see Non-ASCII characters in names for details.

So we need corresponding Vim character classes, and the obvious starting point is https://vimhelp.org/pattern.txt.html#%2F%5Cw

    \w  word character:                 [0-9A-Za-z_]    /\w
    \W  non-word character:             [^0-9A-Za-z_]   /\W
    \h  head of word character:         [A-Za-z_]       /\h
    \H  non-head of word character:     [^A-Za-z_]      /\H

But this doesn't include Unicode identifier classes. A better option appears to be https://vimhelp.org/pattern.txt.html#%2F%5Ci

    \i  identifier character (see 'isident' option)     /\i
    \I  like "\i", but excluding digits                 /\I

But when we follow the reference to https://vimhelp.org/options.txt.html#%27isident%27, we see

    For '@' only characters up to 255 are used.

In contrast, https://vimhelp.org/options.txt.html#%27iskeyword%27 says

    For '@' characters above 255 check the "word" character class (any
    character that is categorized as a letter, number or emoji according
    to the Unicode general category).

Which takes us back to to https://vimhelp.org/pattern.txt.html#%2F%5Ck

    \k	keyword character (see 'iskeyword' option)	/\k
    \K	like "\k", but excluding digits			/\K

This appears to be our best option?
