# import the python datetime module to help us create a timestamp
from datetime import date


# Slithering /Swimming


class Python:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species        
        self.swimming = True
        self.venomous = False
        self.slithering = True
        self.food = food
        self.date_added = date.today()        

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class Boa:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species        
        self.swimming = True
        self.venomous = False
        self.slithering = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class Cobra:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species        
        self.swimming = False
        self.venomous = True
        self.slithering = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class BlackMamba:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.swimming = False
        self.venomous = True
        self.slithering = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class Alligator:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species
        self.swimming = True
        self.venomous = False
        self.slithering = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"