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
    enclosure_list = []

    def __init__(self, size=str, biome=str):
        self.__enclosure_id = self.get_next_id()
        self.__enclosure_name = "Empty Enclosure"
        self.__enclosure_size = size
        self.__enclosure_biome = biome
        self.__enclosure_cleanliness = 10
        self.__enclosure_animal = []

        Enclosure.enclosure_list.append(self)

    @classmethod
    def get_next_id(cls):
        """Returns the first available enclosure-id that isn't already assigned."""
        next_available_id = 1
        while any(next_available_id == enclosure._Enclosure__enclosure_id for enclosure in cls.enclosure_list):
            next_available_id += 1
        return next_available_id

    @classmethod
    def list_all_enclosures(cls):
        """Lists all enclosures and their details."""
        if not cls.enclosure_list:
            print("No enclosures exist.")
        else:
            for enclosure in cls.enclosure_list:
                print(enclosure)

    @property
    def enclosure_id(self):
        return self.__enclosure_id

    def __str__(self):
        animal_status = "Empty" if not self.__enclosure_animal else type(self.__enclosure_animal[0]).__name__
        return (
            f"Enclosure # {self.__enclosure_id} | "
            f"Name: {self.__enclosure_name} | "
            f"Biome: {self.__enclosure_biome} | "
            f"Size: {self.__enclosure_size} | "
            f"Cleanliness: {self.__enclosure_cleanliness} | "
            f"Animal Type: {animal_status}"
        )

# EnclosureOps
def add_enclosure():
    """Adds an enclosure to the Zoo"""
    print(f"\nAdding new {self.animal_type} enclosure")

    size_options = {1: "Small", 2: "Medium", 3: "Large"}

    valid_size = False
    while not valid_size:
        try:
            print("\nSelect Enclosure Size:")
            for key, val in size_options.items():
                print(f"{key} {val}")
            choice = int(input("Enter choice (1-3): "))
            if choice in size_options:
                enclosure_size = size_options[choice]
                valid_size = True
            else:
                print("Invalid selection. Enter 1, 2, or 3.")
        except ValueError:
            print("Input must be a number (1-3).")

    biome_options = {
        1: "Savannah / Grassland",
        2: "Tropical / Rainforest",
        3: "Forest / Temperate",
        4: "Arctic / Polar",
        5: "Desert",
        6: "Aquatic / Marine"
    }

    valid_biome = False
    while not valid_biome:
        try:
            print("\nSelect Biome:")
            print("1 Savannah / Grassland  2 Tropical / Rainforest  3 Forest / Temperate")
            print("4 Arctic / Polar  5 Desert  6 Aquatic / Marine")
            choice = int(input("Enter choice (1-6): "))
            if choice in biome_options:
                biome = biome_options[choice]
                valid_biome = True
            else:
                print(f"Invalid selection. Enter a number between 1 and 6.")
        except ValueError:
            print("Input must be a number.")

    enclosure = Enclosure(enclosure_size, biome)
    print("\nEnclosure created:")
    print(enclosure)
    return enclosure


def remove_enclosures(enclosure_id):
    """Removes the enclosure from the list of enclosure_ids."""
    if self.__enclosure_id in Enclosure.enclosure_ids:
        Enclosure.enclosure_ids.remove(self.__enclosure_id)