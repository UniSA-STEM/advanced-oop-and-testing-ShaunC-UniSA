"""
File: aquatic.py
Description: Contains the subclasses, attributes and methods for aquatic animals.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from animal import Animal


# Main class
class Aquatic(Animal):
    """All aquatic animals share these demo traits"""
    def __init__(self, id, name, species, age, diet, biome, enclosure_size,
                 can_swim=True, water_type="Freshwater"):
        super().__init__(id, name, species, age, diet, biome, enclosure_size)
        self.can_swim = can_swim
        self.water_type = water_type  # "Freshwater" or "Saltwater"
        self._Animal__cry = "Blub"
        self._Animal__food = diet
        self._Animal__sleep = "submerged"

    def unique_action(self):
        print(f"{self.name} swims around gracefully.")


# Subclasses
class Dolphin(Aquatic):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Dolphin", age, diet, "Aquatic / Marine", "Large",
                         water_type="Saltwater")
        self._Animal__cry = "Click/Whistle"
        self._Animal__sleep = "half of brain sleeps at a time"

    def unique_action(self):
        print(f"{self.name} performs flips and jumps out of water.")

class Seal(Aquatic):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Seal", age, diet, "Aquatic / Marine", "Medium")
        self._Animal__cry = "Bark"
        self._Animal__sleep = "floating or on rocks"

    def unique_action(self):
        print(f"{self.name} dives and claps fins.")

class Shark(Aquatic):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Shark", age, diet, "Aquatic / Marine", "Large",
                         water_type="Saltwater")
        self._Animal__cry = "Silent"
        self._Animal__sleep = "semi-active rest"

    def unique_action(self):
        print(f"{self.name} patrols the tank slowly but constantly.")

class Clownfish(Aquatic):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Clownfish", age, diet, "Aquatic / Marine", "Small",
                         water_type="Saltwater")
        self._Animal__cry = "Blub"
        self._Animal__sleep = "hidden among anemones"

    def unique_action(self):
        print(f"{self.name} darts in and out of coral.")

class Seahorse(Aquatic):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Seahorse", age, diet, "Aquatic / Marine", "Small",
                         water_type="Saltwater")
        self._Animal__cry = "Silent"
        self._Animal__sleep = "clinging to seaweed"

    def unique_action(self):
        print(f"{self.name} swims upright using dorsal fin.")

class SeaTurtle(Aquatic):
    def __init__(self, id, name, age, diet="Herbivore"):
        super().__init__(id, name, "Sea Turtle", age, diet, "Aquatic / Marine", "Medium",
                         water_type="Saltwater")
        self._Animal__cry = "Silent"
        self._Animal__sleep = "floating or resting on seafloor"

    def unique_action(self):
        print(f"{self.name} glides smoothly through water.")

class Octopus(Aquatic):
    def __init__(self, id, name, age, diet="Carnivore"):
        super().__init__(id, name, "Octopus", age, diet, "Aquatic / Marine", "Medium",
                         water_type="Saltwater")
        self._Animal__cry = "Ink squirt"
        self._Animal__sleep = "hidden in crevices"

    def unique_action(self):
        print(f"{self.name} uses its tentacles to explore and manipulate objects.")

class Crab(Aquatic):
    def __init__(self, id, name, age, diet="Omnivore"):
        super().__init__(id, name, "Crab", age, diet, "Aquatic / Marine", "Small",
                         water_type="Saltwater")
        self._Animal__cry = "Clack"
        self._Animal__sleep = "in burrows or rocks"

    def unique_action(self):
        print(f"{self.name} scuttles sideways along the tank floor.")