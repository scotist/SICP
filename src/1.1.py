# Below is a sequence of expressions, each followed by the result printed by the interpreter in response to that expression.

 # Of course the following is extremely rudimentary. The point in SICP is to show familiarity with the operation of the interpreter; for the purposes of this project it show basic differences in Python syntax vs Scheme syntax. This file shows the Python version.

>>> 10
10

>>> 5 + 3 + 4
12

>>> 9 - 1
8

>>> 6 / 2
3.0

>>> (2 * 4) + (4 - 6)
6

>>> a = 3
#  no output

>>> b = a + 1
#  no output

>>> a = b
# no output; in Scheme this checks *whether* a is the same as b; here it *reassigns* the value of a as the value of b. They will need to be reset for the rest of the exercise to work.

>>> if b > a and b < a * b:
...     b
4