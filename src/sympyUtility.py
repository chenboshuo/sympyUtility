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


def show(s,latex=False,cpp=False,cpp_format=lambda *args: args[0]):
    if __name__ == "__main__" :
        if isinstance(s, Iterable):
            for exp in s:
                show_item(exp,latex,cpp,cpp_format)
        else:
            show_item(s,latex,cpp,cpp_format)

def bernstein_func(m,i,param):
    return (param**i)*((1-param)**(m-i))*(
#         math.factorial(m) // math.factorial(i) // math.factorial(m - i)
        sp.binomial(m, i)
    )


def reverse(d):
    return {
        v:k for k,v in d.items()
    }
