# cbrt/config.py
import os

API_KEY_ENV_VAR = "CBRT_API_KEY"

def set_api_key(api_key: str):
    """Sets the CBRT API key in the environment for use in requests."""
    os.environ[API_KEY_ENV_VAR] = api_key
    print("CBRT API key has been set.")

def get_api_key():
    """Retrieves the CBRT API key from the environment."""
    api_key = os.getenv(API_KEY_ENV_VAR)
    if api_key is None:
        raise ValueError("API key not set. Use set_api_key('your_api_key') to set it.")
    return api_key
