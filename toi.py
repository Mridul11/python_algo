# A B C -> 3 -> A -> B = A -> C = B -> C = A -> B
class TowerOfHanoi(object):
    def hanoi(self, n , A, B ,C):
        if(n == 1):
            print("Plate no %s from %s to %s" % (n, A, C))
            return

        self.hanoi(n-1, A, C ,B)
        print("Plate no %s from %s to %s"%(n, A, C))
        self.hanoi(n-1, B, A ,C)


toh = TowerOfHanoi()
toh.hanoi(3, "A", "B", "C")



