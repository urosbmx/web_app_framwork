import logging
from typing import List

import pytest
from pydantic import TypeAdapter
import requests
from api_tests.tests.final_space_tests.model import Episode

logger = logging.getLogger(__name__)


class TestFinalSpace:
    """
    Test suite for Final Space API endpoints.

    Tests include:
    - Retrieving all episodes and validating response structure.
    - Retrieving single episodes with valid and invalid IDs.
    - Sorting episodes and limiting number of results.
    """

    def test_final_space_all_episodes(self, base_url):
        """
        Test retrieving all episodes from the API.

        Verifies:
        - Status code is 200
        - Response can be validated against the Episode model
        - All items in response are instances of Episode
        """
        logger.info("Starting test")
        r = requests.get(base_url)
        response = r.json()
        logger.info(f"Requested URL {r.request.url}")
        logger.info(f"Response is {response}")
        assert r.status_code == 200
        episodes_adapter = TypeAdapter(List[Episode])
        episodes = episodes_adapter.validate_python(response)
        assert all(isinstance(ep, Episode) for ep in episodes)
        logger.info(f"Validated {len(episodes)} episodes")

    @pytest.mark.parametrize("episodes", [1, 2, 3, 4, 5])
    def test_final_space_get_singe_episode(self, episodes, base_url):
        """
        Test retrieving a single episode by ID.

        Parameters:
        - episodes: ID of the episode to retrieve

        Verifies:
        - Status code is 200
        - Response can be validated against the Episode model
        """
        logger.info("Starting test")
        r = requests.get(f"{base_url}{episodes}")
        logger.info(f"Requested URL {r.request.url}")
        response = r.json()
        logger.info(f"Response is {response}")
        assert r.status_code == 200
        assert Episode.model_validate(response)

    @pytest.mark.parametrize("episodes", ["test", True, None])
    def test_final_space_get_singe_episode_with_invalid_type(self, episodes, base_url):
        """
        Test retrieving a single episode with invalid ID types.

        Parameters:
        - episodes: invalid type values to test API validation

        Verifies:
        - API returns 400 Bad Request for invalid types
        """
        logger.info("Starting test")
        r = requests.get(f"{base_url}{episodes}")
        response = r.json()
        logger.info(f"Requested URL {r.request.url}")
        logger.info(f"Response is {response}")
        assert r.status_code == 400

    @pytest.mark.parametrize("order, number", [
        ("asc", 1),
        ("desc", 23),
    ])
    def test_final_space_get_all_episodes_and_sort(self, order, number, base_url):
        """
        Test retrieving all episodes with sorting.

        Parameters:
        - order: sort order ("asc" or "desc")
        - number: expected first episode ID after sorting

        Verifies:
        - Status code is 200
        - Response can be validated against the Episode model
        - All items are instances of Episode
        - First episode matches expected ID based on sort order
        """
        logger.info("Starting test")
        r = requests.get(base_url, params={"sort": order})
        response = r.json()
        logger.info(f"Requested URL {r.request.url}")
        logger.info(f"Response is {response}")
        assert r.status_code == 200
        episodes_adapter = TypeAdapter(List[Episode])
        episodes = episodes_adapter.validate_python(response)
        assert all(isinstance(ep, Episode) for ep in episodes)
        logger.info(f"Validated {len(episodes)} episodes")
        assert response[0]["id"] == number

    @pytest.mark.parametrize("order, number", [
        ("asc", 1),
        ("desc", 1),
        ("desc", 14),
        ("asc", 21),
    ])
    def test_final_space_get_all_episodes_and_sort_and_limit(self, order, number, base_url):
        """
        Test retrieving episodes with sorting and limit.

        Parameters:
        - order: sort order ("asc" or "desc")
        - number: limit on the number of episodes returned

        Verifies:
        - Status code is 200
        - Response contains exactly 'number' episodes
        """
        logger.info("Starting test")
        r = requests.get(base_url, params={"sort": order, "limit": number})
        response = r.json()
        logger.info(f"Requested URL {r.request.url}")
        logger.info(f"Response is {response}")
        assert r.status_code == 200
        assert len(response) == number




