"""
File: mammals.py
Description: Contains the subclasses, attributes and methods for mammals.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from animal import Animal
from typing import Any

# Main class
class Mammal(Animal):
    """All mammals have these traits"""
    ABSTRACT = True

    def __init__(self, name: str, species: str, age: int, diet: str, biome: str,
                 enclosure_size: str, zoo: Any, nocturnal: bool = False, aggressiveness: int = 5) -> None:
        super().__init__(name, species, age, diet, biome, enclosure_size, zoo)
        self.nocturnal: bool = nocturnal
        self.aggressiveness: int = aggressiveness
        self.set_cry("Growl")
        self.set_sleep("in den")

    def unique_action(self):
        """Mammal unique action"""
        print(f"{self.name} does zoomies around the enclosure!")

# Subclasses
class Lion(Mammal):
    """Lion mammal in Savannah/Grassland biome."""
    BIOME = "Savannah / Grassland"
    SIZE = "Large"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Lion", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=8)
        self.set_cry("Roar")
        self.set_sleep("in the shade")

    def unique_action(self) -> None:
        """Lion-specific unique action."""
        print(f"{self.name} stalks its prey stealthily.")

class Elephant(Mammal):
    """Elephant mammal in Savannah/Grassland biome."""
    BIOME = "Savannah / Grassland"
    SIZE = "Large"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Elephant", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=3)
        self.set_cry("Trumpet")
        self.set_sleep("standing up")

    def unique_action(self) -> None:
        """Elephant-specific unique action."""
        print(f"{self.name} sprays water with its trunk.")

class Giraffe(Mammal):
    """Giraffe mammal in Savannah/Grassland biome."""
    BIOME = "Savannah / Grassland"
    SIZE = "Large"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Giraffe", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=2)
        self.set_cry("Bleat")
        self.set_sleep("lying down")

    def unique_action(self) -> None:
        """Giraffe-specific unique action."""
        print(f"{self.name} stretches its neck to reach high leaves.")

class Zebra(Mammal):
    """Zebra mammal in Savannah/Grassland biome."""
    BIOME = "Savannah / Grassland"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Zebra", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=4)
        self.set_cry("Whinny")
        self.set_sleep("standing up")

    def unique_action(self) -> None:
        """Zebra-specific unique action."""
        print(f"{self.name} gallops across the plains.")

class Meerkat(Mammal):
    """Meerkat mammal in Savannah/Grassland biome."""
    BIOME = "Savannah / Grassland"
    SIZE = "Small"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Omnivore") -> None:
        super().__init__(name, "Meerkat", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=4)
        self.set_cry("Chirp")
        self.set_sleep("in burrow")

    def unique_action(self) -> None:
        """Meerkat-specific unique action."""
        print(f"{self.name} stands on hind legs to watch for predators.")

class Hyena(Mammal):
    """Hyena mammal in Savannah/Grassland biome."""
    BIOME = "Savannah / Grassland"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Hyena", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=7)
        self.set_cry("Laugh")
        self.set_sleep("in dens")

    def unique_action(self) -> None:
        """Hyena-specific unique action."""
        print(f"{self.name} scavenges loudly and laughs.")

class Chimpanzee(Mammal):
    """Chimpanzee mammal in Tropical/Rainforest biome."""
    BIOME = "Tropical / Rainforest"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Omnivore") -> None:
        super().__init__(name, "Chimpanzee", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=5)
        self.set_cry("Hoo-ha")
        self.set_sleep("in trees")

    def unique_action(self) -> None:
        """Chimpanzee-specific unique action."""
        print(f"{self.name} swings through the branches.")

class Tiger(Mammal):
    """Tiger mammal in Tropical/Rainforest biome."""
    BIOME = "Tropical / Rainforest"
    SIZE = "Large"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Tiger", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=9)
        self.set_cry("Growl")
        self.set_sleep("in a shaded den")

    def unique_action(self) -> None:
        """Tiger-specific unique action."""
        print(f"{self.name} prowls stealthily through the jungle.")

class Sloth(Mammal):
    """Sloth mammal in Tropical/Rainforest biome."""
    BIOME = "Tropical / Rainforest"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Sloth", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=1)
        self.set_cry("Squeak")
        self.set_sleep("hanging from a tree")

    def unique_action(self) -> None:
        """Sloth-specific unique action."""
        print(f"{self.name} moves slowly from branch to branch.")

class BrownBear(Mammal):
    """Brown Bear mammal in Forest/Temperate biome."""
    BIOME = "Forest / Temperate"
    SIZE = "Large"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Omnivore") -> None:
        super().__init__(name, "Brown Bear", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=8)
        self.set_cry("Growl")
        self.set_sleep("in a cave")

    def unique_action(self) -> None:
        """Brown Bear-specific unique action."""
        print(f"{self.name} digs for roots and berries.")

class Wolf(Mammal):
    """Wolf mammal in Forest/Temperate biome."""
    BIOME = "Forest / Temperate"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Wolf", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=6)
        self.set_cry("Howl")
        self.set_sleep("in a den")

    def unique_action(self) -> None:
        """Wolf-specific unique action."""
        print(f"{self.name} hunts in a pack.")

class Deer(Mammal):
    """Deer mammal in Forest/Temperate biome."""
    BIOME = "Forest / Temperate"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Deer", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=2)
        self.set_cry("Bleat")
        self.set_sleep("in the undergrowth")

    def unique_action(self) -> None:
        """Deer-specific unique action."""
        print(f"{self.name} grazes quietly in the forest.")

class Fox(Mammal):
    """Fox mammal in Forest/Temperate biome."""
    BIOME = "Forest / Temperate"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Omnivore") -> None:
        super().__init__(name, "Fox", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=4)
        self.set_cry("Yip")
        self.set_sleep("in a burrow")

    def unique_action(self) -> None:
        """Fox-specific unique action."""
        print(f"{self.name} sneaks and hunts small prey.")

class PolarBear(Mammal):
    """Polar Bear mammal in Arctic/Polar biome."""
    BIOME = "Arctic / Polar"
    SIZE = "Large"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Polar Bear", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=9)
        self.set_cry("Roar")
        self.set_sleep("on ice floes")

    def unique_action(self) -> None:
        """Polar Bear-specific unique action."""
        print(f"{self.name} swims in icy waters.")

class ArcticFox(Mammal):
    """Arctic Fox mammal in Arctic/Polar biome."""
    BIOME = "Arctic / Polar"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Omnivore") -> None:
        super().__init__(name, "Arctic Fox", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=True, aggressiveness=3)
        self.set_cry("Yip")
        self.set_sleep("in snow dens")

    def unique_action(self) -> None:
        """Arctic Fox-specific unique action."""
        print(f"{self.name} hunts for small rodents in the snow.")

class Seal(Mammal):
    """Seal mammal in Arctic/Polar biome."""
    BIOME = "Arctic / Polar"
    SIZE = "Large"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Carnivore") -> None:
        super().__init__(name, "Seal", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=2)
        self.set_cry("Bark")
        self.set_sleep("on ice")

    def unique_action(self) -> None:
        """Seal-specific unique action."""
        print(f"{self.name} dives and catches fish.")

class Walrus(Mammal):
    """Walrus mammal in Arctic/Polar biome."""
    BIOME = "Arctic / Polar"
    SIZE = "Large"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Omnivore") -> None:
        super().__init__(name, "Walrus", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=4)
        self.set_cry("Bellow")
        self.set_sleep("on the shore")

    def unique_action(self) -> None:
        """Walrus-specific unique action."""
        print(f"{self.name} uses tusks to move ice blocks.")

class Reindeer(Mammal):
    """Reindeer mammal in Arctic/Polar biome."""
    BIOME = "Arctic / Polar"
    SIZE = "Medium"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Reindeer", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=1)
        self.set_cry("Bleat")
        self.set_sleep("in snow")

    def unique_action(self) -> None:
        """Reindeer-specific unique action."""
        print(f"{self.name} migrates across snowy tundra.")

class Camel(Mammal):
    """Camel mammal in Desert biome."""
    BIOME = "Desert"
    SIZE = "Large"

    def __init__(self, name: str, age: int, zoo: Any, diet: str = "Herbivore") -> None:
        super().__init__(name, "Camel", age, diet, self.BIOME, self.SIZE, zoo,
                         nocturnal=False, aggressiveness=3)
        self.set_cry("Grunt")
        self.set_sleep("in the sand")

    def unique_action(self) -> None:
        """Camel-specific unique action."""
        print(f"{self.name} stores water in its hump.")