"""
File: health.py
Description: Contains the classes, functions, and methods related to animal health records.
Author: Shaun Cantley
ID: 110450842
Username: CANSY012
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Imports
from datetime import datetime

# Classes
class HealthRecord:
    """Represents a health issue for an animal, including severity, treatment, and resolution status."""
    def __init__(self, description, severity, treatment_plan=""):
        self.description = description
        self.date_reported = datetime.now().strftime("%Y-%m-%d")
        self.severity = severity  # "Low", "Moderate", "High"
        self.treatment_plan = treatment_plan
        self.resolved = False

    def __str__(self):
        """Returns a summary of the health record."""
        status = "Resolved" if self.resolved else "Active"
        return (f"[{self.date_reported}] {self.description} | "
                f"Severity: {self.severity} | Status: {status} | "
                f"Treatment: {self.treatment_plan}")
