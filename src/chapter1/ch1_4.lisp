; describe the behavior of the following procedure:

(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b))

; This function takes two numeric parameters, a and b. If b is negative, it changes its value to positive and adds it to a. If b is positive, it adds it to a.
