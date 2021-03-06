class Test(object):

    def test_print_2d_array(self, n):
        print( [[None for i in range(n)] for j in range(n)] )

    def test_print_dict_values_to_list(self):
        dict = {}
        for i in range(3):
            dict[i] = i
        print([ v  for ( k ,v ) in dict.items() ])

    def test_2d_array(self):
      print( [ [1 for i in range(3)]  for j in range(3)] )

    def test_recursion(self, n):
        if (n <= 1):
            return n
        else:
            # self.recursion(n-1) -> n*  n * self.recursion(n-1) -> n * n * self.recursion(n-1)
            return n * self.test_recursion(n - 1)

    #   mridul => ludirm
    def test_reverse(self, str):
        if (len(str) <= 1):
            return str
        else:
            return str[len(str) - 1] + self.test_reverse(str[0: len(str) - 1])

    def product(self, a, b):
        return "product is : " + str(a * b)

    def add(self, a ,b ):
        return "adddition is : " + str(a + b)

    def isPalindrome(self, n):
        i = 0
        pre = 0
        k = n
        l = len( str(n) )
        while(n > 0):
            i = n % 10
            l -= 1
            pre += i * (10 ** l)
            n = n // 10

        return ( k == pre )




test = Test()
# answer = (test.product if True else test.add) (2,3)
# print( answer )
# test.test_print_2d_array(3)
# test.test_print_dict_values_to_list()
# test.test_2d_array()
# print(test.test_reverse("mridul") )
# print(test.test_recursion(5) )
print( test.isPalindrome( 12021 ) )

