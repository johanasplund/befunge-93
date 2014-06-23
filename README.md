# Befunge-93 Interpreter

This is a Befunge-93 interpreter written in python 3.4 with the use of pygame. The code has not properly been tested on python 2.X.

Johan Asplund

## How to use
Run the script as ``python befunge.py arg1 arg2``, where ``arg1`` is the befunge code, and where  ``arg2`` is an integer specifying the time between each iteration (one iteration = one step of the cursor) which defaults to 50 ms.

### Controls
- ``space`` to pause the code
- ``r`` to reset the code
- ``right arrow`` to step once
- ``esc`` to quit

## TODO
- ~~Add syntax coloring~~
- ~~Maybe promt the user for inputs in some other way than in the terminal~~
- Prevent the output to go off screen

### Other notes
The font *Inconsolata*, which is used in the interpreter, is owned by [Raph Levien](http://levien.com/type/myfonts/inconsolata.html).

# Quick reference for Befunge-93

Character |Description 
 -------- | ---------- 
`0-9` | Push this number to the stack
`+` | Pop `a` and `b`, then push `a+b`.
`-` | Pop `a` and `b`, then push `a-b`.
`*` | Pop `a` and `b`, then push `a*b`.
`/` | Pop `a` and `b`, then push `floor(b/a)`, provided that `a` is not zero.
`%` | Pop `a` and `b`, then push `a (mod b)`.
`!` | Pop `a`. If `a = 0`, push 1, otherwise push 0.
` ` ` | Pop `a` and `b`, then push 1 if `b > a`, otherwise 0.
`>` | Move right.
`<^ | Move left.
`^` | Move up.
`v` | Move down.
`?` | Move in a random direction.
`_` | Pop `a`. If `a = 0`, move right, otherwise move left.
<code>&#124;</code> | Pop `a`. If `a = 0` , move down, otherwise move up.
`"` | Start string mode. Push each characters ASCII value all the way up to the next ".
`:` | Duplicate value on top of the stack.
`\` | Swap the two values on top of the stack.
`$` | Remove the value on top of the stack.
`.` | Pop `a`. Output the integer value of `a`.
`,` | Pop `a`. Output `chr(a)`.
`#` | Skip next cell.
`p` | Pop `y`, `y` and `v`. Change the character in position `(x,y)` to `chr(v)`.
`g` | Pop `y` and `x` , the push the ASCII value of the character in position `(x,y)`.
`&` | Prompt user for a number and push it.
`~` | Prompt user for a character and push its ASCII value.
`@` | Stop instruction pointer