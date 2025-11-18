"""
File: mammals.py
Description: Contains the subclasses, attributes and methods for mammals.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from animal import Animal

class Mammal(Animal):
    """All mammals have these traits"""
    def __init__(self, id, name, species, age, diet, biome, enclosure_size,
                 nocturnal=False, aggressiveness=5):
        super().__init__(id, name, species, age, diet, biome, enclosure_size)
        self.nocturnal = nocturnal
        self.aggressiveness = aggressiveness
        self._Animal__cry = "Growl"
        self._Animal__food = diet
        self._Animal__sleep = "in den"

    def unique_action(self):
        print(f"{self.name} does zoomies around the enclosure!")


# Subclasses
class Lion(Mammal):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Lion", age, diet, "Savannah / Grassland", "Large",
                         nocturnal=False, aggressiveness=8)
        self._Mammal__cry = "Roar"
        self._Mammal__sleep = "in the shade"

    def unique_action(self):
        print(f"{self.name} stalks its prey stealthily.")

class Elephant(Mammal):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Elephant", age, diet, "Savannah / Grassland", "Large",
                         nocturnal=False, aggressiveness=3)
        self._Mammal__cry = "Trumpet"
        self._Mammal__sleep = "standing up"

    def unique_action(self):
        print(f"{self.name} sprays water with its trunk.")

class Giraffe(Mammal):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Giraffe", age, diet, "Savannah / Grassland", "Large",
                         nocturnal=False, aggressiveness=2)
        self._Mammal__cry = "Bleat"
        self._Mammal__sleep = "lying down"

    def unique_action(self):
        print(f"{self.name} stretches its neck to reach high leaves.")

class Zebra(Mammal):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Zebra", age, diet, "Savannah / Grassland", "Medium",
                         nocturnal=False, aggressiveness=4)
        self._Mammal__cry = "Whinny"
        self._Mammal__sleep = "standing up"

    def unique_action(self):
        print(f"{self.name} gallops across the plains.")

class Meerkat(Mammal):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Meerkat", age, diet, "Savannah / Grassland", "Small",
                         nocturnal=True, aggressiveness=4)
        self._Mammal__cry = "Chirp"
        self._Mammal__sleep = "in burrow"

    def unique_action(self):
        print(f"{self.name} stands on hind legs to watch for predators.")

class Hyena(Mammal):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Hyena", age, diet, "Savannah / Grassland", "Medium",
                         nocturnal=True, aggressiveness=7)
        self._Mammal__cry = "Laugh"
        self._Mammal__sleep = "in dens"

    def unique_action(self):
        print(f"{self.name} scavenges loudly and laughs.")

class Chimpanzee(Mammal):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Chimpanzee", age, diet, "Tropical / Rainforest", "Medium",
                         nocturnal=False, aggressiveness=5)
        self._Mammal__cry = "Hoo-ha"
        self._Mammal__sleep = "in trees"

    def unique_action(self):
        print(f"{self.name} swings through the branches.")

class Tiger(Mammal):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Tiger", age, diet, "Tropical / Rainforest", "Large",
                         nocturnal=True, aggressiveness=9)
        self._Mammal__cry = "Growl"
        self._Mammal__sleep = "in a shaded den"

    def unique_action(self):
        print(f"{self.name} prowls stealthily through the jungle.")

class Sloth(Mammal):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Sloth", age, diet, "Tropical / Rainforest", "Medium",
                         nocturnal=False, aggressiveness=1)
        self._Mammal__cry = "Squeak"
        self._Mammal__sleep = "hanging from a tree"

    def unique_action(self):
        print(f"{self.name} moves slowly from branch to branch.")

class BrownBear(Mammal):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Brown Bear", age, diet, "Forest / Temperate", "Large",
                         nocturnal=True, aggressiveness=8)
        self._Mammal__cry = "Growl"
        self._Mammal__sleep = "in a cave"

    def unique_action(self):
        print(f"{self.name} digs for roots and berries.")

class Wolf(Mammal):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Wolf", age, diet, "Forest / Temperate", "Medium",
                         nocturnal=True, aggressiveness=6)
        self._Mammal__cry = "Howl"
        self._Mammal__sleep = "in a den"

    def unique_action(self):
        print(f"{self.name} hunts in a pack.")

class Deer(Mammal):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Deer", age, diet, "Forest / Temperate", "Medium",
                         nocturnal=False, aggressiveness=2)
        self._Mammal__cry = "Bleat"
        self._Mammal__sleep = "in the undergrowth"

    def unique_action(self):
        print(f"{self.name} grazes quietly in the forest.")

class Fox(Mammal):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Fox", age, diet, "Forest / Temperate", "Medium",
                         nocturnal=True, aggressiveness=4)
        self._Mammal__cry = "Yip"
        self._Mammal__sleep = "in a burrow"

    def unique_action(self):
        print(f"{self.name} sneaks and hunts small prey.")

class PolarBear(Mammal):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Polar Bear", age, diet, "Arctic / Polar", "Large",
                         nocturnal=False, aggressiveness=9)
        self._Mammal__cry = "Roar"
        self._Mammal__sleep = "on ice floes"

    def unique_action(self):
        print(f"{self.name} swims in icy waters.")

class ArcticFox(Mammal):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Arctic Fox", age, diet, "Arctic / Polar", "Medium",
                         nocturnal=True, aggressiveness=3)
        self._Mammal__cry = "Yip"
        self._Mammal__sleep = "in snow dens"

    def unique_action(self):
        print(f"{self.name} hunts for small rodents in the snow.")

class Seal(Mammal):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Seal", age, diet, "Arctic / Polar", "Large",
                         nocturnal=False, aggressiveness=2)
        self._Mammal__cry = "Bark"
        self._Mammal__sleep = "on ice"

    def unique_action(self):
        print(f"{self.name} dives and catches fish.")

class Walrus(Mammal):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Walrus", age, diet, "Arctic / Polar", "Large",
                         nocturnal=False, aggressiveness=4)
        self._Mammal__cry = "Bellow"
        self._Mammal__sleep = "on the shore"

    def unique_action(self):
        print(f"{self.name} uses tusks to move ice blocks.")

class Reindeer(Mammal):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Reindeer", age, diet, "Arctic / Polar", "Medium",
                         nocturnal=False, aggressiveness=1)
        self._Mammal__cry = "Bleat"
        self._Mammal__sleep = "in snow"

    def unique_action(self):
        print(f"{self.name} migrates across snowy tundra.")

class Camel(Mammal):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Camel", age, diet, "Desert", "Large",
                         nocturnal=False, aggressiveness=3)
        self._Mammal__cry = "Grunt"
        self._Mammal__sleep = "in the sand"

    def unique_action(self):
        print(f"{self.name} stores water in its hump.")

class MeerkatDesert(Mammal):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Meerkat", age, diet, "Desert", "Small",
                         nocturnal=True, aggressiveness=4)
        self._Mammal__cry = "Chirp"
        self._Mammal__sleep = "in burrow"

    def unique_action(self):
        print(f"{self.name} keeps watch from the desert mound.")