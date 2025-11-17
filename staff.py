"""
File: staff.py
Description: Contains the classes, functions, and methods related to zoo staff.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from animal import animal
from enclosure import enclosure

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
def add_staff():
    """Add a staff member to the Zoo."""
    valid_name = False
    while not valid_name:
        firstname = input("Enter first name: ").strip()
        lastname = input("Enter last name: ").strip()
        salutation = input("Enter salutation (e.g., Mr., Ms., Dr.): ").strip()
        if firstname and lastname and salutation:
            valid_name = True
        else:
            print("All three fields must be filled: first name, last name, salutation.")

    roles = {1: "Zookeeper", 2: "Veterinarian", 3: "Groundskeeper"}
    valid_role = False
    while not valid_role:
        print("\nSelect staff role:")
        print("1 Zookeeper  2 Veterinarian  3 Groundskeeper")
        try:
            choice = int(input("Enter choice (1-3): "))
            if choice in roles:
                role = roles[choice]
                valid_role = True
            else:
                print("Invalid selection. Enter 1, 2, or 3.")
        except ValueError:
            print("Input must be a number (1-3).")

    staff_member = Staff(firstname, lastname, salutation, role)
    print("\nStaff member created:")
    print(staff_member)
    return staff_member


def remove_staff():
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