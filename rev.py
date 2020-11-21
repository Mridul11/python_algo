def rev(str):
    s = str.split(" ")
    for i in range(len(s)):
       s[i] = s[i][::-1]

    s =  " ".join(s)
    print(s)

rev("python is amazing!")
