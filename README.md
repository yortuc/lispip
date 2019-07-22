# Lisp Clone in Python


### Install
```
> pipenv install
> pipenv shell
```

### Run
```
> python runner.py example1.lispip
```

### Run tests
```
> pytest
```

### Basic syntax

```
; define a recursive function
(defun factorial (params x)
    (if (< x 2)
        1
        (mul x (factorial (- x 1)))
    )
)

; print factorial 5
(print (factorial 5))
```

### TODO
- Remove `params` keyword in function definition
- Package management
- Simple http server example
