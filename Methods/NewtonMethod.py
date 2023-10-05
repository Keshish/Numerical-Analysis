class NewtonMethod:
    def __init__(self, f, df, sp, precision):
        self.f = f
        self.df = df
        self.sp = sp
        self.precision = precision

    def solve(self):
        iterations = 0

        while abs(self.f(self.sp)) > self.precision :
            if self.df(self.sp) == 0:
                print("zero error")
                break

            self.sp = self.sp - self.f(self.sp) / self.df(self.sp)
            iterations += 1

        print("Root:", self.sp)
        print("Iterations:", iterations)
        return self.sp, iterations
