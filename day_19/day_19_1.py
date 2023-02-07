# inheritance class.

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

class Human(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this on land.")

    def walk(self):
        print("moving on land.")

nemo = Fish()
nemo.breathe()


class Human:
    def __init__(self) -> None:
        self.num_eyes = 2
        self.num_legs = 2

# def do_nothing():
#     fact = "The world has about 8 billion people"


# def count_letter(words):
#     return len(words)


# my_name = "Elotam"
# sentence = f"The number of letters in {my_name} is {count_letter(my_name)}"
# print(sentence)


# def addition(num1, num2):
#     sum = num1 + num2
#     print(sum)


# def try_addition():
#     _ret = addition(num1=14, num2=78)

#     print("The sume of 14 and 78 is {0}".format(_ret))