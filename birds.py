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
    def __init__(self, id, name, species, age, diet, biome, enclosure_size,
                 wingspan_cm=50, can_fly=True):
        super().__init__(id, name, species, age, diet, biome, enclosure_size)
        self.wingspan_cm = wingspan_cm
        self.can_fly = can_fly
        self._Animal__cry = "Chirp"
        self._Animal__food = diet
        self._Animal__sleep = "perched"

    def unique_action(self):
        print(f"{self.name} flies or hops around.")


# Subclasses
class Ostrich(Bird):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Ostrich", age, diet, "Savannah / Grassland", "Medium",
                         wingspan_cm=200, can_fly=False)
        self._Animal__cry = "Boom"
        self._Animal__sleep = "on the ground"

    def unique_action(self):
        print(f"{self.name} runs at high speed.")

class Vulture(Bird):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Vulture", age, diet, "Savannah / Grassland", "Medium",
                         wingspan_cm=250, can_fly=True)
        self._Animal__cry = "Screech"
        self._Animal__sleep = "in trees"

    def unique_action(self):
        print(f"{self.name} circles high in the sky searching for carrion.")

class Parrot(Bird):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Parrot", age, diet, "Tropical / Rainforest", "Small",
                         wingspan_cm=40, can_fly=True)
        self._Animal__cry = "Squawk"
        self._Animal__sleep = "in trees"

    def unique_action(self):
        print(f"{self.name} mimics sounds and talks.")

class Toucan(Bird):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Toucan", age, diet, "Tropical / Rainforest", "Small",
                         wingspan_cm=60, can_fly=True)
        self._Animal__cry = "Croak"
        self._Animal__sleep = "in tree branches"

    def unique_action(self):
        print(f"{self.name} uses its large bill to reach fruit.")

class Macaw(Bird):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Macaw", age, diet, "Tropical / Rainforest", "Medium",
                         wingspan_cm=100, can_fly=True)
        self._Animal__cry = "Squawk"
        self._Animal__sleep = "in treetops"

    def unique_action(self):
        print(f"{self.name} glides through the rainforest canopy.")

class Owl(Bird):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Owl", age, diet, "Forest / Temperate", "Small",
                         wingspan_cm=120, can_fly=True)
        self._Animal__cry = "Hoot"
        self._Animal__sleep = "in tree hollows during the day"

    def unique_action(self):
        print(f"{self.name} hunts silently at night.")

class Woodpecker(Bird):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Woodpecker", age, diet, "Forest / Temperate", "Small",
                         wingspan_cm=30, can_fly=True)
        self._Animal__cry = "Drill"
        self._Animal__sleep = "in tree cavities"

    def unique_action(self):
        print(f"{self.name} pecks at tree trunks to find insects.")

class Penguin(Bird):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Penguin", age, diet, "Arctic / Polar", "Medium",
                         wingspan_cm=0, can_fly=False)
        self._Animal__cry = "Honk"
        self._Animal__sleep = "on ice"

    def unique_action(self):
        print(f"{self.name} waddles and swims skillfully.")

class Puffin(Bird):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Puffin", age, diet, "Arctic / Polar", "Small",
                         wingspan_cm=50, can_fly=True)
        self._Animal__cry = "Growl"
        self._Animal__sleep = "in burrows"

    def unique_action(self):
        print(f"{self.name} dives into the sea to catch fish.")

class SnowyOwl(Bird):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Snowy Owl", age, diet, "Arctic / Polar", "Small",
                         wingspan_cm=150, can_fly=True)
        self._Animal__cry = "Hoot"
        self._Animal__sleep = "on snowy branches"

    def unique_action(self):
        print(f"{self.name} hunts quietly over snow fields.")

class Roadrunner(Bird):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Roadrunner", age, diet, "Desert", "Small",
                         wingspan_cm=45, can_fly=True)
        self._Animal__cry = "Beep-beep"
        self._Animal__sleep = "in desert shrubs"

    def unique_action(self):
        print(f"{self.name} runs at amazing speed on the ground.")