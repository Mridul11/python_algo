class InsertionSort(object):
    def insertion(self, arr):
        for i in range(1,len(arr)):
            min_elem = arr[i]
            j = i - 1
            while ( j >= 0 and arr[j] > min_elem ):
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = min_elem

        return arr

insertion_sort = InsertionSort()
arr = [ 12, 3, 45, 67, 78, 1 , 4, 6 , 34, 75, 89, 312 ]
print( insertion_sort.insertion(arr) )
