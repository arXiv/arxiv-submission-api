import sys
import os

from metadata.factory import create_api_app

if 'JWT_SECRET' not in os.environ:
    os.environ['JWT_SECRET'] = 'foosecret'


app = create_api_app()
"""Provides application for development purposes."""