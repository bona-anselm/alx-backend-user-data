#!/usr/bin/env python3
""" Defines the class Auth """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Manages authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks that authorization is required """
        return False

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets the current user """
        return None
