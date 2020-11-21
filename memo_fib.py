class MemoFibonacci(object):
    def fib(self, n, memo):
        if n == 0 or n == 1:
            memo[n] = n

        if memo[n] is None:
            memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
            print(memo[n])

        return memo[n]

mf = MemoFibonacci()
n = 50
mf.fib(n, [None] * (n+1))

