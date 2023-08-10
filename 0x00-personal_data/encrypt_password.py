#!/usr/bin/env python3
"""A module for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a salted hashed password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks if a hashed password is the same as the gievn password """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
