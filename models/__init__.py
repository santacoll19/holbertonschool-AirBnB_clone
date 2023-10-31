#!/usr/bin/python3
"""Module init"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
