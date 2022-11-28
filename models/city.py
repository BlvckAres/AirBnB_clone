#!/usr/bin/python3
"""Creates the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """ Defines the users' city attributes.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
