class SecantMethod:
    def __init__(self, f, x0, x1, precision):
        self.f = f
        self.x0 = x0
        self.x1 = x1
        self.precision = precision

    def solve(self):
        iterations = 0

        while True:
            f_x0 = self.f(self.x0)
            f_x1 = self.f(self.x1)

            if abs(f_x1) < self.precision:
                print("Root:", self.x1)
                print("Iterations:", iterations)
                return self.x1, iterations

            denominator = (f_x1 - f_x0)

            x_new = self.x1 - (f_x1 * (self.x1 - self.x0)) / denominator

            if abs(x_new - self.x1) < self.precision:
                print("Root:", x_new)
                print("Iterations:", iterations)
                return x_new, iterations

            self.x0 = self.x1
            self.x1 = x_new
            iterations += 1
