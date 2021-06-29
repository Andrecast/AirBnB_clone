#!/usr/bin/python3
"""Module for class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from models
    """
    place_id = ""
    user_id = ""
    txt = ""
