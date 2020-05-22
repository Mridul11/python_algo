class MergeSort(object):
    def merge(self, arr1, arr2):
        i = j = 0
        new_arr = []
        while(i < len(arr1) and j < len(arr2)):
            if(arr1[i] < arr2[j]):
                new_arr.append(arr1[i])
                i += 1
            else:
                new_arr.append(arr2[j])
                j += 1

        while(i < len(arr1)):
            new_arr.append(arr1[i])
            i += 1

        while(j < len(arr2)):
            new_arr.append(arr2[j])
            j += 1

        return  new_arr


    def divide(self, arr):
        if( len(arr) <= 1 ):
            return arr
        else:
            mid = len(arr) // 2
            left = arr[0 : mid]
            right = arr[mid : len(arr)]

        return self.merge(self.divide(left) , self.divide(right))


arr = [ 1,3,5,2,4,6,67,98,45,324 ]

myMerge = MergeSort()

print(myMerge.divide(arr))

