#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
try:
    from decouple import config as getenv
except ImportError:
    from os import getenv

storage_env = getenv("HBNB_TYPE_STORAGE")

if storage_env == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
