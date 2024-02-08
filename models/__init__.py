#!/usr/bin/python3
"""
Initialization Script for File Storage

This script initializes a FileStorage instance and reloads
data from a JSON file.
"""

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
