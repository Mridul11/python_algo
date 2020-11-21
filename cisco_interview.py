# find the misssing number
def find_missing_one(lst):
    n = len(lst)
    total = (n+1) * (n+2) / 2 
    lst_sum = sum(lst)
    print(total)
    print(lst_sum)
    return total - lst_sum 

a = [1,3,5,2,6]
val = find_missing_one(a)
print(val)

def reverse(s):
    a = s.split(" ")
    a = a[::-1]
    a = " ".join(a)
    print(a)

reverse("This is me !")

