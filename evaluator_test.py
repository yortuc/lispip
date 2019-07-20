from tokenizer import tokenize
from parser import parse
from evaluator import evl

ctx = { 
    'add': lambda x, y: x + y,
    'mul': lambda x, y: x * y,
    'eq' : lambda x, y: x == y,
    'id' : lambda x: x
}

def test_evaluate_single_expression():
    ast = parse(tokenize('(add 1 2)'))
    result = evl(ast, ctx)
    assert result == 3

def test_evaluate_list_of_expressions_return_last_one():
    ast = parse(tokenize('(add 1 2) (mul 9 8)'))
    result = evl(ast, ctx)
    assert result == 72

def test_define_function_in_local_scope():
    ast = parse(tokenize('(defun double (params x) (mul x 2))'))
    context = {}
    result = evl(ast, context)
    assert 'double' in context

def test_if_true():
    ast = parse(tokenize('(if (eq 1 1) (id TRUE) (id FALSE))'))
    result = evl(ast, ctx)
    assert result == 'TRUE'