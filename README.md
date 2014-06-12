# Befunge-93 Interpreter

This is a Befunge-93 interpreter written in python 3.4 with the use of pygame. The code has not properly been tested on python 2.X.

Johan Asplund

## How to use
Run the script as ``python befunge.py arg1 arg2``, where ``arg1`` is the befunge code, and where  ``arg2`` is an integer specifying the time between each iteration (one iteration = one step of the cursor) which defaults to 100 ms.

### Controls
- ``space`` to pause the code
- ``r`` to reset the code
- ``right arrow`` to step once
- ``esc`` to quit

## TODO
- ~Add syntax coloring~
- Maybe promt the user for inputs in some other way than in the terminal
- Prevent the output to go off screen

### Other notes
The font *Inconsolata* is owned by [Raph Levien](http://levien.com/type/myfonts/inconsolata.html).
