import sys
from pathlib import Path

from tokenizer import tokenize
from parser import parse
from evaluator import evl
from standart_context import ctx

def run(expr, context=ctx):
    return evl(parse(tokenize(expr)), context)

file_path = sys.argv[1]
source_code = Path(file_path).read_text()

run(source_code)