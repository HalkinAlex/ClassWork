class Dog:
    def __init__(self, name, voice, age):
        self.name = name
        self.voice = voice
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting.")

    def stay(self):
        if self.age >= 1:
            print(f"{self.name} is staying.")
        else:
            print(f"{self.name} is too young to stay.")

    def come(self):
        if self.age >= 1:
            print(f"{self.name} is coming.")
        else:
            print(f"{self.name} is too young to come.")


class DogRex(Dog):
    def __init__(self, name="Rex", voice="bow-wow", age=0):
        super().__init__(name, voice, age)

    def learn_tricks(self):
        tricks = [
            ("Sit", 0),
            ("Stay", 1),
            ("Come", 1)
        ]
        for trick, min_age in tricks:
            if self.age >= min_age:
                print(f"{self.name} learned {trick.lower()}.")

my_dog = DogRex(age=2)

my_dog.learn_tricks()

my_dog.sit()
my_dog.stay()
my_dog.come()