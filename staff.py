"""
File: staff.py
Description: Contains the classes, functions, and methods related to zoo staff.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from enclosure import Enclosure

# Staff
class Staff:
    """Staff help keep the zoo running and can be assigned to tasks."""
    staff_list = []

    def __init__(self, firstname: str, lastname: str, salutation: str, role: str, task: str = ""):
        self.__id = self.get_next_id()
        self.__name_firstname = firstname
        self.__name_lastname = lastname
        self.__name_salutation = salutation
        self.__role = role
        self.__task = task

        Staff.staff_list.append(self)

    @classmethod
    def get_next_id(cls):
        """Returns the first available staff-id that isn't already assigned."""
        next_available_id = 1
        while any(next_available_id == staff_member._Staff__id for staff_member in cls.staff_list):
            next_available_id += 1
        return next_available_id

    @classmethod
    def list_all_staff(cls):
        """Lists all staff and their details."""
        if not cls.staff_list:
            print("No staff exist.")
        else:
            for staff_member in cls.staff_list:
                print(staff_member)

    @property
    def id(self):
        return self.__id

    @property
    def firstname(self):
        return self.__name_firstname

    @property
    def lastname(self):
        return self.__name_lastname

    @property
    def salutation(self):
        return self.__name_salutation

    @property
    def role(self):
        return self.__role

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, new_task):
        self.__task = new_task

    def __str__(self):
        full_name = f"{self.__name_firstname} {self.__name_lastname} {self.__name_salutation}"
        task_status = self.__task if self.__task else "No task assigned"
        return f"Staff #{self.__id} | Name: {full_name} | Role: {self.__role} | Task: {task_status}"

# StaffOps
def add_staff(zoo):
    """Add a staff member to the Zoo."""

    salutations = {1: "Mr.", 2: "Ms.", 3: "Mrs.", 4: "Dr."}
    valid_salutation = False

    while not valid_salutation:
        print("\nSelect salutation:\n")
        print("1. Mr.\n2. Ms.\n3. Mrs.\n4. Dr.")

        try:
            choice = int(input("\nEnter choice (1–4): "))
            if choice in salutations:
                salutation = salutations[choice]
                valid_salutation = True
            else:
                print("Invalid selection. Enter 1–3.")
        except ValueError:
            print("Input must be a number (1–3).")

    valid_name = False
    while not valid_name:
        firstname = input("Enter first name: ").strip()
        lastname = input("Enter last name: ").strip()

        if firstname and lastname:
            valid_name = True
        else:
            print("Both first name and last name must be filled.")

    roles = {1: "Zookeeper", 2: "Veterinarian", 3: "Groundskeeper"}
    valid_role = False

    while not valid_role:
        print("\nSelect staff role:\n")
        print("1. Zookeeper\n2. Veterinarian\n3. Groundskeeper")
        try:
            choice = int(input("\nEnter choice (1–3): "))
            if choice in roles:
                role = roles[choice]
                valid_role = True
            else:
                print("Invalid selection. Enter 1–3.")
        except ValueError:
            print("Input must be a number (1–3).")

    staff_member = Staff(firstname, lastname, salutation, role)
    print("\nStaff member created:")
    print(staff_member)
    return staff_member


def remove_staff(zoo):
    """Removes a staff member from the Zoo."""
    if not Staff.staff_list:
        print("No staff exist.")
        return

    Staff.list_all_staff()
    try:
        staff_id = int(input("Enter the ID of the staff to remove: "))
        for staff in Staff.staff_list:
            if staff.id == staff_id:
                Staff.staff_list.remove(staff)
                print(f"Staff #{staff_id} removed.")
                return
        print(f"No staff found with ID {staff_id}.")
    except ValueError:
        print("Input must be a number.")


def feed_animals():
    """Feeds animals in an enclosure."""

    # List enclosures with animals
    occupied_enclosures = [enc for enc in Enclosure.enclosure_list if enc.animals]

    if not occupied_enclosures:
        print("\nNo animals to feed in any enclosure.")
        return

    print("\nEnclosures with animals:")
    for index, enclosure in enumerate(occupied_enclosures, start=1):
        animal_types = [type(animal).__name__ for animal in enclosure.animals]
        print(f"{index}. Enclosure #{enclosure.enclosure_id} | Biome: {enclosure.biome} | "
            f"Size: {enclosure.size} | Animals: {', '.join(animal_types)}")

    # Select enclosure to feed
    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("\nSelect an enclosure to feed animals: "))
            if 1 <= choice <= len(occupied_enclosures):
                valid_choice = True
                selected_enclosure = occupied_enclosures[choice - 1]
            else:
                print(f"Enter a number between 1 and {len(occupied_enclosures)}.")
        except ValueError:
            print("Enter a valid number.")

    # Feed animals in the enclosure
    for animal in selected_enclosure.animals:
        animal._Animal__food = 10

    print(f"\nFed all animals in Enclosure #{selected_enclosure.enclosure_id}. "
          f"Food level is now 10 for each animal.")

def move_animals():
    """Moves animals between enclosures."""

    # List occupied enclosures
    occupied_enclosures = [
        enclosure for enclosure in Enclosure.enclosure_list
        if enclosure.animals]

    if not occupied_enclosures:
        print("\nNo animals in any enclosure to move.")
        return

    print("\nOccupied Enclosures:")
    for index, enclosure in enumerate(occupied_enclosures, start=1):
        animal_types = [type(animal).__name__ for animal in enclosure.animals]
        print(
            f"{index}. Enclosure #{enclosure.enclosure_id} | "
            f"Biome: {enclosure.biome} | "
            f"Size: {enclosure.size} | "
            f"Animals: {', '.join(animal_types)}")

    # Select enclosure to move an animal from
    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("\nSelect an enclosure to move an animal from: "))
            if 1 <= choice <= len(occupied_enclosures):
                valid_choice = True
                source_enclosure = occupied_enclosures[choice - 1]
            else:
                print(f"Enter a number between 1 and {len(occupied_enclosures)}.")
        except ValueError:
            print("Enter a valid number.")

    # List animals in that enclosure
    animals_in_source = source_enclosure.animals
    print("\nAnimals in selected enclosure:")
    for index, animal in enumerate(animals_in_source, start=1):
        print(f"{index}. {type(animal).__name__}")

    # Select animal
    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("\nSelect an animal to move: "))
            if 1 <= choice <= len(animals_in_source):
                valid_choice = True
                animal_to_move = animals_in_source[choice - 1]
            else:
                print(f"Enter a number between 1 and {len(animals_in_source)}.")
        except ValueError:
            print("Enter a valid number.")

    # Step 5: List compatible enclosures
    compatible_enclosures = [
        enclosure for enclosure in Enclosure.enclosure_list
        if enclosure != source_enclosure
        and enclosure.biome == source_enclosure.biome
        and enclosure.size == source_enclosure.size]

    if not compatible_enclosures:
        print("\nNo compatible enclosures available for this animal.")
        return

    print("\nCompatible Enclosures:")
    for index, enclosure in enumerate(compatible_enclosures, start=1):
        animal_count = len(enclosure.animals)
        print(f"{index}. Enclosure #{enclosure.enclosure_id} | "
            f"Animals: {animal_count} | "
            f"Biome: {enclosure.biome} | "
            f"Size: {enclosure.size}")

    # Destination enclosure
    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("\nSelect an enclosure to move the animal to: "))
            if 1 <= choice <= len(compatible_enclosures):
                valid_choice = True
                destination_enclosure = compatible_enclosures[choice - 1]
            else:
                print(f"Enter a number between 1 and {len(compatible_enclosures)}.")
        except ValueError:
            print("Enter a valid number.")

    # Move the animal
    source_enclosure.animals.remove(animal_to_move)
    destination_enclosure.animals.append(animal_to_move)
    animal_to_move.enclosure = destination_enclosure

    print(f"\nMoved {type(animal_to_move).__name__} from "
        f"Enclosure #{source_enclosure.enclosure_id} to "
        f"Enclosure #{destination_enclosure.enclosure_id}.")

def clean_enclosure(enclosure_id):
    """Cleans an enclosure."""

    # List unclean enclosures
    dirty_enclosures = []

    for enclosure in Enclosure.enclosure_list:
        if enclosure.cleanliness < 10:
            dirty_enclosures.append(enclosure)

    if not dirty_enclosures:
        print("\nAll enclosures are clean!")
        return

    print("\nDirty Enclosures:")
    for index, enclosure in enumerate(dirty_enclosures, start=1):
        print(
            f"{index}. Enclosure #{enclosure.enclosure_id} | "
            f"Cleanliness: {enclosure.cleanliness} | "
            f"Biome: {enclosure.biome} | "
            f"Size: {enclosure.size}")

    # Choose the enclosure to clean
    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("\nSelect an enclosure to clean: "))

            if 1 <= choice <= len(dirty_enclosures):
                valid_choice = True
                selected_enclosure = dirty_enclosures[choice - 1]
                selected_enclosure.cleanliness = 10
                print(
                    f"Enclosure #{selected_enclosure.enclosure_id} is now fully clean "
                    f"(Cleanliness: {selected_enclosure.cleanliness}).")
            else:
                print(f"Invalid selection. Enter a number between 1 and {len(dirty_enclosures)}.")
        except ValueError:
            print("Enter a valid number.")