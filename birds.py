"""
File: birds.py
Description: Contains the subclasses, attributes and methods for birds.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from animal import Animal
from typing import Any

# Main class
class Bird(Animal):
    """All birds have these traits."""
    ABSTRACT = True

    def __init__(self, name: str, species: str, age: int, diet: str, biome: str,
                 enclosure_size: str, zoo: Any, wingspan_cm: int = 50, can_fly: bool = True) -> None:
        super().__init__(name, species, age, diet, biome, enclosure_size, zoo)
        self.wingspan_cm: int = wingspan_cm
        self.can_fly: bool = can_fly
        self.set_cry("Chirp")
        self._Animal__food = diet
        self.set_sleep("perched")

    def unique_action(self) -> None:
        """Bird unique action."""
        print(f"{self.name} flies or hops around.")

# Subclasses
class Ostrich(Bird):
    """Ostrich bird in Savannah/Grassland biome."""
    BIOME = "Savannah / Grassland"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Omnivore") -> None:
        super().__init__(name, "Ostrich", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=200, can_fly=False)
        self.set_cry("Boom")
        self.set_sleep("on the ground")

    def unique_action(self) -> None:
        print(f"{self.name} runs at high speed.")


class Vulture(Bird):
    """Vulture bird in Savannah/Grassland biome."""
    BIOME = "Savannah / Grassland"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Vulture", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=250)
        self.set_cry("Screech")
        self.set_sleep("in trees")

    def unique_action(self) -> None:
        print(f"{self.name} circles high in the sky searching for carrion.")


class Parrot(Bird):
    """Parrot bird in Tropical/Rainforest biome."""
    BIOME = "Tropical / Rainforest"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Parrot", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=40)
        self.set_cry("Squawk")
        self.set_sleep("in trees")

    def unique_action(self) -> None:
        print(f"{self.name} mimics sounds and talks.")


class Toucan(Bird):
    """Toucan bird in Tropical/Rainforest biome."""
    BIOME = "Tropical / Rainforest"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Omnivore") -> None:
        super().__init__(name, "Toucan", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=60)
        self.set_cry("Croak")
        self.set_sleep("in tree branches")

    def unique_action(self) -> None:
        print(f"{self.name} uses its large bill to reach fruit.")


class Macaw(Bird):
    """Macaw bird in Tropical/Rainforest biome."""
    BIOME = "Tropical / Rainforest"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Macaw", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=100)
        self.set_cry("Squawk")
        self.set_sleep("in treetops")

    def unique_action(self) -> None:
        print(f"{self.name} glides through the rainforest canopy.")


class Owl(Bird):
    """Owl bird in Forest/Temperate biome."""
    BIOME = "Forest / Temperate"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Owl", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=120)
        self.set_cry("Hoot")
        self.set_sleep("in tree hollows during the day")

    def unique_action(self) -> None:
        print(f"{self.name} hunts silently at night.")


class Woodpecker(Bird):
    """Woodpecker bird in Forest/Temperate biome."""
    BIOME = "Forest / Temperate"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Omnivore") -> None:
        super().__init__(name, "Woodpecker", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=30)
        self.set_cry("Drill")
        self.set_sleep("in tree cavities")

    def unique_action(self) -> None:
        print(f"{self.name} pecks at tree trunks to find insects.")


class Penguin(Bird):
    """Penguin bird in Arctic/Polar biome."""
    BIOME = "Arctic / Polar"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Penguin", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=0, can_fly=False)
        self.set_cry("Honk")
        self.set_sleep("on ice")

    def unique_action(self) -> None:
        print(f"{self.name} waddles and swims skillfully.")


class Puffin(Bird):
    """Puffin bird in Arctic/Polar biome."""
    BIOME = "Arctic / Polar"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Puffin", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=50)
        self.set_cry("Growl")
        self.set_sleep("in burrows")

    def unique_action(self) -> None:
        print(f"{self.name} dives into the sea to catch fish.")


class SnowyOwl(Bird):
    """Snowy Owl bird in Arctic/Polar biome."""
    BIOME = "Arctic / Polar"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Snowy Owl", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=150)
        self.set_cry("Hoot")
        self.set_sleep("on snowy branches")

    def unique_action(self) -> None:
        print(f"{self.name} hunts quietly over snow fields.")


class Roadrunner(Bird):
    """Roadrunner bird in Desert biome."""
    BIOME = "Desert"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Omnivore") -> None:
        super().__init__(name, "Roadrunner", age, diet, self.BIOME, self.SIZE, zoo, wingspan_cm=45)
        self.set_cry("Beep-beep")
        self.set_sleep("in desert shrubs")

    def unique_action(self) -> None:
        print(f"{self.name} runs at amazing speed on the ground.")