"""
File: reptiles.py
Description: Contains the subclasses, attributes and methods for reptiles.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from animal import Animal


# Main Class
class Reptile(Animal):
    """All reptiles have these traits"""
    def __init__(self, id, name, species, age, diet, biome, enclosure_size,
                 cold_blooded=True, scales=True):
        super().__init__(id, name, species, age, diet, biome, enclosure_size)
        self.cold_blooded = cold_blooded
        self.scales = scales
        self._Animal__cry = "Hiss"
        self._Animal__food = diet
        self._Animal__sleep = "in sun or hidden"

    def unique_action(self):
        print(f"{self.name} crawls or slithers around.")


# Subclasses
class Python(Reptile):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Python", age, diet, "Tropical / Rainforest", "Medium")
        self._Animal__cry = "Hiss"
        self._Animal__sleep = "coiled in a hidden spot"

    def unique_action(self):
        print(f"{self.name} constricts its prey.")

class Iguana(Reptile):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Iguana", age, diet, "Tropical / Rainforest", "Small")
        self._Animal__cry = "Hiss"
        self._Animal__sleep = "on tree branches"

    def unique_action(self):
        print(f"{self.name} basks in the sun.")

class MonitorLizard(Reptile):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Monitor Lizard", age, diet, "Desert", "Medium")
        self._Animal__cry = "Hiss"
        self._Animal__sleep = "in burrows or shade"

    def unique_action(self):
        print(f"{self.name} explores rocks and burrows.")

class Rattlesnake(Reptile):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Rattlesnake", age, diet, "Desert", "Small")
        self._Animal__cry = "Rattle"
        self._Animal__sleep = "hidden in sand or rocks"

    def unique_action(self):
        print(f"{self.name} shakes its rattle as a warning.")

class Tortoise(Reptile):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Tortoise", age, diet, "Desert", "Medium")
        self._Animal__cry = "Silent"
        self._Animal__sleep = "in shell or under rocks"

    def unique_action(self):
        print(f"{self.name} slowly walks and grazes plants.")

class SeaTurtle(Reptile):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Sea Turtle", age, diet, "Aquatic / Marine", "Medium")
        self._Animal__cry = "Silent"
        self._Animal__sleep = "floating or resting underwater"

    def unique_action(self):
        print(f"{self.name} swims gracefully in the ocean.")