; Define a procedure that takes three numbers as arguments and returns the sum of the squares of the two larger numbers.

(define (square x) (* x x))

(define (sum-of-squares x y)
  (+ (square x) (square y)))

(define (squares-of-largest x y z)
  (cond ((<= x y z) (sum-of-squares y z))
        ((<= y x z) (sum-of-squares x z))
        ((<= z x y) (sum-of-squares y x))))
