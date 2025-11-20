"""
File: office.py
Description: Manages Zoo elements and meta functions. Acts as the interactive interface.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
import os
import pickle
from staff import Staff, add_staff, remove_staff, list_all_staff
import tasks


# Zoo class with save/load function
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []
        self.enclosures = []

    def save(self, filename=None):
        if filename is None:
            filename = self.name + ".zoo"
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
            print(f"Zoo saved as {filename}")
        except Exception as e:
            print(f"Error saving zoo: {e}")

    @staticmethod
    def load():
        zoo_files = [f for f in os.listdir() if f.endswith(".zoo")]
        if not zoo_files:
            print("No zoo files found in the current directory.")
            return None

        print("\nAvailable zoo files:")
        for i, f in enumerate(zoo_files, start=1):
            print(f"{i}. {f}")

        filename = None
        while filename is None:
            choice = input("\nEnter the filename to load (or number from list): ").strip()
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(zoo_files):
                    filename = zoo_files[index]
                else:
                    print("Invalid number. Try again.")
            elif choice in zoo_files:
                filename = choice
            else:
                print("File not found. Try again.")

        try:
            with open(filename, "rb") as file:
                zoo = pickle.load(file)
            print(f"Zoo loaded from {filename}")
            return zoo
        except Exception as e:
            print(f"Error loading zoo: {e}")
            return None


# Animal Management
def manage_animals(zoo):
    from animal import add_animal, remove_animal, list_animals

    while True:
        print("\n=== Manage Animals ===\n")
        print("1. Add Animal")
        print("2. Remove Animal")
        print("3. List Animals")
        print("4. Return to Main Menu")
        choice = input("\nSelect an option: ")

        if choice == "1":
            add_animal(zoo)
        elif choice == "2":
            remove_animal(zoo)
        elif choice == "3":
            list_animals(zoo)
        elif choice == "4":
            return
        else:
            print("Invalid choice. Enter 1–4.")


# Enclosure Management
def manage_enclosures(zoo):
    from enclosure import add_enclosure, remove_enclosure, list_enclosures

    while True:
        print("\n=== Manage Enclosures ===\n")
        print("1. Add Enclosure")
        print("2. Remove Enclosure")
        print("3. List Enclosures")
        print("4. Return to Main Menu")
        choice = input("\nSelect an option: ")

        if choice == "1":
            add_enclosure(zoo)
        elif choice == "2":
            if not zoo.enclosures:
                print("No enclosures to remove.")
            else:
                try:
                    enclosure_id = int(input("Enter the Enclosure ID to remove: "))
                    remove_enclosure(zoo, enclosure_id)
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == "3":
            list_enclosures(zoo)
        elif choice == "4":
            return
        else:
            print("Invalid choice. Enter 1–4.")


# Staff Management
def manage_staff(zoo):
    while True:
        print("\n=== Manage Staff ===\n")
        print("1. Add Staff")
        print("2. Remove Staff")
        print("3. List Staff")
        print("4. Assign Task to Staff")
        print("5. Remove Task from Staff")
        print("6. View Staff Schedule")
        print("7. Complete Task")
        print("8. Return to Main Menu")
        choice = input("\nSelect an option: ")

        if choice == "1":
            add_staff(zoo)
        elif choice == "2":
            remove_staff(zoo)
        elif choice == "3":
            list_all_staff(zoo)
        elif choice == "4":
            assign_task_menu(zoo)
        elif choice == "5":
            remove_task_menu(zoo)
        elif choice == "6":
            view_schedule_menu(zoo)
        elif choice == "7":
            complete_task_menu(zoo)
        elif choice == "8":
            return
        else:
            print("Invalid choice. Enter 1–8.")


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

        # Map task names to functions
        task_map = {
            "Feed Animals": tasks.feed_animals,
            "Clean Enclosure": tasks.clean_enclosure,
            "Move Animals": tasks.move_animal
        }

        if task_name not in task_map:
            print(f"Task '{task_name}' not implemented.")
            return

        # Execute task
        if task_name == "Feed Animals":
            task_map[task_name]()
        elif task_name == "Clean Enclosure":
            task_map[task_name]()
        elif task_name == "Move Animals":
            task_map[task_name](zoo)

        # Mark task as completed
        staff_member.remove_task(hour)
        print(f"Task '{task_name}' completed and removed from schedule.")

    except ValueError:
        print("Invalid input. Enter a number.")

def assign_task_menu(zoo):
    if not zoo.staff:
        print("No staff to assign tasks.")
        return

    list_all_staff(zoo)
    try:
        staff_id = int(input("Enter staff ID: "))
        staff_member = next((s for s in zoo.staff if s.id == staff_id), None)
        if not staff_member:
            print("Staff not found.")
            return

        print("\nAvailable hours 1–7:")
        for hour, task in enumerate(staff_member.schedule, start=1):
            status = task if task else "Free"
            print(f"Hour {hour}: {status}")

        hour = int(input("Select hour to assign task (1–7): "))

        # Example tasks
        tasks = ["Feed Animals", "Move Animals", "Clean Enclosure"]
        print("\nAvailable tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        task_choice = int(input("Select task: "))
        staff_member.set_task(hour, tasks[task_choice - 1])
        print(f"Task assigned for Hour {hour}.")
    except ValueError:
        print("Invalid input.")

def remove_task_menu(zoo):
    if not zoo.staff:
        print("No staff to remove tasks from.")
        return

    list_all_staff(zoo)
    try:
        staff_id = int(input("Enter staff ID to remove task: "))
        staff_member = next((s for s in zoo.staff if s.id == staff_id), None)
        if not staff_member:
            print("Staff not found.")
            return

        hour = int(input("Remove task from hour (1–7): "))
        if staff_member.remove_task(hour):
            print(f"Task removed from hour {hour} for {staff_member.firstname}.")
        else:
            print("Invalid hour. Must be 1–7.")
    except ValueError:
        print("Invalid input.")

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


# Vet Management
def manage_vet(zoo):
    pass  # TODO


# Zoo Preloader Menu
def zoo_init():
    running = True
    while running:
        print("\n=== ZooInit Preloader \u00A9 ByteWise Consulting ===\n")
        print("1. Create a New Zoo")
        print("2. Load Existing Zoo")
        print("3. Test / Debug Menu")
        print("4. Quit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            name = input("Enter name for new zoo: ")
            return Zoo(name)

        elif choice == "2":
            return Zoo.load()

        elif choice == "3":
            pass # TODO: implement test here later

        elif choice == "4":
            print("Shutting down ZooInit.")
            return None

        else:
            print("Invalid choice. Enter 1–4.")


# Zoo Main Menu
def main_menu(zoo):
    running = True
    while running:
        print("\n=== Welcome to", zoo.name, "Management System ===\n")
        print("1. Manage Animals")
        print("2. Manage Enclosures")
        print("3. Manage Staff")
        print("4. Manage Vet Services")
        print("5. Quit")
        option = input("\nSelect an option: ")

        if option == "1":
            manage_animals(zoo)
        elif option == "2":
            manage_enclosures(zoo)
        elif option == "3":
            manage_staff(zoo)
        elif option == "4":
            manage_vet(zoo)
        elif option == "5":
            print("\nSaving Zoo data and exiting...")
            zoo.save()
            running = False
        else:
            print("Invalid choice. Enter 1–5.")


# Start the ZMS
zoo = zoo_init()
if zoo is None:
    print("Exiting Program. Have a nice day!")
else:
    main_menu(zoo)