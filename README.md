# Lisp Clone in Python

Slack day project

```
(app
    (defun square (params x) 
        (mul x x))
    
    (defun volume (params x height) 
        (mul (square x) height))
        
    (print (volume 2 6)))
```