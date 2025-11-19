import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url() -> str:
    """
    Returns the base URL of the Final Space API from .env
    """
    return os.getenv("FINALSPACE_API_URL")
