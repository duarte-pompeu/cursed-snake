
cursed-snake
=====

Snake game in a terminal window using python and lib curses.


[![asciicast](https://asciinema.org/a/P1beJzsxA6GlYbmR3zZ9K2Tl5.svg)](https://asciinema.org/a/P1beJzsxA6GlYbmR3zZ9K2Tl5)

# History:

- 2015: develop the game while learning python 2
- 2017: add the MIT license
- 2021: 
	- port to python 3
	- add support to poetry to manage packages and use virtual envs
	- create a Makefile and add container support
	- improve graphics

# Platform / Terminal support

Unfortunately, curses support depends on the terminal used.

## Windows


Worked in VS Code, using a bash shell, and also on CMD. Simply run `make run`.

To use with with *git bash*, need to use `make run-win`. 


## Linux

Should work with most terminals.


