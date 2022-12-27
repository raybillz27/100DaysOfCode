#simple function

def greet():
    print("hello")
    print("how are you today ?")
greet()


#functions that allows for inputs

def greet_with_name(name):
    print(f"hello {name}")
    print(f"how are you today {name} ?")


greet_with_name("testimony")

#functions with more than one inputs

def greet_with(name,location):
    print(F"hello {name}")
    print(f"what is the weather like in {location}")
greet_with("testimony","umuahia")

#keyword argument

def greet_with(name,location ):
    print(F"hello {name}")
    print(f"what is the weather like in {location}")
greet_with( location = "umuahia",name = "testimony")