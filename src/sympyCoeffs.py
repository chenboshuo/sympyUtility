from typing import *
import sympy as sp
from itertools import product
from sympyUtility import show
from copy import deepcopy


class Coefficients():
    def __init__(self,
                 expr,
                 degrees: Tuple[int, int],
                 params: Tuple[sp.Symbol, sp.Symbol],
                 left_notation: str = r'\boldsymbol{d}',
                 conditions: dict = {}):
        self.conditions = conditions
        self.degrees = degrees
        self.left = sp.Matrix([[
            sp.Symbol(left_notation + "_{" + f"{i}{j}" + "}")
            for j in range(degrees[1] + 1)
        ] for i in range(degrees[0] + 1)])
        self.expr = expr
        self.params = params
        self.coeffs = self.collect_coeffs(conditions)

    def show_all(self, **argv):
        for i, j in product(range(self.degrees[0] + 1),
                            range(self.degrees[1] + 1)):
            show(sp.Eq(self.left[i, j], self.coeffs[i][j]), **argv)

    def collect_coeffs(self, conditions):
        return {
            i: {
                j: self.expr.subs(conditions).coeff(self.params[0],
                                                      i).coeff(
                                                          self.params[1], j)
                for j in range(self.degrees[1] + 1)
            }
            for i in range(self.degrees[0] + 1)
        }

    def append_conditions(self, conditions, copy=True):
        if copy:
            c = deepcopy(self)
            c.append_conditions(conditions, copy=False)
            return None
        else:
            self.conditions.update(conditions)
            self.coeffs = self.collect_coeffs(self.conditions)

    def coeff(self,i,j,eq=True,**argv):
            equation = sp.Eq(self.left[i, j], self.coeffs[i][j])
            show(equation,**argv)
            if eq:
                return equation
            else:
                return self.coeffs[i][j]

    def show_conditions(self,**argv):
        for k,v in self.conditions.items():
            show(sp.Eq(k,v),**argv)

