"""
File: animal.py
Description: Contains the classes, functions, and methods relating to zoo animals.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from enclosure import enclosure
from staff import staff

# Animals
class Animal:
    """Represents a zoo animal."""
    def __init__(self, id, name, species, age, diet, biome, enclosure_size):
        self.__id = id
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__biome = biome
        self.__enclosure_size = enclosure_size
        self.__cry = "Animal noises"
        self.__food = diet
        self.__sleep = "peacefully"
        self.__injuries = None
        self.__illnesses = None
        self.__behavior = None
        self.__under_treatment = False

    # Properties
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

    @property
    def age(self):
        return self.__age

    @property
    def diet(self):
        return self.__diet

    @property
    def biome(self):
        return self.__biome

    @property
    def enclosure_size(self):
        return self.__enclosure_size

    @property
    def cry_sound(self):
        return self.__cry

    @property
    def food(self):
        return self.__food

    @property
    def sleep_place(self):
        return self.__sleep

    # Methods
    def cry(self):
        print(f"{self.name} says {self.cry_sound}.")

    def eat(self):
        print(f"{self.name} eats {self.food}.")

    def sleep(self):
        print(f"{self.name} sleeps {self.sleep_place}.")

    def unique_action(self):
        print(f"{self.name} does something unique.")

    def __str__(self):
        return (f"{self.name} ({self.species}) - Age: {self.age}, Diet: {self.diet}, "
                f"Biome: {self.biome}, Enclosure: {self.enclosure_size}")


# Operations
def add_animals():


def remove_animals():