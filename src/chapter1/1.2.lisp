; translate the following expression into prefix form:
; (5 + 4 + (2 - (3 - (6 + (4/5))))) / 3(6-2)(2-7)

(/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5)))))
   (* 3 (- 6 2) (- 2 7)))

; this evaluates to -37/150, an approximation of - 1/4