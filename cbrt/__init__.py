# cbrt/__init__.py

"""
cbrt - A Python package for accessing data from the Central Bank of the Republic of Türkiye (CBRT).
"""

from .config import set_api_key
from .api import fetch_data

__version__ = "0.1.0"
