# [1,2,4,5,7,8 ] = sum of 3 consecutive digits .
class SlidingProblem(object):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def sliding(arr):
        for i in range(len(arr)-2):
            sum = 0
            sum += arr[i] + arr[i+1] + arr[i+2]
            print(sum)

    @classmethod
    def myClass( cls, arr ):
        cls.sliding(arr)

    def __str__(self):
        return "Class is something worth status {} ".format(self.name)

sp = SlidingProblem("Mridul")

SlidingProblem.myClass([4,3,2,1,10])
print("======================")
SlidingProblem.sliding([ 1,2,4,5,7,8 ])
print(sp)

