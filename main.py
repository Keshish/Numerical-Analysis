import sympy as sp
import math

from Methods.NewtonMethod import NewtonMethod
from Methods.SecantMethod import SecantMethod
from Methods.BisectionMethod import BisectionMethod
from Methods.SimpleIteration import SimpleIteration


# Rest of your code

def f1(x):
    return x ** 3 + 2 * x ** 2 + 10 * x - 20


def df1(x_value):
    return sp.diff(f1(x), x).subs(x, x_value).evalf()


x = sp.symbols('x')

lsp = 1.0
rsp = 2.0
precision = 1e-4

print("\n\n##############################################")
print("Exercise 2")


# Problem Statement:
# In 1225, Leonardo Pisano (Fibonacci) calculated one of the solutions of the equation:
# f(x) = x^3 + 2x^2 + 10x - 20 = 0, which is approximately x ≈ 1.3688.
# We want to show that there is a solution of (2) in [1, 2], and that it is the only real solution on ℝ.

# Step 1: Prove Existence in [1, 2] using Intermediate Value Theorem
# Calculate f(1) and f(2) to show that they have opposite signs:
f_at_1 = 1**3 + 2*(1**2) + 10*1 - 20  # f(1)
f_at_2 = 2**3 + 2*(2**2) + 10*2 - 20  # f(2)

# If f(1) and f(2) have opposite signs, by the Intermediate Value Theorem, there exists a root in [1, 2].
# Check if f(1) and f(2) have opposite signs:
if f_at_1 * f_at_2 < 0:
    print("A root exists in [1, 2] by the Intermediate Value Theorem.")
else:
    print("The Intermediate Value Theorem does not guarantee a root in [1, 2].")

# Step 2: Prove Uniqueness on ℝ using Calculus
# Calculate the derivative of f(x):
def f_prime(x):
    return 3*x**2 + 4*x + 10

# Calculate the discriminant of the quadratic term in f'(x):
discriminant = 4**2 - 4*3*10

# Check the sign of the discriminant to determine if f'(x) is always positive:
if discriminant < 0:
    print("The discriminant is negative, and f'(x) is always positive.")
    print("Therefore, f(x) is strictly increasing on ℝ, and it has at most one real root.")

# Conclusion:
# The solution x ≈ 1.3688 in [1, 2] is the only real solution on ℝ for the equation f(x) = x^3 + 2x^2 + 10x - 20 = 0.




# #Newton's Method
print("\nNewton's Method")
Nsolver = NewtonMethod(f1, df1, 1, precision)
Nsolver.solve()

# Secant Method
print("\nSecant Method")
Ssolver = SecantMethod(f1, lsp, rsp, precision)
Ssolver.solve()

# Bisection Method
print("\nBisection Method")
Bsolver = BisectionMethod(f1, 1, 2, precision)
Bsolver.solve()
print("##############################################")


print("\n\n\n")
print("Exercise 3")

def f2(x):
    return math.tan(x)

def df2(x_value):
    return sp.diff(f1(x), x).subs(x, x_value).evalf()

lsp = -5.0
rsp = -4.0
precision = 1e-4




# Newton's Method
print("\nNewton's Method")
Nsolver = NewtonMethod(f2, df2, -1, precision)
Nsolver.solve()

# Secant Method
print("\nSecant Method")
Ssolver = SecantMethod(f2, lsp, rsp, precision)
Ssolver.solve()

# Bisection Method
print("\nBisection Method")
Bsolver = BisectionMethod(f2, 5, 10, precision)
Bsolver.solve()
###########################################
print("\n\n\n\n\n\n")
print("##############################################")


print("Exersice 4")
# To show that the Contraction Mapping Theorem is applicable to the function g(x) = 20 / (x^2 + 2x + 10) on [1, 2],
# we need to demonstrate that g(x) is a contraction mapping on this interval.
# we need to show that there exists a constant L such that for all x, y in [1, 2],
# the following condition holds: |g(x) - g(y)| <= L * |x - y|.
# Here, L is a positive constant less than 1.

# Calculate the derivative of g(x) with respect to x:
# g'(x) = -20(2x+2) / (x^2+2x+10)^2

# Now, we need to find the maximum value of |g'(x)| on the interval [1, 2]
# to determine a bound for L.

# To find the maximum value of |g'(x)|, we'll evaluate it at both endpoints of [1, 2]
# and take the larger absolute value:
# 1. |g'(1)| = -40 / 169
# 2. |g'(2)| = -60 / 324

# Now, let's find the maximum of these absolute values:
# max(|g'(1)|, |g'(2)|) = -40 / 169

# So, we have L = -40 / 169. To apply the Contraction Mapping Theorem, we need L < 1.
# In this case, L is a negative number, but its absolute value |L| = 40 / 169 is less than 1.

# Therefore, the Contraction Mapping Theorem is applicable to the function g(x) on [1, 2],
# and g(x) is a contraction mapping on this interval.


def g(x):
    return 20 / (x ** 2 + 2 * x + 10)


def g_prime(x):
    return (-20 * (2 * x + 2)) / (x ** 2 + 2 * x + 10) ** 2


solver = SimpleIteration()
x0 = 1.5
epsilon = 1e-6  # Tolerance for convergence
root, iterations = solver.solve(g, g_prime, x0, epsilon)
print(f"Estimated root: {root}")
print(f"Number of iterations: {iterations}")