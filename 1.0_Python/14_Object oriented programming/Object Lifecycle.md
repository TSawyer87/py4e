- Objects are created, used and discarded
- We have special blocks of code(methods) that get called
	- At the moment of creation(constructor)
	- At the moment of destruction(destructor)
- Constructors are used a lot 
- Destructors are seldom used

# Constructor
The primary purpose of the constructor is to set up some instance variables to have the proper initial values when the object is created.`__init__`
```python
class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far',self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)
```

Out:
```python
I am constructed
So far 1 
So far 2
I am destructed 2
an contains 42
```
- The constructor and destructor are optional.
- The constructor is typically used to set up variables.
- The destructor is seldom used.

- Every time you overwrite a variable Python reclaims that memory back.

## Many Instances
- We can create lots of objects - the class is the template for the object
- We can store each distinct object in its own variable
- We call this having multiple instances of the same class
- Each instance has its own copy of the instance variables

```python
class PartyAnimal:

    def __init__(self, nam):
        self.x = 0
        self.name = nam
        print(self.name,"constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):

    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = FootballFan("Jim")
j.party()
j.touchdown()
```
Out:
```python
Sally constructed
Sally party count 1
Jim constructed
Jim party count 1
Jim party count 2
Jim points 7
```

**Class** - a template
**Attribute** - A variable within a class
**Method** - A function within a class
**Object** - A particular instance of a class
**Constructor** - Code that runs when an object is created
**Inheritance** - The ability to extend a class to make a new class

## Summary

- Object Oriented programming is a very structured approach to code reuse.
- We can group data and functionality together and create many independent instances of a class