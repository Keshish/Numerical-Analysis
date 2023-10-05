import matplotlib.pyplot as plt
import numpy as np

class BisectionMethod:
    def __init__(self, f, lsp, rsp, precision):
        self.f = f
        self.lsp = lsp
        self.rsp = rsp
        self.precision = precision
        self.iterations = 0
        self.roots = []
        self.intervals = []

    def solve(self):
        while (self.rsp - self.lsp) / 2 > self.precision:
            c = (self.lsp + self.rsp) / 2
            fc = self.f(c)

            if fc == 0:
                self.roots.append(c)
                return c

            if self.f(self.lsp) * fc < 0:
                self.rsp = c  # Update the right bound
            else:
                self.lsp = c  # Update the left bound

            self.roots.append((self.lsp + self.rsp) / 2)  # Store current root estimate
            self.intervals.append((self.lsp, self.rsp))  # Store current interval
            self.iterations += 1

        root = (self.lsp + self.rsp) / 2
        self.roots.append(root)
        self.intervals.append((self.lsp, self.rsp))
        print("Root:", root)
        print("Iterations:", self.iterations)
        return root, self.iterations

        return root

    def plot_iterations(self):
        x = np.linspace(self.lsp, self.rsp, 1000)
        y = [self.f(xi) for xi in x]

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label="Function")  # Plot the function

        for i, (l, r) in enumerate(self.intervals):
            plt.axvline(x=l, color='red', linestyle='--', label=f"Interval Left (Iteration {i})")
            plt.axvline(x=r, color='blue', linestyle='--', label=f"Interval Right (Iteration {i})")

        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Bisection Method Iterations")
        plt.legend()
        plt.grid()
        plt.show()






#method = BisectionSolver(f, 0, 5, 0.001)


