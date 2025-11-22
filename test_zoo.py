"""
File: test_zoo.py
Description: Contains a range of tests for zoo animal functions and features.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
import pytest
from unittest.mock import patch
from office import Zoo
from enclosure import Enclosure
from vet import add_health_issue, resolve_health_issue
from health import HealthRecord
from amphibians import TreeFrog, Toad
from birds import Ostrich, Vulture, Parrot, Toucan, Macaw, Owl, Woodpecker, Penguin, Puffin, SnowyOwl, Roadrunner
from aquatic import Dolphin, Seal, Shark, Clownfish, Seahorse, SeaTurtle, Octopus, Crab
from mammals import Lion, Elephant, Giraffe, Zebra, Meerkat, Hyena, Chimpanzee, Tiger, Sloth, BrownBear, Wolf, Deer, Fox, PolarBear, ArcticFox, Walrus, Reindeer, Camel
from reptiles import Python, Iguana, MonitorLizard, Tortoise, Rattlesnake
from animal import Animal, all_subclasses
from tasks import can_perform_task, clean_enclosure, feed_animals, move_animal

# Fixtures
@pytest.fixture
def zoo():
    Enclosure.enclosure_list.clear()
    z = Zoo("TestZoo")
    enc = Enclosure(size="Small", biome="Savannah", zoo=z)
    enc.name = "Test Enclosure"
    z.enclosures.append(enc)
    return z

@pytest.fixture
def zoo_with_enclosures():
    Enclosure.enclosure_list.clear()
    zoo = Zoo("TestZoo")
    enc1 = Enclosure(size="Small", biome="Savannah", zoo=zoo, name="Old Enclosure")
    enc2 = Enclosure(size="Small", biome="Savannah", zoo=zoo, name="New Enclosure")
    zoo.enclosures.extend([enc1, enc2])
    return zoo, enc1, enc2

@pytest.fixture
def zoo_with_animals(zoo_with_enclosures):
    zoo, enc1, enc2 = zoo_with_enclosures
    animal = Lion(name="Leo", age=3, zoo=zoo)
    enc1.animals.append(animal)
    animal.enclosure = enc1
    zoo.animals.append(animal)
    return zoo, enc1, enc2, animal

# Tests
def test_add_animal_to_enclosure(zoo):
    enc = zoo.enclosures[0]
    animal = Lion(name="TestAnimal", age=3, zoo=zoo)
    zoo.add_animal_to_enclosure(animal, enc)
    assert len(zoo.animals) == 1
    assert zoo.animals[0].name == "TestAnimal"
    assert zoo.animals[0].enclosure.name == enc.name

def test_enclosure_max_population(zoo):
    enc = zoo.enclosures[0]
    for i in range(3):
        zoo.add_animal_to_enclosure(Lion(name=f"Animal{i+1}", age=2, zoo=zoo), enc)
    assert len(enc.animals) == 3

def test_add_and_resolve_health_issue(zoo):
    enc = zoo.enclosures[0]
    enc.biome = "Quarantine"
    animal = Lion(name="SickAnimal", age=4, zoo=zoo)
    zoo.add_animal_to_enclosure(animal, enc)
    with patch("builtins.input", side_effect=["1", "Broken leg", "High"]):
        add_health_issue(animal)
    assert animal.under_treatment
    assert len(animal.injuries) == 1
    assert isinstance(animal.injuries[0], HealthRecord)
    resolve_health_issue(animal)
    assert not animal.under_treatment
    assert all(record.resolved for record in animal.injuries)

def test_can_perform_task():
    class MockStaff:
        def __init__(self, role): self.role = role
    zookeeper = MockStaff("Zookeeper")
    groundskeeper = MockStaff("Groundskeeper")
    vet = MockStaff("Veterinarian")
    assert can_perform_task(zookeeper, "Feed Animals")
    assert not can_perform_task(groundskeeper, "Feed Animals")
    assert can_perform_task(vet, "Health Check")
    assert not can_perform_task(vet, "Move Animals")
    assert not can_perform_task(zookeeper, "Unknown Task")

def test_clean_enclosure(zoo_with_enclosures):
    zoo, enc1, enc2 = zoo_with_enclosures
    enc1.cleanliness = 3
    with patch("builtins.input", return_value="1"):
        clean_enclosure()
    assert enc1.cleanliness == 10

def test_feed_animals(capsys, zoo_with_animals):
    zoo, old_enc, new_enc, animal = zoo_with_animals
    feed_animals()
    captured = capsys.readouterr()
    assert "Feeding Leo the Lion" in captured.out

def test_move_animal(zoo_with_animals):
    zoo, old_enc, new_enc, animal = zoo_with_animals
    enc_index = zoo.enclosures.index(new_enc) + 1
    with patch("builtins.input", side_effect=["1", str(enc_index), ""]):
        move_animal(zoo)
    assert animal.enclosure is new_enc
    assert animal in new_enc.animals
    assert animal not in old_enc.animals

def test_move_animal_blocked_by_treatment(zoo_with_animals):
    zoo, old_enc, new_enc, animal = zoo_with_animals
    animal.under_treatment = True
    with patch("builtins.input", side_effect=["1"]):
        move_animal(zoo)
    assert animal.enclosure.name == old_enc.name