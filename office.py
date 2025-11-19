"""
File: office.py
Description: Manages Zoo elements and meta functions. Acts as the interactive interface.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
import pickle


# Zoo class with save/load function
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []
        self.enclosures = []

    def save(self, filename=None):
        if filename is None:
            filename = self.name + ".pkl"
        file = open(filename, "wb")
        pickle.dump(self, file)
        file.close()
        print("Zoo saved as", filename)

    @staticmethod
    def load():
        filename = input("Enter filename to load zoo (e.g., CityZoo.pkl): ")
        file = open(filename, "rb")
        zoo = pickle.load(file)
        file.close()
        print("Zoo loaded from", filename)
        return zoo


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
    from enclosure import Enclosure, add_enclosure, remove_enclosure, list_enclosures

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
            if not Enclosure.enclosure_list:
                print("No enclosures to remove.")
            else:
                try:
                    enclosure_id = int(input("Enter the Enclosure ID to remove: "))
                    remove_enclosure(enclosure_id)
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
    from staff import Staff, add_staff, remove_staff

    while True:
        print("\n=== Manage Staff ===\n")
        print("1. Add Staff")
        print("2. Remove Staff")
        print("3. List Staff")
        print("4. Return to Main Menu")
        choice = input("\nSelect an option: ")

        if choice == "1":
            add_staff(zoo)
        elif choice == "2":
            remove_staff(zoo)
        elif choice == "3":
            Staff.list_all_staff()
        elif choice == "4":
            return
        else:
            print("Invalid choice. Enter 1–4.")


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
            print("Exiting... saving zoo...")
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