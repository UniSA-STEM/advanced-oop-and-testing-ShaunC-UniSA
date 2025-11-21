"""
File: birds.py
Description: Contains the subclasses, attributes and methods for birds.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from animal import Animal

# Main class
class Bird(Animal):
    """All birds have these traits"""
    ABSTRACT = True  # Mark as abstract for build_animal_database

    def __init__(self, name, species, age, diet, biome, enclosure_size, zoo,
                 wingspan_cm=50, can_fly=True):
        super().__init__(name, species, age, diet, biome, enclosure_size, zoo)
        self.wingspan_cm = wingspan_cm
        self.can_fly = can_fly
        self._set_cry("Chirp")
        self._Animal__food = diet
        self._set_sleep("perched")

    def unique_action(self):
        print(f"{self.name} flies or hops around.")

# Subclasses
class Ostrich(Bird):
    BIOME = "Savannah / Grassland"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Ostrich", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=200, can_fly=False)
        self._set_cry("Boom")
        self._set_sleep("on the ground")

    def unique_action(self):
        print(f"{self.name} runs at high speed.")

class Vulture(Bird):
    BIOME = "Savannah / Grassland"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Vulture", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=250)
        self._set_cry("Screech")
        self._set_sleep("in trees")

    def unique_action(self):
        print(f"{self.name} circles high in the sky searching for carrion.")

class Parrot(Bird):
    BIOME = "Tropical / Rainforest"
    SIZE = "Small"

    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Parrot", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=40)
        self._set_cry("Squawk")
        self._set_sleep("in trees")

    def unique_action(self):
        print(f"{self.name} mimics sounds and talks.")

class Toucan(Bird):
    BIOME = "Tropical / Rainforest"
    SIZE = "Small"

    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Toucan", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=60)
        self._set_cry("Croak")
        self._set_sleep("in tree branches")

    def unique_action(self):
        print(f"{self.name} uses its large bill to reach fruit.")

class Macaw(Bird):
    BIOME = "Tropical / Rainforest"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Macaw", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=100)
        self._set_cry("Squawk")
        self._set_sleep("in treetops")

    def unique_action(self):
        print(f"{self.name} glides through the rainforest canopy.")

class Owl(Bird):
    BIOME = "Forest / Temperate"
    SIZE = "Small"

    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Owl", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=120)
        self._set_cry("Hoot")
        self._set_sleep("in tree hollows during the day")

    def unique_action(self):
        print(f"{self.name} hunts silently at night.")

class Woodpecker(Bird):
    BIOME = "Forest / Temperate"
    SIZE = "Small"

    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Woodpecker", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=30)
        self._set_cry("Drill")
        self._set_sleep("in tree cavities")

    def unique_action(self):
        print(f"{self.name} pecks at tree trunks to find insects.")

class Penguin(Bird):
    BIOME = "Arctic / Polar"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Penguin", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=0, can_fly=False)
        self._set_cry("Honk")
        self._set_sleep("on ice")

    def unique_action(self):
        print(f"{self.name} waddles and swims skillfully.")

class Puffin(Bird):
    BIOME = "Arctic / Polar"
    SIZE = "Small"

    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Puffin", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=50)
        self._set_cry("Growl")
        self._set_sleep("in burrows")

    def unique_action(self):
        print(f"{self.name} dives into the sea to catch fish.")

class SnowyOwl(Bird):
    BIOME = "Arctic / Polar"
    SIZE = "Small"

    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Snowy Owl", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=150)
        self._set_cry("Hoot")
        self._set_sleep("on snowy branches")

    def unique_action(self):
        print(f"{self.name} hunts quietly over snow fields.")

class Roadrunner(Bird):
    BIOME = "Desert"
    SIZE = "Small"

    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Roadrunner", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=45)
        self._set_cry("Beep-beep")
        self._set_sleep("in desert shrubs")

    def unique_action(self):
        print(f"{self.name} runs at amazing speed on the ground.")