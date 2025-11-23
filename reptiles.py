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
from typing import Any

# Main Class
class Reptile(Animal):
    """All reptiles have these traits."""
    ABSTRACT = True

    def __init__(self, name: str, species: str, age: int, diet: str, biome: str,
                 enclosure_size: str, zoo: Any, cold_blooded: bool = True, scales: bool = True) -> None:
        super().__init__(name, species, age, diet, biome, enclosure_size, zoo)
        self.cold_blooded: bool = cold_blooded
        self.scales: bool = scales
        self.set_cry("Hiss")
        self._Animal__food = diet
        self.set_sleep("in sun or hidden")

    def unique_action(self) -> None:
        """Reptile unique action."""
        print(f"{self.name} crawls or slithers around.")

# Subclasses
class Python(Reptile):
    """Python snake in Tropical/Rainforest biome."""
    BIOME = "Tropical / Rainforest"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Python", age, diet, self.BIOME, self.SIZE, zoo)
        self.set_cry("Hiss")
        self.set_sleep("coiled in a hidden spot")

    def unique_action(self) -> None:
        print(f"{self.name} constricts its prey.")


class Iguana(Reptile):
    """Iguana in Tropical/Rainforest biome."""
    BIOME = "Tropical / Rainforest"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Iguana", age, diet, self.BIOME, self.SIZE, zoo)
        self.set_cry("Hiss")
        self.set_sleep("on tree branches")

    def unique_action(self) -> None:
        print(f"{self.name} basks in the sun.")


class MonitorLizard(Reptile):
    """Monitor Lizard in Desert biome."""
    BIOME = "Desert"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Monitor Lizard", age, diet, self.BIOME, self.SIZE, zoo)
        self.set_cry("Hiss")
        self.set_sleep("in burrows or shade")

    def unique_action(self) -> None:
        print(f"{self.name} explores rocks and burrows.")


class Rattlesnake(Reptile):
    """Rattlesnake in Desert biome."""
    BIOME = "Desert"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Rattlesnake", age, diet, self.BIOME, self.SIZE, zoo)
        self.set_cry("Rattle")
        self.set_sleep("hidden in sand or rocks")

    def unique_action(self) -> None:
        print(f"{self.name} shakes its rattle as a warning.")


class Tortoise(Reptile):
    """Tortoise in Desert biome."""
    BIOME = "Desert"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Tortoise", age, diet, self.BIOME, self.SIZE, zoo)
        self.set_cry("Silent")
        self.set_sleep("in shell or under rocks")

    def unique_action(self) -> None:
        print(f"{self.name} slowly walks and grazes plants.")


class SeaTurtle(Reptile):
    """Sea Turtle in Aquatic/Marine biome."""
    BIOME = "Aquatic / Marine"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Sea Turtle", age, diet, self.BIOME, self.SIZE, zoo)
        self.set_cry("Silent")
        self.set_sleep("floating or resting underwater")

    def unique_action(self) -> None:
        print(f"{self.name} swims gracefully in the ocean.")