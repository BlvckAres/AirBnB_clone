#!/usr/bin/python3
"""Initializes the magic method of the models directory"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()