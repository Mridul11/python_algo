class Person:
		def __private(self,num):
				print("I am private!") 
				print(num)

		def run(self):
			print("I am running!")
			print("This is from feature-a branch!")


		def public(self):
				print("I am public!")
				self.__private(1)

		@staticmethod
		def staticMathod():
			print("I am static method !")

		@classmethod
		def classMethodExample(cls):
			print(cls)



p = Person()
p.public()
Person.staticMathod()


