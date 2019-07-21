# Lisp Clone in Python


### Install
```
> pipenv install
```

### Run
```
> pipenv shell
> runner.py
```

### Run tests
```
> pipenv shell
> pytest
```

### Basic syntax

```
(defun factorial (params x)
    (if (< x 2)
        1
        (mul x (factorial (- x 1)))
    )
)
(print (factorial 5))
```

### TODO
- Remove `params` keyword in function definition
- Package management
