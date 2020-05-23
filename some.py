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
			print("Master branch code")
			print("I am a feature_a change!")
			print(cls)



p = Person()
p.public()
Person.staticMathod()


