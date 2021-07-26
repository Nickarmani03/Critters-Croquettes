# import the python datetime module to help us create a timestamp
from datetime import date


# Walking


class  Camels:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species        
        self.walking = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class  Llama:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species        
        self.walking = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


class Pegusus:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species        
        self.walking = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class Griffin:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species        
        self.walking = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class Unicorn:

    def __init__(self, name, species, food):
        # Establish the propertis of each animal with a default value
        self.name = name
        self.species = species        
        self.walking = True
        self.food = food
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"