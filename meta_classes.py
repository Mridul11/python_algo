class Meta(type):
    def __new__(self, class_name, bases, attrs):
        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        print(a)
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5 
    y = 10 

    def hello(self):
        print("Hello")

d = Dog()

print(d.X)



