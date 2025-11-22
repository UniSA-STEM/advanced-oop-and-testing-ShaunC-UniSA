"""
File: enclosure.py
Description: Contains the classes, functions, and methods related to zoo enclosures.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Enclosures
class Enclosure:
    """Enclosures can hold animals of various types."""
    enclosure_list = []

    def __init__(self, size=str, biome=str, zoo=None, name=None):
        self.__enclosure_id = self.get_next_id()
        self.__enclosure_name = name if name else "Empty Enclosure"
        self.__enclosure_size = size
        self.__enclosure_biome = biome
        self.__enclosure_cleanliness = 10
        self.__enclosure_animal = []

        Enclosure.enclosure_list.append(self)

        if zoo:
            zoo.enclosures.append(self)

    @classmethod
    def get_next_id(cls):
        """Returns the first available enclosure-id that isn't already assigned."""
        next_available_id = 1
        while any(next_available_id == enclosure._Enclosure__enclosure_id for enclosure in cls.enclosure_list):
            next_available_id += 1
        return next_available_id


    @property
    def enclosure_id(self):
        return self.__enclosure_id

    @property
    def name(self):
        return self.__enclosure_name

    @property
    def size(self):
        return self.__enclosure_size

    @property
    def biome(self):
        return self.__enclosure_biome

    @property
    def cleanliness(self):
        return self.__enclosure_cleanliness

    @property
    def animals(self):
        return self.__enclosure_animal

    @name.setter
    def name(self, value):
        self.__enclosure_name = value

    @biome.setter
    def biome(self, value):
        self.__enclosure_biome = value

    @cleanliness.setter
    def cleanliness(self, value):
        self.__enclosure_cleanliness = max(1, min(10, value))

    def __eq__(self, other):
        if not isinstance(other, Enclosure):
            return False
        return self.name == other.name and self.biome == other.biome and self.size == other.size

    def __str__(self):
        animal_status = "Empty" if not self.__enclosure_animal else type(self.__enclosure_animal[0]).__name__
        return (
            f"Enclosure # {self.__enclosure_id} | "
            f"Name: {self.__enclosure_name} | "
            f"Biome: {self.__enclosure_biome} | "
            f"Size: {self.__enclosure_size} | "
            f"Cleanliness: {self.__enclosure_cleanliness} | "
            f"Animal Type: {animal_status}")

# EnclosureOps
def add_enclosure(zoo):
    """Adds an enclosure to the Zoo"""
    print("\nAdding new enclosure:")

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
        6: "Aquatic / Marine",
        7: "Quarantine"}

    valid_biome = False
    while not valid_biome:
        try:
            print("\nSelect Biome:")
            for key, val in biome_options.items():
                print(f"{key}. {val}")
            choice = int(input("Enter choice (1-7): "))
            if choice in biome_options:
                biome = biome_options[choice]
                valid_biome = True
            else:
                print("Invalid selection. Enter a number between 1 and 7.")
        except ValueError:
            print("Input must be a number.")

    name_input = input("\nEnter Enclosure Name (press Enter for 'Empty Enclosure'): ").strip()
    enclosure_name = name_input if name_input else "Empty Enclosure"

    enclosure = Enclosure(enclosure_size, biome, zoo)
    enclosure.name = enclosure_name
    print("\nEnclosure created:")
    print(enclosure)
    return enclosure


def remove_enclosure(zoo, enclosure_id):
    """Removes an enclosure from the list of enclosures."""
    for enclosure in zoo.enclosures:
        if enclosure.enclosure_id == enclosure_id:
            zoo.enclosures.remove(enclosure)
            print(f"Enclosure #{enclosure_id} removed.")
            return
    print(f"No enclosure found with ID #{enclosure_id}.")


def list_enclosures(zoo):
    """Lists all enclosures and their details."""
    if not zoo.enclosures:
        print("No enclosures in the zoo.")
    else:
        print("\n=== Zoo Enclosures ===\n")
        for enclosure in zoo.enclosures:
            print("-", enclosure)