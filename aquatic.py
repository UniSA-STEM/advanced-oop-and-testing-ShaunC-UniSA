"""
File: aquatic.py
Description: Contains the subclasses, attributes and methods for aquatic animals.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

from animal import Animal

# Main class
class Aquatic(Animal):
    """All aquatic animals share these traits"""
    def __init__(self, name, species, age, diet, biome, enclosure_size, zoo,
                 can_swim=True, water_type="Freshwater"):
        super().__init__(name, species, age, diet, biome, enclosure_size, zoo)
        self.can_swim = can_swim
        self.water_type = water_type
        self._set_cry("Blub")
        self._Animal__food = diet
        self._set_sleep("submerged")

    def unique_action(self):
        print(f"{self.name} swims around gracefully.")


# Subclasses
class Dolphin(Aquatic):
    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Dolphin", age, diet, "Aquatic / Marine", "Large",
                         zoo, water_type="Saltwater")
        self._set_cry("Click/Whistle")
        self._set_sleep("half of brain sleeps at a time")

    def unique_action(self):
        print(f"{self.name} performs flips and jumps out of water.")


class Seal(Aquatic):
    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Seal", age, diet, "Aquatic / Marine", "Medium", zoo)
        self._set_cry("Bark")
        self._set_sleep("floating or on rocks")

    def unique_action(self):
        print(f"{self.name} dives and claps fins.")


class Shark(Aquatic):
    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Shark", age, diet, "Aquatic / Marine", "Large",
                         zoo, water_type="Saltwater")
        self._set_cry("Silent")
        self._set_sleep("semi-active rest")

    def unique_action(self):
        print(f"{self.name} patrols the tank slowly but constantly.")


class Clownfish(Aquatic):
    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Clownfish", age, diet, "Aquatic / Marine", "Small",
                         zoo, water_type="Saltwater")
        self._set_cry("Blub")
        self._set_sleep("hidden among anemones")

    def unique_action(self):
        print(f"{self.name} darts in and out of coral.")


class Seahorse(Aquatic):
    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Seahorse", age, diet, "Aquatic / Marine", "Small",
                         zoo, water_type="Saltwater")
        self._set_cry("Silent")
        self._set_sleep("clinging to seaweed")

    def unique_action(self):
        print(f"{self.name} swims upright using dorsal fin.")


class SeaTurtle(Aquatic):
    def __init__(self, name, age, zoo, diet="Herbivore"):
        super().__init__(name, "Sea Turtle", age, diet, "Aquatic / Marine", "Medium",
                         zoo, water_type="Saltwater")
        self._set_cry("Silent")
        self._set_sleep("floating or resting on seafloor")

    def unique_action(self):
        print(f"{self.name} glides smoothly through water.")


class Octopus(Aquatic):
    def __init__(self, name, age, zoo, diet="Carnivore"):
        super().__init__(name, "Octopus", age, diet, "Aquatic / Marine", "Medium",
                         zoo, water_type="Saltwater")
        self._set_cry("Ink squirt")
        self._set_sleep("hidden in crevices")

    def unique_action(self):
        print(f"{self.name} uses its tentacles to explore and manipulate objects.")


class Crab(Aquatic):
    def __init__(self, name, age, zoo, diet="Omnivore"):
        super().__init__(name, "Crab", age, diet, "Aquatic / Marine", "Small",
                         zoo, water_type="Saltwater")
        self._set_cry("Clack")
        self._set_sleep("in burrows or rocks")

    def unique_action(self):
        print(f"{self.name} scuttles sideways along the tank floor.")