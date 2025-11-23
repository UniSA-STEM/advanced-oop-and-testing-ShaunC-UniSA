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
from typing import Any

# Main class
class Aquatic(Animal):
    """All aquatic animals have these traits."""
    ABSTRACT = True

    def __init__(self, name: str, species: str, age: int, diet: str, biome: str,
                 enclosure_size: str, zoo: Any, can_swim: bool = True, water_type: str = "Freshwater") -> None:
        super().__init__(name, species, age, diet, biome, enclosure_size, zoo)
        self.can_swim: bool = can_swim
        self.water_type: str = water_type
        self.set_cry("Blub")
        self._Animal__food = diet
        self.set_sleep("submerged")

    def unique_action(self) -> None:
        """Aquatic animal unique action."""
        print(f"{self.name} swims around gracefully.")

# Subclasses
class Dolphin(Aquatic):
    """Dolphin in Aquatic/Marine biome."""
    BIOME = "Aquatic / Marine"
    SIZE = "Large"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Dolphin", age, diet, self.BIOME, self.SIZE, zoo, water_type="Saltwater")
        self.set_cry("Click/Whistle")
        self.set_sleep("half of brain sleeps at a time")

    def unique_action(self) -> None:
        print(f"{self.name} performs flips and jumps out of water.")


class Seal(Aquatic):
    """Seal in Aquatic/Marine biome."""
    BIOME = "Aquatic / Marine"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Seal", age, diet, self.BIOME, self.SIZE, zoo)
        self.set_cry("Bark")
        self.set_sleep("floating or on rocks")

    def unique_action(self) -> None:
        print(f"{self.name} dives and claps fins.")


class Shark(Aquatic):
    """Shark in Aquatic/Marine biome."""
    BIOME = "Aquatic / Marine"
    SIZE = "Large"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Shark", age, diet, self.BIOME, self.SIZE, zoo, water_type="Saltwater")
        self.set_cry("Silent")
        self.set_sleep("semi-active rest")

    def unique_action(self) -> None:
        print(f"{self.name} patrols the tank slowly but constantly.")


class Clownfish(Aquatic):
    """Clownfish in Aquatic/Marine biome."""
    BIOME = "Aquatic / Marine"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Omnivore") -> None:
        super().__init__(name, "Clownfish", age, diet, self.BIOME, self.SIZE, zoo, water_type="Saltwater")
        self.set_cry("Blub")
        self.set_sleep("hidden among anemones")

    def unique_action(self) -> None:
        print(f"{self.name} darts in and out of coral.")


class Seahorse(Aquatic):
    """Seahorse in Aquatic/Marine biome."""
    BIOME = "Aquatic / Marine"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Seahorse", age, diet, self.BIOME, self.SIZE, zoo, water_type="Saltwater")
        self.set_cry("Silent")
        self.set_sleep("clinging to seaweed")

    def unique_action(self) -> None:
        print(f"{self.name} swims upright using dorsal fin.")


class SeaTurtle(Aquatic):
    """Sea Turtle in Aquatic/Marine biome."""
    BIOME = "Aquatic / Marine"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Sea Turtle", age, diet, self.BIOME, self.SIZE, zoo, water_type="Saltwater")
        self.set_cry("Silent")
        self.set_sleep("floating or resting on seafloor")

    def unique_action(self) -> None:
        print(f"{self.name} glides smoothly through water.")


class Octopus(Aquatic):
    """Octopus in Aquatic/Marine biome."""
    BIOME = "Aquatic / Marine"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Octopus", age, diet, self.BIOME, self.SIZE, zoo, water_type="Saltwater")
        self.set_cry("Ink squirt")
        self.set_sleep("hidden in crevices")

    def unique_action(self) -> None:
        print(f"{self.name} uses its tentacles to explore and manipulate objects.")


class Crab(Aquatic):
    """Crab in Aquatic/Marine biome."""
    BIOME = "Aquatic / Marine"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Omnivore") -> None:
        super().__init__(name, "Crab", age, diet, self.BIOME, self.SIZE, zoo, water_type="Saltwater")
        self.set_cry("Clack")
        self.set_sleep("in burrows or rocks")

    def unique_action(self) -> None:
        print(f"{self.name} scuttles sideways along the tank floor.")