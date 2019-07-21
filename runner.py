from tokenizer import tokenize
from parser import parse
from evaluator import evl
from standart_context import ctx

def run(expr, context=ctx):
    return evl(parse(tokenize(expr)), context)

run(
'''
(defun factorial (params x)
    (if (< x 2)
        1
        (mul x (factorial (- x 1)))
    )
)
(print (factorial 5))
''')

run(
'''
(defun double (params x) (mul x 2))
(print (map double '(1 2 3)))
'''
)
