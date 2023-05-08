import sympy as sp
from collections.abc import Iterable
from IPython.display import display, Math
from itertools import product

from collections.abc import Iterable
from IPython.display import display, Math

def show_item(s,latex,cpp,cpp_format):
    if latex:
        print(sp.latex(s))
    if cpp:
        print(cpp_format(sp.printing.cxxcode(s)))
    display(Math(sp.latex(s)))


def show(s,latex=False,cpp=False,cpp_format=lambda *args: None):
    if isinstance(s, Iterable):
        for exp in s:
            show_item(exp,latex,cpp,cpp_format)
    else:
        show_item(s,latex,cpp,cpp_format)


def reverse(d):
    return {
        v:k for k,v in d.items()
    }
