"""
File: animal.py
Description: Contains the classes, functions, and methods relating to zoo animals.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
import mammals
import birds
import reptiles
import amphibians
import aquatic

# Animals
class Animal:
    """Represents a zoo animal."""
    zoo_animals = []

    def __init__(self, name: str, species: str, age: int, diet: str, biome: str, enclosure_size: str) -> None:
        self.__id = self.get_next_id()
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

        Animal.zoo_animals.append(self)

    @classmethod
    def get_next_id(cls):
        next_available_id = 1
        while any(next_available_id == animal._Animal__id for animal in cls.zoo_animals):
            next_available_id += 1
        return next_available_id

    @classmethod
    def list_all_animals(cls):
        if not cls.zoo_animals:
            print("No animals exist.")
        else:
            for animal in cls.zoo_animals:
                print(animal)

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

    def _set_cry(self, cry):
        self.__cry = cry

    def _set_sleep(self, sleep):
        self.__sleep = sleep

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


# AnimalOps
def add_animal():
    """Adds an animal to the Zoo."""
    animal_types = {
        1: ("Mammal", mammals.Mammal),
        2: ("Bird", birds.Bird),
        3: ("Reptile", reptiles.Reptile),
        4: ("Amphibian", amphibians.Amphibian),
        5: ("Aquatic", aquatic.AquaticAnimal)}

    print("Select animal type:")
    for key, (name, _) in animal_types.items():
        print(f"{key}: {name}")

    animal_type = None
    while animal_type not in animal_types:
        try:
            animal_type = int(input("Enter choice (1-5): "))
        except ValueError:
            print("Please enter a number between 1 and 5.")

    type_name, base_class = animal_types[animal_type]

    # Find all subclasses of the base class
    subclasses = [cls for cls in base_class.__subclasses__()]
    print(f"\nAvailable {type_name}s:")
    for i, cls in enumerate(subclasses, start=1):
        print(f"{i}: {cls.__name__}")

    subclass = None
    while not subclass:
        try:
            choice = int(input(f"Select {type_name} (1-{len(subclasses)}): "))
            if 1 <= choice <= len(subclasses):
                subclass = subclasses[choice - 1]
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a number.")

    # Ask for the animal's name
    animal_name = input(f"Enter {subclass.__name__}'s name: ")

    # Create animal
    animal_instance = subclass(name=animal_name, age=0)

    print(f"\nAdded {type_name} '{animal_name}' ({subclass.__name__}) with ID {animal_instance.id}")
    return animal_instance


def remove_animal():
    """Removes an animal from the Zoo"""
    if not Animal.zoo_animals:
        print("No animals exist.")
        return

    Animal.list_all_animals()
    try:
        animal_id = int(input("Enter the ID of the animal to remove: "))
        for animal in Animal.zoo_animals:
            if animal.id == animal_id:
                Animal.zoo_animals.remove(animal)
                print(f"Animal #{animal_id} removed.")
                return
        print(f"No animal found with ID {animal_id}.")
    except ValueError:
        print("Input must be a number.")