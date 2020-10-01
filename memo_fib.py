class MemoFibonacci(object):
    def fib(self, n, memo):
        if n == 0 or n == 1:
            print(memo)
            memo[n] = n

        if memo[n] is None:
            memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)

        return memo[n]

mf = MemoFibonacci()
n = 50
print( mf.fib(n, [None] * (n+1)) )

