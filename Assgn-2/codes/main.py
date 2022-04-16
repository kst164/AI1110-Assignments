import sympy
from sympy.abc import x, a, b, c
from sympy.matrices import Matrix

matrix = Matrix([[x+a, b, c],
                 [c, x+b, a],
                 [a, b, x+c]])
roots = sympy.roots(matrix.det(), x) # roots of x in determinant of matrix

for root in roots:
    if root == 0:
        # Question says x != 0
        continue
    print(f"{root} is a nonzero value of x with multiplicity {roots[root]}")

# Output: `-a - b - c is a nonzero value of x with multiplicity 1`
