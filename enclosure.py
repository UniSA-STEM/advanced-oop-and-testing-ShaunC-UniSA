"""
File: enclosure.py
Description: Contains the classes, functions, and methods related to zoo enclosures.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from animal import animal
from staff import staff

# Enclosures
class Enclosure:
    """Enclosures can hold animals of various types."""
    def __init__(self, size=str, environment=str, cleanliness=int):
        self.__size = size
        self.__environment = environment
        self.__cleanliness = cleanliness

    # Each enclosure is restricted to a single type of animal, meaning incompatible species should not be housed
    # together (e.g., koalas should not be placed in a penguin enclosure).

    def __str__(self):
        return f'{self.__size} {self.__environment} {self.__cleanliness}'


# Operations
def add_enclosures():


def remove_enclosures():