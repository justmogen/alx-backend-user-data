#!/usr/bin/env python3
""" Auth mmethod that takes in a password string arguments and
returns a byte string.
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hashes a password. """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
