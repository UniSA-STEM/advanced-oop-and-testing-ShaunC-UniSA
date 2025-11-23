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
from typing import Any

# Main Class
class Amphibian(Animal):
    """All amphibians have these traits."""
    ABSTRACT = True

    def __init__(self, name: str, species: str, age: int, diet: str, biome: str,
                 enclosure_size: str, zoo: Any, moist_skin: bool = True, cold_blooded: bool = True) -> None:
        super().__init__(name, species, age, diet, biome, enclosure_size, zoo)
        self.moist_skin: bool = moist_skin
        self.cold_blooded: bool = cold_blooded
        self.set_cry("Croak")
        self._Animal__food = diet
        self.set_sleep("hidden in damp areas")

    def unique_action(self) -> None:
        """Amphibian unique action."""
        print(f"{self.name} jumps or swims around.")

# Subclasses
class TreeFrog(Amphibian):
    """Tree Frog in Tropical/Rainforest biome."""
    BIOME = "Tropical / Rainforest"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Insectivore") -> None:
        super().__init__(name, "Tree Frog", age, diet, self.BIOME, self.SIZE, zoo)
        self.set_cry("Ribbit")
        self.set_sleep("on leaves or branches")

    def unique_action(self) -> None:
        print(f"{self.name} jumps between leaves and branches.")


class Toad(Amphibian):
    """Toad in Forest/Temperate biome."""
    BIOME = "Forest / Temperate"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Insectivore") -> None:
        super().__init__(name, "Toad", age, diet, self.BIOME, self.SIZE, zoo)
        self.set_cry("Croak")
        self.set_sleep("in burrows or under rocks")

    def unique_action(self) -> None:
        print(f"{self.name} hops slowly and hides under cover.")