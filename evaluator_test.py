from tokenizer import tokenize
from parser import parse
from evaluator import evl
from standart_context import ctx


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
    ast = parse(tokenize('(if (= 1 1) TRUE FALSE)'))
    result = evl(ast, ctx)
    assert result == 'TRUE'

def test_if_false():
    ast = parse(tokenize('(if (= 5 1) TRUE FALSE)'))
    result = evl(ast, ctx)
    assert result == 'FALSE'

def test_eval_list():
    ast = parse(tokenize("'(1 2 3)"))
    result = evl(ast, ctx)
    assert result == [1, 2, 3]

def test_eval_list_functions():
    ast = parse(tokenize("(avg '(1 2 3))"))
    result = evl(ast, ctx)
    assert result == 2.0