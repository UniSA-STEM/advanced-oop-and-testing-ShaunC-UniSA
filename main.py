"""
File: main.py
Description: Demonstration script for various features of the zoo.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from animal import animal
from enclosure import enclosure
from staff import staff

# Zoo Operations
def assign_enclosure(animal, enclosure):
    """Assigns enclosures to animals."""
    print(f"{animal} enclosure is {enclosure}")

def schedule_cleaning(enclosure):
    """Assigns staff to clean an enclosure."""
    print(f"{staff.name} is assigned to clean {enclosure}")

def schedule_feeding(animal, enclosure):
    """Assigns staff to feed an animal"""
    print(f"{staff.name} is assigned to feed {enclosure}")

def animal_report(animal):
    """Returns the status of an animal."""
    return animal # TODO Animal Report

def enclosure_report(enclosure):
    """Returns the status of an enclosure"""
    return enclosure # TODO Enclosure Report