class Person:
		def __private(self,num):
				print("I am private!") 
				print("Hey tis private")
				print("printintg anothee one!")
				print(num)

		def run(self):
			print("I am running!")


		def public(self):
				print("I am public!")
				self.__private(1)

		@staticmethod
		def staticMathod():
			print("I am static method !")
			print(f'1 is one')
			print(1+1)
			print(f"This si static method which is working fine")

		@classmethod
		def classMethodExample(cls):
			print("Adding class Method")
			print("I am a feature_a change!")
			print("Master branch change")
			print(cls)



p = Person()
p.public()
Person.staticMathod()


