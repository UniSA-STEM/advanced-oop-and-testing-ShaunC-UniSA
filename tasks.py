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
    """Move an animal to a suitable enclosure chosen by the user."""
    if not zoo.animals:
        print("No animals exist to move.")
        return

    # Select animal
    print("\nSelect an animal to move:")
    for i, animal in enumerate(zoo.animals, start=1):
        enc_name = animal.enclosure.name if animal.enclosure else "None"
        print(f"{i}. {animal.name} ({animal.species}) | Current Enclosure: {enc_name}")

    try:
        choice = int(input("Enter number: ")) - 1
        if 0 <= choice < len(zoo.animals):
            animal = zoo.animals[choice]
        else:
            print("Invalid selection.")
            return
    except ValueError:
        print("Enter a valid number.")
        return

    # Don't allow movement of animals under treatment
    if getattr(animal, "under_treatment", False) or getattr(animal, "health_flag", False):
        print(f"{animal.name} is under treatment and cannot be moved.")
        return

    # Find a suitable enclosures
    suitable = [
        enc for enc in zoo.enclosures
        if enc.biome == animal.biome and enc.size == animal.enclosure_size]

    if not suitable:
        print(f"No suitable enclosures available for {animal.name}.")
        return

    # Pick from suitable enclosures
    print("\nSelect enclosure for the animal:")
    for i, enc in enumerate(suitable, start=1):
        animal_count = len(enc.animals)
        print(f"{i}. {enc.name} (ID {enc.enclosure_id}) | Biome: {enc.biome} | "
              f"Size: {enc.size} | Animals: {animal_count}")

    try:
        enc_choice = int(input("Enter number of enclosure: ")) - 1
        if 0 <= enc_choice < len(suitable):
            target_enc = suitable[enc_choice]
        else:
            print("Invalid selection.")
            return
    except ValueError:
        print("Enter a valid number.")
        return

    # Rename the enclosure
    new_name = input(
        f"Enter new name for enclosure '{target_enc.name}' (press Enter to keep current): "
    ).strip()
    if new_name:
        target_enc.name = new_name

    # Remove animal from old enclosure if needed
    if animal.enclosure and animal in animal.enclosure.animals:
        animal.enclosure.animals.remove(animal)

    # Place animal in chosen enclosure
    target_enc.animals.append(animal)
    animal.enclosure = target_enc

    print(f"{animal.name} moved to enclosure '{target_enc.name}' (ID {target_enc.enclosure_id}).")