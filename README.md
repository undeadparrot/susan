susan - notes & ad-hoc wiki
===========================

```
   _____
  / ___/__  ___________ _____
  \__ \/ / / / ___/ __ `/ __ \
 ___/ / /_/ (__  ) /_/ / / / /
/____/\__,_/____/\__,_/_/ /_/
```
[![PyPI version](https://badge.fury.io/py/susan.svg)](https://badge.fury.io/py/susan)
[![GitHub version](https://badge.fury.io/gh/undeadparrot%2Fsusan.svg)](https://badge.fury.io/gh/undeadparrot%2Fsusan)
[![Build Status](https://travis-ci.org/undeadparrot/susan.svg?branch=master)](https://travis-ci.org/undeadparrot/susan)
[![BCH compliance](https://bettercodehub.com/edge/badge/undeadparrot/susan?branch=master)](https://bettercodehub.com/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2ba162c956b348c8b7cb4f246aa9c27a)](https://www.codacy.com/app/smatuszeksa/susan?utm_source=github.com&utm_medium=referral&utm_content=undeadparrot/susan&utm_campaign=badger)

Susan is a very simple note-taker and wiki tool for the command line / cli.

Usage
-----

The first command you should type is `susan` because it shows the help. All subcommands have help through `--help`. To get things done, you'll mostly be interested in `susan note` and `susan head`.

### aliases

I recommend making some short aliases for common `susan` subcommands. For example

```
alias susn "susan note"
alias sush "susan head"
alias suhh "susan head -1" #this only prints the top note
```

### susan note

```
> susan note "Write this on the default topic"
> susan note "This is another note"
```

```
> susan note -ttodo "I have so much todo"
```

### susan head

```
> susan head
This is another note
Write this on the default topic
```

```
> susan head todo
I have so much todo
```

License 
-------------------
MIT License

Copyright (c) 2017 Shane Matuszek 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
