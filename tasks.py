"""
File: Tasks.py
Description: Holds functions that can be performed by staff to support Zoo operations.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from enclosure import Enclosure
from staff import list_all_staff

# Allowed roles
TASK_ROLES = {
    "Feed Animals": "Zookeeper",
    "Clean Enclosure": "Groundskeeper",
    "Move Animals": "Zookeeper",
    "Health Check": "Veterinarian"}

def can_perform_task(staff_member, task_name):
    """Returns True if the staff member can perform the given task."""
    required_role = TASK_ROLES.get(task_name)
    if not required_role:
        return False  # Unknown task
    return staff_member.role == required_role

# Tasks
def adhoc_task(zoo):
    """Assign a one-time task to a staff member."""
    from staff import list_all_staff

    if not zoo.staff:
        print("No staff available.")
        return

    # Select staff member
    list_all_staff(zoo)
    try:
        staff_id = int(input("\nEnter staff ID to perform adhoc task: "))
        staff_member = next((s for s in zoo.staff if s.id == staff_id), None)
        if not staff_member:
            print("Staff not found.")
            return

        # Select task
        tasks_list = ["Feed Animals", "Clean Enclosure", "Move Animals"]
        print("\nAvailable tasks:")
        for i, task in enumerate(tasks_list, start=1):
            print(f"{i}. {task}")

        task_choice = int(input("Select task: "))
        if not (1 <= task_choice <= len(tasks_list)):
            print("Invalid selection.")
            return

        task_name = tasks_list[task_choice - 1]

        # Check if staff member can perform this task
        if not can_perform_task(staff_member, task_name):
            print(f"{staff_member.role} cannot perform the task '{task_name}'.")
            return

        # Execute task
        if task_name == "Feed Animals":
            feed_animals()
        elif task_name == "Clean Enclosure":
            clean_enclosure()
        elif task_name == "Move Animals":
            move_animal(zoo)

        print(f"Adhoc task '{task_name}' completed by {staff_member.firstname}.")

    except ValueError:
        print("Invalid input. Enter a number.")


def view_schedule_menu(zoo):
    """Displays a staff member's schedule."""
    if not zoo.staff:
        print("No staff to view.")
        return

    list_all_staff(zoo)
    try:
        staff_id = int(input("Enter staff ID to view schedule: "))
        staff_member = next((s for s in zoo.staff if s.id == staff_id), None)
        if staff_member:
            staff_member.list_schedule()
        else:
            print("Staff not found.")
    except ValueError:
        print("Invalid input.")


def complete_task_menu(zoo):
    """Completes a scheduled task for a staff member and removes it from their schedule."""
    if not zoo.staff:
        print("No staff available.")
        return

    # Select staff member
    list_all_staff(zoo)
    try:
        staff_id = int(input("\nEnter staff ID to complete task: "))
        staff_member = next((s for s in zoo.staff if s.id == staff_id), None)
        if not staff_member:
            print("Staff not found.")
            return

        # Show schedule
        print(f"\nSchedule for {staff_member.firstname}:")
        for i, task in enumerate(staff_member.schedule, start=1):
            status = task if task else "Free"
            print(f"{i}. {status}")

        # Select hour with task
        hour = int(input("Select hour number to complete task: "))
        if not (1 <= hour <= 7) or not staff_member.schedule[hour - 1]:
            print("Invalid selection or no task assigned at this hour.")
            return

        task_name = staff_member.schedule[hour - 1]

        # Check if staff member can perform this task
        if not can_perform_task(staff_member, task_name):
            print(f"{staff_member.role} cannot perform the task '{task_name}'.")
            return

        # Execute the appropriate task
        if task_name == "Feed Animals":
            feed_animals()
        elif task_name == "Clean Enclosure":
            clean_enclosure()
        elif task_name == "Move Animals":
            move_animal(zoo)
        else:
            print(f"Task '{task_name}' not implemented.")
            return

        # Mark task as completed
        staff_member.remove_task(hour)
        print(f"Task '{task_name}' completed and removed from schedule.")

    except ValueError:
        print("Invalid input. Enter a number.")


def clean_enclosure():
    """Sets cleanliness of an enclosure to 10."""
    if not Enclosure.enclosure_list:
        print("No enclosures exist.")
        return

    print("\nSelect an enclosure to clean:")
    for i, enc in enumerate(Enclosure.enclosure_list, start=1):
        print(f"{i}. {enc}")

    try:
        choice = int(input("Enter number: ")) - 1
        if 0 <= choice < len(Enclosure.enclosure_list):
            enclosure = Enclosure.enclosure_list[choice]
            enclosure.cleanliness = 10
            print(f"Enclosure '{enclosure.name}' cleaned. Cleanliness now 10.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Enter a valid number.")


def feed_animals():
    """Feeds all animals in occupied enclosures."""
    occupied = [enc for enc in Enclosure.enclosure_list if enc.animals]
    if not occupied:
        print("\nNo animals to feed in any enclosure.")
        return

    print("\nEnclosures with animals:")
    for index, enc in enumerate(occupied, start=1):
        animal_names = [f"{animal.name} ({type(animal).__name__})" for animal in enc.animals]
        print(f"{index}. Enclosure #{enc.enclosure_id} | Biome: {enc.biome} | "
              f"Size: {enc.size} | Animals: {', '.join(animal_names)}")

    for enc in occupied:
        for animal in enc.animals:
            print(f"Feeding {animal.name} the {animal.species}...")


def move_animal(zoo):
    """Moves an animal to a different enclosure if not under treatment."""
    if not zoo.animals:
        print("No animals to move.")
        return

    # List animals with current enclosure info
    print("\nAnimals available to move:")
    for i, a in enumerate(zoo.animals, 1):
        enc_name = a.enclosure.name if a.enclosure else "No enclosure"
        print(f"{i}. {a.name} ({a.species}) in {enc_name}")

    choice = input("Select animal to move: ")
    try:
        animal = zoo.animals[int(choice)-1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    if animal.under_treatment:
        print(f"{animal.name} is under treatment and cannot be moved.")
        return

    # List all enclosures
    print("\nEnclosures:")
    for i, enc in enumerate(zoo.enclosures, 1):
        print(f"{i}. {enc.name} ({enc.biome})")

    choice = input("Select new enclosure: ")
    try:
        new_enc = zoo.enclosures[int(choice)-1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    # Remove from old enclosure if it exists
    if animal.enclosure:
        animal.enclosure.animals.remove(animal)

    # Assign new enclosure
    animal.enclosure = new_enc
    new_enc.animals.append(animal)

    print(f"{animal.name} moved to {new_enc.name}.")