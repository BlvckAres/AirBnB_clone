#!/usr/bin/python3
"""Creates a state class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents the state class attributes.

    Attributes:
        name (str): The name of the state.
    """

    name = ""