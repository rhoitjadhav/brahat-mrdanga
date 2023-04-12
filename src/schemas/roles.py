# Packages
from enum import Enum


class Roles(str, Enum):
    admin = "admin"
    devotee = "devotee"
    counsellor = "counsellor"


class RolesAddSchema:
    name: Roles
