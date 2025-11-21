"""
File: main.py
Description: Demonstration script for various features of the zoo.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
import random
from animal import Animal, all_subclasses
from enclosure import Enclosure
from staff import Staff
import tasks
import vet

def pause():
    input("\nPress Enter to continue…\n")

# Staff
STAFF_NAMES = [
    {"firstname": "Whiskers", "lastname": "McFluffy", "salutation": "Dr.", "role": "Zookeeper"},
    {"firstname": "Barkley", "lastname": "Woofington", "salutation": "Mr.", "role": "Veterinarian"},
    {"firstname": "Snappy", "lastname": "Claws", "salutation": "Ms.", "role": "Groundskeeper"}
]

# Max population per enclosure size
MAX_POPULATION = {
    "Small": 3,
    "Medium": 5,
    "Large": 8
}

# Quickstart
def build_animal_database() -> list[dict]:
    """Build a list of all concrete Animal subclasses with BIOME and SIZE."""

    db = []

    for subclass in all_subclasses(Animal):
        # Skip abstract base classes
        if getattr(subclass, "ABSTRACT", False):
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

    # DEBUG: show what was actually added
    print(f"DEBUG: Built Animal Database: {[entry['name'] for entry in db]}")

    return db


def setup_quickstart_zoo(zoo_name: str):
    from office import Zoo

    print("=== Quickstart Zoo Setup ===")
    zoo = Zoo(zoo_name)

    # Create Staff
    print("\n=== Creating Staff ===")
    for s in STAFF_NAMES:
        staff_member = Staff(s["firstname"], s["lastname"], s["salutation"], s["role"], zoo)
        print(f"{staff_member.firstname} {staff_member.salutation} {staff_member.lastname} ({staff_member.role})")
    pause()

    # Create Enclosures
    num_enclosures = int(input("How many enclosures to create? "))
    print(f"\nCreating {num_enclosures} random enclosures…")
    SIZES = ["Small", "Medium", "Large"]
    available_biomes = ["Tropical / Rainforest", "Desert", "Aquatic / Marine", "Savannah", "Temperate Forest"]

    for i in range(num_enclosures):
        size = random.choice(SIZES)
        biome = random.choice(available_biomes)
        enc = Enclosure(size=size, biome=biome, zoo=zoo)
        enc.name = f"Enclosure #{enc.enclosure_id}"
        print(enc)
    pause()

    all_classes = all_subclasses(Animal)
    print("Loaded Animal subclasses:", [cls.__name__ for cls in all_classes])

    # Build Animal Database **now**
    ANIMAL_DATABASE = build_animal_database()
    if not ANIMAL_DATABASE:
        print("Warning: No animals found in database.")
        return zoo

    # Populate Enclosures
    print("\nPopulating enclosures with animals…")
    for enc in zoo.enclosures:
        if enc.biome == "Quarantine":
            continue  # skip quarantine

        # Filter animal database for species matching enclosure biome and size
        eligible_species = [
            sp for sp in ANIMAL_DATABASE
            if sp["biome"] == enc.biome and sp["size"] == enc.size
        ]

        if not eligible_species:
            print(f"No suitable animals for {enc.name} ({enc.biome}, {enc.size})")
            continue

        # Randomly choose a species for this enclosure
        species_data = random.choice(eligible_species)
        cls = species_data["class_ref"]

        # Random number of animals per enclosure
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

    print(f"\nZoo '{zoo.name}' setup complete with {len(zoo.enclosures)} enclosures, "
          f"{len(zoo.animals)} animals, {len(zoo.staff)} staff.\n")
    pause()

    return zoo

# Demo functions
def demo_feed_animals(zoo):
    print("\n=== Demo: Feeding Animals ===")
    tasks.feed_animals()
    pause()

def demo_clean_enclosures(zoo):
    print("\n=== Demo: Cleaning Enclosures ===")
    tasks.clean_enclosure()
    pause()

def demo_random_staff_tasks(zoo):
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
    print("\n=== Demo: Vet / Health Checks ===")
    if not zoo.animals:
        print("No animals to check.")
    else:
        animal = random.choice(zoo.animals)
        animal.injuries = "Scratch Paw"
        animal.under_treatment = True
        print(f"{animal.name} admitted to quarantine with injury: {animal.injuries}")
        vet.animal_health_report(animal)
        vet.resolve_health_issue(animal)
        vet.zoo_health_report(zoo)
    pause()

def demo_walk_the_zoo(zoo):
    print("\n=== TODO: Walk the Zoo Function ===")
    pause()

# Demo Menu
def demo_menu(zoo):
    selection = None
    while selection != "6":
        print("\n=== Demo Menu ===")
        print("1. Feed Animals Loop")
        print("2. Clean Enclosures Loop")
        print("3. Assign/Remove Random Staff Tasks")
        print("4. Vet / Health Check Loop")
        print("5. Walk the Zoo (TODO)")
        print("6. Exit Demo")
        selection = input("Select option: ")
        if selection == "1":
            demo_feed_animals(zoo)
        elif selection == "2":
            demo_clean_enclosures(zoo)
        elif selection == "3":
            demo_random_staff_tasks(zoo)
        elif selection == "4":
            demo_vet_loop(zoo)
        elif selection == "5":
            demo_walk_the_zoo(zoo)
        elif selection == "6":
            print("Exiting demo…")
        else:
            print("Invalid selection.")

# Quickstart Demo Entry
def run_quickstart_demo(zoo_name: str):
    zoo = setup_quickstart_zoo(zoo_name)
    demo_menu(zoo)

# Standalone execution
if __name__ == "__main__":
    name = input("Enter a name for your demo zoo: ")
    run_quickstart_demo(name)