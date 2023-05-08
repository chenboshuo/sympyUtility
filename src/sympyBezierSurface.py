import sympy as sp
from typing import *
from itertools import product
from sympyUtility import show


def bernstein_func(m, i, param):
    return (param**i) * ((1 - param)**(m - i)) * (sp.binomial(m, i))


class BezierSurface:
    def __init__(self, degree: Tuple[int, int], control_point_symbol: str,
                 param_symbol: Tuple[str, str], poly_coeff_symbol: str):
        self.degree = degree
        self.control_points = sp.Matrix([[
            sp.symbols(r"\boldsymbol{" + control_point_symbol + "}_{" +
                       f"{i}{j}" + "}") for j in range(degree[1] + 1)
        ] for i in range(degree[0] + 1)])
        self.params = sp.symbols(" ".join(param_symbol))
        self.bernstein = self.bezier_surface()
        self.coeffs_symbols = sp.Matrix([[
            sp.Symbol(r"\boldsymbol{" + poly_coeff_symbol + "}_{" + f"{i}{j}" +
                      "}") for j in range(degree[1] + 1)
        ] for i in range(degree[0] + 1)])
        self.poly_format = sum(self.coeffs_symbols[i, j] *
                               self.params[0]**i *
                               self.params[1]**j for i, j in self.ij())
        self.coeffs = {
            i: {
                j:
                self.bernstein.expand().coeff(self.params[0],
                                              i).coeff(self.params[1], j)
                for j in range(self.degree[1] + 1)
            }
            for i in range(self.degree[0] + 1)
        }

    def ij(self):
        for i, j in product(range(self.degree[0] + 1),
                            range(self.degree[1] + 1)):
            yield (i, j)

    def bezier_surface(self):
        s = 0
        for i, j in product(range(self.degree[0] + 1),
                            range(self.degree[1] + 1)):
            s += bernstein_func(
                self.degree[0], i, self.params[0]) * bernstein_func(
                    self.degree[1], j, self.params[1]) * \
                self.control_points[i, j]
        return s

    def show_coeffs(self, conditions={}, latex=False, cpp=False):
        for i, j in self.ij():
            show(
                sp.Eq(self.coeffs_symbols[i, j],
                      self.coeffs[i][j].subs(conditions)), latex, cpp)

    @classmethod
    def surface_p(cls, degree):
        return BezierSurface(degree, 'p', ('s', 't'), 'a')

    @classmethod
    def surface_q(cls, degree):
        return BezierSurface(degree, 'q', ('u', 'v'), 'b')
