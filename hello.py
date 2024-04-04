class DogRex:
    def __init__(self):
        self.name = 'chihuahua'
        self.voice = 'meow'
        self.hungry = True
    
    def feed(self):
        self.hungry = False
    
    def walk(self):
        self.hungry = True

my_dog = DogRex()

print('my dog name:', my_dog.name) # chihuahua
print('my dog voice:', my_dog.voice) # meow
print('my dog is hungry:', my_dog.hungry) # True

my_dog.feed()
print('my dog is hungry:', my_dog.hungry) # False

my_dog.walk()
print('my dog is hungry:', my_dog.hungry) # True