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
    def __init__(self, name=str, species=str, age=int, diet=str):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__injuries = None
        self.__illnesses = None
        self.__behavior = None
        self.__under_treatment = False

    def cry(self):
        print(f'{self.__name} says {self.__cry}.') # TODO: Cry

    def eat(self):
        print(f'{self.__name} eats {self.__food}.') # TODO: Eat

    def sleep(self):
        print(f'{self.__name} sleeps {self.__sleep}.')  # TODO: Sleep

    def __str__(self):
        return f'{self.__name} {self.__species} {self.__age} {self.__diet}'


# Operations
def add_animals():


def remove_animals():