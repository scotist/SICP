;Below is a sequence of expressions, each followed by the result printed by the interpreter in response to that expression.

;Of course the following is extremely rudimentary. The point in SICP is to show familiarity with the operation of the interpreter; for the purposes of this project it show basic differences in Python syntax vs Scheme syntax. This file shows the Scheme version; the interpreter is Dr Racket.

 > 10
 10

 > (+ 5 3 4)
 12

 > (/ 6 2)
 3

 > (+ (* 2 4) (- 4 6))
 6

 > (define a 3)
; no output

 > (define b(+ a 1))
;  no output

 > (+ a b (* a b))
 19

 > (= a b)
 #f

> (if (and (> b a) (< b(* a b)))
      b
      a)
 4

> (cond ((= a 4) 6)
        ((= b 4) (+ 6 7 a))
        (else 25))
 16

 > (+ 2 (if (> b a) b a))
 6

 > (* (cond((> a b) a)
           ((< a b) b)
           (else -1))
      (+ a 1))
 16


