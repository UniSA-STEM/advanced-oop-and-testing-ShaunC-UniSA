"""
File: staff.py
Description: Contains the classes, functions, and methods related to zoo staff.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from typing import List, Optional

# Staff
class Staff:
    """Staff help keep the zoo running and can be assigned to tasks."""
    WORKDAY_HOURS = 7

    def __init__(self, firstname: str, lastname: str, salutation: str, role: str, zoo):
        self.__id = self.get_next_id(zoo)
        self.__name_firstname = firstname
        self.__name_lastname = lastname
        self.__name_salutation = salutation
        self.__role = role

        # Daily schedule
        self.__schedule: List[Optional[str]] = [None] * Staff.WORKDAY_HOURS

        # Add staff to the zoo
        zoo.staff.append(self)

    @staticmethod
    def get_next_id(zoo):
        """Returns the first available staff-id that isn't already assigned."""
        next_available_id = 1
        while any(next_available_id == staff_member.id for staff_member in zoo.staff):
            next_available_id += 1
        return next_available_id

    @property
    def id(self) -> int:
        """Staff ID."""
        return self.__id

    @property
    def firstname(self) -> str:
        """First name."""
        return self.__name_firstname

    @property
    def lastname(self) -> str:
        """Last name."""
        return self.__name_lastname

    @property
    def salutation(self) -> str:
        """Salutation."""
        return self.__name_salutation

    @property
    def role(self) -> str:
        """Role in the zoo."""
        return self.__role

    @property
    def schedule(self) -> list:
        """Copy of the workday schedule."""
        return self.__schedule.copy()

    def set_task(self, hour: int, task: str) -> bool:
        """Assign a task to a specific hour."""
        if 1 <= hour <= Staff.WORKDAY_HOURS:
            self.__schedule[hour - 1] = task
            return True
        return False

    def remove_task(self, hour: int) -> bool:
        """Remove a task from a specific hour."""
        if 1 <= hour <= Staff.WORKDAY_HOURS:
            self.__schedule[hour - 1] = None
            return True
        return False

    def list_schedule(self):
        """Print the schedule."""
        print(f"\nSchedule for {self.__name_firstname} {self.__name_lastname}:")
        for i, task in enumerate(self.__schedule, start=1):
            print(f"Hour {i}: {task if task else 'Free'}")

    def __str__(self) -> str:
        """Return a readable staff summary."""
        full_name = f"{self.__name_salutation} {self.__name_firstname} {self.__name_lastname}"
        return f"Staff #{self.__id} | Name: {full_name} | Role: {self.__role}"


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
                print("Invalid selection. Enter 1–4.")
        except ValueError:
            print("Input must be a number (1–4).")

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

    staff_member = Staff(firstname, lastname, salutation, role, zoo)
    print("\nStaff member created:")
    print(staff_member)
    return staff_member


def remove_staff(zoo):
    """Removes a staff member from the Zoo."""
    if not zoo.staff:
        print("No staff exist.")
        return

    list_all_staff(zoo)
    try:
        staff_id = int(input("Enter the ID of the staff to remove: "))
        for staff in zoo.staff:
            if staff.id == staff_id:
                zoo.staff.remove(staff)
                print(f"Staff #{staff_id} removed.")
                return
        print(f"No staff found with ID {staff_id}.")
    except ValueError:
        print("Input must be a number.")


def list_all_staff(zoo):
    """Lists all staff and their details."""
    if not zoo.staff:
        print("No staff exist.")
    else:
        for staff_member in zoo.staff:
            print(staff_member)