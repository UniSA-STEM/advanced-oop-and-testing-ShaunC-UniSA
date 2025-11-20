"""
File: mammals.py
Description: Contains the subclasses, attributes and methods for mammals.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

class Mammal(Animal):
    """All mammals have these traits"""
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
    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Lion", age, diet, "Savannah / Grassland", "Large",
                         zoo, nocturnal=False, aggressiveness=8)
        self._set_cry("Roar")
        self._set_sleep("in the shade")

    def unique_action(self):
        print(f"{self.name} stalks its prey stealthily.")


class Elephant(Mammal):
    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Elephant", age, diet, "Savannah / Grassland", "Large",
                         zoo, nocturnal=False, aggressiveness=3)
        self._set_cry("Trumpet")
        self._set_sleep("standing up")

    def unique_action(self):
        print(f"{self.name} sprays water with its trunk.")


class Giraffe(Mammal):
    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Giraffe", age, diet, "Savannah / Grassland", "Large",
                         zoo, nocturnal=False, aggressiveness=2)
        self._set_cry("Bleat")
        self._set_sleep("lying down")

    def unique_action(self):
        print(f"{self.name} stretches its neck to reach high leaves.")


class Zebra(Mammal):
    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Zebra", age, diet, "Savannah / Grassland", "Medium",
                         zoo, nocturnal=False, aggressiveness=4)
        self._set_cry("Whinny")
        self._set_sleep("standing up")

    def unique_action(self):
        print(f"{self.name} gallops across the plains.")


class Meerkat(Mammal):
    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Meerkat", age, diet, "Savannah / Grassland", "Small",
                         zoo, nocturnal=True, aggressiveness=4)
        self._set_cry("Chirp")
        self._set_sleep("in burrow")

    def unique_action(self):
        print(f"{self.name} stands on hind legs to watch for predators.")


class Hyena(Mammal):
    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Hyena", age, diet, "Savannah / Grassland", "Medium",
                         zoo, nocturnal=True, aggressiveness=7)
        self._set_cry("Laugh")
        self._set_sleep("in dens")

    def unique_action(self):
        print(f"{self.name} scavenges loudly and laughs.")


class Chimpanzee(Mammal):
    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Chimpanzee", age, diet, "Tropical / Rainforest", "Medium",
                         zoo, nocturnal=False, aggressiveness=5)
        self._set_cry("Hoo-ha")
        self._set_sleep("in trees")

    def unique_action(self):
        print(f"{self.name} swings through the branches.")


class Tiger(Mammal):
    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Tiger", age, diet, "Tropical / Rainforest", "Large",
                         zoo, nocturnal=True, aggressiveness=9)
        self._set_cry("Growl")
        self._set_sleep("in a shaded den")

    def unique_action(self):
        print(f"{self.name} prowls stealthily through the jungle.")


class Sloth(Mammal):
    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Sloth", age, diet, "Tropical / Rainforest", "Medium",
                         zoo, nocturnal=False, aggressiveness=1)
        self._set_cry("Squeak")
        self._set_sleep("hanging from a tree")

    def unique_action(self):
        print(f"{self.name} moves slowly from branch to branch.")


class BrownBear(Mammal):
    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Brown Bear", age, diet, "Forest / Temperate", "Large",
                         zoo, nocturnal=True, aggressiveness=8)
        self._set_cry("Growl")
        self._set_sleep("in a cave")

    def unique_action(self):
        print(f"{self.name} digs for roots and berries.")


class Wolf(Mammal):
    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Wolf", age, diet, "Forest / Temperate", "Medium",
                         zoo, nocturnal=True, aggressiveness=6)
        self._set_cry("Howl")
        self._set_sleep("in a den")

    def unique_action(self):
        print(f"{self.name} hunts in a pack.")


class Deer(Mammal):
    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Deer", age, diet, "Forest / Temperate", "Medium",
                         zoo, nocturnal=False, aggressiveness=2)
        self._set_cry("Bleat")
        self._set_sleep("in the undergrowth")

    def unique_action(self):
        print(f"{self.name} grazes quietly in the forest.")


class Fox(Mammal):
    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Fox", age, diet, "Forest / Temperate", "Medium",
                         zoo, nocturnal=True, aggressiveness=4)
        self._set_cry("Yip")
        self._set_sleep("in a burrow")

    def unique_action(self):
        print(f"{self.name} sneaks and hunts small prey.")


class PolarBear(Mammal):
    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Polar Bear", age, diet, "Arctic / Polar", "Large",
                         zoo, nocturnal=False, aggressiveness=9)
        self._set_cry("Roar")
        self._set_sleep("on ice floes")

    def unique_action(self):
        print(f"{self.name} swims in icy waters.")


class ArcticFox(Mammal):
    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Arctic Fox", age, diet, "Arctic / Polar", "Medium",
                         zoo, nocturnal=True, aggressiveness=3)
        self._set_cry("Yip")
        self._set_sleep("in snow dens")

    def unique_action(self):
        print(f"{self.name} hunts for small rodents in the snow.")


class Seal(Mammal):
    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Seal", age, diet, "Arctic / Polar", "Large",
                         zoo, nocturnal=False, aggressiveness=2)
        self._set_cry("Bark")
        self._set_sleep("on ice")

    def unique_action(self):
        print(f"{self.name} dives and catches fish.")


class Walrus(Mammal):
    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Walrus", age, diet, "Arctic / Polar", "Large",
                         zoo, nocturnal=False, aggressiveness=4)
        self._set_cry("Bellow")
        self._set_sleep("on the shore")

    def unique_action(self):
        print(f"{self.name} uses tusks to move ice blocks.")


class Reindeer(Mammal):
    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Reindeer", age, diet, "Arctic / Polar", "Medium",
                         zoo, nocturnal=False, aggressiveness=1)
        self._set_cry("Bleat")
        self._set_sleep("in snow")

    def unique_action(self):
        print(f"{self.name} migrates across snowy tundra.")


class Camel(Mammal):
    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Camel", age, diet, "Desert", "Large",
                         zoo, nocturnal=False, aggressiveness=3)
        self._set_cry("Grunt")
        self._set_sleep("in the sand")

    def unique_action(self):
        print(f"{self.name} stores water in its hump.")


class MeerkatDesert(Mammal):
    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Meerkat", age, diet, "Desert", "Small",
                         zoo, nocturnal=True, aggressiveness=4)
        self._set_cry("Chirp")
        self._set_sleep("in burrow")

    def unique_action(self):
        print(f"{self.name} keeps watch from the desert mound.")
