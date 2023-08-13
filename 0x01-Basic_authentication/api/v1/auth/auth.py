#!/usr/bin/env python3
""" Defines the class Auth """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Manages authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks that authorization is required """
        if not path:
            return True
        if not excluded_paths or excluded_paths == []:
            return True
        if not path.endswith("/"):
            path += "/"
        if path in excluded_paths:
            return False
        for paths in excluded_paths:
            paths = paths.rstrip("*")
            if path.find(paths) != -1:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves the authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets the current user """
        return None
