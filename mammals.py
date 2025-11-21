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

# Main class
class Mammal(Animal):
    """All mammals have these traits"""
    ABSTRACT = True  # Mark as abstract for dynamic database

    def __init__(self, name, species, age, diet, biome, enclosure_size, zoo,
                 nocturnal=False, aggressiveness=5):
        super().__init__(name, species, age, diet, biome, enclosure_size, zoo)
        self.nocturnal = nocturnal
        self.aggressiveness = aggressiveness
        self._set_cry("Growl")
        self._set_sleep("in den")

    def unique_action(self):
        print(f"{self.name} does zoomies around the enclosure!")

# Subclasses
class Lion(Mammal):
    BIOME = "Savannah / Grassland"
    SIZE = "Large"

    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Lion", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=8)
        self._set_cry("Roar")
        self._set_sleep("in the shade")

    def unique_action(self):
        print(f"{self.name} stalks its prey stealthily.")

class Elephant(Mammal):
    BIOME = "Savannah / Grassland"
    SIZE = "Large"

    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Elephant", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=3)
        self._set_cry("Trumpet")
        self._set_sleep("standing up")

    def unique_action(self):
        print(f"{self.name} sprays water with its trunk.")

class Giraffe(Mammal):
    BIOME = "Savannah / Grassland"
    SIZE = "Large"

    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Giraffe", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=2)
        self._set_cry("Bleat")
        self._set_sleep("lying down")

    def unique_action(self):
        print(f"{self.name} stretches its neck to reach high leaves.")

class Zebra(Mammal):
    BIOME = "Savannah / Grassland"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Zebra", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=4)
        self._set_cry("Whinny")
        self._set_sleep("standing up")

    def unique_action(self):
        print(f"{self.name} gallops across the plains.")

class Meerkat(Mammal):
    BIOME = "Savannah / Grassland"
    SIZE = "Small"

    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Meerkat", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=4)
        self._set_cry("Chirp")
        self._set_sleep("in burrow")

    def unique_action(self):
        print(f"{self.name} stands on hind legs to watch for predators.")

class Hyena(Mammal):
    BIOME = "Savannah / Grassland"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Hyena", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=7)
        self._set_cry("Laugh")
        self._set_sleep("in dens")

    def unique_action(self):
        print(f"{self.name} scavenges loudly and laughs.")

class Chimpanzee(Mammal):
    BIOME = "Tropical / Rainforest"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Chimpanzee", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=5)
        self._set_cry("Hoo-ha")
        self._set_sleep("in trees")

    def unique_action(self):
        print(f"{self.name} swings through the branches.")

class Tiger(Mammal):
    BIOME = "Tropical / Rainforest"
    SIZE = "Large"

    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Tiger", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=9)
        self._set_cry("Growl")
        self._set_sleep("in a shaded den")

    def unique_action(self):
        print(f"{self.name} prowls stealthily through the jungle.")

class Sloth(Mammal):
    BIOME = "Tropical / Rainforest"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Sloth", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=1)
        self._set_cry("Squeak")
        self._set_sleep("hanging from a tree")

    def unique_action(self):
        print(f"{self.name} moves slowly from branch to branch.")

class BrownBear(Mammal):
    BIOME = "Forest / Temperate"
    SIZE = "Large"

    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Brown Bear", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=8)
        self._set_cry("Growl")
        self._set_sleep("in a cave")

    def unique_action(self):
        print(f"{self.name} digs for roots and berries.")

class Wolf(Mammal):
    BIOME = "Forest / Temperate"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Wolf", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=6)
        self._set_cry("Howl")
        self._set_sleep("in a den")

    def unique_action(self):
        print(f"{self.name} hunts in a pack.")

class Deer(Mammal):
    BIOME = "Forest / Temperate"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Deer", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=2)
        self._set_cry("Bleat")
        self._set_sleep("in the undergrowth")

    def unique_action(self):
        print(f"{self.name} grazes quietly in the forest.")

class Fox(Mammal):
    BIOME = "Forest / Temperate"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Fox", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=4)
        self._set_cry("Yip")
        self._set_sleep("in a burrow")

    def unique_action(self):
        print(f"{self.name} sneaks and hunts small prey.")

class PolarBear(Mammal):
    BIOME = "Arctic / Polar"
    SIZE = "Large"

    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Polar Bear", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=9)
        self._set_cry("Roar")
        self._set_sleep("on ice floes")

    def unique_action(self):
        print(f"{self.name} swims in icy waters.")

class ArcticFox(Mammal):
    BIOME = "Arctic / Polar"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Arctic Fox", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=3)
        self._set_cry("Yip")
        self._set_sleep("in snow dens")

    def unique_action(self):
        print(f"{self.name} hunts for small rodents in the snow.")

class Seal(Mammal):
    BIOME = "Arctic / Polar"
    SIZE = "Large"

    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Seal", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=2)
        self._set_cry("Bark")
        self._set_sleep("on ice")

    def unique_action(self):
        print(f"{self.name} dives and catches fish.")

class Walrus(Mammal):
    BIOME = "Arctic / Polar"
    SIZE = "Large"

    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Walrus", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=4)
        self._set_cry("Bellow")
        self._set_sleep("on the shore")

    def unique_action(self):
        print(f"{self.name} uses tusks to move ice blocks.")

class Reindeer(Mammal):
    BIOME = "Arctic / Polar"
    SIZE = "Medium"

    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Reindeer", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=1)
        self._set_cry("Bleat")
        self._set_sleep("in snow")

    def unique_action(self):
        print(f"{self.name} migrates across snowy tundra.")

class Camel(Mammal):
    BIOME = "Desert"
    SIZE = "Large"

    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Camel", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=3)
        self._set_cry("Grunt")
        self._set_sleep("in the sand")

    def unique_action(self):
        print(f"{self.name} stores water in its hump.")

class MeerkatDesert(Mammal):
    BIOME = "Desert"
    SIZE = "Small"

    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Meerkat", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=4)
        self._set_cry("Chirp")
        self._set_sleep("in burrow")

    def unique_action(self):
        print(f"{self.name} keeps watch from the desert mound.")
