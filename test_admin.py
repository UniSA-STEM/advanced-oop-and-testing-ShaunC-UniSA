"""
File: test_admin.py
Description: Contains a range of tests for zoo administration functions and features.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

import pytest
from office import Zoo, Staff
from enclosure import Enclosure

def test_zoo_creation():
    zoo = Zoo("TestZoo")
    assert zoo.name == "TestZoo"
    assert zoo.enclosures == []
    assert zoo.animals == []
    assert zoo.staff == []

def test_add_staff_to_zoo():
    zoo = Zoo("TestZoo")
    staff_member = Staff("John", "Doe", "Mr", "Zookeeper", zoo)
    assert len(zoo.staff) == 1
    assert zoo.staff[0].role == "Zookeeper"

def test_add_enclosure_to_zoo():
    zoo = Zoo("TestZoo")
    enc = Enclosure(size="Small", biome="Savannah", zoo=zoo)
    zoo.enclosures.append(enc)
    assert enc in zoo.enclosures

def test_save_and_load_zoo(tmp_path):
    zoo = Zoo("SaveZoo")
    file_path = tmp_path / "zoo_test.zoo"
    zoo.save(filename=file_path)
    loaded = Zoo.load(filename=file_path)
    assert loaded.name == zoo.name