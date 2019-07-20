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
(defun square (params x) 
    (mul x x))

(defun volume (params x height) 
    (mul (square x) height))
    
(print (volume 2 6))
```