"""
File: vet.py
Description: Contains the classes, functions, and methods related to animal welfare functions.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from health import HealthRecord

# Vet Services
def vet_menu(zoo):
    while True:
        print("\n=== Vet Services ===")
        print("1. Add Health Issue")
        print("2. Resolve Health Issue")
        print("3. View Animal Health Report")
        print("4. Zoo Health Report")
        print("5. Return")

        choice = input("Select option: ").strip()

        if choice == "5":
            return

        # pick an animal
        print("\nSelect an animal:")
        for i, a in enumerate(zoo.animals, start=1):
            print(f"{i}. {a.name} ({a.species})")
        try:
            idx = int(input("Enter number: ")) - 1
            animal = zoo.animals[idx]
        except:
            print("Invalid animal.")
            continue

        if choice == "1":
            add_health_issue(animal)
        elif choice == "2":
            resolve_health_issue(animal)
        elif choice == "3":
            health_report(animal)
        elif choice == "4":
            zoo_health_report(zoo)
        else:
            print("Invalid option.")


# Vet Functions
def add_health_issue(animal):
    """Add an injury, illness, or behaviour issue."""
    print(f"\nAdd health issue for {animal.name}:")
    print("1. Injury")
    print("2. Illness")
    print("3. Behaviour Issue")

    choice = input("Select type: ").strip()

    desc = input("Enter description: ").strip()
    if not desc:
        print("Description required.")
        return

    if choice == "1":
        animal.injuries = desc
    elif choice == "2":
        animal.illnesses = desc
    elif choice == "3":
        animal.behavior = desc
    else:
        print("Invalid choice.")
        return

    animal.under_treatment = True
    print(f"Issue recorded for {animal.name}. Animal marked as under treatment.")


def resolve_health_issue(animal):
    """Animals in quarantine can be treated."""
    if not animal.enclosure or animal.enclosure.biome != "Quarantine":
        print(f"{animal.name} must be in Quarantine to resolve health issues.")
        return

    animal.injuries = None
    animal.illnesses = None
    animal.behavior = None
    animal.under_treatment = False
    print(f"Health issues for {animal.name} have been resolved.")


def health_report(animal):
    """Print health information for a single animal."""
    print(f"\n--- Health Report: {animal.name} ---")
    print(f"Injuries: {animal.injuries if animal.injuries else 'None'}")
    print(f"Illnesses: {animal.illnesses if animal.illnesses else 'None'}")
    print(f"Behaviour Issues: {animal.behavior if animal.behavior else 'None'}")
    print(f"Under Treatment: {'Yes' if animal.under_treatment else 'No'}")


def zoo_health_report(zoo):
    """Print health report for all animals with issues."""
    print("\n=== Zoo Health Report ===")
    any_issue = False
    for animal in zoo.animals:
        if animal.injuries or animal.illnesses or animal.behavior or animal.under_treatment:
            any_issue = True
            print(f"\n--- {animal.name} ({animal.species}) ---")
            print(f"Injuries: {animal.injuries if animal.injuries else 'None'}")
            print(f"Illnesses: {animal.illnesses if animal.illnesses else 'None'}")
            print(f"Behaviour Issues: {animal.behavior if animal.behavior else 'None'}")
            print(f"Under Treatment: {'Yes' if animal.under_treatment else 'No'}")
    if not any_issue:
        print("No animals with health issues.")
    print("End of report.\n")