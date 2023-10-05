class SimpleIteration:
    def __init__(self, max_iterations=1000):
        self.max_iterations = max_iterations

    def solve(self, g, g_prime, x0, epsilon):
        x = x0

        for i in range(self.max_iterations):
            x_new = g(x)
            error = abs(x_new - x)

            if error < epsilon:
                return x_new, i + 1  # Return the root and number of iterations

            x = x_new

        raise ValueError("The method did not converge within the maximum number of iterations.")
