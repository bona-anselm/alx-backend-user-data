#!/usr/bin/env python3
""" Defines the class Auth """
from flask import request
from typing import List, TypeVar
import os


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
        if request:
            return request.headers.get("Authorization", None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Gets the current user """
        return None

    def session_cookie(self, request=None) -> str:
        """ Retrieves the value of the cookie named SESSION_NAME """
        if request:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
