class Person:
		def __private(self,num):
				print("I am private!") 
				print(num)

		def public(self):
				print("I am public!")
				self.__private(1)

		@staticmethod
		def staticMethod():
			print("I am static method !")

		@classmethod
		def classMethodExample(cls):
			print("Adding class Method")
			print("Adding class Method again!")
			print(cls)



p = Person()
p.public()
Person.staticMathod()


