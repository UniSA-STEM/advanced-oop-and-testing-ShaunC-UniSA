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
    ABSTRACT = True  # Mark base class as abstract for build_animal_database

    def __init__(self, name, species, age, diet, biome, enclosure_size, zoo,
                 moist_skin=True, cold_blooded=True):
        super().__init__(name, species, age, diet, biome, enclosure_size, zoo)
        self.moist_skin = moist_skin
        self.cold_blooded = cold_blooded
        self._set_cry("Croak")
        self._Animal__food = diet
        self._set_sleep("hidden in damp areas")

    def unique_action(self):
        print(f"{self.name} jumps or swims around.")

# Subclasses
class TreeFrog(Amphibian):
    BIOME = "Tropical / Rainforest"
    SIZE = "Small"

    def __init__(self, name, age, zoo, diet="Insectivore"):
        super().__init__(name, "Tree Frog", age, diet, self.BIOME, self.SIZE, zoo)
        self._set_cry("Ribbit")
        self._set_sleep("on leaves or branches")

    def unique_action(self):
        print(f"{self.name} jumps between leaves and branches.")

class Toad(Amphibian):
    BIOME = "Forest / Temperate"
    SIZE = "Small"

    def __init__(self, name, age, zoo, diet="Insectivore"):
        super().__init__(name, "Toad", age, diet, self.BIOME, self.SIZE, zoo)
        self._set_cry("Croak")
        self._set_sleep("in burrows or under rocks")

    def unique_action(self):
        print(f"{self.name} hops slowly and hides under cover.")