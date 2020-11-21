def occ(lst):
    obj = {}
    for i in range(len(lst)):
        if lst[i] in obj:
            obj[lst[i]] += 1
        else:
            obj[lst[i]] = 1

    print(obj)

lst = [1,2,2,3,5,2]
occ(lst)

