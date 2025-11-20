"""
File: animal.py
Description: Contains the classes, functions, attributes and methods relating to zoo animals.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Animal:
    """Represents a zoo animal."""

    def __init__(self, name: str, species: str, age: int, diet: str,
                 biome: str, enclosure_size: str, zoo, enclosure=None) -> None:
        self.__id = self.get_next_id(zoo)
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
        self.__enclosure = enclosure
        self.zoo = zoo

    @staticmethod
    def get_next_id(zoo):
        next_id = 1
        if zoo:
            existing_ids = [animal.id for animal in zoo.animals]
            while next_id in existing_ids:
                next_id += 1
        return next_id

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
    def enclosure(self):
        return self.__enclosure

    @enclosure.setter
    def enclosure(self, enclosure):
        self.__enclosure = enclosure

    def _set_cry(self, sound):
        self.cry = sound

    def _set_sleep(self, place):
        self.sleeping_place = place

    def __str__(self):
        enclosure_info = f"{self.enclosure.enclosure_id} - {self.enclosure.name}" if self.enclosure else "None"
        return (f"ID {self.id}: {self.name} ({self.species}) - Age: {self.age}, Diet: {self.diet}, "
                f"Biome: {self.biome}, Enclosure: {enclosure_info}")

# AnimalOps
def add_animal(zoo):
    """Adds an animal to the Zoo."""

    import mammals
    import birds
    import reptiles
    import amphibians
    import aquatic

    animal_types = {
        1: ("Mammal", mammals.Mammal),
        2: ("Bird", birds.Bird),
        3: ("Reptile", reptiles.Reptile),
        4: ("Amphibian", amphibians.Amphibian),
        5: ("Aquatic", aquatic.Aquatic)
    }

    print("\n=== Select animal type ===\n")
    for key, (name, _) in animal_types.items():
        print(f"{key}: {name}")

    # Select animal type
    animal_type = None
    while animal_type not in animal_types:
        try:
            animal_type = int(input("Enter choice (1-5): "))
        except ValueError:
            print("Please enter a number between 1 and 5.")

    type_name, base_class = animal_types[animal_type]

    # List all subclasses
    def all_subclasses(cls):
        result = []
        for subclass in cls.__subclasses__():
            result.append(subclass)
            result.extend(all_subclasses(subclass))
        return result

    subclasses = all_subclasses(base_class)
    if not subclasses:
        print(f"No {type_name} subclasses found.")
        return None

    # Let user pick subclass
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

    # Name animal
    animal_name = input(f"Enter {subclass.__name__}'s name: ")

    # Create animal
    animal_instance = subclass(name=animal_name, age=0, zoo=zoo)

    # Add to zoo
    zoo.animals.append(animal_instance)

    print(f"\nAdded {type_name} '{animal_name}' ({subclass.__name__}) with animal ID {animal_instance.id}")
    return animal_instance


def remove_animal(zoo):
    """Removes an animal from the Zoo"""
    if not zoo.animals:
        print("No animals exist.")
        return
    list_animals(zoo)
    try:
        animal_id = int(input("Enter the ID of the animal to remove: "))
        animal_to_remove = next((a for a in zoo.animals if a.id == animal_id), None)
        if animal_to_remove:
            zoo.animals.remove(animal_to_remove)
            print(f"Animal #{animal_id} removed.")
        else:
            print(f"No animal found with ID {animal_id}.")
    except ValueError:
        print("Input must be a number.")


def list_animals(zoo):
    """Lists all animals and their details."""
    if not zoo.animals:
        print("No animals in the zoo.")
    else:
        for animal in zoo.animals:
            print(animal)