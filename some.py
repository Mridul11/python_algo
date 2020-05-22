class Person:
		def __private(self,num):
				print("I am private!") 
				print(num)

		def public(self):
				print("I am public!")
				self.__private(1)

		@staticmethod
		def staticMethod():
			print("I am static method!")



p = Person()
p.public()
Person.staticMathod()


