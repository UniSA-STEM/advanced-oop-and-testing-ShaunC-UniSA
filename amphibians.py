"""
File: amphibians.py
Description: Contains the subclasses, attributes and methods for amphibian animals.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from animal import Animal


# Main class
class Amphibian(Animal):
    """All amphibians have these traits"""
    def __init__(self, name, species, age, diet, biome, enclosure_size,
                 moist_skin=True, cold_blooded=True):
        super().__init__(name, species, age, diet, biome, enclosure_size)
        self.moist_skin = moist_skin
        self.cold_blooded = cold_blooded
        self._set_cry("Croak")
        self._Animal__food = diet
        self._set_sleep("hidden in damp areas")

    def unique_action(self):
        print(f"{self.name} jumps or swims around.")


# Subclasses
class TreeFrog(Amphibian):
    def __init__(self, name, age, diet="Insectivore"):
        super().__init__(name, "Tree Frog", age, diet, "Tropical / Rainforest", "Small")
        self._set_cry("Ribbit")
        self._set_sleep("on leaves or branches")

    def unique_action(self):
        print(f"{self.name} jumps between leaves and branches.")


class Toad(Amphibian):
    def __init__(self, name, age, diet="Insectivore"):
        super().__init__(name, "Toad", age, diet, "Forest / Temperate", "Small")
        self._set_cry("Croak")
        self._set_sleep("in burrows or under rocks")

    def unique_action(self):
        print(f"{self.name} hops slowly and hides under cover.")
