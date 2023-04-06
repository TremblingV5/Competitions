from sko.GA import GA


class Optimizer:

    def __init__(self, func, lb, ub):
        self.func = func
        self.lb = lb
        self.ub = ub

        if len(lb) != len(ub):
            raise Exception("Num of lb & ub error")
        self.ndim = len(lb)

    def run(self):
        pass


class GAOptimizer(Optimizer):

    def run(self, size_pop=50, max_iter=800, prob_mut=0.001, precision=1e-7):
        return GA(
            func=self.func,
            n_dim=self.ndim,
            lb=self.lb,
            ub=self.ub,
            size_pop=size_pop,
            prob_mut=prob_mut,
            precision=precision
        ).run()
