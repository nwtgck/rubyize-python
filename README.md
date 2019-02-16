# rubyize

![Rubyize logo](logo.png)

| branch | Travis status|
| --- | --- |
| [`develop`](https://github.com/nwtgck/rubyize-python/tree/develop) | [![Build Status](https://travis-ci.com/nwtgck/rubyize-python.svg?token=TuxNpqznwwyy7hyJwBVm&branch=develop)](https://travis-ci.com/nwtgck/rubyize-python) |

Write Python in Ruby-like way

## Installation

```bash
pip3 install toml
pip3 install git+https://github.com/nwtgck/rubyize-python
```

## Usages

Here is an import-magic for adding methods to collection classes such as `list`.

```py
import rubyize
```

```py
[1, 2, 3].length()
# => 3

[1, 2, 3].map(lambda x: x*2)
# => [2, 4, 6]

[1, 2, 3].filter(lambda x: x % 2 == 0)
# => [2]

[1, 2, 3].inject(lambda s, e: s + e)
# => 6

[1, 2, 3].inject(100, lambda s, e: s + e)
# => 106

[1, 2, 3].take(2)
# => [1, 2]

[1, 2, 3].drop(2)
# => [3]

[1, 2, 3, 4, 5, 6].group_by(lambda e: e % 2 == 0)
# => {True: [2, 4, 6], False: [1, 3, 5]}

[1, 2, None, 4, None, 6].compact()
# => [1, 2, 4, 6]

[1, 2, 3].flat_map(lambda e: [e] * 2)
# => [1, 1, 2, 2, 3, 3]

[1, 2, 3, 4, 5].each_cons(3)
# => [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

[1, 2, 3, 4, 5].each_slice(2)
# => [[1, 2], [3, 4], [5]]

[1, 2, 3, 4, 5].join(',')
# => "1,2,3,4,5"
```

## Not only list

```py
map(lambda e: e, [1, 2, 3]).map(lambda x: x * 2)
map(lambda e: e, [1, 2, 3]).length()
map(lambda e: e, [1, 2, 3]).take(2)
...
```

## Why Rubyize?

Collection API of Ruby is very rich! Ruby has prepared a lot of methods. So, users can write easily about what they want to do. Users make method chains, which are directly connected to our brain thinking rather than built-in `len(mylist)`, `len(mylist)`  and etc, I think.

## Caution

Rubyize can destroy the Python culture. I think that Python is designed for everyone writing in the same way. However, Rubyize allows users to write code in different ways. Readability in terms of the Python culture can be worse. Thus, I think Rubyize should not be used in production. Rubyize should be used in disposable code or etc.

## Forbidden Fruit

This project is powered by [Forbiddenfruit](https://github.com/clarete/forbiddenfruit).
