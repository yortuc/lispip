from tokenizer import tokenize, Token
from parser import parse, Func

def test_parse_simple_tokens():
    tokens = tokenize('(add 1 2)')
    result = parse(tokens)

    assert result.name == 'add' and result.params == [Token('word', '1'), Token('word', '2')]

def test_parse_cascaded_parans():
    tokens = tokenize('(add (mul 3 4) 5)')
    result = parse(tokens)

    expected_params = [Func('mul', [Token('word', '3'), Token('word', '4')]), Token('word', '5')]

    assert result.name == 'add' and all([a == b for a, b in zip(result.params, expected_params)])
    