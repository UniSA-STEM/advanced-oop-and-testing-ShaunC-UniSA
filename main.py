"""
File: main.py
Description: Demonstration scripts for various features of the zoo.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
import random
import time
import tasks
import vet
from abc import ABC
from health import HealthRecord
from animal import Animal, all_subclasses
from enclosure import Enclosure
from staff import Staff

# Animal imports for zoo quickstart
from mammals import (Mammal, Lion, Elephant, Giraffe, Zebra, Meerkat, Hyena, Chimpanzee,
                     Tiger, Sloth, BrownBear, Wolf, Deer, Fox, PolarBear, ArcticFox, Walrus, Reindeer, Camel)
from birds import (Bird, Ostrich, Vulture, Parrot, Toucan, Macaw, Owl, Woodpecker,
                   Penguin, Puffin, SnowyOwl, Roadrunner)
from amphibians import Amphibian, TreeFrog, Toad
from aquatic import Aquatic, Dolphin, Seal, Shark, Clownfish, Seahorse, SeaTurtle, Octopus, Crab
from reptiles import Reptile, Python, Iguana, MonitorLizard, Tortoise, Rattlesnake

# Hardcoded staff for zoo quickstart
STAFF_NAMES = [
    {"firstname": "Fawnella", "lastname": "O'Deer", "salutation": "Ms.", "role": "Zookeeper"},
    {"firstname": "Dolittle", "lastname": "Eachweek", "salutation": "Dr.", "role": "Veterinarian"},
    {"firstname": "Willy", "lastname": "Makeit", "salutation": "Mr.", "role": "Groundskeeper"}
]

# Enclosure population limit examples
MAX_POPULATION = {
    "Small": 3,
    "Medium": 5,
    "Large": 8
}

# Pause helper function
def pause():
    """Pause until user presses Enter."""
    input("\nPress Enter to continue…\n")

# Dynamically create animal list for zoo quickstart
def build_animal_database() -> list[dict]:
    """Build a list of all concrete Animal subclasses"""
    db = []
    subclasses = all_subclasses(Animal)

    for subclass in subclasses:
        # Skip abstract classes
        if isinstance(subclass, ABC) and subclass is not Animal:
            continue

        biome = getattr(subclass, "BIOME", None)
        size = getattr(subclass, "SIZE", None)

        if not biome or not size:
            continue

        db.append({
            "name": subclass.__name__,
            "biome": biome,
            "size": size,
            "class_ref": subclass
        })
    return db


# Zoo quickstart setup
def setup_quickstart_zoo(zoo_name: str):
    """Initialise zoo with demo staff, enclosures, and populate with animals."""
    from office import Zoo

    print("=== Quickstart Zoo Setup ===")
    zoo = Zoo(zoo_name)

    # Create Staff
    print("\n=== Creating Staff ===")
    for s in STAFF_NAMES:
        staff_member = Staff(s["firstname"], s["lastname"], s["salutation"], s["role"], zoo)
        print(f"{staff_member.salutation} {staff_member.firstname} {staff_member.lastname} ({staff_member.role})")
    pause()

    # Create Enclosures
    num_enclosures = input("How many enclosures to create? ")
    while not num_enclosures.isdigit() or int(num_enclosures) <= 0:
        print("Please enter a number.")
        num_enclosures = input("How many enclosures to create? ")

    num_enclosures = int(num_enclosures)
    print(f"\nCreating {num_enclosures} randomised enclosures…")
    SIZES = ["Small", "Medium", "Large"]
    available_biomes = ["Tropical / Rainforest", "Desert", "Aquatic / Marine",
                        "Savannah / Grassland", "Forest / Temperate"]

    for i in range(num_enclosures):
        size = random.choice(SIZES)
        biome = random.choice(available_biomes)
        enc = Enclosure(size=size, biome=biome, zoo=zoo)
        enc.name = f"Enclosure #{enc.enclosure_id}"
        print(enc)
    pause()

    ANIMAL_DATABASE = build_animal_database()
    if not ANIMAL_DATABASE:
        print("Warning: No animals found in database.")
        return zoo

    print("\nPopulating enclosures with animals…")
    for enc in zoo.enclosures:
        if enc.biome == "Quarantine":
            continue  # Dont populate quarantine

        eligible_species = [
            sp for sp in ANIMAL_DATABASE
            if sp["biome"] == enc.biome and sp["size"] == enc.size
        ]

        if not eligible_species:
            print(f"No suitable animals for {enc.name} ({enc.biome}, {enc.size})")
            continue

        species_data = random.choice(eligible_species)
        cls = species_data["class_ref"]
        num_animals = random.randint(1, MAX_POPULATION[enc.size])
        enc.animals.clear()

        for i in range(num_animals):
            name = f"{cls.__name__}_{i+1}"
            age = random.randint(1, 10)
            animal_instance = cls(name=name, age=age, zoo=zoo)
            animal_instance.enclosure = enc
            enc.animals.append(animal_instance)
            zoo.animals.append(animal_instance)

        print(f"{enc.name} ({enc.biome}, {enc.size}) has animals: {[a.name for a in enc.animals]}")
    pause()

    print(f"Zoo '{zoo.name}' setup complete with {len(zoo.enclosures)} enclosures, "
          f"{len(zoo.animals)} animals, {len(zoo.staff)} staff.")
    pause()

    return zoo


# Demo functions

def demo_feed_animals(zoo):
    """Simulate feeding animals."""
    print("\n=== Demo: Feeding Animals ===")
    tasks.feed_animals()
    pause()

def demo_clean_enclosures(zoo):
    """Simulate cleaning enclosures."""
    print("\n=== Demo: Cleaning Enclosures ===")
    tasks.clean_enclosure()
    pause()

def demo_random_staff_tasks(zoo):
    """Assign and remove random tasks for staff."""
    print("\n=== Demo: Assigning / Removing Random Staff Tasks ===")
    for s in zoo.staff:
        task = random.choice(["Feed Animals", "Clean Enclosure", "Move Animals"])
        hour = random.randint(1, 7)
        s.set_task(hour, task)
        print(f"Assigned {task} to {s.salutation} {s.firstname} at hour {hour}")
    pause()
    for s in zoo.staff:
        hour = random.randint(1, 7)
        s.remove_task(hour)
        print(f"Removed task from {s.salutation} {s.firstname} at hour {hour}")
    pause()

def demo_vet_loop(zoo):
    """Simulate vet check for a random animal."""
    print("\n=== Demo: Vet / Health Checks ===")
    if not zoo.animals:
        print("No animals to check.")
    else:
        animal = random.choice(zoo.animals)
        animal.injuries = [HealthRecord(description="Scratch Paw", severity="Low")]
        animal.under_treatment = True
        print(f"{animal.name} admitted to quarantine with injury: {animal.injuries[0]}")
        vet.animal_health_report(animal)
        vet.resolve_health_issue(animal)
        vet.zoo_health_report(zoo)
    pause()

def walk_the_zoo(zoo):
    """Simulate walking through the zoo and observing animals."""
    for enclosure in zoo.enclosures:
        print(f"\nWalking to {enclosure.name} ({enclosure.biome} - {enclosure.size})...", end="")
        for _ in range(3):
            time.sleep(1)
            print(".", end="", flush=True)
        print()
        if len(enclosure.animals) == 0:
            print(f"Hmmm... nothing there. Let's move on.")
            continue
        print(f"Watching animals in the {enclosure.name}:")
        for animal in enclosure.animals:
            action = random.choice([animal.cry, animal.sleep, animal.unique_action])
            result = action()

            if result:
                print(f"{animal.name} the {animal.__class__.__name__}: {result}")
                time.sleep(1)

def demo_menu(zoo):
    """Interactive demo menu."""
    selection = None
    while selection != "6":
        print("\n=== Demo Menu ===\n")
        print("1. Feed Animals Loop")
        print("2. Clean Enclosures Loop")
        print("3. Assign/Remove Random Staff Tasks")
        print("4. Vet / Health Check Loop")
        print("5. Tour the Zoo")
        print("6. Exit Demo")
        selection = input("\nSelect option: ")
        if selection == "1":
            demo_feed_animals(zoo)
        elif selection == "2":
            demo_clean_enclosures(zoo)
        elif selection == "3":
            demo_random_staff_tasks(zoo)
        elif selection == "4":
            demo_vet_loop(zoo)
        elif selection == "5":
            walk_the_zoo(zoo)
        elif selection == "6":
            print("Exiting demo…")
        else:
            print("Invalid selection.")


# Entrypoint from office.py init menu
def run_quickstart_demo(zoo_name: str):
    """Run the quickstart demo with a new zoo."""
    zoo = setup_quickstart_zoo(zoo_name)
    demo_menu(zoo)