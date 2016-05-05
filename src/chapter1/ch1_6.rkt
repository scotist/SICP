#lang racket
(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))

(define (average x y)
  (/ (+ x y) 2))

(define (improve guess x)
  (average guess (/ x guess)))

(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))

(define (sqrt-iter guess x)
  (if (good-enough? guess x)
          guess
          (sqrt-iter (improve guess x)
                     x)))

; sqrt-iter defined with new-if instead of with plain if causes an infinite loop, because always evaluates both of the arguments before applying the function to them. It calls the function recursively on both the conditional's consequent and its alternative, rather than evaluating the condition and applying either the consequent or the alternative.
