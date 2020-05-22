def selection(arr):
    for i in range(0, len(arr)):
         min_index = i 
         for j in range(i+1 , len(arr)):
             if(arr[j] < arr[min_index]):
                 min_index = j 

         arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr 

arr = [23,34,56,78,3,2,1567,5] 
print(selection(arr))
