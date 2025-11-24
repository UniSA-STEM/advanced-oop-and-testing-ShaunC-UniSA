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
    """Displays the vet services menu for managing animal health."""
    while True:
        print("\n=== Vet Services ===")
        print("1. Add Health Issue")
        print("2. Resolve Health Issue")
        print("3. View Animal Health Report")
        print("4. Zoo Health Report")
        print("5. Return")

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            animal = select_animal(zoo)
            if animal:
                add_health_issue(animal)

        elif choice == "2":
            animal = select_animal(zoo)
            if animal:
                resolve_health_issue(animal)

        elif choice == "3":
            animal = select_animal(zoo)
            if animal:
                animal_health_report(animal)

        elif choice == "4":
            zoo_health_report(zoo)

        elif choice == "5":
            return

        else:
            print("Invalid option.")


def select_animal(zoo):
    """Prompts the user to select an animal from the zoo and returns it."""
    print("\nAnimals:")
    for i, a in enumerate(zoo.animals, start=1):
        print(f"{i}. {a.name} ({a.species})")

    try:
        num = int(input("Enter number: ").strip())
        if 1 <= num <= len(zoo.animals):
            return zoo.animals[num - 1]
        else:
            print("Invalid number.")
            return None
    except ValueError:
        print("Invalid input.")
        return None


# Vet Functions
def add_health_issue(animal):
    """Add an injury, illness, or behaviour issue as a HealthRecord."""
    print(f"\nAdd health issue for {animal.name}:")
    print("1. Injury")
    print("2. Illness")
    print("3. Behaviour Issue")

    choice = input("Select type: ").strip()
    desc = input("Enter description: ").strip()
    if not desc:
        print("Description required.")
        return

    severity = input("Enter severity (Low/Moderate/High): ").strip().capitalize()
    if severity not in ["Low", "Moderate", "High"]:
        print("Invalid severity, defaulting to Low.")
        severity = "Low"

    record = HealthRecord(description=desc, severity=severity)

    if choice == "1":
        animal.injuries = animal.injuries or []
        animal.injuries.append(record)
    elif choice == "2":
        animal.illnesses = animal.illnesses or []
        animal.illnesses.append(record)
    elif choice == "3":
        animal.behavior = animal.behavior or []
        animal.behavior.append(record)
    else:
        print("Invalid choice.")
        return

    animal.under_treatment = True
    print(f"Issue recorded for {animal.name}. Animal marked as under treatment.")


def resolve_health_issue(animal):
    """Resolve all active HealthRecords if in Quarantine."""
    if not animal.enclosure or animal.enclosure.biome != "Quarantine":
        print(f"{animal.name} must be in Quarantine to resolve health issues.")
        return

    for record_list in [animal.injuries, animal.illnesses, animal.behavior]:
        if record_list:
            for record in record_list:
                record.resolved = True

    animal.under_treatment = False
    print(f"All health issues for {animal.name} have been resolved.")


def animal_health_report(animal):
    """Print health information for a single animal using HealthRecords."""
    print(f"\n=== Health Report: {animal.name} ===")

    def print_records(title, records):
        print(f"{title}:")
        if records:
            for r in records:
                print(f"  - {r}")
        else:
            print("  None")

    print_records("Injuries", animal.injuries)
    print_records("Illnesses", animal.illnesses)
    print_records("Behaviour Issues", animal.behavior)
    print(f"Under Treatment: {'Yes' if animal.under_treatment else 'No'}")


def zoo_health_report(zoo):
    """Print health report for all animals with active HealthRecords."""
    print("\n=== Zoo Health Report ===")
    any_issue = False
    for animal in zoo.animals:
        records_exist = any([animal.injuries, animal.illnesses, animal.behavior])
        if records_exist:
            any_issue = True
            print(f"\n--- {animal.name} ({animal.species}) ---")
            animal_health_report(animal)
    if not any_issue:
        print("No animals with health issues.")
    print("End of report.\n")