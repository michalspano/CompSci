## High school exam - Exercises

The following directory contains a list of exercises that I worked on whilst
preparing myself for the **High school exam** (in Slovakia) called
["Maturita"](https://en.wikipedia.org/wiki/Matura).

The exercises are taken from the book ["Maturujeme v Pythone"][book-slovak],
the English variant of the book is called ["Creating with Python"][book-english].

The exercises have been worked on between the years 2022-2024. It may be the
case that at the time you're reading this file, the order of the exercises (or
their content) has changed. Nevertheless, I hope that the exercises will help
you to prepare for the exam or to get better at programming in Python.

I'm aware that the the book provides solutions to the exercises, however, I felt,
at the time of reading the book, that the suggestions were not always the best
practice, so I decided to solve some of the exercises in a different way. See the
inline comments for additional information of each exercise.

### Custom script

I made an additional script which tracks which exercises are in the directory
and it picks a random exercise for you to solve. I found this to be useful when
crunching for the exam. The script is called `rand_ex.py`. You can use it
in the following manner

```sh
# Executed from the high school exam directory
./rand_ex.py --read # -r
# This reads all the exercises in the directory and sorted them to a file sorted.txt.
# Each exercise has its own sub-directory.
./rand_ex.py --pick # -p
# Picks a random exercise from the sorted.txt file.
```

[book-slovak]: http://creatingwithpython.com/eknihy.html#mvp
[book-english]: http://creatingwithpython.com/eknihy.html#spwp
